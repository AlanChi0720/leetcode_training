def inorderTraversal(root):
    res = []
    
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res

def inorderTraversal(root):
    res = []
    stack = []
    cur = root

    while cur or stack:
        while cur :
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


n = [1,2,3,4,5,6,7]
print(n.pop())