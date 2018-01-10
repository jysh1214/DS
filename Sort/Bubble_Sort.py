import random

def Bubblesort(A):
    n = len(A)

    for i in range(1, n):
        swap = False
        for j in range(n-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swap = True

        if not swap: break

    return A

def main():
    length = 10
    A = [random.randint(0, 100) for i in range(length)]

    print(A)
    print(Bubblesort(A))

if __name__ == '__main__':
    main()
