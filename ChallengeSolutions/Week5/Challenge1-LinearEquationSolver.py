import numpy as np

lineqmat = [
    [2,6,5], #[ax,by,c] in ax+by=c...eqn 1 [a b c]
    [4,7,2]  #[cx,dy,e] in cx+dy=e...eqn 2 [d e f]
]
lineqmat_arr = np.array(lineqmat)
print(lineqmat_arr)

def lineqnsolve(matrix_array):
    a = matrix_array[0, 0]
    b = matrix_array[0, 1]
    c = matrix_array[0, 2]
    d = matrix_array[1, 0]
    e = matrix_array[1, 1]
    f = matrix_array[1, 2]

    x = (c-((b*f)/e))/(a-((b*d)/e))
    y = (f-d*x)/e

    return x,y

print(f"\nx = {lineqnsolve(lineqmat_arr)[0]}; y = {lineqnsolve(lineqmat_arr)[1]}\n")
