import re 
import os

dir_path = 'some/file/name_001.txt'
file_name = os.listdir(dir_path)

file_num = re.findall("name_(\d+).txt")
print(file_num)
