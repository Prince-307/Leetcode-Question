class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] & nums[j] is target:
        #             return [i,j]
        # return [-1,-1]  

        # left = 0
        # right = len(nums)-1

        # while left < right:
        #     if nums[left] == target and nums[right] == target:
        #         return [left, right]

        #     if nums[left]< target:
        #         left+=1
        #     if nums[right]>target:
        #         right-=1

        # return [-1,-1]    

        def first():
            left=0 
            right =len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1     
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def last():
            left=0
            right =len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1      
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [first(), last()]

        