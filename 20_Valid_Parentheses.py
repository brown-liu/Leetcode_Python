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

    def isValidAlternative(self, s: str) -> bool:
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []