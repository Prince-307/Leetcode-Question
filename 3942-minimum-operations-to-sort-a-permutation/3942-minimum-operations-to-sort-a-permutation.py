class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = float('inf')

        # Case 1: Increasing cyclic order
        if all(nums[i] == (nums[0] + i) % n
               for i in range(n)):

            k = nums[0]
            ans = min(ans, (n - k) % n, k + 2)

        # Case 2: Decreasing cyclic order
        if all(nums[i] == (nums[0] - i) % n
               for i in range(n)):

            k = (n - 1 - nums[0]) % n
            ans = min(ans, 1 + min(k, (n - k) % n))

        return ans if ans != float('inf') else -1