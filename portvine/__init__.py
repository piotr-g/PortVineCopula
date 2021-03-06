import os, sys, cffi

ffi = cffi.FFI()

# TODO!
if sys.platform == 'win32':
    os.environ['PATH'] += os.pathsep + 'C:\\Program Files\\R\\R-3.3.2\\bin\\x64'
    os.environ['PATH'] += os.pathsep + 'C:\\Program Files\\R\\R-3.3.2\\library\\VineCopula\\libs\\x64'
    lib = ffi.dlopen("VineCopula.dll")
elif sys.platform.startswith('linux'):
    lib = ffi.dlopen("/usr/local/lib/R/site-library/VineCopula/libs/VineCopula.so")
else:
    raise Exception("unsupported platform")

from portvine.AD import AD