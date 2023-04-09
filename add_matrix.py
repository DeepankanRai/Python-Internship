A=[[1,3,5],[3,4,7],[2,6,7]]
B=[[2,56,7],[45,3,5],[4,78,9]]

result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]= A[i][j] + B[i][j]

for r in result:
    print(r)