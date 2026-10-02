def main():
    number_of_tests = int(input())

    for _ in range(number_of_tests):
        n = int(input())
        nums = list(map(int, input().split()))

        positive = True
        number_of_zeros = 0

        for num in nums:
            if num == 0:
                number_of_zeros += 1
            elif num < 0:
                positive = not positive

        output = 2 * (not positive) + number_of_zeros
        print(output)


if __name__ == "__main__":
    main()
    