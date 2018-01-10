import random

def Insort(A):
    n = len(A)
    for i in range(1, n):
        B = Insert(A[0:i], A[i])   
        # A[0:i+1] replace by B
        for j in range(i+1):
            A[j] = B[j]

    return A

def Insert(m, data):
    # insert data to sorted list
    # input: m_list, data

    l = len(m) - 1
    m.append(0)

    while  data < m[l]:
        m[l+1] = m[l]
        l -= 1
        if l < 0: break

    m[l+1] = data

    return m

def main():
    length = 10
    A = [random.randint(0, 100) for i in range(length)]

    print(A)
    print(Insort(A))

if __name__ == '__main__':
    main()
