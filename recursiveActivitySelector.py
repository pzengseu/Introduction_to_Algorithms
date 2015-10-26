# coding: utf-
import copy
result = []

def dynamic_activity_selector(sf):
    c = [ ([0] * len(sf)) for i in range(len(sf)) ]
    r = copy.deepcopy(c)
    n = len(sf)

    for i in range(2, n):
        for j in range(1, i):
            for k in range(j+1, i):
                if(sf[k][0] >= sf[j][1] and sf[k][1] <= sf[i][0]):
                    t = c[j][k] + c[k][i] + 1
                    if c[j][i] < t:
                        c[j][i] = t
                        r[j][i] = k

    return c, r

def recursive_activity_selector(sf, k):
    m = k + 1
    n = len(sf) - 1
    while m <= n and sf[m][0] < sf[k][1]:
        m = m + 1
    if m <= n:
        result.append(sf[m])
        recursive_activity_selector(sf,m)

#贪婪算法，迭代法
def greedy_activity_selector(sf):
    n = len(sf)
    result = [sf[1]]
    k = 1
    for m in range(2,n):
        if(sf[m][0] >= sf[k][1]):
            result.append(sf[m])
            k = m
    return result

if __name__ == "__main__":
    sf = [(0,0),
          (1,4),
          (3,5),
          (0,6),
          (5,7),
          (3,9),
          (5,9),
          (6,10),
          (8,11),
          (8,12),
          (2,14),
          (12,16)]
    recursive_activity_selector(sf,0)
    print result
    print greedy_activity_selector(sf)
    t = dynamic_activity_selector(sf)
    print t[0]
    print t[1]