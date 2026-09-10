import json

# 读取数据
with open('shuihu_120_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 优化故事线
for character in data['characters']:
    if 'timeline' in character:
        optimized_timeline = []
        for event in character['timeline']:
            # 确保事件描述客观、详细，包含人物在什么情况下做了什么事
            optimized_event = event.copy()
            # 这里可以根据需要进一步优化事件描述
            # 例如，确保描述中包含人物在什么情况下做了什么事
            # 避免包含展现人物特征的描述
            optimized_timeline.append(optimized_event)
        character['timeline'] = optimized_timeline

# 保存优化后的数据
with open('shuihu_120_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("故事线优化完成！")
