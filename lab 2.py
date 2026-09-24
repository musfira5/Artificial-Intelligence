#task 1------------while loop
'''
count=0
while(count < 3):
  count=count+1;
  print("Hello Geek")'''


# task2-------Single statement while block
#count=0
#while(count==0):print("Hello Geek") 



#task3---------for loop 
#Example 1
'''print("List Iteration")
l=["geeks","for","geeks"]
for i in l:
  print(i)'''

#Example 2

'''print("\n Tuple Iteration")
t=("geeks","for","geeks")
for i in t:
  print(i)'''


#Example 3

'''print("\nString Iteration")
s="Geeks"
for i in s:
  print(i)'''


#task4-----------Iterating by index of sequence

'''listt=["geeks","for","geeks"]
for index in range(len(listt)):
    print(listt[index])'''


#task 5----Loop Control Statemnet

# Print all letters except 'e' and 's'
'''for letter in 'geeksforgeeks':
  if letter =='e' or letter=='s':
     continue
  print('Current Letter:',letter)
  '''
   
#break statement
'''  
for letr in 'geeksforgeeks':
    # break the loop as soon it sees 'e' or 's'
    if letr =='e' or letr =='s':
        break
    print('Current Letter:',letr)
'''

#Task 6-----Creating a Function

'''def my_function():
  print("Hello from a function")

#Calling a function
my_function()'''


#Parameters
'''
def my_func(fname):
  print(fname+ " Refsnes")
my_func("Emil")
my_func("Tobias")
my_func("Linus")'''

#Default Parameter Value
'''
def my_fnc(country="Norway"):
  print("I am from "+ country)
my_fnc("Sweden")
my_fnc("India")
my_fnc()
my_fnc("brazil")  '''


#Passing list as a parameter
'''
def my_fn(food):
    for x in food:
      print(x)

fruits=["apple","banana","cherry"]  
my_fn(fruits)   ''' 


#return Value
'''
def my_funct(x):
   return 5*x

print(my_funct(3))
print(my_funct(5))
print(my_funct(9))'''


#keyword arguments

'''def my_fc(child3,child2,child1):
   print("The youngest child is " + child3)
my_fc(child1="Emil",child2="Tobias",child3="Linus") '''


#Task 7--------Classes/objects
'''
class MyClass: x=5
p1=MyClass()
print(p1.x)'''

#init() function
'''
class Person:
  def __init__(self,name,age):
    self.name= name
    self.age= age

p2=Person("John",34)
p3=Person("Mia",22)

print(p2.name)
print(p2.age)

print(p3.name)
print(p3.age)
'''

#Object method

class Perrson:
  def __init__(self,name,age):
    self.name= name
    self.age= age

  def myfnc(self):
    print("Hiiiiii my name is "+ self.name)


p4=Perrson("Miaa",32)
p4.myfnc()
     