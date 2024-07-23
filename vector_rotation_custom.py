from Vector import Vector
import Vector as vec
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys


# Define the rotation matrix
def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = axis / math.sqrt(vec.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return Vector([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

# Initial vector
v = Vector([1/math.sqrt(3), 1/math.sqrt(3), 1/math.sqrt(3)])

# Rotation axis and angle
axis = Vector([1/math.sqrt(2), 1/math.sqrt(2), 0])
theta = 1  # Small angle for smooth animation
omega = axis * theta
R = rotation_matrix(axis, theta) # Initial rotation matrix

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])


def unitary_step(U):
    """Returns a step U_{k+1} in the "Newton's method" calculation of a matrix's
    unitary matrix U in its polar decomposition.
    Averages the matrix U_k with the inverse of its transpose.
    A = UP, where U is unitary and P is positive semi-definite Hermitian.
    U_{k+1} = (1/2) * (U_k + (U_k^{*})^{-1}), k = 0, 1, 2, ...,
    where
    U_0 = A.
    """
    U_inv_transpose = vec.inv(U).T.copy()
    return 0.5 * (U + U_inv_transpose)


def polar_decomposition(A: Vector, tol=1e-12):
    """Returns the unitary matrix U in the polar decomposition of a matrix A.
    A = UP, where U is unitary and P is positive semi-definite Hermitian.
    A - matrix to be decomposed.
    tol - tolerance for convergence.
    """
    U = A.copy()
    while True:
        U_new = unitary_step(U)
        # print(f"Determinant of U_new: {vec.det(U_new)}")
        # print(f"Orthogonality check: {vec.dot(U_new.T, U_new)}")
        if vec.norm(U_new - U) < tol:
            return U_new
        U = U_new


def update(num):
    global R, v, quiver
    Psi = Vector([[0, -omega[2]*theta, omega[1]*theta],
                    [omega[2]*theta, 0, -omega[0]*theta],
                    [-omega[1]*theta, omega[0]*theta, 0]])
    R_dot = Psi @ R
    R += R_dot
    R = polar_decomposition(R)
    det = vec.det(R)
    print(f"Determinant of R: {det}", end='\n\n')
    if det < 0:
        sys.exit(1)
    # print(vec.det(R))
    # print(R)
    v_new = vec.dot(R, v)
    quiver.remove()
    quiver = ax.quiver(0, 0, 0, v_new[0], v_new[1], v_new[2])


def init():
    global quiver
    if 'quiver' in globals():
        try:
            quiver.remove()
        except:
            pass
    quiver = ax.quiver(0, 0, 0, v[0], v[1], v[2])
    return quiver


ani = FuncAnimation(fig, update, frames=500, init_func=init, interval=50, blit=False)

origins = vec.zeros((3, 3))
directions = vec.eye(3)
colors = ['r', 'g', 'b']

for i in range(3):
    ax.quiver(*origins[i], *directions[i], color=colors[i], arrow_length_ratio=0.1)
    ax.quiver(*origins[i], *-directions[i], color=colors[i], arrow_length_ratio=0.1)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()

