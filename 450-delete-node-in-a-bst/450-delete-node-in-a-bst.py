# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        
        if not root.right:
            temp = root.left
            del root
            return temp
        elif not root.left:
            temp = root.right
            del root
            return temp
        else:
            succParent = root
            succ = root.right

            while succ.left:
                succParent = succ
                succ = succ.left
            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
            
            root.val = succ.val
            del succ
            return root