#################################################Multi Dimention#############################################################
# x=1
# y=1
# z=1
# n=2
#
#
# list=[[a,b,c] for a in range(x+1)  for b in range(y+1) for c in range(z+1) if a+b+c!=n]
# print(list)

############################################Nested Lists#######################################################################
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

newlist=sorted(students,key=lambda x:(-x[1],x[0]),reverse=True)

for i in range(len([x for x in newlist if x[1]==newlist[0][1]])):
    newlist.pop(0)
li=[]
for i in range(len([x for x in newlist if x[1]==newlist[0][1]])):
    li.append(newlist.pop(0))
li.sort()
for i in li:
    print(i[0])