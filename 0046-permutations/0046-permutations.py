class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(path):
          
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return ans
    




        