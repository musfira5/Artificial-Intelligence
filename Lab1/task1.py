print("Hello world")

#Task 1: Comments  in python

x=1
#The initial value of x is 1:

if x>0:
    print("These are two commnets") #Print a string.


#getting input

txt=input("Type something to test this out: ")
print(txt)


#Task 2: Multiple Statement on a single line

print("Statement 1")
print("Statement 2")    


#You can write above two statements on a single line

print("Statement 1");print("Statement 2")

#Task 3: Indentation Error

y=1
if y>0 :
 print ("This statement has no indentation")
 print ("This statement has no indentation")


# single statement indentation

z=1
if z>0 :
 print ("This statement has single indentation")
 print ("This statement has single indentation")
 

  #single statement indentation +space 

z=1
if z>0 :
    print ("This statement has space  + tab indentation")
    print ("This statement has space  + tab indentation")


#Task 4: Data Types 

a=1452
print(type(a))

b=(-4587)
print(type(b))

c=0
print(type(c))

g=1.03
print(type(g))

h=-11.23
print(type(h))

i=.34
print(type(i))

j=2.12e-10
print(type(j))

k=5E220
print(type(k))

#Task 4: Real + imaginary numbers

x= complex(1,2)
type(x)
print(x)

 
z= complex(1,2)
type(z)
print(z)


#Task 5: Bool expression

x=True
type(x)
print(type(x))


y=False
type(y)
print(type(y))


#Task 6: Strings 

str1="String1" #string start and end with double quotes
print(str1)


str2='String 2' #string start and end with double quotes
print(str2)

#str3='String" #string start and end with double quotes
#print(str3)

#str4="String' #string start and end with double quotes
#print(str4)

str5="Day `sss" #string start and end with double quotes
print(str5)

str2='Day "s ' #string start and end with double quotes
print(str2)


# Task 6: Special Characters

print("This is a backslash (\\) mark.")

print("This is tab \t key")

print("These are \'single quotes\'")

print("These are \"double quotes\  " )

print("This is a new line \nNew line")



#Task 7: String indices and assessing elements

string1="PYTHON TUTORIAL"
print(string1[0])  #Print first Character


print(string1[-15])  #Print first Character


print(string1[14])  #Print last Character


print(string1[-1])  #Print last Character

      
print(string1[4])  #Print 4th Character

print(string1[-11])  #Print 4th Character

# print(string1[16])  #Print 4th Character

#Task 8: Creating lists

my_list1=[5,12,13,14] #the list contains all integer values

print(my_list1)

my_list2=['red','blue','black','white'] #the list contain ins all string values 

print(my_list2)

#Task 9 : List indices

my_list=[]

print(my_list)


color_list=["RED","BLUE","BLACK","WHITE"]

#The list have four elements indices start 0 and end at 3

color_list[0]  #Return  first Element

print(color_list[0],color_list[3]) #Return  first Element and last elements


color_list[-1] #return Last element

#print(color_list[4]) #This will raise an IndexError since the index is out of bounds

 
#Task 10: List slicing

color_list=['Red','Blue','Black','White'] #The list have four elements indices start 0 and end at 3 

print(color_list[0:2]) #cut first two items


print(color_list[1:2]) #cut second items


print(color_list[1:-2]) #cut second items


print(color_list[:3]) #cut first three  items

print(color_list[:]) #Creates copy of original line

