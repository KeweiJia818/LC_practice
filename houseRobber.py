class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        answer = [0] * len(nums)
        if len(nums) == 0:
        	return 0

        if len(nums) == 1:
        	return nums[0]
        elif len(nums) == 2:
        	return max(nums[0], nums[1])

        for i in range(0, len(nums)):
        	if i ==0:
        		answer[0] = nums[0]
        	elif i ==1:
        		answer[1] = max(nums[0], nums[1])
        	else:
        		answer[i] = max(answer[i-1], nums[i] + answer[i-2])

        return answer[len(answer) - 1]


