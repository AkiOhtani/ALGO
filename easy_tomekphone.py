class TomekPhone:
    def minKeystrokes(self, frequency, KeySizes):
        if sum(KeySizes) < len(frequency):
            return -1
        frequency.sort(reverse=True)
        count = []
        for size in KeySizes:
            count += [c for c in range(1, size+1)]
        count.sort()
        
        return sum(frequency[i]*count[i] for i in range(len(frequency)))

def main():
    frequency = list(map(int, input().split()))
    KeySizes = list(map(int, input().split()))
    print(TomekPhone().minKeystrokes(frequency, KeySizes))

if __name__ == "__main__":
    main()