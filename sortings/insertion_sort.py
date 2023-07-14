def insertion_sort(A):

    for j in range(1,len(A)):
        key = A[j]    
        print("key =",key)    
        i=j-1
        while i>=0 and A[i]>key:
            # print("i =",i)
            # print(A[i],">",key)
            # print(A[i],i,"->",A[i+1],i)
            A[i+1]=A[i]
            i-=1
        # print(A[i],"<-",key)
        A[i+1]=key
        print("New array ->",A)

A = [2,4,1,7,42,12]

print("Input array ->",A)

insertion_sort(A)

print("Sorted Array ->",A)

# 2 3 90 31 90
