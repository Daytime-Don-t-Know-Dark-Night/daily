# -*-coding:utf-8-*- 
# ���ߣ�   29511
# �ļ���:  generate_multiple_txt_files.py
# ����ʱ�䣺2021/5/12��11:13
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
