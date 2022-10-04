# super slow solution

def evaluate_for_j(j, test_line):
    total_diff = 0
    for num in test_line:
        total_diff += abs(num - j)

    return total_diff


def main():
    tests = int(input())
    for i in range(tests):
        test_line = list(map(int, input().split(" ")))

        del test_line[0]

        minimum = min(test_line)
        maximum = max(test_line)
        answer_list = []

        for j in range(minimum, maximum + 1):
            answer_list.append(evaluate_for_j(j, test_line))

        print(min(answer_list))


if __name__ == '__main__':
    main()
