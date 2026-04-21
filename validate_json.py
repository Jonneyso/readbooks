import json

with open('hongloumeng/hongloumeng_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print('JSON文件语法正确，包含', len(data['characters']), '个人物')
