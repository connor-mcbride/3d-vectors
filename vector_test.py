from Vector import Vector
import Vector as vec

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([[1, 0], [0, 1]])
v4 = Vector([[0, 1], [1, 0]])

print(vec.norm(v1))
print(vec.norm([1, 2, 3, 4]))