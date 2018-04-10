# import os
import cffi


ffi = cffi.FFI()

ffi.set_source('sndfile._sndfile', '''
#include <stdint.h>
#include <sndfile.h>
''', libraries=['sndfile'])

# here = os.path.dirname(__file__)
# with open(os.path.join(here, 'sndfile.h'), 'r') as header:
#     ffi.cdef(header.read())

ffi.cdef('''
typedef ... SNDFILE;

enum { SFM_READ, SFM_WRITE, SFM_RDWR };

typedef int64_t sf_count_t;

typedef struct {
    sf_count_t frames;
    int samplerate;
    int channels;
    int format;
    int sections;
    int seekable;
} SF_INFO;

SNDFILE *sf_open(const char *path, int mode, SF_INFO *sfinfo);
int sf_close(SNDFILE *sndfile);

sf_count_t sf_readf_short(SNDFILE *sndfile, short *ptr, sf_count_t frames);
sf_count_t sf_readf_int(SNDFILE *sndfile, int *ptr, sf_count_t frames);
sf_count_t sf_readf_float(SNDFILE *sndfile, float *ptr, sf_count_t frames);
sf_count_t sf_readf_double(SNDFILE *sndfile, double *ptr, sf_count_t frames);
''')


if __name__ == '__main__':
    ffi.compile()
