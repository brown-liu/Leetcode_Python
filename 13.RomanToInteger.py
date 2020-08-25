class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': (1, None),
            "V": (5, 1),
            "X": (10, 1),
            "L": (50, 10),
            "C": (100, 10),
            "D": (500, 100),
            "M": (1000, 100)
        }
        list = []
        for roman in s:
            if len(list) != 0 and list[-1] == dic[roman][1]:
                list.append(dic[roman][0] - list.pop())
            else:
                list.append(dic[roman][0])
        return sum(list)


solution = Solution()
print(solution.romanToInt('LVIII'))
