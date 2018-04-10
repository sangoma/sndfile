import os
import cffi


here = os.path.dirname(__file__)
ffi = cffi.FFI()


ffi.set_source('sndfile._sndfile', '''
#include <stdint.h>
#include <sndfile.h>
''', libraries=['sndfile'])


with open(os.path.join(here, 'sndfile.h')) as header:
    ffi.cdef(header.read())


if __name__ == '__main__':
    ffi.compile()
