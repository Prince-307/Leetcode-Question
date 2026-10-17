class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        n = len(nums)

        # Sort by digit sum, then by the number itself
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its correct index
        position = {value: i for i, value in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or position[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = position[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
