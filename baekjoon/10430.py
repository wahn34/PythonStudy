def solution():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
    
solution()