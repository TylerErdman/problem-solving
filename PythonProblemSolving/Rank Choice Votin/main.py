from itertools import permutations


def main():
    ar = [1, 2, 3, 4, 5, 6]
    perms = permutations(ar)
    for thing in perms:
        print(thing)


if __name__ == '__main__':
    main()
