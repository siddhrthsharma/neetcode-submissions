class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack or stack[-1] != match[char]:
                    return False
                stack.pop()
                
        return not stack