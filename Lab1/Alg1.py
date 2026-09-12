A=[10,25,7,18,30]
t=18

found=False

for i in range(len(A)):
    if A[i]==t:
        found=True
        break   
    
if found:
    print("Number is found")
else:
    print("Number  is not found")