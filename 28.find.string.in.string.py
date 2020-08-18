class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle != '':
            # needle_list=[]
            # if len(needle)>2
            # for i in range(1,len(needle)+1):
            #     if needle[i-1] in haystack and needle[i] in haystack:
            #         if abs(haystack.index(needle[i-1])-haystack.index(needle[i]))==1:
            #             return i-1
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1
                # else: return -1

        else:
            return 0
