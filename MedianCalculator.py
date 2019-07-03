#Program computes the median val in an entered list

def median(meep):
    mark=sorted(meep)
    for i in mark:
    #Odd Numbers bigger than 1
        if len(mark)%2!=0:
            middle=len(mark)//2
            return mark[middle]
        #Even Numbers
        else:
            mil1=len(mark)/2 -1
            mil2=len(mark)/2
            mean=(mark[mil1]+mark[mil2])/2.0
    return mean
