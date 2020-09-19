# leetcode_python
<h2>Main Takeaways</h2>
<h5>Q14    max()   all()</h5>
To find the longest/shortest string in a list  <br>
max(list,key=len)  key=>lambda
<br>To make a list:<br>
li=[a for a in range(10)]=[1,2,3,4,....10]<br>
li=list(range(10))

<h5>Q9   [::-1]   slice  </h5>
Reverse String <br>
str(x)=>str(x)[::-1]
##namedtuple from collections

Exprience = namedtuple("myexperience":('driving','coding','flying','learning'))
e=Experience(2,4,5,6)
output>>> myexperince(driving = 2,coding = 4,flying =5,learning=6)

string="ilovepython"
sli=slice(3)=slice(0,3)=slice(0,3,1)
string[sli]=string[0:3]=string[0:3:1]

<h5>Q21 </h5>
if not a or not b: <br>
    print(a or b)

<h5>Q66 map()</h5>
map(function,iterables)

<h5>sorted() return new list/string  & OBJ.sort() do not handle string . inline operation</h5>
  sorted('dbca') ='abcd'
sort is list.methods 
sorted can work on any iterative obejcts.
sorted(iterable, cmp=None, key=None, reverse=False)
example: => see 'hackerrank\Print Function.py'
