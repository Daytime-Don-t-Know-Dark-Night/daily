# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  窗口选择文件返回文件的路径.py
# 日期时间：2021/4/25，17:05
import tkinter as tk
from tkinter import filedialog


def get_local_file():
    """
    选择本地文件
    :return: 返回选择文件的路径
    """
    root = tk.Tk()
    root.withdraw()
    get_file_path = filedialog.askopenfilename()
    return get_file_path


if __name__ == '__main__':
    file_path = get_local_file()
    print('文件路径：', file_path)
