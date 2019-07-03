#Dynamic score system based on keys in a dictionary

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                "x": 8, "z": 10}

def scrabble_score(word):
    #Score Counter
    total=0
    #Puts all characters in word as lowercase chars
    word=word.lower()
        #iterates through word for the length of the word
        for char in word:
            #iterates through the score dictionary
            for chars in score:
                if char==chars:
                #Increments total score counter based on score associated in scores dictionary
                    total= total+ score[chars]
        return total

#Test Case
print scrabble_score("LoveYouMf")
