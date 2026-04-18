import json

# 读取数据
with open('shuihu_120_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查所有人物的故事线
for character in data['characters']:
    name = character['name']
    timeline = character.get('timeline', [])
    
    print(f"\n检查人物: {name}")
    print(f"故事线长度: {len(timeline)}")
    
    if len(timeline) == 0:
        print("警告: 该人物没有故事线")
    else:
        # 检查首次出场
        first_event = timeline[0]
        print(f"首次出场: 第{first_event.get('chapter')}回 {first_event.get('title')}")
        
        # 检查最终结局
        last_event = timeline[-1]
        print(f"最终结局: 第{last_event.get('chapter')}回 {last_event.get('title')}")
        
        # 检查故事线是否完整
        if len(timeline) < 3:
            print("警告: 该人物的故事线可能不完整")

print("\n故事线检查完成！")
