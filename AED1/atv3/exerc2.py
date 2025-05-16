def max_score(A, B, MAX_SUM):
    current_sum = 0
    score = 0
    while A or B:
        if not A:
            next_value = B.pop(0)
        elif not B:
            next_value = A.pop(0)
        else:
            if A[0] <= B[0]:
                next_value = A.pop(0)
            else:
                next_value = B.pop(0)

        if current_sum + next_value > MAX_SUM:
            break

        current_sum += next_value
        score += 1
    return score

A = [5, 2, 9, 4, 6, 3, 1, 2, 4]
B = [2, 6, 9, 7, 2, 5, 1, 4, 2, 5, 3]
MAX_SUM = 20

resultado = max_score(A, B, MAX_SUM)
print("Pontuação máxima:", resultado)

# sum = 2 + 5 + 2 + 6  = 4