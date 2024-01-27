#作者：戏人看戏
#qq: 3500079813
import glob
import os
import subprocess
import time
import re
from pynput.keyboard import  Controller
import pyperclip as pc
def copy_image_to_clipboard(file_path):
    # 检查文件是否存在
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
md_files = glob.glob('*.md')
# file_path = '设计模式-day01.md'
with open(md_files[0], 'r', encoding='utf-8') as file:
    text = file.read()

# 输出读取的文本内容
# print(text)


# 使用正则表达式为分隔符分割文本，并获取图片地址
split_pattern = r'\!\[.*?\]\(.*?\)'
image_urls = re.findall(r'\!\[.*?\]\((.*?)\)', text)
split_parts = re.split(split_pattern, text)

# 过滤掉空字符串
split_parts = [part.strip() for part in split_parts if part.strip()]

keyboard = Controller()
def wrap():
    #换行
    pc.copy("\r\n" )
    # 调用函数执行粘贴操作
    paste_image_to_textbox()
    time.sleep(1)
# 输出分割后的文本列表和提取的图片地址列表
print("Split Text:")
for index, part in enumerate(split_parts):
    print("------")
    part  = part + "\r\n" 
    pc.copy(part)
    time.sleep(1)
    # 调用函数执行粘贴操作
    paste_image_to_textbox()
    # pyautogui.hotkey("ctrl", "v")
    if index < len(image_urls):
        copy_image_to_clipboard(image_urls[index])
        # 调用函数执行粘贴操作
        paste_image_to_textbox()
        time.sleep(1)
        wrap()
        

print("\nImage URLs:", image_urls)