def create_new_deck_of_cards():

    deck_of_cards = []

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    for suit in suits:
        for nums in numbers:
            card = nums + " of " + suit
            deck_of_cards.append(card)

    return deck_of_cards


def execute_shuffle(deck_of_cards, shuffle):
    new_deck_of_cards = []

    for index in shuffle:
        new_deck_of_cards.append(deck_of_cards[index - 1])

    return new_deck_of_cards


def main():

    number_of_cases = int(input())
    input()

    # run for every case
    for i in range(number_of_cases):

        # collect values
        number_of_shuffles_known = int(input())
        all_shuffles = []

        # Write every shuffle to list
        while len(all_shuffles) < 52 * number_of_shuffles_known:
            shuffle_line = list(map(int, input().split(" ")))
            all_shuffles.extend(shuffle_line)

        new_shuffle_list = []
        for j in range(0, 52 * number_of_shuffles_known, 52):
            shuffle = all_shuffles[j:j+52]
            new_shuffle_list.append(shuffle)

        # shuffles seen
        shuffles_seen = []
        while True:
            try:
                shuffle = int(input())
                shuffles_seen.append(shuffle)
            except Exception:
                break

        deck_of_cards = create_new_deck_of_cards()

        for shuffle in shuffles_seen:
            deck_of_cards = execute_shuffle(deck_of_cards, new_shuffle_list[shuffle-1])

        for card in deck_of_cards:
            print(card)

        if i < number_of_cases - 1:
            print()


if __name__ == '__main__':
    main()
