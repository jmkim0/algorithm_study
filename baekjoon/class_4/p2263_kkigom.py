import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i

def preorder(inorder_left, inorder_right, postorder_left, postorder_right):
    if inorder_left > inorder_right or postorder_left > postorder_right:
        return
    
    parent = postorder[postorder_right]
    print(parent, end = " ")

    left_cnt = pos[parent] - inorder_left
    right_cnt = inorder_right - pos[parent]

    preorder(inorder_left, inorder_left + left_cnt - 1, postorder_left, postorder_left + left_cnt - 1)
    preorder(inorder_right - right_cnt + 1, inorder_right, postorder_right - right_cnt, postorder_right - 1)

preorder(0, n - 1, 0, n - 1)