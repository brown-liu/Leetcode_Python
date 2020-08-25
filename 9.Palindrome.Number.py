class Solution:
    def isPalindrome(self, x):
        temp = str(x)
        reverse = ''
        for i in range(len(temp) - 1, -1, -1):
            reverse += temp[i]
        if reverse == temp:
            return True
        else:
            return False


question = [141, 3883, 134, 541]
answer = [True, True, False, False]

solution = Solution()
result = []
for q in question:
    job = solution.isPalindrome(q)
    result.append(job)
print(result)
if result == answer:
    print('correct')
else:
    print('wrong')

## Other solutions
# str(x)==str(x)[::-1]
