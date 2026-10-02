#----------Task 1-------Stack Implementation-------
'''
class Stack:
 def __init__(self):
     self.stack = []

 def push(self,item):
     self.stack.append(item)

 def pop(self):
   if len(self.stack) == 0:
     print("Stack is empty ")
   else:
     self.stack.pop()

 def display(self):
   print("Stack: ",self.stack)
   
s=Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()

s.display()

'''

#------Task 2-----------Queue Implementation------

'''
class Queue:
 def __init__(self):
     self.queue = []

 def enqueue(self,item):
     self.queue.append(item)

 def dequeue(self):
   if len(self.queue) == 0:
     print("Queue is empty ")
   else:
     self.queue.pop(0)

 def display(self):
   print("Queue: ",self.queue)


q= Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.display()

'''

#------Task 3---------Binary Search------------

numbers = [10,20,30,40,50,60,70]

target = 30

low = 0
high = len(numbers) - 1

while low <= high:

    mid = (low + high ) // 2

    if numbers[mid] == target :
        print("Elements found at index :", mid)
        break

    elif numbers[mid]< target: 
        low = mid + 1

    else:
        high = mid - 1       

else :
   print("Element  not found")        