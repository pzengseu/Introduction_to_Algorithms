# coding : utf-8

#01背包问题
def  knapsack(w, v, c):
    n = len(w)
    x = [0] * n
    V = [ ([0] * (c+1) ) for i in range(n) ]

    for i in range(1,n):
        for j in range(1,c+1):
            if j < w[i]:
                V[i][j] = V[i-1][j]
            else:
                V[i][j] = max(V[i-1][j], V[i-1][j-w[i]]+v[i])

    j = c
    for i in range(1,n)[::-1]:
        if V[i][j] > V[i-1][j]:
            x[i] = 1
            j = j - w[i]

    return x,V

if __name__ == '__main__':
    w = [0,4,5,6,2,2]
    v = [0,6,4,5,3,6]
    k = knapsack(w,v,10)
    for i in range(len(w))[::-1]:
        print k[1][i]
    print k[0]