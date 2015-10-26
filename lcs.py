# coding: utf-8
import copy

def lcs_lenght(x , y):
    m = len(x)
    n = len(y)
    c = [ ([0] * n) for i in range(m) ]
    b = copy.deepcopy(c)

    """
    1表示斜上
    2表示向↑
    3表示向←
    """
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j]  = c[i-1][j-1] + 1
                b[i][j] = 1
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            elif c[i-1][j] < c[i][j-1]:
                c[i][j] = c[i][j-1]
                b[i][j] = 3
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 4

    return c,b

result = [0] * 10
count = 0
#输出所有的最长公共子序列
def print_lcs(b, x, i ,j, current_len):
    global  count
    global change
    if i==0 or j==0:
        count += 1
        print result
        return
    if b[i][j] == 1:
        result[current_len] = x[i]
        print_lcs(b, x, i-1, j-1, current_len - 1)
    elif b[i][j] == 2:
        print_lcs(b, x, i-1, j, current_len)
    elif b[i][j] == 3:
        print_lcs(b, x, i, j-1, current_len)
    else:
        print_lcs(b, x, i, j-1, current_len)
        print_lcs(b, x, i-1, j, current_len)

if __name__ == "__main__":
    x = [0, 'A', 'B', 'C', 'B', 'D', 'A', 'B']
    y = [0, 'B', 'D', 'C', 'A', 'B', 'A']
    cb = lcs_lenght(x,y)
    for i in range(len(cb[0])):
        print cb[0][i]
    print
    for i in range(len(cb[1])):
        print cb[1][i]
    print_lcs(cb[1], x, len(x)-1, len(y)-1, cb[0][len(x)-1][len(y)-1])
    print count