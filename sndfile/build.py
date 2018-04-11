import pathlib

import cffi


ffi = cffi.FFI()
ffi.set_source('sndfile._sndfile', '''
#include <stdint.h>
#include <sndfile.h>
''', libraries=['sndfile'])


here = pathlib.Path(__file__).absolute().parent
with open(here / 'sndfile.h') as header:
    ffi.cdef(header.read())


if __name__ == '__main__':
    ffi.compile()
