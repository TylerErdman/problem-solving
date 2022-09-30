def separate_test_cases(all_test_cases):
    new_test_case_list = []

    while all_test_cases:
        first_number = all_test_cases[1] + 2

        test_case = all_test_cases[:first_number]
        del all_test_cases[:first_number]
        new_test_case_list.append(test_case)

    return new_test_case_list


def check_val_in_list(val, val_list):
    val_in_list = False
    for pairs in val_list:
        if val == pairs[0]:
            val_in_list = True

    return val_in_list


def get_opposite(param):
    if param == "blk":
        return "red"
    else:
        return "blk"


def evaluate_test_case(test_case):
    dictionary = assign_blk_red(test_case)

    for ordered in test_case:
        if dictionary.get(ordered[0]) == dictionary.get((ordered[1])):
            return False

    return True


def assign_blk_red(test_case):
    dictionary = {}
    for ordered in test_case:

        boo = check_val_in_list(ordered[0], dictionary)
        boo2 = check_val_in_list(ordered[1], dictionary)

        if boo and not boo2:
            new_val = get_opposite(dictionary.get(ordered[0]))
            dictionary[ordered[1]] = new_val
        elif boo2 and not boo:
            new_val = get_opposite(dictionary.get(ordered[1]))
            dictionary[ordered[0]] = new_val
        else:
            dictionary[ordered[0]] = "blk"
            dictionary[ordered[1]] = "red"
    return dictionary


def main():
    all_test_cases = []
    line = ""
    output = []

    while line != 0:

        line = input()
        if " " in line:
            line = tuple(line.split(" "))
        else:
            line = int(line)
        all_test_cases.append(line)

    all_test_cases.remove(0)

    all_test_cases = separate_test_cases(all_test_cases)

    for test_case in all_test_cases:

        del test_case[:2]

        yesno = evaluate_test_case(test_case)
        if yesno is True:
            output.append("BICOLORABLE.")
        else:
            output.append("NOT BICOLORABLE.")

    for line in output:
        print(line)


if __name__ == '__main__':
    main()
