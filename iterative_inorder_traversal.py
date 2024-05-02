

class Node:
    def __init__(self,  value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def iterativeInOrderTraversal(tree, callback): # Verified on AlgoExpert
    cur: Node = tree
    while cur:
        if not hasattr(cur, 'leftVisited'):
            cur.leftVisited = True
            if cur.left:
                cur = cur.left
        elif not hasattr(cur, 'selfVisited'):
            callback(cur)
            cur.selfVisited = True
        elif not hasattr(cur, 'rightVisited'):
            cur.rightVisited = True
            if cur.right:
                cur = cur.right
        else:
            cur = cur.parent
