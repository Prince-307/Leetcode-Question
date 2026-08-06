class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result=[]

        for i in range(len(nums)-2):

            left = i+1
            right = len(nums)-1

            while left<right:
                total = nums[i]+nums[left]+nums[right]

                if total==0:
                    triplet = [nums[i],nums[left],nums[right]]

                    if triplet not in result:
                        result.append(triplet)

                    left = left + 1
                    right = right -1    

                elif total<0:
                    left = left+1
                else:
                    right = right-1
        return result                
                        
        