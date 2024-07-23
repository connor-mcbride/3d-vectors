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
    