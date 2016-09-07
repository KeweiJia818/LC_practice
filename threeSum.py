class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = []
        sortedList = sorted(nums)

        for i in range(1, len(nums)-1):
        	left = 0
        	right = len(nums) - 1

        	while True:
        		if (sortedList[left] + sortedList[i] + sortedList[right]) == 0:
        			answer.append([sortedList[left], sortedList[i], sortedList[right]])
        			if left == i-1 or right == i+1:
        				break
        			else:
        				left = left +1
        				right = right - 1
        		elif (sortedList[left] + sortedList[i] + sortedList[right]) > 0:
        			right = right - 1
        			if right <= i:
        				break
        		elif (sortedList[left] + sortedList[i] + sortedList[right]) < 0:
        			left = left + 1
        			if left >= i:
        				break
        
        unified = []
        for i in range(0, len(answer)):
        	if i ==0:
        		unified.append(answer[0])
        	else:
        		noDuplicate = True
        		for candidate in unified:
        			if set(answer[i])== set(candidate):
        				noDuplicate = False
        		if noDuplicate:
        			unified.append(answer[i])
        return unified










a = Solution()

print a.threeSum([7,5,-8,-6,-13,7,10,1,1,-4,-14,0,-1,-10,1,-13,-4,6,-11,8,-6,0,0,-5,0,11,-9,8,2,-6,4,-14,6,4,-5,0,-12,12,-13,5,-6,10,-10,0,7,-2,-5,-12,12,-9,12,-9,6,-11,1,14,8,-1,7,-13,8,-11,-11,0,0,-1,-15,3,-11,9,-7,-10,4,-2,5,-4,12,7,-8,9,14,-11,7,5,-15,-15,-4,0,0,-11,3,-15,-15,7,0,0,13,-7,-12,9,9,-3,14,-1,2,5,2,-9,-3,1,7,-12,-3,-1,1,-2,0,12,5,7,8,-7,7,8,7,-15])


