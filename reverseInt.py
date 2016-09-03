
class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = ''
        if x >=0:
        	for i in range(0, len(str(x))):
        		answer = str(x)[i] + answer
        	return int(answer)
        else:
        	temp = x*-1
        	for i in range(0, len(str(temp))):
        		answer = str(temp)[i] + answer
        	return int('-'+answer)




