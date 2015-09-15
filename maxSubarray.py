import math

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = 0
    sumA = 0
    i =  mid
    max_left = 0
    while i >= low:
        sumA += A[i]
        if sumA > left_sum:
            left_sum = sumA
            max_left = i
        i -=1

    right_sum = 0
    sumA = 0
    max_right = 0
    j = mid + 1
    while j<= high:
        sumA += A[j]
        if sumA > right_sum:
            right_sum = sumA
            max_right = j
        j += 1

    return (max_left, max_right, right_sum + left_sum)

def find_max_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = int(math.floor((low + high)/2.0))
        (left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(A, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if left_sum > right_sum and left_sum > cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum > left_sum and right_sum > cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print find_max_subarray(A, 0, len(A)-1)
