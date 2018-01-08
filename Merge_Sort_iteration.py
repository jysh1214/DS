import random

def Mergesort(A):
    # input: unsorted A_list; output: sorted A
    temp_1 = []
    temp_2 = []
    i = 0

    while True:
        temp_1.append(A[i])
        i += 1
        if ((len(A)-i)>1) or (len(A)%2==0):
            temp_1.append(A[i])
            i += 1
        
        temp_1 = merge_and_sort(temp_1)
        temp_2.append(temp_1)
        temp_1 = []

        if i == len(A):
            i = 0
            A = temp_2
            temp_1 = []
            temp_2 = []

        if len(A) == 1: break
 
    return A

def merge_and_sort(temp_1):
    # input two slice and merge to one
    # input: temp_1[0], temp_1[1]; output: merged one
    if len(temp_1) == 1: return temp_1[0]

    temp = []
    i, j = 0, 0
    while True:
        #i:temp_1[0]
        #j:temp_1[1]

        if (temp_1[0][i] < temp_1[1][j]):
            temp.append(temp_1[0][i])
            i += 1

        else:
            temp.append(temp_1[1][j])
            j += 1

        # one side comparison is completed 
        if (i==len(temp_1[0])):
            temp = put_all(temp_1[1][j:], temp)
            break

        if (j==len(temp_1[1])):
            temp = put_all(temp_1[0][i:], temp)
            break
    
    return temp
 
def put_all(temp_1, temp_2):
    # input: A_list, B_list; put all elements from A to B; output: B
    for x in temp_1:
        temp_2.append(x)

    return temp_2
                    
def main():
    length = 10
    A = [random.randint(0, 100) for i in range(length)]
    A = [[x] for x in A]
    print(A)
    print(Mergesort(A))

if __name__ == '__main__':
    main()
