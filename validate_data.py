import json

try:
    with open('shuihu_120_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('JSON file is valid.')
    print(f'Total characters: {len(data["characters"])}')
    print('First 10 characters:')
    for i, character in enumerate(data["characters"][:10]):
        print(f'{i+1}. {character["name"]} ({character["nickname"]})')
    print('\nLast 10 characters:')
    for i, character in enumerate(data["characters"][-10:]):
        print(f'{i+1}. {character["name"]} ({character["nickname"]})')
except json.JSONDecodeError as e:
    print(f'JSON decode error: {e}')
except Exception as e:
    print(f'Error: {e}')
