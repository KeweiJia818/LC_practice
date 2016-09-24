class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 1
        j = 1
        numsLength = len(nums)
        


        while i < numsLength:
        	if (nums[i - 1] < nums[i] ):
        		nums[j] = nums[i]
        		j =j + 1
        	i = i+1

        return len(set(nums))



a = Solution()

print a.removeDuplicates([1,1,2])