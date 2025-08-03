def coins(count: int, amount: int, coin_dict: dict) -> (bool, dict):
    if count == 0 and amount == 0:
        return True, coin_dict
    elif (count == 0 and amount > 0) or (count > 0 and amount == 0):
        return False, {}
    else:
        for coin in coin_dict.keys():
            if amount - coin < 0:
                continue
            coin_dict[coin] += 1
            ok, _ = coins(count - 1, amount - coin, coin_dict)
            if ok:
                return True, coin_dict
            else:
                coin_dict[coin] -= 1
        return False, {}

if __name__ == "__main__":
    denominations_list = [25, 10, 5, 1]
    coin = dict.fromkeys(denominations_list, 0)
    coin_count = 6
    coin_amount = 64
    result, result_dict = coins(coin_count, coin_amount, coin)
    if result:
        print(f"We can get {coin_amount} amount with {coin_count} coins with this denominations {denominations_list}, here are how:")
        print(result_dict)
    else:
        print(f"Impossible to get {coin_amount} with {coin_count} coins with this denominations {denominations_list}")