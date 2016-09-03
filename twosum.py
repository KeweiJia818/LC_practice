
class Solution(object):
	def twoSum(self, nums, target):
		for i in range(0, len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i]+ nums[j] ==target:
					answer = []
					answer.append(i)
					answer.append(j)
					return answer



a = Solution()

print a.twoSum([3,2,4], 6)
