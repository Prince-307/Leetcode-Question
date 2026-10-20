class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target = sorted(nums)
        ans = 0

        # Generate divisors of n efficiently
        divisors = []
        d = 1

        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d != n // d:
                    divisors.append(n // d)
            d += 1

        for k in divisors:
            valid = True

            for start in range(0, n, k):
                # Find the unique circular descent
                rotation = 0
                descents = 0

                for j in range(k):
                    a = nums[start + j]
                    b = nums[start + (j + 1) % k]

                    if a > b:
                        descents += 1
                        rotation = (j + 1) % k

                        if descents > 1:
                            valid = False
                            break

                if not valid:
                    break

                # Compare the rotated block with its sorted target
                for j in range(k):
                    if nums[start + (rotation + j) % k] != target[start + j]:
                        valid = False
                        break

                if not valid:
                    break

            if valid:
                ans += k

        return ans