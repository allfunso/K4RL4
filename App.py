import json

with open("codigos.json", "r") as file:
    dict = json.load(file)
    keys = list(dict.keys())
    values = list(dict.values())

def decode(code):
    text = ""
    words = code.split()
    for word in words:
        letters = word.split(".")
        for letter in letters:
            try:
                text += keys[values.index(letter)]
            except ValueError:
                text += letter
        text += " "
    return text

def encode(text):
    text = text.upper()
    code = ""
    words = text.split()
    for word in words:
        for letter in word:
            try:
                code += dict[letter]
            except KeyError:
                code += letter
            code += "."
        code = code[0:-1] + " "
    return code

#-------- MAIN LOOP --------#

while True:
    print("Type D to decode file, type E to encode one.")
    choice = input("[D / E / EXIT / HELP] ")
    result = ""

    if choice.upper() == "D":
        print("Type the name of the file you wish to DECODE. Include .txt")
        filename = input()
        with open(filename, "r") as file:
            lines = file.readlines()
            code = ""
            for line in lines:
                code += line

        result = decode(code)
    
    elif choice.upper() == "E":
        print("Type the name of the file you wish to ENCODE. Include the extension .txt")
        filename = input()
        with open(filename, "r") as file:
            lines = file.readlines()
            text = ""
            for line in lines:
                text += line

        result = encode(text)

    elif choice.upper() == "EXIT":
        break

    elif choice.upper() == "HELP":
        print('''
    This program works with text files (.txt). Before running, you should add the text file
    to the same directory where this program is. 
    Use the encode function to create a pseudo-binary file from a regular text file.
    Use the decode function to create a regular text file from an encoded pseudo-binary.
        ''')

    else:
        print("ERROR: We had trouble reading your input")

    if result != "":
        with open("result.txt", "w") as file:
            file.write(result)
        print("A new file has been created under the name result.txt\nMake sure to rename it so it doesn't get overwritten!")
        break
