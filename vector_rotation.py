import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Define the rotation matrix
def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / np.sqrt(np.dot(axis, axis))
    a = np.cos(theta / 2.0)
    b, c, d = -axis * np.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

# Initial vector
v = np.array([1, 0, 0])

# Rotation axis and angle
axis = np.array([1 / np.sqrt(2), 1 / np.sqrt(2), 0])
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
    U_inv_transpose = np.linalg.inv(U).T
    return 0.5 * (U + U_inv_transpose)


def polar_decomposition(A, tol=1e-6):
    """Returns the unitary matrix U in the polar decomposition of a matrix A.
    A = UP, where U is unitary and P is positive semi-definite Hermitian.
    A - matrix to be decomposed.
    tol - tolerance for convergence.
    """
    U = A
    while True:
        U_new = unitary_step(U)
        if np.linalg.norm(U_new - U) < tol:
            return U_new
        U = U_new


def update(num):
    global R, v, quiver
    Psi = np.array([[0, -omega[2]*theta, omega[1]*theta],
                      [omega[2]*theta, 0, -omega[0]*theta],
                      [-omega[1]*theta, omega[0]*theta, 0]])
    R_dot = Psi @ R
    R += R_dot
    R = polar_decomposition(R)
    print(R)
    print(np.linalg.det(R))
    v_new = np.dot(R, v)
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


ani = FuncAnimation(fig, update, frames=100, init_func=init, interval=50, blit=False)

origins = np.zeros((3, 3))
directions = np.eye(3)
colors = ['r', 'g', 'b']

for i in range(3):
    ax.quiver(*origins[i], *directions[i], color=colors[i], arrow_length_ratio=0.1)
    ax.quiver(*origins[i], *-directions[i], color=colors[i], arrow_length_ratio=0.1)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()

