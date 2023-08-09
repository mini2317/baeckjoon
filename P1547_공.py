n = int(input())
balls = [1, 2, 3]
for _ in range(n):
    a, b = map(int, input().split())
    balls[a - 1], balls[b - 1] = balls[b - 1], balls[a - 1]
for i in range(3):
    if balls[i] == 1:
        print(i + 1)
        break