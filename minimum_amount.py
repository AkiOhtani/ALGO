from sys import maxsize

def minAmount():
    N = int(input())

    prices = []

    cost_sum = 0
    min_price = maxsize

    for i in range(N):
        price = int(input())
        if i == 0:
            cost_sum += price
        else:
            cost_sum += max(0, price - min_price)
        min_price = min(min_price, price)

    return cost_sum

if __name__ == '__main__':
    cost_sum = minAmount()
    print(cost_sum)