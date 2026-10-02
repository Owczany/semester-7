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
            return leader - 1
        # searching if it is possible to help with that operation
        i1, j1 = leader_positions[0]
        i2, j2 = leader_positions[1]
        i3, j3 = leader_positions[2]

        bi = -1
        bj = -1
        if i1 == i2 :
            bi = i1

        for (i, j) in leader_positions[3:]:
            if (i != i1 and i != i2) and j != j1 and j != j2:
                return leader

        return leader - 1
        
