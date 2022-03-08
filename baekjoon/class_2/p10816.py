import sys


n = int(sys.stdin.readline())
n_cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_cards = list(map(int, sys.stdin.readline().split()))

cards_dict = {}

for card in n_cards:
    if card not in cards_dict:
        cards_dict[card] = 1
    else:
        cards_dict[card] += 1

print(*[cards_dict[card] if card in cards_dict else 0 for card in m_cards])

