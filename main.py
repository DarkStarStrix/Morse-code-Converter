# morse code converter

# import modules
import sys
import time
import os
import winsound

# define morse code dictionary
morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'}


# define function to convert text to morse code
def text_to_morse(text):
    # initialize empty string
    morse = ''
    # loop through each character in text
    for char in text:
        # if character is a space, add a space to morse string
        if char == ' ':
            morse += ' '
        # if character is a letter, add morse code equivalent to morse string
        elif char.upper() in morse_code:
            morse += morse_code[char.upper()] + ' '
        # if character is not a letter or space, add a question mark to morse string
        else:
            morse += '? '
    # return morse string
    return morse


# create input for user to enter text
text = input('Enter text to convert to morse code: ')

# convert text to morse code
morse = text_to_morse(text)

# print morse code
print(morse)

# loop through each character in morse code
for char in morse:
    # if character is a dot, play a dot sound
    if char == '.':
        winsound.PlaySound('dot.wav', winsound.SND_FILENAME)
    # if character is a dash, play a dash sound
    elif char == '-':
        winsound.PlaySound('dash.wav', winsound.SND_FILENAME)
    # if character is a space, wait for 0.5 seconds
    elif char == ' ':
        time.sleep(0.5)
    # if character is a question mark, wait for 1 second
    elif char == '?':
        time.sleep(1)
    # if character is not a dot, dash, space, or question mark, print an error message
    else:
        print('Error: Invalid character')

# print a new line
print()

# kill program
os.system('pause')
sys.exit()

# end of program

