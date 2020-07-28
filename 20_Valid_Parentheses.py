class Solution:
    def isValid(self,s):
        left = ['[', '(', '{']
        right = [']', ')', '}']
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if len(stack) <= 0:
                    return False
                if left.index(stack.pop()) != right.index(char):
                    return False
        return len(stack) == 0
