from sys import stdin

# 10038


def main():

    cases = []
    while True:
        try:
            case = list(map(int, stdin.readline().strip().split(" ")))
            cases.append(case)
        except Exception:
            break

    solutions = []

    for arr in cases:
        int_list = []
        solution = True
        for num in range(1, arr[0]):
            difference = arr[num] - arr[num + 1]
            absolute_val_of_diff = abs(difference)
            if absolute_val_of_diff < 1 or absolute_val_of_diff >= arr[0] or absolute_val_of_diff in int_list:
                solution = False
            else:
                int_list.append(absolute_val_of_diff)

        solutions.append(solution)

    for sol in solutions:
        if sol is True:
            print("Jolly")
        else:
            print("Not jolly")


if __name__ == '__main__':
    main()
