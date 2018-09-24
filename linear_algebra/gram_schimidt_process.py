import numpy as np
import numpy.linalg as la

verySmallNumber = 1e-14

def gsBasis(A):
    B = np.array(A, dtype=np.float_)  # Make B as a copy of A, since we're going to alter it's values.
    # Loop over all vectors, starting with zero, label them with i
    for i in range(B.shape[1]):
        # Inside that loop, loop over all previous vectors, j, to subtract.
        for j in range(i):
            # Complete the code to subtract the overlap with previous vectors.
            # you'll need the current vector B[:, i] and a previous vector B[:, j]
            B[:, i] = B[:, i] - B[:, i] @ B[:, j] * B[:, j]
        # Next insert code to do the normalisation test for B[:, i]
        if la.norm(B[:, i]) > verySmallNumber:
            B[:, i] = B[:, i] / la.norm(B[:, i])
        else:
            B[:, i] = np.zeros_like(B[:, i])

    return B

def dimensions(A) :
    return np.sum(la.norm(gsBasis(A), axis=0))


if __name__ == "__main__":
    V = np.array([[1, 0, 2, 6],
                  [0, 1, 8, 2],
                  [2, 8, 3, 1],
                  [1, -6, 2, 3]], dtype=np.float_)
    print(gsBasis(V))
