import sys
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
in_val2idx = {}
post_idx = 0

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_util(inorder, postorder, in_start, in_end):
    global post_idx
     
    if in_start > in_end:
        return None
 
    cur = postorder[post_idx]
    node = Node(cur)
    post_idx -= 1
 
    if in_start == in_end:
        return node

    in_idx = in_val2idx[cur]

    node.right = build_util(inorder, postorder, in_idx + 1, in_end)
    node.left = build_util(inorder, postorder, in_start, in_idx - 1)
 
    return node
 
def build_tree(inorder, postorder):
    global post_idx
    n = len(inorder)
    for i in range(n):
        in_val2idx[inorder[i]] = i
    
    post_idx = n - 1
    return build_util(inorder, postorder, 0, n-1)

def preorder(node):
    if not node:
        return    
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

root = build_tree(inorder, postorder)
preorder(root)