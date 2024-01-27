import re

# 定义文本
text = '''
你好
![Markdown Image 1](image1.png)
在干什么？
<img src="img/HTML Image 1.png" style="zoom:80%;" />
好的你行
![Markdown Image 2](image2.png)
<img src="img/HTML Image 2.png" style="zoom:80%;" />
'''

# 使用正则表达式定义分隔符
split_pattern = r'(?:\!\[.*?\]\(.*?\)|<img.*?src=["\'](.*?)["\'].*?>)'

# 使用正则表达式进行分割
split_texts = re.split(split_pattern, text)

# 分别保存文字和图片地址的列表
text_list = []
image_url_list = []
def is_image_file(filename):
    image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp']

    # 正则表达式匹配文件名是否以图片扩展名结尾
    pattern = re.compile(r'\.(' + '|'.join(image_extensions) + ')$', re.IGNORECASE)
    return bool(pattern.search(filename))
for index , part in enumerate(split_texts):
    if part is not None:
        stripped_part = part.strip()
        if stripped_part:
            if is_image_file(stripped_part):
                image_url_list.append(stripped_part)
            else:
                text_list.append(stripped_part)

# 打印结果
print("文字列表:", text_list)
print("图片地址列表:", image_url_list)
