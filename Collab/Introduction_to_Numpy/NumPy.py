import sys
import numpy as np
import time

if __name__ == "__main__":
    # ===========================================================================
    # 1. Basics NumPy array & array types
    a = np.array([1, 2, 3, 4])

    print(a, type(a), a.dtype),
    print(a[0], a[1])
    print(a[:])
    print(a[1:3])   # Explanation: from index 1 to 3
    print(a[1:-1])  # Explanation: from index 1 to the last index
    print(a[::2])  # Explanation: from index 0 to the last index with step 2
    print()

    b = np.array([0, .5, 1, 1.5, 2])

    print(b, type(b), b.dtype)
    print(b[0], b[2], b[-1])
    print(b[[0, 2, -1]])  # Explanation: get the value at index 0, 2, -1
    print()

    print(np.array([1, 2, 3, 4], dtype=np.float16))
    print(np.array([1, 2, 3, 4], dtype=np.int8))
    print()

    c = np.array(['a', 'b', 'c'])
    print(c, type(c), c.dtype)
    print()

    d = np.array([{'a': 1}, sys])
    print(d, type(d), d.dtype)
    print()

    # ===========================================================================
    # 2. Dimensions and shapes
    A = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print(A, type(A), A.dtype)
    print(A.shape, A.ndim, A.size)
    # Explanation: shape is the dimension of the array,
    # ndim is the number of dimensions, size is the total number of elements

    B = np.array([
        [
            [12, 11, 10],
            [9, 8, 7],
        ],
        [
            [6, 5, 4],
            [3, 2, 1]
        ]
    ])

    print(B, type(B), B.dtype)
    print(B.shape, B.ndim, B.size)
    print()

    # C = np.array([
    #     [
    #         [12, 11, 10],
    #         [9, 8, 7],
    #     ],
    #     [
    #         [6, 5, 4]
    #     ]
    # ])
    #
    # print(C, type(C), C.dtype)
    # print(C.shape, C.ndim, C.size)
    # print(type(C[0]))
    # print()

    # ===========================================================================
    # 3. Indexing and slicing
    A = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print(A[1], A[1][0], A[1, 0])  # A[1][0] = A[1, 0]
    print(A[:, :2])  # Explanation: get all rows and the first 2 columns
    print(A[:2, :2])  # Explanation: get the first 2 rows and the first 2 columns
    print(A[:2, 2:])  # Explanation: get the first 2 rows and the last column
    # :2 means "select rows from the start-up to (but not including) row index 2".
    # 2: means "select columns from column index 2 to the end".
    A[1] = np.array([10, 10, 10])
    print(A)
    A[2] = 99
    print(A)
    print()

    # ===========================================================================
    # 4. Summary statistics
    x = np.array([1, 2, 3, 4])
    print(x.sum())
    print(x.mean())
    print(x.std())
    print(x.var())
    print(x.sum(axis=0))
    print(x.mean(axis=0))
    print(x.std(axis=0))
    # Standard Deviation: The standard deviation measures the amount of variation or dispersion of a set of values.
    # For the array [1, 2, 3, 4], the standard deviation is calculated as:
    # First, find the mean: 2.5.
    # Then, calculate the variance: ((1-2.5)^2 + (2-2.5)^2 + (3-2.5)^2 + (4-2.5)^2) / 4 = 1.25.
    # Finally, take the square root of the variance: sqrt(1.25) ≈ 1.118.
    print()

    # ===========================================================================
    # 5. Broadcasting and vectorized operations
    y = np.arange(1, 5)
    print(y)
    print(y + 10)
    print(y * 10)
    y += 100
    print(y)
    z = [0, 1, 2, 3]
    print(list(i * 10 for i in z))
    print(y + z)
    print()

    # ===========================================================================
    # 6. Boolean arrays
    d = np.array([1, 2, 3, 4, 5])
    print(d[[True, False, False, True, True]])
    print(d[d > 2])
    print(d > 2)
    print(d.mean())
    print(d[d > d.mean()])
    print(d[~(d > d.mean())])  # ~ means "not"
    print()

    e = np.random.randint(100, size=(3, 3))
    print(e)
    print()

    # ===========================================================================
    # 7. Linear algebra
    print(f"-- Linear algebra --")
    M = np.array([[1, 2], [3, 4], [5, 6]])
    N = np.array([[5, 6], [7, 8]])
    print(f"{M.dot(N)}\n")  # Explanation: dot product of M and N == np.dot(M, N) == M @ N
    print(f"{M.T}\n")
    print()

    # ===========================================================================
    # 8.Size of objects in memory
    print(f"-- Size of objects in memory --")
    # An integer in Python is > 24bytes
    print(sys.getsizeof(1))
    # Longs are even larger
    print(sys.getsizeof(10 ** 100))
    # NumPy size is much smaller
    print(np.dtype(int).itemsize)
    # Numpy size is much smaller
    print(np.dtype(np.int8).itemsize)
    print(np.dtype(np.float16).itemsize)
    # A one-element list
    print(sys.getsizeof([1]))
    # An array of one element in numpy
    print(np.array([1]).nbytes)

    # Performance

    normal = list(range(100000))
    start_time = time.time()
    sum([i ** 2 for i in normal])
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    array_numpy = np.arange(100000)
    start_time = time.time()
    array_numpy ** 2
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    # ===========================================================================
    # 9. Useful Numpy functions
    print(f"-- Useful Numpy functions --")
    # Random
    print(f"{"Random":-^20}")
    print(np.random.random(size=2))  # Explanation: generate 2 random numbers between 0 and 1
    print(np.random.normal(size=2))  # Explanation: generate 2 random numbers from the normal distribution
    print(np.random.rand(2, 4))  # Explanation: generate a 2x4 array of random numbers between 0 and 1
    print()

    # Arrange
    print(f"{"Arrange":-^20}")
    print(np.arange(10))  # Explanation: generate an array from 0 to 9
    print(np.arange(5, 10))  # Explanation: generate an array from 5 to 9
    print(np.arange(0, 1, .1))  # Explanation: generate an array from 0 to 1 with step 0.1
    print()

    # Lin-space
    print(f"{"Lin-space":-^20}")
    print(np.linspace(0, 1, 5))  # Explanation: generate 5 numbers from 0 to 1
    print(np.linspace(0, 1, 20))
    print(np.linspace(0, 1, 20, False))  # Explanation: generate 20 numbers from 0 to 1, excluding 1
    print()

    # Reshape
    print(f"{"Reshape":-^20}")
    print(np.arange(10).reshape(2, 5))  # Explanation: reshape the array from 1x10 to 2x5
    print(np.arange(10).reshape(5, 2))  # Explanation: reshape the array from 1x10 to 5x2
    print()

    # Zeros, Ones, Empty
    print(f"{"Zeros, Ones, Empty":-^20}")
    print(np.zeros(5))  # Explanation: generate an array of 5 zeros
    print(np.zeros((3, 3)))  # Explanation: generate a 3x3 array of zeros
    print(np.ones(5))  # Explanation: generate an array of 5 ones
    print(np.ones((3, 3)))  # Explanation: generate a 3x3 array of ones
    print(np.empty(5))  # Explanation: generate an array of 5 empty elements
    print(np.empty((3, 3)))  # Explanation: generate a 3x3 array of empty elements
    print()

    # Identity and eye
    print(f"{"Identity and eye":-^20}")
    print(np.eye(3))  # Explanation: generate a 3x3 identity matrix
    print(np.identity(3))  # Explanation: generate a 3x3 identity matrix
    # np.eye(N, M=None, k=0):
    # Creates a 2D array with shape (N, M).
    # N: Number of rows.
    # M: Number of columns (defaults to N if not provided).
    # k: Diagonal offset (0 is the main diagonal, positive is above, negative is below).
    # np.identity(n):
    # Creates a square 2D array with shape (n, n).
    # n: Number of rows and columns.
    print(np.eye(3, 2))
    # Explanation: generate a 3x2 matrix with ones on the diagonal and zeros elsewhere
    print(np.eye(3, 2, 1))
    # Explanation: generate a 3x2 matrix with ones on the first upper diagonal and zeros elsewhere
    # k = 1 means the first upper diagonal
    print()
