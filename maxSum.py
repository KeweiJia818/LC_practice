
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]

        for i in range(1, len(nums)):
        	if dp[len(dp) - 1] < 0:
        		dp.append(nums[i]) 
        	else:
        		dp.append(dp[len(dp) - 1] + nums[i])
        		
        return max(dp)


       	







a = Solution()
print a.maxSubArray([1,2,3,4,5])