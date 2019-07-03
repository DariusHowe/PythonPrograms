#Program reads the input of a list and removes the duplicate items in that list
#creates unique essence
#Can change to keep history of values that are duplicated i.e. x occurs y times etc
def remove_duplicates(shoop):
    no_dups=[]
    for i in shoop:
        while i not in no_dups:
            no_dups.append(i)
    return no_dups
