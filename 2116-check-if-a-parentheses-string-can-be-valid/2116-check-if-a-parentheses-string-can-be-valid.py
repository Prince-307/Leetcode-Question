class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        n = len(s)

        if n % 2 != 0:
            return False

        balance = 0

        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

        balance = 0

        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

        return True
            