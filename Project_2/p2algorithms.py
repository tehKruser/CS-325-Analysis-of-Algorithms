# Algorithm 1: Enumeration
# Helper function
def change(target, coins, coins_list):
    if sum(coins_list) == target:
        yield coins_list
    elif sum(coins_list) > target:
        pass
    elif coins == []:
        pass
    else:
        for c in change(target, coins[:], coins_list + [coins[0]]):
            yield c
        for c in change(target, coins[1:], coins_list):
            yield c

def ChangeSlow(coins, target):
    # Call helper function and create list of all solutions
    solutions = [s for s in change(target, coins, [])]

    # optimal solution
    opt = min(solutions, key=len)
    m = len(opt)

    c = [0] * len(coins)
    i = 0
    for ea in coins:
        c[i] = opt.count(ea)
        i += 1

    return c, m


# Algorithm 2: Change Greedy
def ChangeGreedy(coins, target):
    c = [0] * len(coins)
    m = 0
    i = len(coins) - 1
    for ea in reversed(coins):
        while target - ea >= 0:
            target -= ea
            m += 1
            c[i]+= 1
        i -= 1
    return c, m


# Algorithm 3: Change Dynamic Programming
def ChangeDP(coins, target):
    T = [9999999999]*(target+1)
    R = [-1]*(target+1)
    T[0] = 0
    R[0] = -1

    for j in range(len(coins)):
        for i in range(1, target+1):
            if i >= coins[j]:
                if T[i - coins[j]] + 1 < T[i]:
                    T[i] = 1 + T[i-coins[j]]
                    R[i] = j

    m = T[-1]

    opt = []
    start = len(R)-1
    while start != 0:
        j = R[start]
        opt.append(coins[j])
        start = start - coins[j]

    c = [0] * len(coins)
    i = 0
    for ea in coins:
        c[i] = opt.count(ea)
        i += 1

    return c, m