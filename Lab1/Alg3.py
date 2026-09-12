A=[10,20,30,40,50]
B=[15,25,30,45,50]

found=False

for i in range(len(A)):
    for j in range(len(B)):
        if A[i]==B[j]:
            print("Common number:",A[i])
            found=True;
            break
    if found:
       break

if not found:
    print("No common number found")

            
            