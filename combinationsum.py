def main():
    # 入力 
    n = int(input())
    a = list(map(int, input().strip().split()))
    k = int(input())
    
    # iまででsumを作って、残りi以降を調べる
    def dfs(i, sum):
        # n個決め終わったら、今までの和sumがkと等しいかを返す
        if i == n: return sum == k
        # a[i]を使わない場合
        if dfs(i + 1, sum): return True
        # a[i]を使う場合
        if dfs(i + 1, sum + a[i]): return True
        # a[i]を使う使わないに拘らずkが作れないのでFalseを返す
        return False

    if dfs(0, 0):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()  