#Program Reverses Text entered as string. Can set up to read input as well
def reverse(text):
    word=""
    l=len(text)-1
    while l>=0:
        word= word+ text[l]
        l-=1
    return word
print reverse("racecar")

#Reverse program set up to read input values as string as well and reverse them
in_val= raw_input("Enter a String to be reversed please: ")
def reverse2(yep):
    wording=""
    ls=len(yep)-1
        while ls>=0:
            wording= wording+ yep[ls]
            ls-=1
        return wording
print reverse2(in_val)


