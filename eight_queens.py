import copy #For deep copy of high dimensional list

queens = []

def plot_queens(n, pos, mark='*'):
    iter_list = [[x, y] for x in range(n + n + 1 + 1) for y in range(n + n + 1 + 1)]
    for i, j in iter_list:
        if i == 0:
            if j == 0 or (j - 1)%2 == 0:
                print(' ', end='')
            else:
                print(int(j/2), end='')
        elif j == 0:
            if (i - 1)%2 == 0:
                print(' ', end='')
            else:
                print(int(i/2), end='')
        elif (i - 1)%2 == 0:
            if (j - 1)%2 == 0:
                print(' ', end='')
            else:
                print('-', end='')
        elif i%2 == 0:
            if (j - 1)%2 == 0:
                print('|', end='')
            else:
                if pos[int((i - 2)/2)][int((j - 2)/2)] == 1:
                    print(mark, end='')
                else:
                    print(' ', end='')
        if j == n + n + 1:
            print()

def eight_queen(index, pos, n):
    temp_pos = copy.deepcopy(pos)
    if index == n - 1:
        for avail_i in range(n):
            temp = pos[avail_i][index]
            if temp == 0:
                pos[avail_i][index] = 1
                queens.append(pos)
                pos = copy.deepcopy(temp_pos)
           
    else:
        for avail_i in range(n):
            if pos[avail_i][index] == 0:
                pos[avail_i][index] = 1
                for next_i in range(index + 1, n):
                    pos[avail_i][next_i] = -1
                    if avail_i + next_i - index < n:
                        pos[avail_i + next_i - index][next_i] = -1
                    if avail_i - (next_i - index) >= 0:
                        pos[avail_i - (next_i - index)][next_i] = -1
                eight_queen(index + 1, pos, n) 
                pos = copy.deepcopy(temp_pos)

if __name__ == '__main__':
    n = 8
    pos = [[0 for i in range(n)] for j in range(n)] 
    eight_queen(0, pos, n)
    len_poss = len(queens)
    print('All {0} possibilities:'.format(len_poss))   
    for i in range(len_poss):
        c_queens = queens[i]
        plot_queens(n, c_queens, mark='@')
        input()
