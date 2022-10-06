from statistics import median


def evaluate_answer(answer_house, test_line):
    total_diff = 0

    for house in test_line:
        total_diff += abs(house - answer_house)

    return total_diff


def main():

    tests = int(input())
    for i in range(tests):
        test_line = input().split(" ")
        test_line = list(map(int, test_line))
        

        del test_line[0]
        test_line.sort()
        
        answer_house = median(test_line)

        answer = evaluate_answer(answer_house, test_line)

        print(int(answer))


if __name__ == '__main__':
    main()
