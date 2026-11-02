def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        books = list(map(int, input().split()))
        print(max(books[0:n-1]) + books[-1])

if __name__ == '__main__':
    main()
