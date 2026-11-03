class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:

            if char != ')':
                stack.append(char)

            else:
                # Store characters until opening bracket
                temp = []

                while stack and stack[-1] != '(':
                    temp.append(stack.pop())

                # Remove opening bracket
                stack.pop()

                # Push reversed substring back
                stack.extend(temp)

        return ''.join(stack)