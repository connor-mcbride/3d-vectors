from Vector import Vector
import Vector as vec
import pytest


def assert_equal(x1, x2): 
    assert abs(x1 - x2) < 1e-6


def test_addition():
    """Test the addition of two vectors."""
    A = Vector([1, 2, 3])
    B = Vector([4, 5, 6])
    C = A + B
    expected_C = Vector([5, 7, 9])
    assert C == expected_C

    D = Vector([1, 2, 3, 4])
    E = Vector([5, 6, 7, 8])
    F = D + E
    expected_F = Vector([6, 8, 10, 12])
    assert F == expected_F

    G = Vector([1, 2, 3])
    H = Vector([4, 5, 6, 7])
    with pytest.raises(ValueError):
        G + H

    I = Vector([[2, 9], [8, 7]])
    J = Vector([[3, 4], [5, 6]])
    K = I + J
    expected_K = Vector([[5, 13], [13, 13]])
    assert K == expected_K

    L = Vector([[0.02435193, 0.12113953, 0.51341871, 0.51406604],
                [0.74607795, 0.68963792, 0.193141, 0.53882405],
                [0.81867092, 0.08676632, 0.86602892, 0.39819585],
                [0.73985199, 0.02076741, 0.91453214, 0.98062587]])
    M = Vector([[0.85073188, 0.55378699, 0.31115142, 0.1628534 ],
                [0.04462666, 0.67452745, 0.58452351, 0.87848518],
                [0.96296666, 0.42955904, 0.92096604, 0.34789241],
                [0.26936911, 0.30010564, 0.99791588, 0.29417954]])
    N = L + M
    expected_N = Vector([[0.87508382, 0.67492652, 0.82457013, 0.67691944],
                         [0.79070461, 1.36416537, 0.77766451, 1.41730923],
                         [1.78163758, 0.51632537, 1.78699496, 0.74608827],
                         [1.0092211 , 0.32087305, 1.91244801, 1.27480541]])
    assert N == expected_N


def test_subtraction():
    """Test the subtraction of two vectors."""
    A = Vector([1, 2, 3])
    B = Vector([4, 5, 6])
    C = A - B
    expected_C = Vector([-3, -3, -3])
    assert C == expected_C

    D = Vector([1, 2, 3, 4])
    E = Vector([5, 6, 7, 8])
    F = D - E
    expected_F = Vector([-4, -4, -4, -4])
    assert F == expected_F

    G = Vector([[1, 2, 3], [0, 2, 1]])
    H = Vector([[3, 1, 2], [9, 3, 2], [6, 2, 0]])
    with pytest.raises(ValueError):
        G - H

    I = Vector([[2, 9], [8, 7]])
    J = Vector([[3, 4], [5, 6]])
    K = I - J
    expected_K = Vector([[-1, 5], [3, 1]])
    assert K == expected_K

    L = Vector([[0.02435193, 0.12113953, 0.51341871, 0.51406604],
                [0.74607795, 0.68963792, 0.193141, 0.53882405],
                [0.81867092, 0.08676632, 0.86602892, 0.39819585],
                [0.73985199, 0.02076741, 0.91453214, 0.98062587]])
    M = Vector([[0.85073188, 0.55378699, 0.31115142, 0.1628534 ],
                [0.04462666, 0.67452745, 0.58452351, 0.87848518],
                [0.96296666, 0.42955904, 0.92096604, 0.34789241],
                [0.26936911, 0.30010564, 0.99791588, 0.29417954]])
    N = L - M
    expected_N = Vector([[-0.82637995, -0.43264746,  0.20226729,  0.35121264],
                         [ 0.70145129,  0.01511047, -0.39138251, -0.33966113],
                         [-0.14429574, -0.34279272, -0.05493712,  0.05030344],
                         [ 0.47048288, -0.27933823, -0.08338374,  0.68644633]])
    assert N == expected_N


def test_scalar_multiplication():
    """Test the scalar multiplication of a vector."""
    A = Vector([1, 2, 3])
    B = 2 * A
    expected_B = Vector([2, 4, 6])
    assert B == expected_B

    C = Vector([1, 2, 3, 4])
    D = 3 * C
    expected_D = Vector([3, 6, 9, 12])
    assert D == expected_D

    E = Vector([[1, 2, 3], [4, 5, 6]])
    F = -4 * E
    expected_F = Vector([[-4, -8, -12], [-16, -20, -24]])
    assert F == expected_F

    G = Vector([[1, 2], [3, 4], [5, 6]])
    H = 5 * G
    expected_H = Vector([[5, 10], [15, 20], [25, 30]])
    assert H == expected_H

    I = Vector([[1, 2, 3, 4], [5, 6, 7, 8]])
    J = 6 * I
    expected_J = Vector([[6, 12, 18, 24], [30, 36, 42, 48]])
    assert J == expected_J

    K = Vector([[9, 2, 5], [8, 6, 1]])
    assert -K == -1 * K

    L = Vector([[2, 4], [6, 8]])
    M = 0.5 * L
    expected_M = Vector([[1, 2], [3, 4]])
    assert M == expected_M

    N = Vector([[5, 2], [9, 1]])
    O = 0 * N
    expected_O = Vector([[0, 0], [0, 0]])
    assert O == expected_O


def test_scalar_division():
    """Test the scalar division of a vector."""
    A = Vector([1, 2, 3])
    B = A / 2
    expected_B = Vector([0.5, 1, 1.5])
    assert B == expected_B

    C = Vector([1, 2, 3, 4])
    D = C / 3
    expected_D = Vector([1/3, 2/3, 1, 4/3])
    assert D == expected_D

    E = Vector([[1, 2, 3], [4, 5, 6]])
    F = E / 4
    expected_F = Vector([[1/4, 1/2, 3/4], [1, 5/4, 3/2]])
    assert F == expected_F

    G = Vector([[1, 2], [3, 4], [5, 6]])
    H = G / 5
    expected_H = Vector([[1/5, 2/5], [3/5, 4/5], [1, 6/5]])
    assert H == expected_H

    I = Vector([[1, 2, 3, 4], [5, 6, 7, 8]])
    J = I / 6
    expected_J = Vector([[1/6, 1/3, 1/2, 2/3], [5/6, 1, 7/6, 4/3]])
    assert J == expected_J

    K = Vector([[9, 2, 5], [8, 6, 1]])
    L = K / 3
    expected_L = Vector([[3, 2/3, 5/3], [8/3, 2, 1/3]])
    assert L == expected_L

    M = Vector([[2, 4], [6, 8]])
    N = M / 2
    expected_N = Vector([[1, 2], [3, 4]])
    assert N == expected_N

    O = Vector([[5, 2], [9, 1]])
    P = O / 5
    expected_P = Vector([[1, 2/5], [9/5, 1/5]])
    assert P == expected_P


def test_dot_product():
    """Test the dot product of two vectors."""
    A = Vector([1, 2, 3])
    B = Vector([4, 5, 6])
    assert_equal(vec.dot(A, B), 32)

    C = Vector([1, 2, 3, 4])
    D = Vector([5, 6, 7, 8])
    assert_equal(vec.dot(C, D), 70)

    E = Vector([-1/3, 5/7, -8/3])
    F = Vector([2/3, 1/7, -4/3])
    assert_equal(vec.dot(E, F), 3.4353741496598635)

    G = Vector([5, 3, 3, 0])
    H = Vector([3, 1, 2])
    with pytest.raises(ValueError):
        vec.dot(G, H)


def test_cross_product():
    """Test the cross product of two vectors."""
    A = Vector([1, 2, 3])
    B = Vector([4, 5, 6])
    C = vec.cross(A, B)
    expected_C = Vector([-3, 6, -3])
    assert C == expected_C

    D = Vector([1, 2, 3, 4])
    E = Vector([5, 6, 7, 8])
    with pytest.raises(ValueError):
        vec.cross(D, E)

    G = Vector([1, 2, 3])
    H = Vector([4, 5, 6, 7])
    with pytest.raises(ValueError):
        vec.cross(G, H)

    I = Vector([5, 3, 1])
    J = Vector([2, 8, 6])
    K = vec.cross(I, J)
    expected_K = Vector([10, -28, 34])
    assert K == expected_K

    L = Vector([[1, 5], [0, 2]])
    M = Vector([[3, 4], [1, 6]])
    with pytest.raises(ValueError):
        vec.cross(L, M)


def test_matrix_multiplication():
    """Test the matrix multiplication of two vectors."""
    A = Vector([[1, 2], [3, 4]])
    B = Vector([[5, 6], [7, 8]])
    C = vec.dot(A, B)
    expected_C = Vector([[19, 22], [43, 50]])
    assert C == expected_C
    C = A @ B
    assert C == expected_C

    D = Vector([[1, 2, 3], [4, 5, 6]])
    E = Vector([[-7, 8], [9, 10], [-11, 12]])
    F = vec.dot(D, E)
    expected_F = Vector([[-22, 64], [-49, 154]])
    assert F == expected_F
    F = D @ E
    assert F == expected_F
    F = vec.matmul(D, E)
    assert F == expected_F

    G = Vector([[1, 2], [3, 4], [-5, 6]])
    H = Vector([[7, 8, 0], [10, 11, 12]])
    I = vec.matmul(G, H)
    expected_I = Vector([[27, 30, 24], [61, 68, 48], [25, 26, 72]])
    assert I == expected_I
    I = vec.dot(G, H)
    assert I == expected_I
    I = G @ H
    assert I == expected_I

    J = Vector([[1, 2, 3, 4], [5, 6, 7, 8]])
    K = Vector([[9, 10], [11, 12], [13, 14], [-5, 16]])
    L = J @ K
    expected_L = Vector([[50, 140], [162, 348]])
    L = vec.matmul(J, K)
    assert L == expected_L

    M = Vector([[1, 2], [3, 4]])
    N = Vector([[5, 6, 7], [8, 9, 10]])
    O = vec.dot(M, N)
    expected_O = Vector([[21, 24, 27], [47, 54, 61]])
    assert O == expected_O

    P = Vector([[1, 2, 3], [4, 5, 6]])
    Q = Vector([[7, 8], [9, 10]])
    with pytest.raises(ValueError):
        vec.dot(P, Q)
    with pytest.raises(ValueError):
        vec.matmul(P, Q)
    with pytest.raises(ValueError):
        P @ Q
    assert vec.dot(Q, P) == Vector([[39, 54, 69], [49, 68, 87]])

    R = Vector([[5, 3, 2], [8, 6, 0], [2, 1, 3]])
    S = Vector([2, 1, 0])
    T = vec.matmul(R, S)
    expected_T = Vector([13, 22, 5])
    assert T == expected_T

    U = Vector([[4, 3, 1], [9, 3, 2], [0, 1, 5]])
    V = Vector([2, 1, 0])
    W = vec.dot(U, V)
    expected_W = Vector([11, 21, 1])
    assert W == expected_W


def test_norm():
    """Test the norm of a vector."""
    A = Vector([1, 2, 3])
    assert_equal(vec.norm(A), 3.7416573867739413)

    B = Vector([1, 2, 3, 4])
    assert_equal(vec.norm(B), 5.477225575051661)

    C = Vector([5, 3, 1])
    assert_equal(vec.norm(C), 5.916079783099616)

    D = Vector([2, 4, 6, 8])
    assert_equal(vec.norm(D), 10.954451150103322)

    E = Vector([0, 0, 0])
    assert_equal(vec.norm(E), 0)

    F = Vector([1, 1, 1])
    assert_equal(vec.norm(F), 1.7320508075688772)

    G = Vector([1, 1, 1, 1])
    assert_equal(vec.norm(G), 2)

    H = Vector([1, 2, 3, 4, 5])
    assert_equal(vec.norm(H), 7.416198487095663)

    I = Vector([1, 2, 3, 4, 5, 6])
    assert_equal(vec.norm(I), 9.539392014169456)

    J = Vector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert_equal(vec.norm(J), 19.621416870348583)

    K = Vector([[1, 2], [3, 4]])
    assert_equal(vec.norm(K), 5.477225575051661)

    L = Vector([[0, 3, 0, 2],
                [5, 8, 0, 1],
                [0, 8, 2, 8],
                [4, 2, 1, 8]])
    assert_equal(vec.norm(L), 17.88854381999832)

    M = Vector([[5, 3, 1], [0, 2, 9]])
    assert_equal(vec.norm(M), 10.954451150103322)


def test_getitem():
    """Test the getitem method of a vector."""
    A = Vector([1, 2, 3])
    assert A[:] == Vector([1, 2, 3])
    assert A[0] == 1
    assert A[1] == 2
    assert A[2] == 3
    with pytest.raises(IndexError):
        A[3]

    B = Vector([1, 2, 3, 4])
    assert B[0] == 1
    assert B[1] == 2
    assert B[2] == 3
    assert B[3] == 4
    with pytest.raises(IndexError):
        B[4]
    with pytest.raises(IndexError):
        B[0, 0]

    C = Vector([[1, 2], [3, 4]])
    assert C[:] == Vector([[1, 2], [3, 4]])
    assert C[0] == Vector([1, 2])
    assert C[1] == Vector([3, 4])
    assert C[0, 0] == 1
    assert C[0][0] == 1
    with pytest.raises(IndexError):
        C[2]
    with pytest.raises(IndexError):
        C[0, 2]

    D = Vector([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert D[1:] == Vector([[4, 5, 6], [7, 8, 9]])
    assert D[:1] == Vector([[1, 2, 3]])
    assert D[1:2] == Vector([[4, 5, 6]])
    assert D[1:3] == Vector([[4, 5, 6], [7, 8, 9]])

    E = Vector([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    assert E[:, :1] == Vector([1, 5, 9])
    assert E[:, 1:3] == Vector([[2, 3], [6, 7], [10, 11]])

    F = Vector([[2, 2, 5], [3, 0, 4], [8, 6, 1]])
    assert F[1:, :2] == Vector([[3, 0], [8, 6]])
    assert F[1:2, 1:3] == Vector([0, 4])
    assert F[:-1, :] == Vector([[2, 2, 5], [3, 0, 4]])
    assert F[1:, ::2] == Vector([[3, 4], [8, 1]])

    G = Vector([1, 2, 3, 4, 5, 6])
    assert G[::2] == Vector([1, 3, 5])
    assert G[1::2] == Vector([2, 4, 6])
    assert G[::3] == Vector([1, 4])


def test_setitem():
    """Test the setitem method of a vector."""
    A = Vector([1, 2, 3])
    A[0] = 4
    A[1] = 5
    A[2] = 6
    expected_A = Vector([4, 5, 6])
    assert A == expected_A
    with pytest.raises(IndexError):
        A[3] = 7

    B = Vector([1, 2, 3, 4])
    B[0] = 5
    B[1] = 6
    B[2] = 7
    B[3] = 8
    expected_B = Vector([5, 6, 7, 8])
    assert B == expected_B

    C = Vector([[1, 2], [3, 4]])
    C[0] = Vector([5, 6])
    C[1] = Vector([7, 8])
    C[0, 0] = 9
    C[1][0] = 3
    expected_C = Vector([[9, 6], [3, 8]])
    assert C == expected_C

    D = Vector([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        D[0] = Vector([7, 8])

    E = Vector([[1, 2, 3, 4], [5, 6, 7, 8]])
    E[:, 0] = Vector([9, 10])
    E[:, 1] = Vector([11, 12])
    E[:, 2] = Vector([13, 14])
    E[:, 3] = Vector([15, 16])
    expected_E = Vector([[9, 11, 13, 15], [10, 12, 14, 16]])
    assert E == expected_E
    E[1] = 4
    expected_E = Vector([[9, 11, 13, 15], [4, 4, 4, 4]])
    assert E == expected_E

    F = Vector([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    F[0, :] = [9, 8, 7]
    F[:, :2] = Vector([[6, 5], [4, 3], [2, 1]])
    F[:-1, :] = Vector([[5, 3, 1], [3, 3, 0]])
    expected_F = Vector([[5, 3, 1], [3, 3, 0], [2, 1, 9]])
    assert F == expected_F

    G = Vector([1, 2, 3, 4, 5, 6])
    G[::2] = Vector([6, 7, 8])
    assert G == Vector([6, 2, 7, 4, 8, 6])
    G[1:5:2] = Vector([9, 10])
    assert G == Vector([6, 9, 7, 10, 8, 6])
    G[::3] = Vector([12, 13])
    assert G == Vector([12, 9, 7, 13, 8, 6])

test_setitem()

def test_determinant():
    """Test the determinant of a matrix."""
    A = Vector([[0, 6], 
                [3, 0]])
    assert_equal(vec.det(A), -18)

    B = Vector([[5, 1, 3],
                [9, 7, 0],
                [5, 5, 0]])
    assert_equal(vec.det(B), 30)

    C = Vector([[2, 6, 8, 6], 
                [9, 8, 3, 5], 
                [3, 1, 2, 5], 
                [3, 7, 5, 0]])
    assert_equal(vec.det(C), 284)

    D = Vector([[4]])
    assert_equal(vec.det(D), 4)

    e = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        vec.det(e)


def test_inverse():
    """Tests the inverse of a matrix."""
    A = Vector([[3, 6],
                [3, 8]])
    A_inv = vec.inv(A)
    expected_A_inv = Vector([[4/3, -1],
                             [-1/2, 1/2]])
    assert A_inv == expected_A_inv

    B = Vector([[4, 9, 3],
                [1, 5, 8],
                [3, 3, 9]])
    B_inv = vec.inv(B)
    expected_B_inv = Vector([[0.1147541, -0.39344262, 0.31147541],
                            [ 0.08196721, 0.14754098, -0.15846995],
                            [-0.06557377, 0.08196721, 0.06010929]])
    assert B_inv == expected_B_inv

    C = Vector([[0, 2, 1, 0],
                [8, 6, 9, 9],
                [9, 0, 8, 7],
                [2, 4, 7, 2]])
    C_inv = vec.inv(C)
    expected_C_inv = Vector([[1.37647059, -0.22352941, 0.38823529, -0.35294118],
                            [ 0.72352941, 0.02352941, 0.01176471, -0.14705882],
                            [-0.44705882, -0.04705882, -0.02352941, 0.29411765],
                            [-1.25882353, 0.34117647, -0.32941176, 0.11764706]])
    assert C_inv == expected_C_inv

    D = Vector([[6]])
    D_inv = vec.inv(D)
    expected_D_inv = Vector([[1/6]])
    assert D_inv == expected_D_inv

    E = Vector([[2, 3], [4, 2], [0, 1]])
    with pytest.raises(ValueError):
        vec.inv(E)


def test_transpose():
    """Tests the transpose of a matrix."""
    A = Vector([[3, 6]])
    A_transpose = vec.transpose(A)
    expected_A_transpose = Vector([[3], 
                                   [6]])
    assert A_transpose == expected_A_transpose

    B = Vector([[4, 9, 3],
                [1, 5, 8]])
    B_transpose = vec.transpose(B)
    expected_B_transpose = Vector([[4, 1],
                                   [9, 5],
                                   [3, 8]])
    assert B_transpose == expected_B_transpose

    C = Vector([[0, 2, 1],
                [8, 6, 9],
                [9, 0, 8]])
    C_transpose = C.T
    expected_C_transpose = Vector([[0, 8, 9],
                                   [2, 6, 0],
                                   [1, 9, 8]])
    assert C_transpose == expected_C_transpose

    D = Vector([[2]])
    D_transpose = D.T
    expected_D_transpose = Vector([[2]])
    assert D_transpose == expected_D_transpose

    E = Vector([[5, 1, 2],
                [2, 8, 6], 
                [8, 3, 1],
                [0, 1, 2]])
    E_transpose = vec.transpose(E)
    expected_E_transpose = Vector([[5, 2, 8, 0],
                                   [1, 8, 3, 1],
                                   [2, 6, 1, 2]])
    assert E_transpose == expected_E_transpose

    F = Vector([5, 1, 2])
    F_transpose = F.T
    expected_F_transpose = Vector([5, 1, 2])
    assert F_transpose == expected_F_transpose
    