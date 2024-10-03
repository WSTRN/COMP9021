# Written by *** for COMP9021
import unicodedata

while True:
    print('Please input two integers a and b with 0 <= a <= b <= 1114111,\n       both integers being separated by ~, with possibly\n       spaces and tabs before and after the numbers:', end = '\n       ')
    number2unicodename = {}
    not_code_point  = 0
    try:
        input_str = input()
        input_str = input_str.replace(' ', '')
        input_str = input_str.replace('\t', '')

        input_num = input_str.split('~')
        input_num = [int(i) for i in input_num]
        if len(input_num) == 2 and input_num[0] <= input_num[1] and input_num[0] >= 0 and input_num[1] <= 1114111:
            for i in range(input_num[0], input_num[1]+1):
                try:
                    number2unicodename[str(i)] = unicodedata.name(chr(i))
                except:
                    number2unicodename[str(i)] = ''
                    not_code_point += 1
            break
        else:
            print('\nIncorrect input, try again!')
    except:
        print('\nIncorrect input, try again!')



if input_num[0] == input_num[1]:
    if not_code_point == 0:
        print('\n' + str(input_num[0]) + ' is the code point of a named character.', end = '\n\n')
    else:
        print('\n' + str(input_num[0]) + ' is not the code point of a named character.', end = '\n\n')
else:
    if not_code_point == 0:
        print('\nAll numbers between ' + str(input_num[0]) + ' and ' + str(input_num[1]) + '\n  are code points of named characters.', end = '\n\n')
    elif not_code_point == input_num[1] - input_num[0] + 1:
        print('\nNo number between ' + str(input_num[0]) + ' and ' + str(input_num[1]) + '\n  is the code point of a named character.')
        exit(0)
    else:
        print('\nAmongst the numbers between ' + str(input_num[0]) + ' and ' + str(input_num[1]) +',')
        print('  ' + str(round(100 * (1 - (not_code_point/(input_num[1] - input_num[0] + 1))), 2)) + '% are code points of named characters.', end = '\n\n')


matched = 0
maxlen = 0
output = []

print('Enter a string: ', end = '')
input_str = input()
for key in number2unicodename:
    if number2unicodename[key].startswith(input_str):
        if maxlen < len(number2unicodename[key]):
            maxlen = len(number2unicodename[key])
        matched += 1

for key in number2unicodename:
    if number2unicodename[key].startswith(input_str):        
        output.append(number2unicodename[key].ljust(maxlen) + ': ' + chr(int(key)) + '\n')


if matched == 0:
    print('\nNone of the characters you want me to consider\n  has a name that starts with ' + input_str + '.')
else:
    print('\nHere are those of the characters under consideration\n  whose name starts with ' + input_str + ':')
    output.sort()
    print(''.join(output))
    # for key in number2unicodename:
    #     if number2unicodename[key].startswith(input_str):
    #         output.append(number2unicodename[key].ljust(maxlen) + ': ' + chr(int(key)))
    #         print(number2unicodename[key].ljust(maxlen) + ': ' + chr(int(key)))

# INSERT YOUR CODE HERE
