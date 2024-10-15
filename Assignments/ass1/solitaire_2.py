from itertools import chain
from random import seed, shuffle
from collections import defaultdict

poker = {
    0 :'🂱', 1 :'🂲', 2 :'🂳', 3 :'🂴', 4 :'🂵', 5 :'🂶', 6 :'🂷', 7 :'🂸', 8 :'🂹', 9 :'🂺', 10:'🂻', 11:'🂽', 12:'🂾',
    13:'🃁', 14:'🃂', 15:'🃃', 16:'🃄', 17:'🃅', 18:'🃆', 19:'🃇', 20:'🃈', 21:'🃉', 22:'🃊', 23:'🃋', 24:'🃍', 25:'🃎',
    26:'🃑', 27:'🃒', 28:'🃓', 29:'🃔', 30:'🃕', 31:'🃖', 32:'🃗', 33:'🃘', 34:'🃙', 35:'🃚', 36:'🃛', 37:'🃝', 38:'🃞',
    39:'🂡', 40:'🂢', 41:'🂣', 42:'🂤', 43:'🂥', 44:'🂦', 45:'🂧', 46:'🂨', 47:'🂩', 48:'🂪', 49:'🂫', 50:'🂭', 51:'🂮',
    52:' '
}
record = []
#Hearts A, Diamonds A, Clubs A, Spades A, Hearts K, Diamonds K, Clubs K, Spades K
stacks = [[], [], [], [], [], [], [], []]

def get_round_word(round_played):
    if round_played == 1:
        return 'first'
    elif round_played == 2:
        return 'second'
    elif round_played == 3:
        return 'third'
    elif round_played > 20 and round_played % 10 == 1:
        return str(round_played) + 'st'
    elif round_played > 20 and round_played % 10 == 2:
        return str(round_played) + 'nd'
    elif round_played > 20 and round_played % 10 == 3:
        return str(round_played) + 'rd'
    else:
        return str(round_played) + 'th'


def show_deck(cards):
    record.append(''.join([']' for _ in cards]))


def get_stack_string(stack):
    L = ['[' for _ in stack] #]
    if len(L) != 0:
        L.pop()
        L.append(poker[stack[-1]])
    return ''.join(L)


def show_taken_cards(cards):
    record.append(get_stack_string(cards))


def show_stacks():
    line1 = '    '
    line2 = '    '
    stack1 = []
    stack2 = []
    for i in range(8):
        if i < 4:
            stack1.append(f'{get_stack_string(stacks[i]):<13}')
        else:
            stack2.append(f'{get_stack_string(stacks[i]):<13}')

    line1 += '  '.join(stack1)
    line2 += '  '.join(stack2)
    record.append(line1.rstrip(' '))
    record.append(line2.rstrip(' '))


def get_3_cards(cards):
    L = []
    if len(cards) < 3:
        for _ in range(len(cards)):
            L.append(cards.pop())
    else:
        for _ in range(3):
            L.append(cards.pop())
    return L


def put_onto_stacks(cards):
    # print(cards)
    card = cards[-1]
    if card % 13 == 0:
        # record.append('')
        record.append('Placing one of the base cards!')
        if card // 13 == 0:
            stacks[0].append(cards.pop())
            return 1, cards
        elif card // 13 == 1:
            stacks[1].append(cards.pop())
            return 1, cards
        elif card // 13 == 2:
            stacks[2].append(cards.pop())
            return 1, cards
        elif card // 13 == 3:
            stacks[3].append(cards.pop())
            return 1, cards
    elif card % 13 == 12:
        # record.append('')
        record.append('Placing one of the base cards!')
        if card // 13 == 0:
            stacks[4].append(cards.pop())
            return 1, cards
        elif card // 13 == 1:
            stacks[5].append(cards.pop())
            return 1, cards
        elif card // 13 == 2:
            stacks[6].append(cards.pop())
            return 1, cards
        elif card // 13 == 3:
            stacks[7].append(cards.pop())
            return 1, cards
    else:
        for i in range(8):
            if len(stacks[i]) != 0:
                if i < 4:
                    if card == stacks[i][-1] + 1:
                        # record.append('')
                        record.append('Making progress on an increasing sequence!')
                        stacks[i].append(cards.pop())
                        return 1, cards
                else:
                    if card == stacks[i][-1] - 1:
                        # record.append('')
                        record.append('Making progress on a decreasing sequence!')
                        stacks[i].append(cards.pop())
                        return 1, cards
    return 0, cards


def play_round(cards):
    round_played = 1
    round_state = 1
    taken_cards = []
    record.append(f'Starting to draw 3 cards (if possible) again and again for the {get_round_word(round_played)} time...')
    record.append('')
    while True:
        new_cards = get_3_cards(cards)
        if len(new_cards) == 0:
            if len(taken_cards) == 0:
                # record.append('All cards have been placed, you won!')
                record.pop()
                return 0
            elif round_state == 0:
                # record.append(f'{len(taken_cards)} cards could not be placed, you lost!')
                record.pop()
                return len(taken_cards)
            else:
                cards = taken_cards[::-1]
                taken_cards = []
                round_state = 0
                round_played += 1
                record.append(f'Starting to draw 3 cards (if possible) again and again for the {get_round_word(round_played)} time...')
                record.append('')
                continue
        taken_cards.extend(new_cards)
        # record.append('')
        show_deck(cards)
        show_taken_cards(taken_cards)
        show_stacks()
        record.append('')
        while True:
            state, taken_cards = put_onto_stacks(taken_cards)
            if state != 0:
                round_state = state
                show_deck(cards)
                show_taken_cards(taken_cards)
                show_stacks()
                record.append('')
            else:
                break
            if len(taken_cards) == 0:
                break


def start(seed_value):
    record.clear()
    for i in stacks:
        i.clear()
    cards = list(range(52))
    seed(int(seed_value))
    shuffle(cards)
    record.append('Deck shuffled, ready to start!')
    show_deck(cards)
    record.append('')
    return play_round(cards)


def main():
    seed_value = input('Please enter an integer to feed the seed() function: ')
    print('')
    n = start(seed_value)
    if n == 0:
        print('All cards have been placed, you won!')
    else:
        print(f'{n} cards could not be placed, you lost!')
    print('')
    print(f'There are {len(record)} lines of output; what do you want me to do?')
    while True:
        print('')
        print('Enter: q to quit')
        print(f'       a last line number (between 1 and {len(record)})')
        print(f'       a first line number (between -1 and -{len(record)})')
        print(f'       a range of line numbers (of the form m--n with 1 <= m <= n <= {len(record)})')
        s = input('       ')
        if s == 'q':
            exit()
        else:
            try:
                if '+' in s:
                    pass
                elif '--' in s:
                    s = s.replace(' ', '')
                    s = s.replace('\t', '')            
                    lines = s.split('--')
                    lines = [int(x) for x in lines]
                    if 1 <= lines[0] <= lines[1] <= len(record):
                        print('')
                        print('\n'.join(record[lines[0]-1:lines[1]]))
                else:
                    lines = [int(s)]
                    if lines[0] > 0:
                        print('')
                        print('\n'.join(record[:lines[0]]))
                    elif lines[0] < 0:
                        print('')
                        print('\n'.join(record[lines[0]:]))
            except:
                pass
                                           
                                           
# print('\n'.join(record))                 
# print(len(record))                       
# print(record)
                                           
                                           
def simulate(loops, i):
    record = {}
    for t in range(loops):
        n = start(i + t)
        if n in record:
            record[n] += 1
        else:
            record[n] = 1
    print('Number of cards left | Frequency')
    print('--------------------------------')
    for i in sorted(record, reverse=True):
        print(f'{i:20} |{record[i]*100/loops:9.2f}%')
                                           
                                           
if __name__ == '__main__':
    main()
                                           
                                           
