def findMedia(a, b):
    if len(a) == 1:
        return b[0] if a[0] > b[0] else a[0]
    mid = (len(a) - 1) / 2
    if a[mid] == b[mid]: return a[mid]
    elif a[mid] < b[mid]:
        return findMedia(a[len(a) - mid - 1 :], b[0 : mid + 1])
    else:
        return findMedia(a[0 : mid + 1], b[len(a) - mid - 1 :])

if __name__ == "__main__":
    a = [1,3,5,7,9]
    b = [2,4,6,8,10]
    print findMedia(a,b)

    c = [2,4,908,234,5,7]
    d = [2,67,123,56,23,7]
    print findMedia(c,d)

