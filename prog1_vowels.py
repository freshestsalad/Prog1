import random
vowels = ["a","e","i","o","u","y"]

def ouputVowels(string):
    for i in range(0, len(string) - 1):
        letter = string[i]
        if letter in vowels:
            print(string[i])

chars = "abcdeiforusy"
string = ""
for i in range (0,24):
    string += random.choice(chars)

print("The string is: " + string)
print("vowels:")
ouputVowels(string)