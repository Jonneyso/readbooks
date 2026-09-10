import urllib.request
import re

def get_chapter_content(chapter_url):
    try:
        # 添加User-Agent头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        req = urllib.request.Request(chapter_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('gbk')  # 这个网站可能使用gbk编码
            
            # 提取章节标题
            title_match = re.search(r'<h1>(.*?)</h1>', html)
            title = title_match.group(1).strip() if title_match else ''
            
            # 提取内容区域
            # 查找内容区域的模式可能需要调整
            content_match = re.search(r'<div class="content">(.*?)</div>', html, re.DOTALL)
            if not content_match:
                # 尝试其他可能的内容区域模式
                content_match = re.search(r'<div[^>]*>(.*?)</div>', html, re.DOTALL)
            
            if content_match:
                content = content_match.group(1)
                # 移除HTML标签
                content = re.sub(r'<.*?>', '', content)
                # 清理空白字符
                content = '\n'.join([line.strip() for line in content.split('\n') if line.strip()])
                return title, content
            return title, ''
    except Exception as e:
        print(f"获取章节内容失败: {e}")
        return '', ''

def main():
    base_url = 'http://www.purepen.com/hlm'
    index_url = f'{base_url}/index.htm'
    
    try:
        # 添加User-Agent头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        req = urllib.request.Request(index_url, headers=headers)
        
        # 获取目录页面
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('gbk')  # 这个网站可能使用gbk编码
            
            # 打印页面前2000个字符，查看页面结构
            print("页面前2000个字符:")
            print(html[:2000])
            
            # 提取所有链接
            all_links = re.findall(r'<a[^>]+href="([^"]+)">', html)
            print(f"\n共找到 {len(all_links)} 个链接")
            print("所有链接:")
            for link in all_links:
                print(link)
            
            # 手动构建章节链接（从1到120）
            chapter_links = []
            for i in range(1, 121):
                chapter_links.append(f'{base_url}/{i}.htm')
            
            print(f"\n共构建了 {len(chapter_links)} 个章节链接")
            print("前5个链接:")
            for link in chapter_links[:5]:
                print(link)
            
            # 创建输出文件
            output_file = '红楼梦.txt'
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('红楼梦\n')
                f.write('曹雪芹、高鹗 著\n')
                f.write('\n')
                
                # 爬取每个章节
                for i, chapter_url in enumerate(chapter_links, 1):
                    print(f'\n正在获取第{i}回: {chapter_url}')
                    title, content = get_chapter_content(chapter_url)
                    if title and content:
                        print(f'成功获取: {title}')
                        f.write(f'{title}\n')
                        f.write(f'{content}\n')
                        f.write('\n')
                    else:
                        print(f'获取失败: {chapter_url}')
            
            print(f'\n红楼梦全文已保存到 {output_file}')
            print(f'共尝试获取 {len(chapter_links)} 回内容')
    except Exception as e:
        print(f"获取目录失败: {e}")

if __name__ == '__main__':
    main()