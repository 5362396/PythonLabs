from random import choice


def deal_the_cards() -> None:
    colors = ['pik', 'kier', 'trefl', 'karo']
    figure = [str(i) for i in range(2, 11)] + ['Walet', 'Dama', 'Król', 'As']
    cards = [j + ' ' + i for i in colors for j in figure]
    player_names = ['Alan', 'Arek', 'Adam', 'Artur']
    drawn_cards = []

    for i in range(4):
        hand = []
        for j in range(5):
            card = choice(cards)
            while card in drawn_cards:
                card = choice(cards)
            drawn_cards.append(card)
            hand.append(card)
        print(f'{player_names[i]} {str(hand)}')


deal_the_cards()
