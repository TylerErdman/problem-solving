# This code solves problem 8 of the MICS 2018 programming contest

def func_h(n, values_of_h):
    # try to get the value from the dict, if not in dict compute
    try:
        value = values_of_h[n]
        return value
    except KeyError:
        pass

    # evaluate and store solutions
    if -8 < n < 10:
        return n
    elif n <= -8:
        for i in range(10, (-n + 1)):
            values_of_h[n] = func_h(i + 5, values_of_h) + func_h(i + 4, values_of_h) + func_h(i + 2, values_of_h)
    else:
        for i in range(8, n + 1):
            values_of_h[i] = func_h(i - 8, values_of_h) + func_h(i - 5, values_of_h) + func_h(i - 3, values_of_h)

    return values_of_h[n]


def main():

    how_many_cases = int(input())
    all_cases = []
    all_output = []
    for i in range(how_many_cases):
        collect_input = int(input())
        all_cases.append(collect_input)

    values_of_h = {}

    for case in all_cases:
        func_h(case, values_of_h)
        all_output.append(values_of_h[case])

    for i in range(how_many_cases):
        print(f"Case {i + 1}: H({all_cases[i]}) = {all_output[i]}")


if __name__ == '__main__':
    main()
