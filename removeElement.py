class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
        	return len(nums)

        if len(nums) == 0:
        	return 0
        

        counter = 0

        for i in range(0, len(nums)):
        	if nums[i]!=val:
        		counter = counter +1
       	i, j = 0, len(nums) - 1
        while True:
        	if nums[i] != val and nums[j] != val:
        		i = i+1
        	elif nums[i] != val and nums[j] == val:
        		i = i+1
        		j = j-1
        	elif nums[i] == val and nums[j] != val:
        		nums[i], nums[j] = nums[j], nums[i]
        	else:
        		j = j-1


        	if i>j:
        		break


a = Solution()

a.removeElement([1], 1)
