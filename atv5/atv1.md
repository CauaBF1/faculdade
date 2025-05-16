a) Preorder: 11,24,40,42,46,26,30,48,58
b) Inorder:  42,40,46,24,26,11,48,30,58
c) Postorder:42,46,40,26,24,48,58,30,11


T (N )=T (L)+T (N−L−1)+C

o pior cenário(L = 0)

T (N )=T (0)+T (N −1)+C
T (N )=T (0)+T (0)+T (0)+T (N −3)+C+C +C
T (N )=(N −1)T (0)+ T (1)+(N −1)C=N T (0)−T (0)+T (1)+ NC−C

T(0) = 1 e T(1) = K
portanto:

T(N) = N – 1 + K + NC – C

resultando em O(n)