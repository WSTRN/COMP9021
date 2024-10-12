from itertools import chain
from random import seed, shuffle
from collections import defaultdict
import os
import sys

poker = {
        0 :'🂱', 1 :'🂲', 2 :'🂳', 3 :'🂴', 4 :'🂵', 5 :'🂶', 6 :'🂷', 7 :'🂸', 8 :'🂹', 9 :'🂺', 10:'🂻', 11:'🂽', 12:'🂾',
        13:'🃁', 14:'🃂', 15:'🃃', 16:'🃄', 17:'🃅', 18:'🃆', 19:'🃇', 20:'🃈', 21:'🃉', 22:'🃊', 23:'🃋', 24:'🃍', 25:'🃎',
        26:'🃑', 27:'🃒', 28:'🃓', 29:'🃔', 30:'🃕', 31:'🃖', 32:'🃗', 33:'🃘', 34:'🃙', 35:'🃚', 36:'🃛', 37:'🃝', 38:'🃞',
        39:'🂡', 40:'🂢', 41:'🂣', 42:'🂤', 43:'🂥', 44:'🂦', 45:'🂧', 46:'🂨', 47:'🂩', 48:'🂪', 49:'🂫', 50:'🂭', 51:'🂮',
        52:' '
}

def show_cards(cards, removed_index = []):
    for i in range(0, 16, 4):
        for j in range(4):
            if i+j in removed_index:
                print(f'\t{poker[52]}', end = '')
            else:
                print(f'\t{poker[cards[i+j]]}', end = '')
        print('')

def show_deck(cards):
    print(''.join([']' for _ in cards]))

def remove_cards(placed_cards):
    removed_index = []
    removed_cards = []
    for i in range(len(placed_cards)):
        # print(i)
        if ((placed_cards[i] % 13) >= 10):
            removed_index.append(i)
            removed_cards.append(placed_cards[i])
    return placed_cards, removed_index, removed_cards

# def place_cards(cards):
#     return [cards.pop() for _ in range(16)]

def refill_cards(cards, placed_cards, removed_index):
    n = len(removed_index)
    if n == 1:
        print(f'Drawing and placing 1 card:')
    else:
        print(f'Drawing and placing {n} cards:')
    for i in removed_index:
        placed_cards[i] = cards.pop()
    return placed_cards

def play_round(cards):
    picture_cards = []
    placed_cards = [52 for _ in range(16)]
    removed_index = [i for i in range(16)]
    while True:
        placed_cards = refill_cards(cards, placed_cards, removed_index)
        show_deck(cards)
        show_cards(placed_cards)
        print('')
        placed_cards, removed_index, removed_cards = remove_cards(placed_cards)
        if len(removed_cards) == 0:
            return picture_cards
        if len(removed_cards) == 1:
            print('Putting 1 picture aside:')
        else:
            print(f'Putting {len(removed_cards)} pictures aside:')
        show_cards(placed_cards, removed_index)
        print('')
        picture_cards.extend(removed_cards)
        if (len(cards) - len(removed_cards) + 16) == 40:
            print('You uncovered all pictures, you won!')
            return picture_cards
    



def play(seed_value):
    # seed_value = input('Please enter an integer to feed the seed() function: ')
    # print('')
    cards = list(range(52))
    seed(int(seed_value))
    shuffle(cards)
    # print(cards)
    print('Deck shuffled, ready to start!')
    show_deck(cards)
    print('')
    print('Starting first round...')
    print('')
    picture_cards = play_round(cards)
    # print(picture_cards)
    
    
    print('After shuffling, starting second round...')
    print('')
    cards = sorted(set(range(52)) - set(picture_cards))
    seed(int(seed_value) + 1)
    shuffle(cards)
    picture_cards += play_round(cards)
    # print(picture_cards)
    
    
    print('After shuffling, starting third round...')
    print('')
    cards = sorted(set(range(52)) - set(picture_cards))
    seed(int(seed_value) + 2)
    shuffle(cards)
    picture_cards += play_round(cards)
    # print(picture_cards)
    
    
    print('After shuffling, starting fourth round...')
    print('')
    cards = sorted(set(range(52)) - set(picture_cards))
    seed(int(seed_value) + 3)
    shuffle(cards)
    picture_cards += play_round(cards)
    # print(picture_cards)
    
    n = len(picture_cards)
    if n == 0:
        print('You uncovered no pictures, you lost!')
    elif n == 1:
        print('You uncovered only 1 picture, you lost!')
    elif n != 12:
        print(f'You uncovered only {n} pictures, you lost!')

    return n



def simulate(loops, i):
    original_stdout = sys.stdout
    f = open(os.devnull, 'w')
    sys.stdout = f
    record = {}
    for t in range(loops):
        n = play(i + t)
        if n in record:
            record[n] += 1
        else:
            record[n] = 1
    sys.stdout = original_stdout
    f.close()

    print('Number of uncovered pictures | Frequency')
    print('----------------------------------------')
    for i in sorted(record):
        print(f'{i:28} |{record[i]*100/loops:9.2f}%')


if __name__ == '__main__':
    seed_value = input('Please enter an integer to feed the seed() function: ')
    print('')
    play(seed_value)




