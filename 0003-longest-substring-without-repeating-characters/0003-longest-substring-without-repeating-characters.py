class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = 0
        max_count = 0

        for right in range(len(s)):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            max_count = max(max_count, right - left + 1)

        return max_count