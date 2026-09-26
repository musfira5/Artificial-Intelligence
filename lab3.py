#-------Task 1 -----Number divisible by 7 and multiple by 5
'''
for number in range(1500,2701):
    if number % 7 == 0 and number % 5 == 0:
        print(number) 
'''

#------Task 2-------------Celcius-----Fahrenhiet
'''
choice = input("Enter C to convert Celsius to Fahrenheit "
                " or F to convert Fahrenheit to  Celsius: ")

if choice.upper() == "C":
    c=float(input("Enter temperature in Celsius: "))
    f=(9*c/5)+32
    print(c,"C is",f,"Fahrenheit")

elif choice.upper() == "F":
    f=float(input("Enter temperature in Fahrenheit: "))
    c = 5*(f-32)/9
    print(f,"F is",c,"Celsisus")

else:
    print("Invalid choice")
'''

#-----Task 3-------Guess a number btw 1 and 9----------

'''
import random

number=random.randint(1,9)

while True:
    guess=int(input("Guess a number between 1 and 9 : "))
    if guess == number:
       print("Guessed! ")
       break
'''

#------Task 4-----Star Pattern using Nested for loop 
'''
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(4,0,-1):
    for j in range(i):  
        print("*",end="")          
    print()    
'''

#-----Task 5----------------Reverse a word 
'''
word=input("Enter a word : ")
reverse=word[::-1]

print("Reverse : ",reverse)
'''

#----------Task 6--------Count even and odd numbers 

'''
numbers =(1,2,3,4,5,6,7,8,9)

even=0
odd=0

for number in numbers:
    if number % 2 == 0:
        even +=1
    else:
        odd +=1
print("Number of even numbers : ",even)
print("Number of odd numbers  : ",odd)            

'''

#------Task 7-----Print each item and its type

'''
datalist=[1452,11.23,1+2j,True,'w3resource',
          (0,-1),[5,12],
{"class":"V","section":"A"}]

for item in datalist:
    print(item,"->",type(item))
'''    

#-----Task 8------Print 0 to 6 except 3 and 6
'''
for number in range(7):

    if(number == 3 or number == 6):
        continue

    print(number)
'''

#----Task 9 (a)-------Fibonnaci Series btw 0 and 50
'''
a=0
b=1

while a <= 50:
    print(a,end=" ")

    c=a+b
    a=b
    b=c
'''
#------Task 9 (b)------FizzBuzz----------------

'''
for number in range(1,51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)        

'''  

#------Task 10------Create a 2D array---------

'''
m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns: "))

array = []

for i in range(m):
    row=[]

    for j in range(n):
        row.append(i*j)
    array.append(row)

print(array)        


'''

#----Task 11----Sequence of lines ----

'''
while True:
    line = input("Enter a line : ")
    if line == "" :
        break

    print(line.lower())

print("program ended")  

'''

#----Task 12---Convert binary numbers and find those divisible by 5

'''
numbers = input("Enter comma-separated 4 digit binary numbers: ")

numbers=numbers.split(",")

result = []

for binary in numbers:
    decimal =int(binary,2)

    if(decimal % 5 == 0):
        result.append(binary)

print(",".join(result))        

'''


#---Task 13--------Count letter and digits

'''
text=input("Enter a string : ")

letters = 0
digits = 0

for character in text:

    if character.isalpha():
        letters +=1

    elif character.isdigit():
        digit +=1

print("Letters: ",letters)
print("Digits: ",digits)            
'''

#---Task 14-----Password Validation


password=input("Enter Password : ")

lower=False
upper=False
digit=False
special=False

for character in password:

    if character.islower():
        lower = True

    elif character.isupper():
        upper = True    

    elif character.isdigit():
        digit = True

    elif character in "$#@":
        special = True
    
if(6 <= len(password) <=16 and lower and
    upper and digit and special):

        print("Valid password ")
        
else:
        print("Invalid password")             