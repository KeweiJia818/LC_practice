# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
	def maxDepth(self, root):
		if root == None:
			return 0


		def helper(node):

			if node.left == None and node.right == None:
				return 1
			else:
				if node.left == None:
					return 1 + helper(node.right)
				elif node.right == None:
					return 1 + helper(node.left)
				else:
					return 1 + max(helper(node.left), helper(node.right))

		return helper(root)


x = Solution()

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.left = b
b.right = c

print x.maxDepth(a)