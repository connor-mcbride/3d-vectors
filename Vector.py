import copy

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


    def __add__(self, vector: list | object) -> 'Vector':
        vector = Vector(vector) if isinstance(vector, list) else vector
        if isinstance(vector, Vector):
            if self.shape != vector.shape:
                raise ValueError("Vectors must have the same shape.")
            
            if self.dimension == 2:
                return Vector([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.components, vector.components)])
            return Vector([a + b for a, b in zip(self.components, vector.components)])
        
        raise TypeError("Unsupported operand type(s) for +: 'Vector' and '{}'".format(type(vector).__name__))


    def __sub__(self, vector: list | object) -> 'Vector':
        vector = Vector(vector) if isinstance(vector, list) else vector
        if isinstance(vector, Vector):
            if self.shape != vector.shape:
                raise ValueError("Vectors must have the same shape.")
            
            if self.dimension == 2:
                return Vector([[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self.components, vector.components)])
            return Vector([a - b for a, b in zip(self.components, vector.components)])
        
        raise TypeError("Unsupported operand type(s) for -: 'Vector' and '{}'".format(type(vector).__name__))


    def __mul__(self, scalar: int | float) -> 'Vector':
        if not isinstance(scalar, (int, float)):
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and '{}'".format(type(scalar).__name__))
        
        if self.dimension == 2:
            return Vector([[scalar * a for a in row] for row in self.components])
        return Vector([scalar * a for a in self.components])
        

    def __truediv__(self, scalar: int | float) -> 'Vector':
        if not isinstance(scalar, (int, float)):
            raise TypeError("Unsupported operand type(s) for /: 'Vector' and '{}'".format(type(scalar).__name__))
        
        if self.dimension == 2:
            return Vector([[a / scalar for a in row] for row in self.components])
        return Vector([a / scalar for a in self.components])
        

    def __rmul__(self, scalar: int | float) -> 'Vector':
        return self.__mul__(scalar)
    

    def __rdiv__(self, scalar: int | float) -> 'Vector':
        return self.__truediv__(scalar)
    

    def __neg__(self) -> 'Vector':
        if self.dimension == 2:
            return Vector([[-a for a in row] for row in self.components])
        return Vector([-a for a in self.components])


    def __eq__(self, vector: 'Vector') -> bool:
        vector = Vector(vector) if isinstance(vector, list) else vector
        if not isinstance(vector, Vector) or self.shape != vector.shape:
            return False
        
        if self.dimension == 2:
            return all(all(abs(a - b) < 1e-6 for a, b in zip(row1, row2)) for row1, row2 in zip(self.components, vector.components))
        else:
            return all(abs(a - b) < 1e-6 for a, b in zip(self.components, vector.components))


    def __getitem__(self, index: int | tuple | slice) -> int | float | object:
        if not isinstance(index, (int, tuple, slice)):
            raise TypeError("Index must be an integer, tuple, or a slice.")
        
        if self.dimension == 2:
            if isinstance(index, tuple):
                if len(index) != 2:
                    raise ValueError("Index tuple must have exactly 2 elements for 2D vectors.")
                return self.components[index[0]][index[1]]
            else:
                return Vector(self.components[index])
        elif self.dimension == 1:
            if isinstance(index, (int, slice)):
                return self.components[index]
            else:
                raise ValueError("Invalid index type.")
        else:
            raise ValueError("Invalid vector dimension.")
        

    def __setitem__(self, index: int | tuple | slice, value: int | float | list | object) -> None:
        if not isinstance(index, (int, tuple, slice)):
            raise TypeError("Index must be an integer, tuple, or slice.")
        
        if self.dimension == 2:
            if isinstance(index, tuple):
                if len(index) != 2:
                    raise ValueError("Index tuple must have exactly 2 elements for 2D vectors.")
                if not isinstance(value, (int, float, list)):
                    raise TypeError("Value must be an integer or float.")
                value = value[0] if isinstance(value, list) else value
                self.components[index[0]][index[1]] = value

            elif isinstance(index, int):
                if isinstance(value, Vector):
                    value = value.components
                if not isinstance(value, list) or len(value) != self.shape[1]:
                    raise ValueError("Value must be a list of the correct length for 2D vectors.")
                self.components[index] = value
            else:
                raise ValueError("Invalid index.")
        elif self.dimension == 1:
            if isinstance(index, int):
                if not isinstance(value, (int, float)):
                    raise TypeError("Value must be an integer, float, or vector.")
                self.components[index] = value
            elif isinstance(index, slice):
                if not isinstance(value, list):
                    raise TypeError("Value must be a list for a slice.")
                if len(value) != len(self.components[index]):
                    raise ValueError("Value must be a list of the correct length.")
                self.components[index] = value
            else:
                raise ValueError("Index must be an integer or slice for 1D vectors.")
        else:
            raise ValueError("Invalid vector dimension.")


    def __matmul__(self, matrix: 'Vector') -> 'Vector':
        return matmul(self, matrix)


    def __rmatmul__(self, matrix: 'Vector') -> 'Vector':
        return matmul(matrix, self)
    

    def __len__(self) -> int:
        return len(self.components)


    def __str__(self) -> str:
        if self.dimension == 2:
            components_str = "\n\t".join(["[" + ", ".join([str(0 if abs(val) < 1e-6 else val) for val in row]) + "]," for row in self.components])
            return f"vector([{components_str[:-1]}])"
        return "vector({})".format(self.components)
    
    
    def __repr__(self) -> str:
        if self.dimension == 2:
            components_str = "\n\t".join(["[" + ", ".join([str(0 if abs(val) < 1e-6 else val) for val in row]) + "]," for row in self.components])
            return f"Vector([{components_str[:-1]}])"
        return "Vector({})".format(self.components)
    

    def copy(self) -> 'Vector':
        new_components = copy.deepcopy(self.components)
        return Vector(new_components)


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
        raise ValueError("Vectors are not correct dimensions for dot product.")
    

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


def argmax(vector: Vector | list) -> int:
    """Returns the index of the maximum value in the vector."""
    vector = vector if isinstance(vector, Vector) else Vector(vector)
    if vector.dimension == 2:
        raise ValueError("Given vector cannot be a matrix.")
    return max(range(len(vector)), key=lambda i: vector[i])


def zeros(shape: tuple) -> Vector:
    """Returns a zero vector or matrix of the given shape."""
    if len(shape) == 1:
        return Vector([0 for _ in range(shape[0])])
    return Vector([[0 for _ in range(shape[1])] for _ in range(shape[0])])


def ones(shape: tuple) -> Vector:
    """Returns a vector or matrix of ones of the given shape."""
    if len(shape) == 1:
        return Vector([1 for _ in range(shape[0])])
    return Vector([[1 for _ in range(shape[1])] for _ in range(shape[0])])


def eye(n: int) -> Vector:
    """Returns the identity matrix of size n x n."""
    return Vector([[1 if i == j else 0 for j in range(n)] for i in range(n)])


def absolute(vector: Vector | list) -> Vector:
    """Returns the absolute value of the given vector."""
    vector = vector if isinstance(vector, Vector) else Vector(vector)
    if vector.dimension == 2:
        return Vector([[abs(a) for a in row] for row in vector])
    return Vector([abs(a) for a in vector])


def lu_decomposition(vector: Vector | list) -> tuple[Vector, Vector, Vector, int]:
    """Returns the LU decomposition of an n x n matrix.
    vector - List of lists representing the matrix.
    Returns a tuple of three matrices, L, U, and P, and an int swap_count.   
    """
    vector = vector if isinstance(vector, Vector) else Vector(vector)
    if vector.dimension != 2 or vector.shape[0] != vector.shape[1]:
        raise ValueError("Matrix must be a square 2D matrix.")
    
    n = vector.shape[0]
    P = eye(n)
    L = eye(n)
    U = vector.copy()
    PF = eye(n)
    LF = zeros((n, n))
    swap_count = 0

    for k in range(n-1):
        max_index = argmax(absolute([row[0] for row in U])) + k
        if max_index != k:
            P = eye(n)
            P[max_index][k:n], P[k][k:n] = P[k][k:n], P[max_index][k:n]
            U[max_index][k:n], U[k][k:n] = U[k][k:n], U[max_index][k:n]
            PF = dot(P, PF)
            LF = dot(P, LF)
            swap_count += 1

        L = eye(n)
        for j in range(k+1, n):
            if U[k][k] != 0:
                L[j][k] = -(U[j][k] / U[k][k])
                LF[j][k] = (U[j][k] / U[k][k])
            else:
                L[j][k] = 0
                LF[j][k] = 0
        U = dot(L, U)

    for i in range(n):
        LF[i, i] = 1

    return LF, U, PF, swap_count


def det(vector: Vector | list) -> float:
    """Calculates the determinant of an n x n matrix.
    Uses the LU decomposition method.
    vector - List of lists representing the matrix.
    """
    vector = vector if isinstance(vector, Vector) else Vector(vector)
    tol = 1e-12
    if vector.dimension == 1:
        raise ValueError("Matrix must be 2D.")
    elif vector.shape[0] != vector.shape[1]:
        raise ValueError("Matrix must be square.")
    
    _, U, _, swap_count = lu_decomposition(vector)
    diag_U = [U[i][i] for i in range(len(U))]
    det_U = 1
    for i in range(len(U)):
        det_U *= diag_U[i]

    # Adjust the determinant if an odd number of row swaps were performed
    if swap_count % 2 == 1:
        det_U *= -1

    return det_U if abs(det_U) > tol else 0.0
    

def inv(vector: Vector | list) -> Vector:
    """Calculates the inverse of an n x n matrix.
    vector - List of lists representing the matrix.
    Raises a ValueError if the matrix is singular.
    """
    vector = vector if isinstance(vector, Vector) else Vector(vector)
    if vector.dimension == 1:
        raise ValueError("Matrix must be 2D.")
    elif vector.shape[0] != vector.shape[1]:
        raise ValueError("Matrix must be square.")

    n = vector.shape[0]
    I = eye(n)
    inv = zeros((n, n))
    L, U, P, _ = lu_decomposition(vector)

    def forward_substitution(L, b):
        y = zeros((n,))
        for i in range(n):
            y[i] = b[i] - dot(L[i][:i], y[:i])
        return y
    
    def backward_substitution(U, y):
        x = zeros((n,))
        for i in range(n-1, -1, -1):
            try:
                x[i] = (y[i] - dot(U[i][i+1:], x[i+1:])) / U[i][i]
            except:
                raise ValueError("Matrix is singular.")
        return x

    # Solve for each column of the inverse
    for i in range(n):
        Pb = dot(P, [row[i] for row in I])
        y = forward_substitution(L, Pb)
        x = backward_substitution(U, y)
        for j in range(n):
            inv[j][i] = x[j]

    return inv


def transpose(vector: Vector | list) -> Vector:
    """Transposes the given the n x n or m x n matrix.
    Given vectors just return the original vector.
    vector - List of lists representing the matrix.
    """
    vector = vector if isinstance(vector, Vector) else Vector(vector)
    if vector.dimension == 1:
        return vector
    
    return Vector([list(row) for row in zip(*vector.components)])
