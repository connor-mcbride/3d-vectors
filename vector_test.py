from Vector import Vector
import Vector as vec

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([[1, 2], [3, 4]])
v4 = Vector([[0, 1], [1, 0]])
v5 = Vector([5, 6])

# print(v3[0, :])
# print(vec.matmul(v2, [[1, 0, 1], [2, 3, 4], [9, 2, 1]]))
# print(vec.matmul([[1, 0, 1], [2, 3, 4], [9, 2, 1]], v2))

# print(vec.dot(v1, v2))
# print(vec.dot(v5, v3))
# print(vec.dot(v3, v5))
# print(vec.matmul(v5, v3))
# print(vec.matmul(v3, v5))

# print(v3.T)
# print(v4.shape)
# print(v3.T)


# v6 = Vector([[1, 2, 3], [4, 5, 6]])
# v7 = Vector([[1, 2], [3, 4], [5, 6]])
# print(vec.transpose(v6.T))
# print(v6.T)
# print(v7.T)
# print(vec.transpose(v6))
# print(vec.transpose(v7))

# print(vec.matmul(v6, v7))

# print(Vector([[1, 2], [3, 4]])[0:][0])
print(vec.det(v3))
print(vec.det([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(vec.det([[2, 9, 2, 4], [3, 4, 2, 0], [1, 1, 9, 8], [4, 2, 8, 4]]))
print(vec.det([[5, 3], [4, 9]]))
print(vec.inv([[5, 1, 2], [0, 1, 5], [9, 3, 5]]))
print(vec.det([[0, 1], [0, 0]]))
# print(v1.copy())
# print(vec.det(v4))
# print(vec.det([[7, 8, 2], [8, 1, 8], [2, 1, 0]]))
# print(vec.det([[4, 3], [8, 4]]))

# print(vec.inv([[5, 3], [4, 9]]))
# print(vec.inv([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
# print(vec.inv(v8))

# mat = [[2, -1, -2],
#        [-4, 6, 3],
#        [-4, -2, 8]]
# L, U, P, _ = vec.lu_decomposition(mat)
# print(L, U)
# print(L @ U == P @ mat)
# print(P)

# L, U, P = vec.lu_decomposition([[0, 1], [1, 0]])
# print(L)
# print(U)
# print(P)
# print(L @ U == P @ [[0, 1], [1, 0]])
# print(L, U)
# print(L @ U)
# print(vec.matmul(P, [[0, 1], [1, 0]]))
# print(vec.inv([[1, 2, 3], [4, 5, 6], [7, 8, 8]]))

# print(vec.inv([[3, 2], [4, 5]]))