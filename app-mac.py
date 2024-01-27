#作者：戏人看戏
#qq: 3500079813
import glob
import os
import subprocess
import time
import re
from pynput.keyboard import  Controller
import pyperclip as pc

dir_path = str(input("输入你的文件目录："))
time.sleep(5)
def copy_image_to_clipboard(file_path):
    # 检查文件是否存在
    file_path = dir_path + file_path
    if not os.path.exists(file_path):
        print(f"文件 '{file_path}' 不存在")
        return

    # 使用 osascript 将图片复制到剪贴板
    os.system(f"osascript -e 'set the clipboard to (read (POSIX file \"{file_path}\") as JPEG picture)'")

    print(f"已将图片文件 '{file_path}' 复制到剪贴板")
    time.sleep(1)

# # 调用函数并指定文件路径
# copy_image_to_clipboard("img/node.png")

def paste_image_to_textbox():
    applescript = '''
    tell application "System Events"
        keystroke "v" using {command down}
    end tell
    '''

    subprocess.run(['osascript', '-e', applescript])

# 调用函数执行粘贴操作
# paste_image_to_textbox()
# -----------------------

# 从文件中读取文本内容
# 获取当前文件夹中所有的 .md 文件
md_files = glob.glob(dir_path+'*.md')
# file_path = '设计模式-day01.md'
with open(md_files[0], 'r', encoding='utf-8') as file:
    text = file.read()

# 使用正则表达式定义分隔符
split_pattern = r'(?:\!\[.*?\]\(.*?\)|<img.*?src=["\'](.*?)["\'].*?>)'

# 使用正则表达式进行分割
split_texts = re.split(split_pattern, text)
split_texts2 = []
for i in split_texts:
    if i is not None and i != '\n\n':
        split_texts2.append(i)
split_texts = split_texts2
# 分别保存文字和图片地址的列表
text_list = []
image_urls = []
image_count_list = []  # 保存每个文本后的图片数量
def is_image_file(filename):
    image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp']

    # 正则表达式匹配文件名是否以图片扩展名结尾
    pattern = re.compile(r'\.(' + '|'.join(image_extensions) + ')$', re.IGNORECASE)
    return bool(pattern.search(filename))
for index , part in  enumerate(split_texts):
    if part is not None:
        stripped_part = part.strip()
        if stripped_part:
            if is_image_file(stripped_part):
                image_urls.append(stripped_part)
            else:
                text_list.append(stripped_part)
                if index + 1 <= len(split_texts) :
                    if index == len(split_texts)-1:
                        image_count_list.append(0)
                        continue
                    #如果不是图片的话则添加为0
                    if not is_image_file(split_texts[index + 1].strip()):
                        image_count_list.append(0)
                        continue
                # 判断当前文本后面是否有两个图片地址
                if index + 2 <= len(split_texts):
                    if split_texts[index + 1] is not None :
                        if split_texts[index + 2] is not None:
                            if index + 2 < len(split_texts) and is_image_file(split_texts[index + 1].strip()) and is_image_file(split_texts[index + 2].strip()):
                                image_count_list.append(2)
                            else:
                                image_count_list.append(1)
                        else:
                            if index + 2 < len(split_texts) and is_image_file(split_texts[index + 1].strip()) and is_image_file(split_texts[index + 3].strip()):
                                image_count_list.append(2)
                            else:
                                image_count_list.append(1)

# 打印结果
print("文字列表:", text_list)
print("图片地址列表:", image_urls)
print("每个文本后的图片数量列表:", image_count_list)
print(len(text_list) , len(image_urls), len(image_count_list))
keyboard = Controller()
def wrap():
    #换行
    pc.copy("\r\n" )
    # 调用函数执行粘贴操作
    paste_image_to_textbox()
    time.sleep(0.5)
# 输出分割后的文本列表和提取的图片地址列表
print("Split Text:")
for index, part in enumerate(text_list):
    print("------")
    part  = part + "\r\n" 
    pc.copy(part)
    time.sleep(1)
    # 调用函数执行粘贴操作
    paste_image_to_textbox()
    # pyautogui.hotkey("ctrl", "v")
    if index < len(image_urls):
        for ii in range(image_count_list[index]):
            copy_image_to_clipboard(image_urls[index+ii])
            # 调用函数执行粘贴图片操作
            paste_image_to_textbox()
            time.sleep(3)#加长一点时间，防止上传时间不够
            wrap() #换行
        