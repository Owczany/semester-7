def main():
    number__of_tests = int(input())

    for _ in range(number__of_tests):
        n, m = list(map(int, input().split()))
        matrix = [list(map(int, input().split())) for _ in range(n)]
        leader = float('-inf')
        leader_positions = []
        # searching for candidates
        for i in range(n):
            for j in range(m):
                if matrix[i][j] > leader:
                    leader = matrix[i][j]
                    leader_positions = [(i, j)]
                elif matrix[i][j] == leader:
                    leader_positions.append((i, j))
        if len(leader_positions) < 3:
            print(leader - 1)
            return
        # searching if it is possible to help with that operation
        row_cords = {leader_positions[0][0], leader_positions[1][0]}
        cols_cords = {leader_positions[0][1], leader_positions[1][1]}
        print
        return
        bi = -1
        bj = -1
        if i1 == i2 :
            bi = i1

        for (i, j) in leader_positions[3:]:
            if (i != i1 and i != i2) and j != j1 and j != j2:
                return leader

        return leader - 1
        
