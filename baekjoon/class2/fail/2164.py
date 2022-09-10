N = int(input())
answer = [i + 1 for i in range(N)]
front = 0
rear = -1
while rear - front != 1:
    front = (front + 1) % len(answer)
    rear = (rear + 1) % len(answer)
    answer[rear] = answer[front]
print(answer[front])
