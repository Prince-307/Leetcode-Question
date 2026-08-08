class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                ans.add(tuple(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])

        return [list(x) for x in ans]




        