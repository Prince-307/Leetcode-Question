class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=lambda x: x * x)

        ans = 0
        n = len(nums)

        for i in range(n):
            if i < (n + 1) // 2:
                ans += nums[n - 1 - i] ** 2
            else:
                ans -= nums[i - (n + 1) // 2] ** 2

        return ans