def matrix(A,B):
    aRows = len(A)
    bColomns = len(B[0])
    aColomns = len(A[0])
    result = [[0 for row in range(bColomns)] for col in range(aRows)]
    for s in range(aRows):
        for j in range(bColomns):
            for k in range(aColomns):
                result[s][j] += A[s][k]*B[k][j]
    return result


A =[1,2],[3,4]
B = [5,6],[7,8]
print(matrix(A,B))
