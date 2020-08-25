class Solution:
    def lengthOfLongestSubstring(self, s):
        str_list = []
        length = 0
        for char in s:
            if char in str_list:
                str_list = str_list[str_list.index(char) + 1:]

            str_list.append(char)
            length = max(length, len(str_list))
        return length


object = Solution()
answer = object.lengthOfLongestSubstring(s='iloveyouloveyou')
print(answer)
