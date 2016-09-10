# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       	if head == None:
       		return None
       	else:
       		pointer = head
       		reversedList = []
       		storage = []
       		while True:
       			print pointer.val
       			storage.append(ListNode(pointer.val))
       			pointer = pointer.next
       			if pointer == None:
       				break

       		for i in range(len(storage)):
       			reversedList.append(storage[len(storage) - i - 1])

       		answer = reversedList[0]
       		pointer = reversedList[0]
       		for i in range(1, len(reversedList)):
       			pointer.next = reversedList[i]
       			pointer = pointer.next

       		return answer



a = ListNode(1) 
b = ListNode(2)
c = ListNode(3)     
a.next = b
b.next = c 	

temp = Solution()

p = temp.reverseList(a)

while True:
	print p.val
	p = p.next
	if p == None:
		break