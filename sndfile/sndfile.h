typedef ... SNDFILE;

enum { SFM_READ, SFM_WRITE, SFM_RDWR };

enum {
    SF_FORMAT_WAV,
    SF_FORMAT_AIFF,
    SF_FORMAT_AU,
    SF_FORMAT_RAW,
    SF_FORMAT_PAF,
    SF_FORMAT_SVX,
    SF_FORMAT_NIST,
    SF_FORMAT_VOC,
    SF_FORMAT_IRCAM,
    SF_FORMAT_W64,
    SF_FORMAT_MAT4,
    SF_FORMAT_MAT5,
    SF_FORMAT_PVF,
    SF_FORMAT_XI,
    SF_FORMAT_HTK,
    SF_FORMAT_SDS,
    SF_FORMAT_AVR,
    SF_FORMAT_WAVEX,
    SF_FORMAT_SD2,
    SF_FORMAT_FLAC,
    SF_FORMAT_CAF,
    SF_FORMAT_WVE,
    SF_FORMAT_OGG,
    SF_FORMAT_MPC2K,
    SF_FORMAT_RF64,
    SF_FORMAT_PCM_S8,
    SF_FORMAT_PCM_16,
    SF_FORMAT_PCM_24,
    SF_FORMAT_PCM_32,
    SF_FORMAT_PCM_U8,
    SF_FORMAT_FLOAT,
    SF_FORMAT_DOUBLE,
    SF_FORMAT_ULAW,
    SF_FORMAT_ALAW,
    SF_FORMAT_IMA_ADPCM,
    SF_FORMAT_MS_ADPCM,
    SF_FORMAT_GSM610,
    SF_FORMAT_VOX_ADPCM,
    SF_FORMAT_G721_32,
    SF_FORMAT_G723_24,
    SF_FORMAT_G723_40,
    SF_FORMAT_DWVW_12,
    SF_FORMAT_DWVW_16,
    SF_FORMAT_DWVW_24,
    SF_FORMAT_DWVW_N,
    SF_FORMAT_DPCM_8,
    SF_FORMAT_DPCM_16,
    SF_FORMAT_VORBIS,

    SF_ENDIAN_FILE,
    SF_ENDIAN_LITTLE,
    SF_ENDIAN_BIG,
    SF_ENDIAN_CPU,

    SF_FORMAT_SUBMASK,
    SF_FORMAT_TYPEMASK,
    SF_FORMAT_ENDMASK,
};

typedef int... sf_count_t;

typedef sf_count_t (*sf_vio_get_filelen)(void *user_data);
typedef sf_count_t (*sf_vio_seek)(sf_count_t offset, int whence, void *user_data);
typedef sf_count_t (*sf_vio_read)(void *ptr, sf_count_t count, void *user_data);
typedef sf_count_t (*sf_vio_write)(const void *ptr, sf_count_t count, void *user_data);
typedef sf_count_t (*sf_vio_tell)(void *user_data);

typedef struct {
    sf_count_t frames;
    int samplerate;
    int channels;
    int format;
    int sections;
    int seekable;
} SF_INFO;

typedef struct {
    sf_vio_get_filelen get_filelen;
    sf_vio_seek seek;
    sf_vio_read read;
    sf_vio_write write;
    sf_vio_tell tell;
} SF_VIRTUAL_IO;

SNDFILE *sf_open(const char *path, int mode, SF_INFO *sfinfo);
SNDFILE *sf_open_virtual(SF_VIRTUAL_IO *sfvirtual, int mode, SF_INFO *sfinfo, void *user_data);
int sf_close(SNDFILE *sndfile);

const char *sf_strerror(SNDFILE *sndfile) ;

sf_count_t sf_readf_short(SNDFILE *sndfile, short *ptr, sf_count_t frames);
sf_count_t sf_readf_int(SNDFILE *sndfile, int *ptr, sf_count_t frames);
sf_count_t sf_readf_float(SNDFILE *sndfile, float *ptr, sf_count_t frames);
sf_count_t sf_readf_double(SNDFILE *sndfile, double *ptr, sf_count_t frames);

extern "Python" sf_count_t vio_get_filelen(void *);
extern "Python" sf_count_t vio_seek(sf_count_t, int, void *);
extern "Python" sf_count_t vio_read(void *, sf_count_t, void *);
extern "Python" sf_count_t vio_write(const void *, sf_count_t, void *);
extern "Python" sf_count_t vio_tell(void *);
