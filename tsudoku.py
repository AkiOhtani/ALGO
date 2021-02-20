from queue import deque

N, M, K = map(int, input().split())

A = input().split()
B = input().split()

que = deque([(0, K, 0, 0)])

max_count = 0

while que:
    count, k, a_index, b_index = que.popleft()
    max_count = max(max_count, count)
    if a_index >= len(A) and b_index >= len(B):
        break
    if a_index < len(A) and 0 <= k-int(A[a_index]):
        que.appendleft((count+1, k-int(A[a_index]), a_index+1, b_index))
    if b_index < len(B) and 0 <= k-int(B[b_index]):
        que.appendleft((count+1, k-int(B[b_index]), a_index, b_index+1))

print(max_count)
