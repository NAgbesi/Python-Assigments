#User is to input the operator to be used to peform the calculation
print("Kindly enter any one of the following operators to be used to perform a calculation : +, -, %, **, / and log ")
Operator = input("Kindly input the operator to be used to perform the calculation: ")
print(Operator)

#if statement to determine which function is to be performed as according to the variable chosen
#if statement to achieve a fast run time
if Operator== "/":
 x,y = [int(x) for x in input("Enter any two values to be divided:").split()]
 print("The dividend is ",x)
 print("The divisor is ",y)
 Z = x/y
 print("The result of the division is: ", Z)

#calculation of modulus. No need for a loop since it's just two variables
elif Operator== "%":
 x,y = [int(x) for x in input("Enter any two values to find the modulus:").split()]
 print("The dividend is ",x)
 print("The divisor is ",y)
 Z = x%y
 print("The result of the modulus is: ", Z)

#calculation of exponentials. No need for a loop since it needs just two variables
elif Operator== "**":
 x,y = [int(x) for x in input("Enter any two values to find the exponential:").split()]
 print("The base is ",x)
 print("The exponent is ",y)
 Z = x**y
 print("The result of the exponential is: ", Z)

#addition section to add multiple values
#use a while loop
#addition performed based on the index of the contents of the list
elif Operator== "+":
    x = [int(x) for x in input("Enter multiple values to be added: ").split()]
    print("The values to be added are: ",x)
    Z = 0
    y = len(x)-1
    while y>=0:
        Z += x[y]
        y = y-1
    print("The summation equals: ",Z)

#subtraction section
#use a while loop to access each value in the list
#values accessed using their indexes in the list
elif Operator== "-":
    x = [int(x) for x in input("Enter multiple values to be subtracted: ").split()]
    print("The values to be subtracted are: ",x)
    Z = x[0]
    y = len(x)-1
    while y>0:
        Z -= x[y]
        y = y-1
    print("The subtraction equals: ",Z)

#log is an inbuilt function in the math library.
#math library must be improted to access the log function
#no need for a loop since it's just two values
elif Operator=="log":
    import math
    x,y = [int(x) for x in input("Kindly enter the argument and base: ").split()]
    Z = math.log(x,y)
    print("The logarithm of "+str(x)+ " base " +str(y)+ " is " +str(Z))

#in the situation where the operator entered is not covered by this code
else:
    print("The operator given is invalid")