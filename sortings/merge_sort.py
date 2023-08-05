

def merge_sort(A,p,r):
    # print("ms->",A,p,r)
    if p<r:
        q = (p+r)//2
        merge_sort(A,p,q)
       
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    
    print("merging->",A[p:q+1],A[q+1:r+1])

    n1 = q-p+1
    n2 = r-q

    L=[]
    R=[]
    
    # copy the divided values into left and right lists
    # for i in range(p,n1):
    #     L.append(A[p+i])
    # for i in range(q,n2):
    #     R.append(A[q+1+i])

    L = A[p:q+1]
    R = A[q+1:r+1]

    inf = 9999999

    L.append(inf)
    R.append(inf)
    
    print("comparing array->",L,R)

    i=0
    j=0

    for k in range(p,r+1):

        # print("k =",k,"r =",r)
        # print("sorting->",L,R,p,r,i,j)
        print("comparing->",L[i],R[j])

        if L[i]<=R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        # print(i,j)
    print("merged array =",A[p:r+1])
# calling the function

A = [2,60,6,98,23,997,4,9,3,1]
p = 0
r = len(A)-1

# print(A[p:q+1],A[q+1:r+1])
print(A)
merge_sort(A,p,r)

print(A)
    
