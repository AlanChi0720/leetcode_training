class Solution:
    def isSymmetric(self, root): # recursively
        if not root:
            return True
        return self.isSym(root.left, root.right)
    def isSym(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return self.isSym(root1.left, root2.right) and self.isSym(root1.right, root2.left)

class Solution:
    def isSymmetric(root) -> bool:
        """
        DFS solution with stack
        Each time pop two elements from stack
        Notice the alternating appending of right and left nodes respectively
        """
        if not root:
            return True
        stack = [root, root]
        while stack:
            r1 = stack.pop()
            r2 = stack.pop()
            if (not r1) and (not r2):
                continue
            if (not r1) or (not r2):
                return False
            if r1.val != r2.val:
                return False
            stack.append(r1.left)
            stack.append(r2.right)
            stack.append(r1.right)
            stack.append(r2.left)
        return True