# path=r'D:\PycharmProjects\leetcode_python'
# import os
# list_file=os.listdir(path)
# for i in list_file:
#     if i[1]=='_'or i[2]=='_':
#         new=i.replace('_','.')
#         os.rename(i,new)


from collections import Counter
s='asdgSDgasfga'
a=[x for x in s]

print(a.count('a'))
x='2 2 2 3 4 4'
arr = map(int, x.split())
print(max(list(arr)))
