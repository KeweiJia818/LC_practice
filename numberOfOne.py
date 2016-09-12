class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
        	return 0
        else:
        	answer = 0
        	temp = bin(n)[2:]
        	print temp
        	for i in range(len(temp)):
        		if temp[i] == '1':
        			answer +=1

        	return answer

a = Solution()

print a.hammingWeight(11)