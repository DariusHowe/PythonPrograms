#Removes the vowels from a string entered
def anti_vowel(text):
    word=""
    vowels="aeiouAEIOU"
    for char in text:
        if char not in vowels:
            word+=char
    return word
