import os, sys

files1 = [item for item in os.listdir('.') if os.path.splitext(item)[-1] == '.mobi']
files2 = [item for item in os.listdir('.') if 'Vol' in item]

count = 1
for item in files2:
    if os.path.isfile(item):
        os.remove(item)
    # os.rename(item, '我想重命名(%s).mp4' %count)
    # count += 1

