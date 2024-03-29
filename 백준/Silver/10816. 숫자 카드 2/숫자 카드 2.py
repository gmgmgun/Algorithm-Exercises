def find_card_counts():
    n = int(input())
    n_cards = list(map(int, input().split()))
    m = int(input())
    m_cards = list(map(int, input().split()))

    m_dict = {key: 0 for key in m_cards}

    for card in n_cards:
        if card in m_dict:
            m_dict[card] += 1

    card_counts = ' '.join(str(m_dict[card]) for card in m_cards)

    print(card_counts)


find_card_counts()