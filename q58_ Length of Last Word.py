'''Given a string s consists of upper/lower-case alphabets and empty space characters ' ',

return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        space=''
        for i in range(len(s)):
            space+=' '
        if space == s:
            return 0
        return len(self.findThatLast(s))
    def findThatLast(self,s):

        s=s.split(' ')
        print(s)
        for space in range(s.count('')):
            s.remove('')
        print(s)
        return s[-1]



solution=Solution()
testset=[' a',' ab ','acbc ',' brown liusarah',' brown l ','brown lu','',' asd  asd asdsad asd as d      ','   ']

for i in testset:
    print(solution.lengthOfLastWord(i))

