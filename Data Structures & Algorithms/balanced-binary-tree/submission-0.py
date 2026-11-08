# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Here we need to  remember:
        # The computation is between the longest of left tree and longest of right tree's difference
        # so calculate max in both side and see difference

        if not root:
            return True

        
        def hight(node):
            if not node:
                return 0
            return 1+max(hight(node.left),hight(node.right))


        
        left= hight(root.left)
        right= hight(root.right)

        if (abs(left-right)>1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

        #What I learnt here
        #Nested recursivity
        # Here hight, recursively sending rightmost or leftmost longest edge
        # Here isBalanced, recursively calculating if left and right side valid
 






            
            
            


