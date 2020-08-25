"""Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321."""


class Solution:
    def plusOne(self, digits):
        if digits == [0]:
            return [1]
        dig = ''
        for i in digits:
            dig += str(i)
        number = int(dig)
        number += 1
        strNum = str(number)
        return [i for i in strNum]


testSet = [['2', '4', '5', '2'], ['0'], ['1', '9'], ['1', '2', '3']]

## Alternative
# return list(map(int, list(str(int(''.join(map(str, digits)))+1))))


solution = Solution()
for i in (testSet):
    print(solution.plusOne(i))
