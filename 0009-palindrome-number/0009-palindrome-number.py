class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x1 = str(x)

        reversed_x = x1[::-1]
        if x1 == reversed_x:
            return True
        else:
            return False

        if result < -2**31 or result > 2**31 - 1:
            return False

        