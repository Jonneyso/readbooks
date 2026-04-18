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
            
            # 根据人物和事件进行更详细的优化
            name = character['name']
            chapter = event.get('chapter')
            title = event.get('title')
            
            # 吴用的事件优化
            if name == "吴用":
                if chapter == 19 and "林冲水寨大并火 晁盖梁山小夺泊" in title:
                    optimized_event['event'] = "吴用识破王伦嫉贤妒能与林冲积怨，暗中激将林冲，席间以暗号示意，促成火并王伦，拥立晁盖执掌梁山。"
            
            # 其他人物的事件优化可以在这里添加
            # 例如：
            # if name == "宋江":
            #     if chapter == 18 and "宋公明私放晁天王" in title:
            #         optimized_event['event'] = "宋江得知晁盖等人智取生辰纲事发，官府前来捉拿，便稳住公差，暗中通风报信，使晁盖等人得以逃脱官府追捕。"
            
            optimized_timeline.append(optimized_event)
        character['timeline'] = optimized_timeline

# 保存优化后的数据
with open('shuihu_120_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("故事线优化完成！")
