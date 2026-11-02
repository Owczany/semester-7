def update(hierarchy: list[int], employee: int, count: int = 0):
    hierarchy[employee]

    res[employee] = count
    pass


def main():
    n = int(input())

    hierarchy = [-1] * n
    res = [0] * n

    for employee in range(n):
        manager = int(input)
        hierarchy[employee] = manager

    for employee, manager in enumerate(hierarchy):
        if res[employee] != 0 or hierarchy[employee] == -1:
            continue

        # rozpatrujemy pracownika
        # jeśli pracownik ma kogoś nad sobą no to rozwazamy go i dodajemy counter += 1










    
