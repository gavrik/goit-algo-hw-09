import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(actual_sum):
    remainder = actual_sum
    coin_idx = 0
    res = {}
    while remainder > 0:
        if remainder < coins[coin_idx]:
            coin_idx += 1
            continue
        c = remainder // coins[coin_idx]
        res[coins[coin_idx]] = c
        remainder = remainder - (coins[coin_idx] * c)
        coin_idx += 1
    return res

def find_min_coins(actual_sum):
    count_coins = [0] + [float("inf")] * actual_sum
    coin_table = [0] + [float("inf")] * actual_sum

    #print(count_coins)
    #print(coin_table)

    for i in range(1, actual_sum + 1):
        for coin in coins:
            #print(f"---- i-{i} : coin-{coin} ----")
            if i >= coin and count_coins[i - coin] + 1 < count_coins[i]:
                count_coins[i] = count_coins[i - coin] + 1
                coin_table[i] = coin
            #print(count_coins)
            #print(coin_table)

    current_sum = actual_sum
    coins_needed = {}
    while current_sum > 0:
        coin = coin_table[current_sum]
        coins_needed[coin] = coins_needed.get(coin, 0) + 1
        current_sum -= coin

    return(coins_needed)


if __name__ == "__main__":
    print(find_coins_greedy(113))
    print(find_coins_greedy(75))
    print(find_coins_greedy(38))
    
    print(find_min_coins(113))
    print(find_min_coins(75))
    print(find_min_coins(38))

    #exit(0)

    cases = [113, 137, 75, 38, 12, 65345, 543210]
    print("\n***** find_coins_greedy *****")
    for cash in cases:
        print('case for cash: ', cash)
        time = timeit.timeit(lambda: find_coins_greedy(cash), number=10000)
        print("Result: ", find_coins_greedy(cash))
        print("Time taken:", time)

    print("\n***** find_min_coins *****")
    for cash in cases:
        print('case for cash: ', cash)
        time = timeit.timeit(lambda: find_min_coins(cash), number=10000)
        print("Result: ", find_min_coins(cash))
        print("Time taken:", time)

