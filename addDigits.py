class Solution(object):
    def addDigits(self, num):
    	while (num >= 10):
    		temp = 0
    		for i in range(0, len(str(num))):
    			temp = temp + int(str(num)[i])
    		num = temp
    	return num
a = Solution()
print a.addDigits(38)