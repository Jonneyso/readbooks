import json

try:
    with open('heroes_ranking.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('Heroes ranking file is valid.')
    print(f'Total heroes: {len(data["ranking"])}')
    print('First 10 heroes:')
    for hero in data["ranking"][:10]:
        print(f'{hero["rank"]}. {hero["name"]}')
    print('\nLast 10 heroes:')
    for hero in data["ranking"][-10:]:
        print(f'{hero["rank"]}. {hero["name"]}')
except json.JSONDecodeError as e:
    print(f'JSON decode error: {e}')
except Exception as e:
    print(f'Error: {e}')
