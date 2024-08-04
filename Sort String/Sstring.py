def main(): 
        letter = input('Enter your sentences :  ')  
        word = [] 
        for i in letter: 
            if i == " " :
                continue
            word.append(i)
        BubbleSort(word,len(word))  
        printlist(word) 
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def BubbleSort(A, n):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            swap(A, i, i + 1)
 
    if n - 1 > 1:
        BubbleSort(A, n - 1)

def printlist(letter):
    str=""
    for i in letter: 
        str=str+i 
    print(str) 

main()
