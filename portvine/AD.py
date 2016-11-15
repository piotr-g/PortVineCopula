from portvine import *

ffi.cdef("void ADtest(double* cdf, int* n, double* out);")


def AD(cdf):
    cdf = numpy.asarray(cdf, dtype=numpy.float64)

    size = ffi.new("int*")
    size[0] = ffi.cast("int", len(cdf))

    ret = ffi.new("double*")

    lib.ADtest(
        ffi.cast("double*", cdf.ctypes.data),
        size,
        ret
    )
    return ret[0]
