from Vector import Vector
import Vector as vec
import pytest


def assert_equal(x1, x2):
    assert abs(x1 - x2) < 1e-6


def test_determinant():
    """Test the determinant of a matrix."""
    A = Vector([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])
    assert_equal(vec.det(A), 0)

    B = Vector([[1, 2], 
                [3, 4]])
    assert_equal(vec.det(B), -2)

    C = Vector([[2, 6, 8, 6], 
                [9, 8, 3, 5], 
                [3, 1, 2, 5], 
                [3, 7, 5, 0]])
    assert_equal(vec.det(C), 284)

    c = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        vec.det(c)


