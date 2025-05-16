from collections import deque

def calcular_stock(prices):
    n = len(prices)
    span = [0] * n
    stack = deque()

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)
    return span

P = [120, 100, 80, 90, 80, 95, 105, 100, 90, 80, 70, 90, 100, 115, 125, 110, 95, 90, 80, 100]
S = calcular_stock(P)
print(S)

'''
P = [100, 80, 60, 70, 60, 75, 85]
S = calcular_stock(P)
print(S)
# [1, 1, 1, 2, 1, 4, 6]
'''