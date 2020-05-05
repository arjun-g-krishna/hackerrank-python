#Function to compute the factorial of the number
def fact(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact
num=int(input("Enter the number: "));
facts=fact(num)
print ("The factorial is "+ str(facts))
