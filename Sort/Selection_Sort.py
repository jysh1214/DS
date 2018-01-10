import random

def Selectionsort(A):
    n = len(A)
    for i in range(n):
        min_num = A[i]
        for j in range(i, n):
            if A[j] <= min_num:
                min_num = A[j]
                x = j # mark the min number

        A[i], A[x] = A[x], A[i]

    return A

def main():
    length = 10
    A = [random.randint(0, 100) for i in range(length)]

    print(A)
    print(Selectionsort(A))

if __name__ == '__main__':
    main()
