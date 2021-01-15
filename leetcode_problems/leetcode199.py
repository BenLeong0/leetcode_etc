"""
> Return what a given binary tree would look like from the right
ie rightmost node on each level
BFS - add nodes to the queue starting from the right
At each level, add the first node in the queue (rightmost) to the output
"""

from collections import deque

def rightSideView(root):
    if not root:
        return []

    queue = deque([root])
    output = []

    while queue:
        number_of_nodes = len(queue)
        output.append(queue[0].val)
        for _ in range(number_of_nodes):
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

    return output
