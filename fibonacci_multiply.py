from typing import List
def fibonacciMul(X:List[int], Y:List[int]) -> List[int]:
    hold = 0
    i = j = 0
    Z = [None for k in range(len(X) + len(Y))]

    for k in range(len(X) + len(Y)):
        for i in range(min(len(X), k+1)):
                if k-i < len(Y) :
                    hold = hold + X[i] * Y[k-i]
        Z[k] = hold % 10
        hold = hold // 10
    return Z[len(X) + len(Y)::-1]

def main():
    X = [4, 3, 9]
    Y = [4, 1, 3]
    print(''.join(map(lambda x: str(x), fibonacciMul(X, Y))))

if __name__ == "__main__":
    main()