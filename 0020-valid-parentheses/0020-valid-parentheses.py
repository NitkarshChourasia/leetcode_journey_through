class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_pairs:
                # Current character is a closing bracket
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False  # Invalid closing bracket
            else:
                # Current character is an opening bracket, push onto the stack
                stack.append(char)

        return not stack  # String is valid if the stack is empty at the end
