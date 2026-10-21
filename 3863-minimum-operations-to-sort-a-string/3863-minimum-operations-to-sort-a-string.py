class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == ''.join(sorted(s)):
            return 0

        n = len(s)
        mn = min(s)
        mx = max(s)

        if n == 1:
            return 0

        if s[0] == mn or s[-1] == mx:
            return 1

        if n == 2:
            return -1

        # Check whether mn appears before the last position
        # or mx appears after the first position
        if mn in s[:-1] or mx in s[1:]:
            return 2

        return 3
