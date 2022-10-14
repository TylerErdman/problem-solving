def get_input() -> list:

    all_rolls = []

    while True:
        try:
            roll = list(map(int, input().split(" ")))
            all_rolls.append(roll)
        except EOFError:
            break

    test_cases = []

    for i in range(0, len(all_rolls), 13):
        test_cases.append(all_rolls[i:i + 13])

    return test_cases


def find_and_remove_yahtzee(case: list) -> int:
    all_yahtzee = []
    for i, roll in enumerate(case):
        if roll[0] == roll[1] == roll[2] == roll[3] == roll[4]:
            all_yahtzee.append(i)

    current_lowest_yahtzee = 7
    lowest_roll_index = None
    for index in all_yahtzee:
        if current_lowest_yahtzee > case[index][0]:
            lowest_roll_index = index

    if lowest_roll_index:
        case.pop(lowest_roll_index)
        return 50
    else:
        return 0


def evaluate_test_case(case: list) -> list:
    running_total = 0
    answer_list = [0 in range(15)]

    if find_and_remove_yahtzee(case) == 50:
        answer_list[9] = 50
        running_total += 50

    


    return answer_list


def main():
    test_cases = get_input()
    answer_list = []

    for case in test_cases:
        answer_list.append(evaluate_test_case(case))

    for i, answer in enumerate(answer_list):
        for j, num in enumerate(answer):
            if j < len(answer):
                print(num, end=" ")
        if i < len(answer_list):
            print("\n")


if __name__ == '__main__':
    main()
