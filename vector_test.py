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

print(v3.T)
# print(v4.shape)
# print(v3.T)


v6 = Vector([[1, 2, 3], [4, 5, 6]])
v7 = Vector([[1, 2], [3, 4], [5, 6]])
print(vec.transpose(v6.T))
print(v6.T)
print(v7.T)
print(vec.transpose(v6))
print(vec.transpose(v7))