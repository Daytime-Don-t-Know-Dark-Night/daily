# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  generate_multiple_txt_files.py
# 日期时间：2021/5/12，11:13
import os

folder = 'test_folder'
if not os.path.exists(folder):
    os.mkdir(folder)
files_number = 21
for name in range(1, files_number):
    if name < 10:
        name = '0' + str(name)
    filename = str(name) + ".txt"
    f = open(os.path.join(folder, filename), 'w')
    f.close()
print("success")
