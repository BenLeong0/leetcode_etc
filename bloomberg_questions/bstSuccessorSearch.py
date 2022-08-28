class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

root = Node(8)
root.left = Node(3,parent=root)
root.left.left=Node(1,parent=root.left)
root.left.right=Node(6,parent=root.left)
root.left.right.left=Node(4,parent=root.left.right)
root.left.right.right=Node(7,parent=root.left.right)
root.right=Node(10,parent=root)
root.right.right=Node(14,parent=root.right)
root.right.right.right=Node(15,parent=root.right.right)

def bstSuccessor(node):
    if node.parent:
        if node == node.parent.left:
            if node.right:
                curr = node.right
                while curr.left:
                    curr = curr.left
                return curr.val
            return node.parent.val
        else:
            ansc=desc=None

            if node.right:
                desc=node.right
                while desc.left:
                    desc = desc.left
            if node.parent:
                ansc = node.parent
                while ansc.parent:
                    if ansc == ansc.parent.left:
                        ansc = ansc.parent
                        break
                    ansc = ansc.parent
                    if ansc == root:
                        ansc=None
                        break

            if ansc and desc:
                return min(ansc,desc,key=lambda x:x.val).val
            elif ansc:
                return ansc.val
            elif desc:
                return desc.val
            else:
                return -1

    else:
        if node.right:
            desc=node.right
            while desc.left:
                desc = desc.left
            return desc.val
        else:
            return -1

print(bstSuccessor(root.left))
