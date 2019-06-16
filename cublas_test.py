import numpy
import ctypes
import time
import matplotlib.pyplot as plt

E = ctypes.cdll.LoadLibrary("cublas_test.so")

cublas_times = []
numpy_times = []
dims = []

def cublas_mm(matrix_dim):
    N = matrix_dim * matrix_dim

    m1 = numpy.ones((N), dtype=numpy.float32)
    m2 = numpy.ones((N), dtype=numpy.float32)
    output_m = numpy.ones((N), dtype=numpy.float32)

    t0 = time.time()

    E.run(ctypes.c_void_p(m1.ctypes.data),
          ctypes.c_void_p(m2.ctypes.data),
          ctypes.c_void_p(output_m.ctypes.data),
          ctypes.c_int(matrix_dim))

    t1 = time.time()
    return t1 - t0


def numpy_mm(matrix_dim):
    m1 = numpy.ones((matrix_dim, matrix_dim), dtype=numpy.float32)
    m2 = numpy.ones((matrix_dim, matrix_dim), dtype=numpy.float32)

    t0 = time.time()

    _ = numpy.dot(m1, m2)

    t1 = time.time()
    return t1 - t0


for i in range(1, 1000, 10):

    print(i)
    cur_cublas = []
    cur_numpy = []

    for _ in range(100):
        cur_cublas.append(cublas_mm(i))
        cur_numpy.append(numpy_mm(i))

    cublas_times.append(numpy.mean(cur_cublas))
    numpy_times.append(numpy.mean(cur_numpy))
    dims.append(i)

plt.plot(dims, cublas_times, label='cublas')
plt.plot(dims, numpy_times, label='numpy')
plt.legend()
plt.xlabel("Input Matrix Dimension")
plt.ylabel("Computation Time")
plt.savefig('cublas_vs_numpy.png')
plt.show()
