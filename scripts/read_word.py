import win32com.client

# 创建Word应用实例
word = win32com.client.Dispatch('Word.Application')
word.Visible = False

# 打开文档
doc = word.Documents.Open(r'c:\Users\su\Documents\trae_projects\readbooks\hongloumeng\红楼梦 100个人 物简介及最终结局！.docx')

# 提取文本
content = doc.Content.Text

# 关闭文档和应用
word.Quit()

# 打印内容
print(content)