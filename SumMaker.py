#Calculates the sum of an input list of integers
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total=0
    for i in scores:
        total+=i
    return total
print grades_sum(grades)

#Calculates average based on sum calculations
def grades_average(grades_input):
    tot=grades_sum(grades_input)
    avg=tot/float(len(grades_input))
    return avg
print grades_average(grades)

#Calculates Variance of input based on average calculations
def grades_variance(scores):
    average=grades_average(scores)
    variance=0
    for score in scores:
        variance=variance+(average-score)**2
    return variance/len(scores)
print grades_variance(grades)

#Calculates Std Deviation of Variance
def grades_std_deviation(variance):
    return variance**0.5
variance=grades_variance(grades)
print grades_std_deviation(variance)

