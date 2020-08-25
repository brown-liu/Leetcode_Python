class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        startnum = '1'
        for i in range(1, n):
            startnum = self.sayNumber(startnum)
        return startnum

    def sayNumber(self, number):
        num = number[0]
        result = ''
        count = 0
        for i in range(len(number)):
            if number[i] == num:
                count += 1
                # print(f"first if,i={num},count={count}")

            elif number[i] != num:
                result += str(count) + number[i - 1]
                count = 1

                num = number[i]
                # print(f'second elif, num= {num} result={result}')
        result += str(count) + num
        return result

    # def ReadString(self,previousOutPut):
    #     string=''
    #     x=''
    #     count = 0
    #     for i in previousOutPut:
    #
    #         if i!=x and count>=1:
    #             string+=str(count)+previousOutPut[previousOutPut.index(i)-1]
    #             count=0
    #             x=i
    #
    #         elif i!=x:
    #             count = 1
    #             x = i
    #         else:
    #             count+=1
    #
    #
    #     return string


testset = {'1112233': '312223', '112222334': '21422314', '44567': '24151617'}

solution = Solution()

# result=solution.sayNumber("112211")
# print(result)
# for i in testset:
#     values=solution.sayNumber(i)
#     print(f"key= {i} ===> {values}")
#     if testset[i]==values:
#         print("correct")

for i in range(10):
    result = solution.countAndSay(i)
    print(result)
