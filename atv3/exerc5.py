import heapq

def connect_ropes(L):
    heapq.heapify(L)
    total_cost = 0

    while len(L) > 1:
        least = heapq.heappop(L)
        second_least = heapq.heappop(L)

        cost = least + second_least
        total_cost += cost
        heapq.heappush(L, cost)
    return total_cost

List = [20, 13, 15, 10, 19, 11, 8, 14, 17, 2, 9, 3, 18, 1, 16, 4, 12, 7, 5, 6]

print(f"Custo total: {connect_ropes(List)}")

'''
(n-1)x(2logn+logn)=(n-1)x3log n=O(nlog n)
{numero de interações do while, logn para cada pop e para push, criação da fila de prioridades é O(n) poranto custo do algoritmo é: O(nlog n)}
'''