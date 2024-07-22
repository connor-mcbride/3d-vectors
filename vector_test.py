from Vector import Vector
import Vector as vec
import pytest


def assert_equal(x1, x2):
    assert abs(x1 - x2) < 1e-6


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