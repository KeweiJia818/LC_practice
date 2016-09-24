class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k= k%len(nums)
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums)-k]


a = Solution()
a.rotate([1,2], 1)