class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        n = len(nums)
        result = set()

        for i in range(n-3):
            for j in range(i+1,n-2):
                left = j+1
                right = n-1

                while left<right:
                    total = nums[i]+nums[j]+nums[left]+nums[right]

                    if total == target:
                        result.add((nums[i],nums[j],nums[left],nums[right]))

                        left+=1
                        right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return [list(x) for x in result]
                       
        


            
                                  