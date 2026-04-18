import requests
from bs4 import BeautifulSoup
import os

def get_chapter_content(chapter_url):
    response = requests.get(chapter_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到章节标题
    title = soup.find('h1').text.strip() if soup.find('h1') else ''
    
    # 找到内容区域
    content_div = soup.find('div', class_='grap')
    if content_div:
        # 提取所有段落
        paragraphs = content_div.find_all('p')
        content = '\n'.join([p.text.strip() for p in paragraphs if p.text.strip()])
        return title, content
    return title, ''

def main():
    base_url = 'https://hongloumeng.5000yan.com'
    index_url = f'{base_url}/index.html'
    
    # 获取目录页面
    response = requests.get(index_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到所有章节链接
    chapter_links = []
    content_div = soup.find('div', class_='grap')
    if content_div:
        links = content_div.find_all('a')
        chapter_links = [base_url + link.get('href') for link in links if link.get('href')]
    
    # 创建输出文件
    output_file = '红楼梦.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('红楼梦\n')
        f.write('曹雪芹、高鹗 著\n')
        f.write('\n')
        
        # 爬取每个章节
        for i, chapter_url in enumerate(chapter_links, 1):
            print(f'正在获取第{i}回...')
            title, content = get_chapter_content(chapter_url)
            if title and content:
                f.write(f'{title}\n')
                f.write(f'{content}\n')
                f.write('\n')
    
    print(f'红楼梦全文已保存到 {output_file}')

if __name__ == '__main__':
    main()