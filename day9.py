#program to loop through a list of numbers and add +2 to every value to elements in list
list=[1,2,3,4,5,6,7,8,9,10]
res=[]
for i in list:
    res.append(i+2)
print(res)


#program to get the below pattern
#54321
#4321
#321
#21
#1
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
    
 #Program to Print the Fibonacci sequence  
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       

#Armstrong number and write a code with a function

#An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.
num1=int(input("Enter a number :"))
sum=0
temp=num1
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num1==sum:
     print(num1,"is an Armstrong number")
else:
     print(num1,"is not an Armstrong number") 
     
     
#program to print the multiplication table of 9
num = 9
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
   
   
#program is negative or positive
num = float(input("Enter a number: "))  
if num > 0:  
 print("{0} is a positive number".format(num))  
elif num == 0:  
   print("{0} is zero".format(num))   
else:  
   print("{0} is negative number".format(num))   
  
    
#program to convert the number of days to ages
def find( number_of_days ):
    year = int(number_of_days / 365)
    print(year,'Years ago !')
no_days=564
find(no_days)


#Trigonometry problem using math function write a program to solve using math function
import math
print(math.sin(math.pi/3)) 
print(math.tan(math.pi/3))
print(math.cos(math.pi/6))


#calculator only on a code level by using if condition (Basic arithmetic calculation)
def add(num1, num2): 
    return num1 + num2 
def subtract(num1, num2): 
    return num1 - num2 
def multiply(num1, num2): 
    return num1 * num2 
def divide(num1, num2): 
    return num1 / num2 
print("Please select operation -\n" , "1. Add\n" , "2. Subtract\n" ,"3. Multiply\n",  "4. Divide\n")
select = int(input("Select operations form 1, 2, 3, 4 :"))
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
if select == 1: 
    print(number_1, "+", number_2, "=", add(number_1, number_2)) 
elif select == 2: 
    print(number_1, "-", number_2, "=", subtract(number_1, number_2)) 
elif select == 3: 
    print(number_1, "*", number_2, "=", multiply(number_1, number_2)) 
elif select == 4: 
    print(number_1, "/", number_2, "=", divide(number_1, number_2)) 
else: 
    print("Invalid input") 