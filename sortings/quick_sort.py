import random


def quick_sort(A, low, high):

    if low < high:
        # print("array->", A)
        pivot = partition(A, low, high)
        quick_sort(A, low, pivot-1)
        quick_sort(A, pivot+1, high)


def partition(A, low, high):

    # print("partition called")
    # print(A[low], " to ", A[high])

    # randomize quick sort
    p = random.randint(low, high)
    A[low], A[p] = A[p], A[low]

    pivot_element = A[low]

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


arr = [19, 12, 232, 123, 454, 42, 3, 444]

print("before sorting->", arr)

quick_sort(arr, 0, len(arr)-1)

print("after sorting->", arr)
