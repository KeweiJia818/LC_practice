class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums)<=1:
            return False
            
        temp = sorted(nums)
            
        for i in range(0, len(nums)-1):
            if temp[i]== temp[i+1]:
                return True
                
        return False
