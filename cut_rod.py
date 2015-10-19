def bottom_up_cut_rod(p, n):
    r = list()
    s = list()

    r.append(0)
    s.append(0)
    for j in range(1, n + 1):
        q = -1
        s.append(0)
        for i in range(1, j + 1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r.append(q)

    return (r, s)

def print_cut_rot_solution(p, n):
    t = bottom_up_cut_rod(p, n)
    while n > 0:
        print t[1][n],
        n = n - t[1][n]
    print t[0]

if __name__ == "__main__":
    p = [0,1,5,8,9,10,17,17,20,24,30]
    print_cut_rot_solution(p,9)