class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # low cannot be negative
            if low < 0:
                low = 0

            # Even the maximum possibility is negative
            if high < 0:
                return False

        return low == 0