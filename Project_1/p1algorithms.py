# Algorithm 1: Enumeration
def MAXSUBARRAY_Enum(array, low, high):
    max_sum = -1
    max_i = 0
    max_j = 0
    for i in range(low, high+1, 1):
        for j in range(i, high+1):
            sa_sum = 0
            for ea in array[i:j+1]:
                sa_sum += int(ea)
            if sa_sum > max_sum:
                max_sum = sa_sum
                max_i = i
                max_j = j
    return max_i, max_j, max_sum


# Algorithm 2: Better Enumeration
def MAXSUBARRAY_BetterEnum(array, low, high):
    max_sum = -1
    max_i = 0
    max_j = 0
    for i in range(low, high+1, 1):
        sa_sum = 0
        for j in range(i, high+1):
            sa_sum += int(array[j])
            if sa_sum > max_sum:
                max_sum = sa_sum
                max_i = i
                max_j = j
    return max_i, max_j, max_sum


# Algorithm 3: Divide and Conquer
# Max crossing sub-array:
def MAX_CROSSING_SUBARRAY(array, low, mid, high):
    left_sum = -99999999
    sa_sum = 0
    max_i = mid
    for i in range(mid, low-1, -1):
        sa_sum += int(array[i])
        if sa_sum > left_sum:
            left_sum = sa_sum
            max_i = i

    right_sum = -99999999
    sa_sum = 0
    max_j = mid
    if mid+1 >= high:
        right_sum = 0
    else:
        for j in range(mid+1, high+1, 1):
            sa_sum += int(array[j])
            if sa_sum > right_sum:
                right_sum = sa_sum
                max_j = j

    return max_i, max_j, left_sum + right_sum

def MAXSUBARRAY_DnC(array, low, high):
    if high == low:
        return low, high, int(array[low])
    else:
        mid = int((low + high)/2)
        left_low, left_high, left_sum = MAXSUBARRAY_DnC(array, int(low), mid)
        right_low, right_high, right_sum = MAXSUBARRAY_DnC(array, mid+1, int(high))
        cross_low, cross_high, cross_sum = MAX_CROSSING_SUBARRAY(array, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


# Algorithm 4: Linear Time
def MAXSUBARRAY_Linear(array, low, high):
    max_sum = -99999999
    max_i = 0
    max_j = 0
    temp = 0
    curr_max = 0

    for i in range(low, high+1, 1):
        curr_max += int(array[i])
        if max_sum < curr_max:
            max_sum = curr_max
            max_i = temp
            max_j = i
        if curr_max < 0:
            curr_max = 0
            temp = i+1
    return max_i, max_j, max_sum