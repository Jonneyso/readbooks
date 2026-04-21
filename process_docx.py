from docx import Document
import json

# 读取Word文档
doc = Document(r'c:\Users\su\Documents\trae_projects\readbooks\hongloumeng\红楼梦100个人物简介及最终结局.docx')

# 提取内容
content = []
for para in doc.paragraphs:
    if para.text.strip():
        content.append(para.text)

# 解析人物信息
characters_from_doc = []
for para in content:
    # 检查是否是人物条目（以数字编号开始）
    if para[0].isdigit():
        # 提取人物信息
        parts = para.split('、', 1)
        if len(parts) == 2:
            # 提取姓名
            name_part = parts[1].split('，', 1)[0]
            name = name_part
            
            # 提取描述
            description = parts[1].split('，', 1)[1] if len(parts[1].split('，', 1)) > 1 else ""
            
            # 创建人物对象
            character = {
                "name": name,
                "description": description
            }
            characters_from_doc.append(character)

# 读取现有JSON数据
with open(r'c:\Users\su\Documents\trae_projects\readbooks\hongloumeng\hongloumeng_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 合并人物信息
existing_names = {char['name'] for char in data['characters']}

for char_from_doc in characters_from_doc:
    name = char_from_doc['name']
    if name not in existing_names:
        # 添加新人物
        new_character = {
            "name": name,
            "nickname": name,
            "alias": [],
            "star": "",
            "portrait": {
                "appearance": "",
                "personality": "",
                "skills": "",
                "特点": char_from_doc['description']
            },
            "timeline": []
        }
        data['characters'].append(new_character)
        print(f"添加新人物: {name}")
    else:
        # 更新现有人物
        for char in data['characters']:
            if char['name'] == name:
                if '特点' in char['portrait']:
                    char['portrait']['特点'] += f"。{char_from_doc['description']}"
                else:
                    char['portrait']['特点'] = char_from_doc['description']
                print(f"更新人物: {name}")
                break

# 保存更新后的数据
with open(r'c:\Users\su\Documents\trae_projects\readbooks\hongloumeng\hongloumeng_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("处理完成！")
