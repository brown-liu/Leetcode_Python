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

string="ilovepython"
sli=slice(3)=slice(0,3)=slice(0,3,1)
string[sli]=string[0:3]=string[0:3:1]

<h5>Q20 pop()</h5>
pop() will kick the last item out.
if a.pop() >10: => no matter if condition is True or False, pop() will act.