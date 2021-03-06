class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect = []
        mydict = {}
        for i in range(0, len(nums1)):
            mydict[i] = nums1[i]
            if mydict[i] in nums2:
                intersect.append(mydict[i])
                nums2.remove(mydict[i])
                
        
        return intersect
            
        