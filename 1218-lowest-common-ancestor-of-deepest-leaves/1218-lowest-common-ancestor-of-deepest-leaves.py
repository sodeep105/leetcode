# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def dfs(node, depth):
            if not node:
                return depth, None  # Return depth and None (no LCA at this point)

            left_depth, left_lca = dfs(node.left, depth + 1)
            right_depth, right_lca = dfs(node.right, depth + 1)

            if left_depth == right_depth:  # If both subtrees have deepest leaves
                return left_depth, node  # This node is the LCA
            elif left_depth > right_depth:
                return left_depth, left_lca  # Deeper subtree LCA
            else:
                return right_depth, right_lca  # Deeper subtree LCA

        return dfs(root, 0)[1]  # Extract only the LCA from return values

