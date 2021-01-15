def searchBST(root, val):
    curr = root
    while curr.val != val:
        if curr.val > val:
            if curr.left:
                curr = curr.left
            else:
                return None
        else:
            if curr.right:
                curr = curr.right
            else:
                return None
    return curr
