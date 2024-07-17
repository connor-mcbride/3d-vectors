from Vector import Vector
import Vector as vec

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([[1, 0], [0, 1]])
v4 = Vector([[0, 1], [1, 0]])
v5 = Vector([5, 6])

print(vec.dot(v1, v2))
print(vec.dot(v3, v4))
print(vec.dot(v4, v5))
print(vec.dot(v5, v3))
print(vec.dot([[1, 0], [0, 1]], [[0, 1], [1, 0]]))