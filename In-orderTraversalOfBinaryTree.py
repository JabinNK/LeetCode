class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []  
        # 中序递归 
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)