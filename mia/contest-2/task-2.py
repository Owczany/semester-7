def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        matrix = []

        for _ in range(2):
            matrix.append(list(map(int, input().split())))
        s = 0
        cand = []
        for i in range(n):
            if matrix[0][i] >= matrix[1][i]:
                s += matrix[0][i]
                cand.append(matrix[1][i])
            else:
                s += matrix[1][i]
                cand.append(matrix[0][i])

        print(s + max(cand))

if __name__ == "__main__":
    main()
