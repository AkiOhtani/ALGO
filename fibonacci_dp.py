def fib(n, memo):
    if n <= 1: return n
    if memo[n] != 0: return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def main():
    n = int(input())
    memo = [0 for i in range(n+1)]
    print(fib(n, memo))

if __name__ == "__main__":
    main()  