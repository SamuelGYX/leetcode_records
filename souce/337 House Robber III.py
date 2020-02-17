'''
337. House Robber III
Medium

Rob a binary tree without adjacent elements.

Solution:

	DFS with two return values:
		
		0 max loot without root
		1 max loot with root
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(f):
            if not f:
                return (0, 0)
            l, r = dfs(f.left), dfs(f.right)
            return (max(l) + max(r), f.val + l[0] + r[0])
        return max(dfs(root))