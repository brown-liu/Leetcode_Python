class Solution:
    def reverse(self, x):
        str_x = str(x)
        sign = ''
        if str_x.startswith('+') or "-" in str_x:
            sign = str_x[0]
            str_x = str_x[1:]

        str_output = ''
        for i in range(0, len(str_x)):
            str_output += str_x[len(str_x) - i - 1]

        str_output = int(sign + str_output)
        if abs(str_output) >= 2 ** 31 - 1:
            str_output = 0

        return str_output


s = Solution()
li = [129, -1222, 339, 1, 200]
for i in li:
    print(s.reverse(i))

x = 2 ** 32
print(x)
