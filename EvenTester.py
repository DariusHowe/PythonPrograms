#Program Tests entry list and returns the even values in it
def purify(nums):
    evens=[]
    for i in nums:
        if i%2==0:
            evens.append(i)
    return evens
