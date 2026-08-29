class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for ch in s:

            if ch in "({[":
                stack.append(ch)
            else:
                
                if not stack:
                    return False

                top = stack.pop()

                if ch == ')' and top != '(':
                    return False

                if ch == '}' and top != '{':
                    return False

                if ch == ']' and top != '[':
                    return False

        return len(stack) == 0

            


        