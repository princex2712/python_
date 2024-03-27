# Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:

# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73
def fun(age):
    if age==1 or age==2:
        return 10.5*age
    return 4*(age-2)+10.5*2
print(fun(15))