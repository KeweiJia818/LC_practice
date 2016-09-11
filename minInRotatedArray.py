import math
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        def helper(nums):

        	if len(nums) == 1:
        		return nums[0]
        	elif len(nums) ==2:
        		return min(nums[0], nums[1])
        	else:
        		found = False
        		for i in range(int(math.log(len(nums), 2)) ):
        			if nums[2**i-1] > nums[2**(i+1) - 1]:
        				found = True
        				return helper(nums[2**i-1 : 2**(i+1)])

        		if not found:
        			if nums[2**(i+1) - 1] <= nums[len(nums) - 1]:
        				return nums[0]
        			else:
        				return helper(nums[2**(i+1) - 1:])

        return helper(nums)
        			



a = Solution()

print a.findMin([3,4,5,6,7,1,2])

