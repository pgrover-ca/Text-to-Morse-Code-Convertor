# Project : Text to Morse Code Convertor
# Author  : PUNEET GROVER
# Date    : 10/01/2021
# Purpose : Converting text to morse code

# Get input from the command line
text = input("Enter text: ").lower()

# Create a dictionary containing morse code conversion of each alphabetic character
morse_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

print(f"Morse Code for {text} is: ")

for letter in text:
    if letter in morse_code:
        print(morse_code[letter], end="")
    else:
        print("Invalid Input: " + letter)

print()
