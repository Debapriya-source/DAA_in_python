import random


def quick_select(A, k):
    if k > 0 and k <= len(A):
        low = 0
        high = len(A)-1

        if low < high:
            print("array->", A)
            pivot = partition(A, low, high)

            less = A[low:pivot]
            greater = A[pivot+1:high+1]
            q = A[pivot]

            print(less, q, greater)

            l = len(less)

            # print("less=", l, "k=", k)

            if l == k-1:
                print(q)
                return q
            elif l > k-1:
                return quick_select(less, k)
            elif l < k-1:
                return quick_select(greater, k-l-1)
        else:
            # print("else")
            print(A[low])
            return A[low]
    else:
        print("invalid value of K")


def partition(A, low, high):

    # print("partition called")
    # print(A[low], " to ", A[high])

    pivot_element = A[low]

    print("pivot element =", pivot_element)
    if len(A) > 1:
        i = low

        for j in range(low+1, high+1):
            # print(A[i], A[j])
            # increment i if any value is less than the pivot element then swap it with current element
            if A[j] <= pivot_element:
                # print("less element found", A[j], pivot_element)
                i += 1
                if i != j:
                    # print("swapping", i, j, A)
                    A[i], A[j] = A[j], A[i]
                    # print("after swapping", A)

        A[i], A[low] = A[low], A[i]
        return i
    # else:
    #     print("else")
    #     return 0


arr = [19, 12, 232, 123, 454, 42, 3, 444]
k = 5


# a = quick_select(arr, k)

print(k, "th smallest->", quick_select(arr, k))
