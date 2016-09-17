#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pointer1 = l1
        pointer2 = l2

        if l1 == None and l2 == None:
        	return None
        elif l1 == None:
        	return l2
        elif l2 == None:
        	return l1
        else:
        	if l1.val < l2.val:
        		head = ListNode(l1.val)
        		pointer = head
        		pointer1 = pointer1.next
        	else:
        		head = ListNode(l2.val)
        		pointer = head
        		pointer2 = pointer2.next
        	
        	while (pointer1!= None and pointer2!= None):
        		if pointer1.val < pointer2.val:
        			temp = ListNode(pointer1.val)
        			pointer.next = temp
        			pointer = pointer.next
        			pointer1 = pointer1.next
        		else:
        			temp = ListNode(pointer2.val)
        			pointer.next = temp
        			pointer = pointer.next
        			pointer2 = pointer2.next

        	if pointer1 == None:
        		pointer.next = pointer2
        		return head
        	else:
        		pointer.next = pointer1
        		return head