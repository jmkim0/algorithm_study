import sys

def preorder(tree, cur):
    result = ''
    l, r = tree[cur]

    result += cur
    if l != '.':
        result += preorder(tree, l)
    if r != '.':
        result += preorder(tree, r)

    return result

def inorder(tree, cur):
    result = ''
    l, r = tree[cur]

    if l != '.':
        result += inorder(tree, l)
    result += cur
    if r != '.':
        result += inorder(tree, r)

    return result

def postorder(tree, cur):
    result = ''
    l, r = tree[cur]

    if l != '.':
        result += postorder(tree, l)
    if r != '.':
        result += postorder(tree, r)
    result += cur

    return result

N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    p, l, r = sys.stdin.readline().split()
    tree[p] = (l, r)

print(preorder(tree, 'A'))
print(inorder(tree, 'A'))
print(postorder(tree, 'A'))
