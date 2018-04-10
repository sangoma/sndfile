from ._sndfile import lib


_MAJOR_FORMATS = {
    lib.SF_FORMAT_WAV: "wav",
    lib.SF_FORMAT_AIFF: "aiff",
    lib.SF_FORMAT_AU: "au",
    lib.SF_FORMAT_PAF: "paf",
    lib.SF_FORMAT_SVX: "svx",
    lib.SF_FORMAT_NIST: "nist",
    lib.SF_FORMAT_VOC: "voc",
    lib.SF_FORMAT_IRCAM: "ircam",
    lib.SF_FORMAT_W64: "w64",
    lib.SF_FORMAT_MAT4: "mat4",
    lib.SF_FORMAT_MAT5: "mat5",
    lib.SF_FORMAT_PVF: "pvf",
    lib.SF_FORMAT_XI: "xi",
    lib.SF_FORMAT_HTK: "htk",
    lib.SF_FORMAT_SDS: "sds",
    lib.SF_FORMAT_AVR: "avr",
    lib.SF_FORMAT_WAVEX: "wavx",
    lib.SF_FORMAT_SD2: "sd2",
    lib.SF_FORMAT_FLAC: "flac",
    lib.SF_FORMAT_CAF: "caf",
    lib.SF_FORMAT_WVE: "wfe"
}


_MINOR_FORMATS = {
    lib.SF_FORMAT_PCM_S8: "int8",
    lib.SF_FORMAT_PCM_U8: "uint8",
    lib.SF_FORMAT_PCM_16: "int16",
    lib.SF_FORMAT_PCM_24: "int24",
    lib.SF_FORMAT_PCM_32: "int32",
    lib.SF_FORMAT_FLOAT: "float",
    lib.SF_FORMAT_DOUBLE: "double",
    lib.SF_FORMAT_ULAW: "ulaw",
    lib.SF_FORMAT_ALAW: "alaw",
    lib.SF_FORMAT_IMA_ADPCM: "ima_adpcm",
    lib.SF_FORMAT_MS_ADPCM: "ms_adpcm",
    lib.SF_FORMAT_GSM610: "gsm610",
    lib.SF_FORMAT_G721_32: "g721_32",
    lib.SF_FORMAT_G723_24: "g723_24",
    lib.SF_FORMAT_G723_40: "g723_40"
}


def major_format_str(format):
    return _MAJOR_FORMATS.get(format & lib.SF_FORMAT_TYPEMASK, "unknown")


def minor_format_str(format):
    return _MINOR_FORMATS.get(format & lib.SF_FORMAT_TYPEMASK, "default")
