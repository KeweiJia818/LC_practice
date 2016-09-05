# Definition for singly-linked list.
 

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None	

    def set_next(self, x):
    	self.next = x

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        #:type l1: ListNode
        #:type l2: ListNode
        #:rtype: ListNode
        """
        leftPointer = l1
        rightPointer = l2
        leftNumberinStr = ''
        rightNumberinStr = ''
        while True:
        	if leftPointer ==None:
        		break

        	leftNumberinStr = leftNumberinStr + str(leftPointer.val)
        	leftPointer = leftPointer.next

        while True:
        	if rightPointer ==None:
        		break

        	rightNumberinStr = rightNumberinStr + str(rightPointer.val)
        	rightPointer = rightPointer.next

       	sum = int(leftNumberinStr[::-1]) + int(rightNumberinStr[::-1])

       	realsum = str(sum)[::-1]
       	print realsum
       	head = ListNode(int(realsum[0]))
       	
       	answer = head



       	for i in range(1, len(realsum)):
       		temp = ListNode(int(realsum[i]))
       		answer.next = temp
       		answer = answer.next

       	return head
