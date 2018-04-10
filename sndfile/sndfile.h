typedef ... SNDFILE;

enum { SFM_READ, SFM_WRITE, SFM_RDWR };

typedef int... sf_count_t;

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
