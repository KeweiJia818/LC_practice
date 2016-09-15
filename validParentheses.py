class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack_alike = []
        
        for i in range(len(s)):
        	if len(stack_alike) == 0:
        		if s[i] == '(' or s[i] == '[' or s[i] == '{':
        			stack_alike.append(s[i])
        		else:
        			return False
        	else:
        		if s[i] == '(' or s[i] == '[' or s[i] == '{':
        			stack_alike.append(s[i])
        		else:
        			if s[i] == ')':
        				if stack_alike[len(stack_alike) - 1] == '(':
        					stack_alike = stack_alike[0:len(stack_alike) - 1]
        				else:
        					return False
        			elif s[i] == ']':
        				if stack_alike[len(stack_alike) - 1] == '[':
        					stack_alike = stack_alike[0:len(stack_alike) - 1]
        				else:
        					return False
        			else:
        				if stack_alike[len(stack_alike) - 1] == '{':
        					stack_alike = stack_alike[0:len(stack_alike) - 1]
        				else:
        					return False

       	if len(stack_alike) == 0:
       		return True
       	else:
       		return False


a = Solution()
print a.isValid('{{[]}}')




