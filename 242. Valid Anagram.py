class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            if char in t:
                print('yes')
                t = t.replace(char, '')
        print(t)
        if t != '':
            return False
        else:
            return True

    def V2isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True


solution = Solution()
print(solution.isAnagram('abcd', 'dbca'))
