import urllib.request

def test_network():
    print("测试网络连接...")
    
    try:
        # 测试基本的网络连接
        response = urllib.request.urlopen('https://www.baidu.com', timeout=10)
        print(f"成功连接到百度: {response.status}")
        
        # 测试访问红楼梦网站
        hongloumeng_url = 'https://hongloumeng.5000yan.com'
        response = urllib.request.urlopen(hongloumeng_url, timeout=10)
        print(f"成功连接到红楼梦网站: {response.status}")
        
        # 读取少量内容
        content = response.read(1000).decode('utf-8')
        print("网站内容预览:")
        print(content[:500] + "...")
        
    except Exception as e:
        print(f"网络测试失败: {e}")

if __name__ == '__main__':
    test_network()