import urllib.request
import re

def main():
    # 使用可靠的在线来源
    base_url = 'https://ctext.org/hongloumeng'
    
    try:
        # 添加User-Agent头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # 创建输出文件
        output_file = '红楼梦.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('红楼梦\n')
            f.write('曹雪芹、高鹗 著\n')
            f.write('\n')
            
            # 红楼梦共120回，尝试获取每回内容
            for i in range(1, 121):
                chapter_url = f'{base_url}/{i}'
                print(f'正在获取第{i}回: {chapter_url}')
                
                try:
                    req = urllib.request.Request(chapter_url, headers=headers)
                    with urllib.request.urlopen(req) as response:
                        html = response.read().decode('utf-8')
                        
                        # 提取章节标题
                        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html)
                        title = title_match.group(1).strip() if title_match else f'第{i}回'
                        
                        # 提取内容区域
                        content_match = re.search(r'<div class="text"[^>]*>(.*?)</div>', html, re.DOTALL)
                        if content_match:
                            content = content_match.group(1)
                            # 移除HTML标签
                            content = re.sub(r'<.*?>', '', content)
                            # 清理空白字符
                            content = '\n'.join([line.strip() for line in content.split('\n') if line.strip()])
                            
                            print(f'成功获取: {title}')
                            f.write(f'{title}\n')
                            f.write(f'{content}\n')
                            f.write('\n')
                        else:
                            print(f'获取内容失败: {chapter_url}')
                except Exception as e:
                    print(f'获取章节失败: {e}')
        
        print(f'\n红楼梦全文已保存到 {output_file}')
    except Exception as e:
        print(f'发生错误: {e}')

if __name__ == '__main__':
    main()