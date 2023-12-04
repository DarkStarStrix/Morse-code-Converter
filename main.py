# morse code converter

# import modules
import os
import sys
import time
import winsound


class MorseCodeConverter:
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': '/'
    }

    def text_to_morse(self, text):
        morse = ''
        for char in text:
            morse += self.morse_code.get (char.upper (), '?') + ' '
        return morse

    def morse_to_text(self, morse):
        text = ''
        morse_words = morse.split (' / ')
        for morse_word in morse_words:
            morse_chars = morse_word.split ()
            for morse_char in morse_chars:
                for char, morse_code in self.morse_code.items ():
                    if morse_code == morse_char:
                        text += char
                        break
            text += ' '
        return text.strip ()

    converter = MorseCodeConverter ()


# Convert text to Morse code
text = "Hello World"
morse = converter.text_to_morse (text)
print (f"Text: {text}\nMorse: {morse}")

# Convert Morse code to text
morse = ". . . .   .   . - . .   . . . .   /   . - . -   ---   .-. . . . .   . . . ."
text = converter.morse_to_text (morse)
print (f"Morse: {morse}\nText: {text}")
