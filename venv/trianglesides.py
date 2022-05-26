'''
#function definition
def valid_triangle(s1, s2, s3):
    answer = s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1
    print (answer)


def if_triangles(s1, s2, s3):
    if (s1 + s2 > s3) and (s1 + s3 > s2) and(s2 + s3 > s1) :
        print("true")
    else:
     print("false")

#function call
if_triangles(23,80,21)

print("Hello Nayra")
print("Loops is going places")
Name = str(input("Your full name please:"))
print(Name)

a = int(input("Value 1 is :"))
b = int(input("Value 2 is :"))
operator = input("Operator to be used is :")
if operator == '+' :
    print(a+b)
elif operator == '-' :
    print(a-b)
elif operator == '*' :
    print(a*b)
elif operator == '/' :
    print(a/b)
else: print("The calculator cannot perform this function")

for a in range(0,5):
    print(a)

n = int(input("Kindly enter a value:"))
while n<9:
    print(n)
    n = n+1
'''
'''
s = "Music is GOLD"
print(s.upper())
print(s.lower())
print("I am ",str(21),"years old")

meal_cost = 65.50
tax = 6.6/100
tip = 20/100
meal_cost = meal_cost + meal_cost*tax
total = meal_cost + tip*meal_cost
print (total)

name = input("What is your name ?")
print("Nice to meet you "+name+ "Have a wonderful time")
'''
'''
x,y,z = input("Enter the values of x,y and z: ").split()
print("The value of x is ",x)
print("The value of y is ",y)
print("The value of z is ",z)
'''
'''
a,b,c = [int(x) for x in input("Enter the values of a and b: ").split()]
print("The value of a is ",a)
print("The value of b is ",b)
print("The value of c is ",c)
print (a+b)
'''

x = [int(x) for x in input("Enter multiple values: ").split()]
print("The values are ",x)
b = len(x) - 1
A = 0
while b >= 0:
    A += x[b]
    b = b-1
print("The sum equals: ",A)

