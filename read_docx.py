from docx import Document

# 读取Word文档
doc = Document(r'c:\Users\su\Documents\trae_projects\readbooks\hongloumeng\红楼梦100个人物简介及最终结局.docx')

# 提取内容
content = []
for para in doc.paragraphs:
    if para.text.strip():
        content.append(para.text)

# 打印内容
print('\n'.join(content))