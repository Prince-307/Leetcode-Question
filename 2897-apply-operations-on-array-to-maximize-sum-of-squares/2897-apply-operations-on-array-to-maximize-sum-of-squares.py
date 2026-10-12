class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        bits = [0] * 32

        # Count set bits at each position
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bits[i] += 1

        ans = 0

        # Construct k maximum numbers
        for _ in range(k):
            num = 0

            for i in range(32):
                if bits[i] > 0:
                    num |= (1 << i)
                    bits[i] -= 1

            ans = (ans + num * num) % MOD

        return ans
        