A=[10,20,30,60,50]

for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i]==A[j]:
            print("True")
            break
    else:
        continue
    break
else:
    print("False")