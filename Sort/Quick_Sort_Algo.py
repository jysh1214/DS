import random

def Quicksort(A, p, r):
    if p < r:
        [A, q] = Partition(A, p, r)
        #A[p:q] = 
        Quicksort(A, p, q)
        #A[q+1:r] = 
        Quicksort(A, q+1, r)

def Partition(A, p, r):
    x = A[r-1]
    i = p - 1
    for j in range(p, r-1):
        if (A[j]<=x):
            i += 1
            A[i], A[j] = A[j], A[i]

    A[r-1], A[i+1] = A[i+1], A[r-1]
    return A,i+1

def main():
    global A # show clear
    length = 10
    A = [random.randint(0, 100) for i in range(length)]
    A = [x for x in A]

    n = len(A)
    print(A)
    Quicksort(A, 0, n)
    print(A)

if __name__ == '__main__':
    main()
