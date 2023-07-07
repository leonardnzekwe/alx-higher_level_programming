#!/usr/bin/python3
"""101-nqueens Module"""


from sys import argv, exit

def main():
    """Testing Out Nqueen Features"""

    if len(argv) != 2:
        print(f"Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        matrix = []
        for j in range(n):
            row = []
            matrix.append(row)
            for k in range(2):
                row.append(k + j)
    print(matrix)
    print(matrix)

if __name__ == "__main__":
    main()
