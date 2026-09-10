import urllib.request
import re

# 红楼梦章节数
TOTAL_CHAPTERS = 120

# 基础URL
BASE_URL = 'https://ctext.org/hongloumeng/zh'  # 使用ctext.org作为数据源

# 输出文件路径
OUTPUT_FILE = '红楼梦.txt'

def get_chapter_content(chapter_num):
    """获取指定章节的内容"""
    chapter_url = f'{BASE_URL}#{chapter_num}'
    print(f'正在获取第{chapter_num}回...')
    
    try:
        # 添加完整的头信息
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        req = urllib.request.Request(chapter_url, headers=headers)
        
        print(f'请求URL: {chapter_url}')
        with urllib.request.urlopen(req, timeout=10) as response:
            print(f'响应状态: {response.status}')
            html = response.read().decode('utf-8')
            print(f'获取到的HTML长度: {len(html)} 字符')
            
            # 提取章节标题
            title_pattern = f'<h3 id="{chapter_num}">(.*?)</h3>'
            title_match = re.search(title_pattern, html)
            if title_match:
                title = title_match.group(1).strip()
                print(f'找到章节标题: {title}')
            else:
                title = f'第{chapter_num}回'
                print(f'未找到章节标题，使用默认标题: {title}')
            
            # 提取内容区域
            # 找到章节标题的结束位置
            if title_match:
                start_pos = title_match.end()
                # 找到下一个章节的开始位置或内容结束
                next_chapter = chapter_num + 1
                end_pattern = f'<h3 id="{next_chapter}">|</div>\s*</div>\s*</body>'
                end_match = re.search(end_pattern, html[start_pos:])
                
                if end_match:
                    end_pos = start_pos + end_match.start()
                    content = html[start_pos:end_pos]
                    # 移除HTML标签
                    content = re.sub(r'<.*?>', '', content)
                    # 清理空白字符
                    content = '\n'.join([line.strip() for line in content.split('\n') if line.strip()])
                    print(f'提取到内容长度: {len(content)} 字符')
                    return title, content
                else:
                    print('未找到内容结束位置')
            return title, ''
    except Exception as e:
        print(f'获取第{chapter_num}回失败: {e}')
        return f'第{chapter_num}回', ''

def main():
    """主函数"""
    print(f'开始下载红楼梦全文，共{TOTAL_CHAPTERS}回')
    # 打开文件，追加模式
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('红楼梦\n')
        f.write('曹雪芹、高鹗 著\n')
        f.write('\n')
        print('文件已创建并写入头部信息')
        
        # 逐章获取内容
        for i in range(1, 3):  # 先测试前2回
            title, content = get_chapter_content(i)
            if title and content:
                print(f'成功获取: {title}')
                print(f'内容长度: {len(content)} 字符')
                f.write(f'## {title}\n')
                f.write(f'{content}\n')
                f.write('\n')
                f.flush()  # 立即写入
            else:
                print(f'获取失败: 第{i}回')
    
    print(f'\n红楼梦前2回已保存到 {OUTPUT_FILE}')
    print(f'测试完成')

if __name__ == '__main__':
    main()