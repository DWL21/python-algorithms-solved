from collections import defaultdict

ROOT = "A"
NONE = "."


binary_tree = dict()
N = int(input())
for _ in range(N):
    parent, left, right = input().split()
    binary_tree[parent] = (left, right)

stack = [ROOT]
visited = defaultdict(bool)
preorder_result = []

while stack:
    now = stack.pop()
    left, right = binary_tree[now]
    if visited[now]:
        continue
    preorder_result.append(now)
    visited[now] = True
    if right is not NONE and not visited[right]:
        stack.append(right)
    if left is not NONE and not visited[left]:
        stack.append(left)


stack = [ROOT]
visited = defaultdict(bool)
inorder_result = []

while stack:
    now = stack.pop()
    left, right = binary_tree[now]
    if visited[now]:
        continue
    if right is not NONE and not visited[right]:
        stack.append(right)
    stack.append(now)
    if left is not NONE and not visited[left]:
        stack.append(left)
    else:
        inorder_result.append(now)
        visited[now] = True


stack = [ROOT]
visited = defaultdict(bool)
postorder_result = []

while stack:
    now = stack.pop()
    left, right = binary_tree[now]
    if visited[now]:
        continue
    stack.append(now)
    times = 0
    if right is not NONE and not visited[right]:
        stack.append(right)
        times += 1
    if left is not NONE and not visited[left]:
        stack.append(left)
        times += 1
    if not times:
        postorder_result.append(now)
        visited[now] = True

print(''.join(preorder_result))
print(''.join(inorder_result))
print(''.join(postorder_result))
