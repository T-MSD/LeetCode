# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def traverse(node, array):
      if node != None:
        traverse(node.left, array)
        array.append(node.val)
        traverse(node.right, array)

    array = []
    traverse(root, array)
    return array 