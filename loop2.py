alphabets = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for letter in alphabets:
    if letter in vowels:
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonent")