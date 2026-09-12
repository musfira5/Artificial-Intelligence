A=[10,25,7,18,30]
B=[5,12,20,35,40]

t=20

found = False

#Search in first array 
for i in range(len(A)):
    if A[i]==t:
        found=True
        break

#Search in second array
if not found:
    for i in range(len(B)):
        if B[i]==t:
            found=True
            break

if found:
    print("Number is found")
else:
    print("Number is not found")