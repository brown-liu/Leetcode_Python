class Solution:
    def countAndSay(self, n: int) -> str:
        out = final= "1"
        for i in range(n):
            final=self.ReadString(out)
            out=final
        return final


    def ReadString(self,previousOutPut):
        string=''
        x=''
        count = 0
        for i in previousOutPut:

            if i!=x and count>=1:
                string+=str(count)+previousOutPut[previousOutPut.index(i)-1]
                count=0
                x=i

            elif i!=x:
                count = 1
                x = i
            else:
                count+=1


        return string





solution=Solution()
result=solution.ReadString("1211")
print(result)
# for i in range(10):
#     print(solution.countAndSay(i))