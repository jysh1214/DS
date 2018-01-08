import random

def Mergesort(A):
    if len(A) == 1: return A
    
    n = int(len(A)/2)
    lMergesort = Mergesort(A[0:n])
    rMergesort = Mergesort(A[n:len(A)])
    return merge_and_sort(lMergesort, rMergesort)

def merge_and_sort(l, r):
    # input two slice and merge to one
    # input: l, r; output: merged one

    temp = []
    i, j = 0, 0
    while True:
        #i->l
        #j->r

        if (l[i] < r[j]):
            temp.append(l[i])
            i += 1

        else:
            temp.append(r[j])
            j += 1

        # one side comparison is completed 
        if (i==len(l)):
            temp = put_all(r[j:], temp)
            break

        if (j==len(r)):
            temp = put_all(l[i:], temp)
            break
    
    return temp 

def put_all(a, b):
    # input: A_list, B_list; put all elements from A to B; output: B
    for x in a:
        b.append(x)

    return b

def main():
    length = 10
    A = [random.randint(0, 100) for i in range(length)]
    print(A)
    print(Mergesort(A))

if __name__ == '__main__':
    main()
