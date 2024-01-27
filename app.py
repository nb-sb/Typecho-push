import re
import time
from pynput.keyboard import Key, Controller
from PIL import Image
import win32clipboard
from io import BytesIO
from io import BytesIO
import win32clipboard
from PIL import Image
import pyperclip as pc
import time
import pyautogui
#作者：戏人看戏
#qq: 3500079813
def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


# 从文件中读取文本内容
file_path = '设计模式-day01.md'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 输出读取的文本内容
print(text)


# 使用正则表达式为分隔符分割文本，并获取图片地址
split_pattern = r'\!\[.*?\]\(.*?\)'
image_urls = re.findall(r'\!\[.*?\]\((.*?)\)', text)
split_parts = re.split(split_pattern, text)

# 过滤掉空字符串
split_parts = [part.strip() for part in split_parts if part.strip()]

keyboard = Controller()

# 输出分割后的文本列表和提取的图片地址列表
print("Split Text:")
for index, part in enumerate(split_parts):
    print("------")
    print(part)
    # # 输入文本
    # for char in part:
    #     print(char)
    #     keyboard.press(char)
    #     keyboard.release(char)
    #     time.sleep(0.00005)
    part  = part + "\n"
    pc.copy(part)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    if index < len(image_urls):
        # send_to_clipboard(image_urls[index])  # 将图片复制到剪贴板
        # image_path = r'1233.png'  # 图片绝对路径
        image_path = image_urls[index] # 图片绝对路径
        image = Image.open(image_path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        send_to_clipboard(win32clipboard.CF_DIB, data)
        time.sleep(1)  # 等待剪贴板操作完成
        # 模拟粘贴操作
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl)
        time.sleep(1)
        #换行
        pc.copy("\n")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")

print("\nImage URLs:", image_urls)