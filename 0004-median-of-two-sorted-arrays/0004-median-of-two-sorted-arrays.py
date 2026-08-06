class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        num3 = nums1 + nums2
        num3.sort()

        n = len(num3)
        
        if n % 2 ==1:
            return float(num3[n//2])
        return (num3[n//2-1]+num3[n//2])/2.0    
        