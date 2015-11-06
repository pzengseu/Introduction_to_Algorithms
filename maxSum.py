# coding: utf-8
"""
状态转移方程
f[i][j] = max{f[i][j], f[l][[j-1]*(sum[i] - sum[l])}, 1<=l<=i-1
f[i][j]表示在前ｉ个书中插入ｊ个乘号的最大值
sum[i]表示前ｉ个数之和
"""

def maxSum(q, k):
    n = len(q)
    s = [0] * n
    for i in range(1,n):
        s[i] = q[i] + s[i-1]

    f = [ ([0] * (n-1)) for i in range(n)]
    for i in range(n):
        f[i][0]=s[i]

    for i in range(2, n):
        t = min(i-1, k)
        for j in range(1,t+1):
            for l in range(1,i):
                f[i][j] = max(f[i][j], f[l][j-1]*(s[i]-s[l]))
    return f

if __name__ == '__main__':
    q = [0, 1, 2, 3, 4, 5]
    print "最大结果 =",maxSum(q, 2)[5][2]
