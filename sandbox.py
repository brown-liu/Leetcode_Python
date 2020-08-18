path=r'D:\PycharmProjects\leetcode_python'
import os
list_file=os.listdir(path)
for i in list_file:
    if i[1]=='_'or i[2]=='_':
        new=i.replace('_','.')
        os.rename(i,new)
