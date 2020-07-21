# FindRpeatingUnit
Find the pattern we are looking for among the large fabric patterns.
Used by sending large and small matrices as parameters to the find_slice () function.
Ex:


a = np.array([[1,0,0],[1,1,0],[1,1,1],[1,0,0],[1,1,0],[1,1,1],[1,0,0],[1,1,0],[1,1,1]])
b = np.array([[1,0,0],[1,1,0],[1,1,1]])
find_slice(a,b)
