class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        answer = [1,2]
        if n == 1 or n ==2:
            return n
        
        for i in range(2, n):
            answer.append(answer[len(answer) - 1] + answer[len(answer) - 2])
            
        return answer[len(answer) - 1]