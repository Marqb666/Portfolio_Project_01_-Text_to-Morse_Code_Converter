MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..----', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ':'.......'}
import sys

def encode():
    try:
        text_to_convert = list(input('Type the text you want to convert:').upper().strip(' '))
        converted_text = [MORSE_CODE_DICT[letter] for letter in text_to_convert]
        converted_text1=''
        for code in converted_text:
            converted_text1 =converted_text1 + " " +code
    except KeyError:
        print('You have used characters that are not allowed, please try again!')
        encode()
    else:
        print(f'This is your code:{converted_text}')
        print(f'This is your code in another form:{converted_text1}')
        return True

def decode():
    code_to_encode = (input('Type code you want to encode:').split())
    text = ''
    for code in code_to_encode:
        for key in MORSE_CODE_DICT.keys():
            if MORSE_CODE_DICT[key] == code:
                text += key
    if not text:
        print('Please try to type the valid code')
        decode()
    else:
        print(f'Your text after decode is: {text}')

def decide():
    while True:
        decision = input("Type E if you want to encode or D if you want to decode or Q if you want to quite:").upper()
        if decision == 'E':
            encode()
        elif decision == 'D':
            decode()
        elif decision == 'Q':
            print('Quite')
            break            #import sys, and after that sys.exit()
        else:
            print('Try to choose E or D or Q')
            decide()

decide()


