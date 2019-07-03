#Program that splits a phrase and changes the hot words to asteriks
def censor(text,word):
    #split our input string based on the spaces
    phrase=text.split()
    #Counter for the number of instances the word appears
    counter=0
    #Creates a variable to hold the new string after adjusting for hot word
    result=""
    #Stars for the length of the hot word
    stars="*"*len(word)
    #for each segment in phrase
    for i in phrase:
        #if the segment is equal to the hot word
        if i==word:
            #setting that index of the hot word equal to our stars variable
            phrase[counter]= stars
        #incrementing our counter
        counter+=1
    #rejoining our split phrase segments
    result= " ".join(phrase)
    return result
