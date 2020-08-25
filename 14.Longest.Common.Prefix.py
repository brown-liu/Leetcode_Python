class Solution:
    def longestCommonPrefix(self, strs):
        output = ''
        if len(strs) == 0:
            return output
        for i in range(len(min(strs))):
            same_char = strs[0][i]
            if all(a[i] == same_char for a in strs):
                output += same_char
            else:
                break
        return output


test = ['ccadcabc', 'cc', 'ccadcfd', 'ccadcbcdef']
solution = Solution()
print(solution.longestCommonPrefix(test))
