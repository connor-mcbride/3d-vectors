class Vector:
    """Vector class for 1D and 2D vectors.
    components - List of integers or floats representing the vector.
                    Can also be a list of lists for 2D vectors.
    
    Example usage:
    v1 = Vector([1, 2, 3])
    v2 = Vector([[1, 0], [3, 1]])
    v3 = Vector([[1, 2], [3, 4], [5, 6]])
    >>> v1.shape
    (3,)
    >>> v2.shape
    (2, 2)
    >>> v3.shape
    (3, 2)
    >>> v3.dimension
    2
    >>> v2.T
    Vector([[1, 3], [0, 1]])
    """
    def __init__(self, components: list) -> None:
        if not isinstance(components, list):
            raise TypeError("Vector must be a list.")
        
        if components and all(isinstance(item, list) for item in components):
            length = len(components[0])
            if not all(len(item) == length for item in components):
                raise ValueError("All sub-vectors must have the same length.")
        elif any(isinstance(item, list) for item in components):
            raise ValueError("Invalid vector format: mix of lists and non-lists.")
        
        if len(components) == 0:
            self.shape = 0,
            self.dimension = 1
        elif isinstance(components[0], list):
            if isinstance(components[0][0], list):
                raise TypeError("Only supports 1D and 2D vectors.")
            self.shape = (len(components), len(components[0]))
            self.dimension = 2
        else:
            self.shape = len(components),
            self.dimension = 1
        self._transposed = False
        self.components = components

    
    @property
    def T(self) -> 'Vector':
        if self.dimension == 1:
            return self
        transposed_view = Vector(self.components)
        transposed_view._transposed = not self._transposed
        return transposed_view
    
    
    @property
    def components(self) -> list:
        if self._transposed:
            return [list(row) for row in zip(*self._components)]
        return self._components
    

    @components.setter
    def components(self, values):
        self._components = values


    def __add__(self, vector: 'Vector') -> 'Vector':
        if isinstance(vector, Vector):
            if self.shape != vector.shape:
                raise ValueError("Vectors must have the same shape.")
            
            if self.dimension == 2:
                return Vector([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.components, vector.components)])
            else:
                return Vector([a + b for a, b in zip(self.components, vector.components)])
        
        raise TypeError("Unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other).__name__))


    def __sub__(self, vector: 'Vector') -> 'Vector':
        if isinstance(vector, Vector):
            if self.shape != vector.shape:
                raise ValueError("Vectors must have the same shape.")
            
            if self.dimension == 2:
                return Vector([[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self.components, vector.components)])
            else:
                return Vector([a - b for a, b in zip(self.components, vector.components)])
        
        raise TypeError("Unsupported operand type(s) for -: 'Vector' and '{}'".format(type(other).__name__))


    def __mul__(self, scalar: int | float) -> 'Vector':
        if not isinstance(scalar, (int, float)):
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and '{}'".format(type(scalar).__name__))
        
        if self.dimension == 2:
            return Vector([[scalar * a for a in row] for row in self.components])
        else:
            return Vector([scalar * a for a in self.components])
        

    def __rmul__(self, scalar: int | float) -> 'Vector':
        return self.__mul__(scalar)


    def __eq__(self, vector: 'Vector') -> bool:
        if not isinstance(vector, Vector):
            return False
        if self.shape != vector.shape:
            return False
        
        if self.dimension == 2:
            return all(all(a == b for a, b in zip(row1, row2)) for row1, row2 in zip(self.components, vector.components))
        else:
            return all(a == b for a, b in zip(self.components, vector.components))


    def __getitem__(self, index: int | tuple) -> int | float | object:
        if not isinstance(index, (int, tuple)):
            raise TypeError("Index must be an integer.")
        
        if self.dimension == 2:
            if isinstance(index, tuple):
                return self.components[index[0]][index[1]]
            else:
                return Vector(self.components[index])
        elif self.dimension == 1 and isinstance(index, int):
            return self.components[index]
        
        raise ValueError("Invalid index.")


    def __setitem__(self, index: int | tuple, value: int | float) -> None:
        if not isinstance(index, (int, tuple)):
            raise TypeError("Index must be an integer.")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float.")
        
        if self.dimension == 2 and isinstance(index, tuple):
            self.components[index[0]][index[1]] = value
        elif self.dimension == 1 and isinstance(index, int):
            self.components[index] = value
        else:
            raise ValueError("Invalid index.")
    

    def __matmul__(self, matrix: 'Vector') -> 'Vector':
        return matmul(self, matrix)


    def __rmatmul__(self, matrix: 'Vector') -> 'Vector':
        return matmul(matrix, self)
    

    def __len__(self) -> int:
        return len(self.components)


    def __str__(self) -> str:
        if self.dimension == 2:
            components_str = "\n\t".join(["[" + ", ".join(map(str, row)) + "]," for row in self.components])
            return f"vector([{components_str[:-1]}])"
        return "vector({})".format(self.components)
    
    
    def __repr__(self) -> str:
        if self.dimension == 2:
            components_str = "\n\t".join(["[" + ", ".join(map(str, row)) + "]," for row in self.components])
            return f"Vector([{components_str[:-1]}])"
        return "Vector({})".format(self.components)


def norm(vector: Vector | list) -> float:
    """Returns the norm of a vector or matrix.
    The matrix norm used is the Frobenius norm.
    vector - List of integers or floats representing the vector.
                Can also be a list of lists for 2D vectors.
    """
    if not isinstance(vector, (Vector, list)):
        raise TypeError("Vector must be of type 'Vector' or 'list'.")
    
    if isinstance(vector, list):
        if not all(isinstance(item, (int, float)) for item in vector):
            raise TypeError("All items in the list must be integers or floats.")
        return sum(a**2 for a in vector)**0.5
    if vector.dimension == 2:
        return sum(sum(a**2 for a in row) for row in vector)**0.5
    return sum(a**2 for a in vector)**0.5


def dot_1d(vector1: Vector, vector2: Vector) -> float:
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length.")
    return sum(a * b for a, b in zip(vector1, vector2))


def dot_2d(vector1: Vector, vector2: Vector) -> Vector:
    if vector1.shape[1] != vector2.shape[0]:
        vector1, vector2 = vector2, vector1
    if vector1.shape[1] != vector2.shape[0]:
        raise ValueError("Vectors are not correct dimensions for dot product.")
    
    return Vector([[sum(a * b for a, b in zip(row, col)) for col in zip(*vector2)] for row in vector1])


def dot(vector1: Vector | list, vector2: Vector | list) -> float:
    """Returns the dot product of two vectors."""
    vector1 = vector1 if isinstance(vector1, Vector) else Vector(vector1)
    vector2 = vector2 if isinstance(vector2, Vector) else Vector(vector2)

    if vector1.dimension == 1 and vector2.dimension == 1:
        return dot_1d(vector1, vector2)
    elif vector1.dimension == 2 and vector2.dimension == 2:
        return dot_2d(vector1, vector2)
    elif vector1.dimension == 2 and vector2.dimension == 1:
        if vector1.shape[1] != vector2.shape[0]:
            raise ValueError("Vectors are not correct dimensions for dot product.")
        return Vector([sum(a * b for a, b in zip(row, vector2)) for row in vector1])
    elif vector1.dimension == 1 and vector2.dimension == 2:
        vector1, vector2 = vector2, vector1
        if vector1.shape[1] != vector2.shape[0]:
            raise ValueError("Vectors are not correct dimensions for dot product.")
        return Vector([sum(a * b for a, b in zip(vector2, col)) for col in zip(*vector1)])
    

def matmul(vector1: Vector | list, vector2: Vector | list) -> Vector:
    """Returns the matrix product of two vectors."""
    vector1 = vector1 if isinstance(vector1, Vector) else Vector(vector1)
    vector2 = vector2 if isinstance(vector2, Vector) else Vector(vector2)

    if vector1.dimension == 1 and vector2.dimension == 1:
        return Vector([dot_1d(vector1, vector2)])
    elif vector1.dimension == 2 and vector2.dimension == 2:
        return dot_2d(vector1, vector2)
    if vector1.dimension == 2 and vector2.dimension == 1:
        if vector1.shape[1] != vector2.shape[0]:
            raise ValueError("Vectors are not correct dimensions for dot product.")
        return Vector([sum(a * b for a, b in zip(row, vector2)) for row in vector1])
    if vector1.dimension == 1 and vector2.dimension == 2:
        vector1, vector2 = vector2, vector1
        if vector1.shape[1] != vector2.shape[0]:
            raise ValueError("Vectors are not correct dimensions for dot product.")
        return Vector([sum(a * b for a, b in zip(vector2, col)) for col in zip(*vector1)])


def cross(vector1: Vector | list, vector2: Vector | list) -> Vector:
    """Returns the cross product of two 3D vectors.
    vector1 - First vector.
    vector2 - Second vector.
    """
    vector1 = vector1 if isinstance(vector1, Vector) else Vector(vector1)
    vector2 = vector2 if isinstance(vector2, Vector) else Vector(vector2)

    if vector1.dimension == 1 and vector2.dimension == 1:
        if len(vector1) != 3 or len(vector2) != 3:
            raise ValueError("Vectors must be 3D.")
        return Vector([vector1[1] * vector2[2] - vector1[2] * vector2[1],
                       vector1[2] * vector2[0] - vector1[0] * vector2[2],
                       vector1[0] * vector2[1] - vector1[1] * vector2[0]])
    raise ValueError("Given vectors cannot be matrices.")


def det(vector: Vector | list) -> float:
    """Calculates the determinant of an n x n matrix.
    vector - List of lists representing the matrix.
    """
    pass


def inv(vector: Vector | list) -> Vector:
    """Calculates the inverse of an n x n matrix.
    vector - List of lists representing the matrix.
    """
    pass


def transpose(vector: Vector | list) -> Vector:
    """Transposes the given the n x n or m x n matrix.
    Given vectors just return the original vector.
    vector - List of lists representing the matrix.
    """
    vector = vector if isinstance(vector, Vector) else Vector(vector)
    if vector.dimension == 1:
        return vector
    
    return Vector([list(row) for row in zip(*vector.components)])
