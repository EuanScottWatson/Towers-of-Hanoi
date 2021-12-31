import sys
import numpy as np

def count(number):
    digit = len(number) - 1
    while not all(number):
        if number[digit] == 0:
            number[digit] = 1
            return number, len(number) - digit
        elif number[digit] == 1:
            number[digit] = 0
            digit -= 1
    return number, -1

def solve(n):
    pegs = np.ones((3, n)) * np.inf
    for i in range(n):
        pegs[0][i] = n - i
    
    binary = [0] * n

    while pegs[2][-1] != 1 and pegs[1][-1] != 1:
        binary, disc = count(binary)
        r, c = np.where(pegs==disc)
        r, c = r[0], c[0]
        pegs[r][c] = np.inf

        next_smallest = min(pegs[(r + 1) % 3])
        cond = next_smallest > disc
        next_r = (r + 1) % 3 if cond else (r + 2) % 3
        next_c = (pegs[next_r]==np.inf).argmax(axis=0)
        pegs[next_r][next_c] = disc

        print("Move disc %d to peg number %d" % (disc, next_r + 1))

    print(pegs)

if __name__ == "__main__":
    towers = 3
    if len(sys.argv) == 2:
        try:
            towers = int(sys.argv[1])
        except:
            print("Incorrect number of towers: %s" % sys.argv[1])
    solve(towers)