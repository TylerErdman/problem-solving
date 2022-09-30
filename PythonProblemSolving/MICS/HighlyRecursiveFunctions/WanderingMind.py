# This code solves problem 8 of the MICS 2017 programming contest

def func_f(n, values_of_f):
    # try to get the value from the dict, if not compute it
    try:
        value = values_of_f[n]
        return value
    except KeyError:
        pass

    # evaluate and store solutions
    # rule 1
    if n <= -3:
        values_of_f[n] = n
        return n
    # rule 2
    elif -3 < n < 3:
        values_of_f[n] = 2 * n
        return 2 * n
    # otherwise process solution tail up
    else:
        for i in range(3, n + 1):
            values_of_f[i] = func_f(i - 6, values_of_f) + func_f(i - 4, values_of_f) + func_f(i - 1, values_of_f)

    return values_of_f[n]


def main():

    # get input
    how_many_cases = int(input())

    # making lists to hold input/output
    all_cases = []
    all_output = []

    # get rest of input
    for i in range(how_many_cases):
        collect_input = int(input())
        all_cases.append(collect_input)

    # create dict
    values_of_f = {}

    # evaluate each case
    for case in all_cases:
        func_f(case, values_of_f)
        all_output.append(values_of_f[case])

    # print out with desired formatting
    for i in range(how_many_cases):
        print(f"Case {i + 1}: H({all_cases[i]}) = {all_output[i]}")


if __name__ == '__main__':
    main()
