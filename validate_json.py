import json

try:
    with open('shuihu_120_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('JSON file is valid.')
    print(f'Total characters: {len(str(data))}')
    print(f'Total characters: {len(data["characters"])}')
except json.JSONDecodeError as e:
    print(f'JSON decode error: {e}')
except Exception as e:
    print(f'Error: {e}')
