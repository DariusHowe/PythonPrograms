#Iterates through a sequence of numbers and outputs the number of times a selected number appears
def count(sequence, item):
    sup=0
    for i in sequence:
        if i==item:
            sup+=1
    return sup
