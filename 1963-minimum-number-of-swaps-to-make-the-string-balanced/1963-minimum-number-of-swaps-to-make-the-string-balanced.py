class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        unmatched = 0

        for char in s:
            if char == '[':
                unmatched += 1

            elif unmatched > 0:
                unmatched -= 1

        return (unmatched + 1) // 2
        