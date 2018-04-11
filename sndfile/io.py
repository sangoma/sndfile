import os
from array import array

from ._sndfile import lib, ffi
from .formats import major_format_str, minor_format_str


class SndFileWrapper:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

        if mode == "r":
            sndfile_mode = lib.SFM_READ
        else:
            raise ValueError("Don't understand: {}".format(mode))

        self._info = ffi.new("SF_INFO *")
        self.handle = lib.sf_open(os.fsencode(self.name), sndfile_mode,
                                  self._info)

    def close(self):
        if self.handle:
            lib.sf_close(self.handle)
            self.handle = None

    def read_frames(self, typecode, frames=-1):
        if not self.handle:
            raise ValueError("I/O operation on closed file.")

        if frames < 0:
            frames = self._info.frames

        if typecode in ("h", "i"):
            data = ffi.new("short[]", frames * self._info.channels)
            lib.sf_readf_short(self.handle, data, frames)
        elif typecode == "l":
            data = ffi.new("int[]", frames * self._info.channels)
            lib.sf_readf_int(self.handle, data, frames)
        elif typecode == "f":
            data = ffi.new("float[]", frames * self._info.channels)
            lib.sf_readf_float(self.handle, data, frames)
        elif typecode == "d":
            data = ffi.new("double[]", frames * self._info.channels)
            lib.sf_readf_double(self.handle, data, frames)
        else:
            raise ValueError("Bad typecode")

        return array(typecode, data)

    def __repr__(self):
        return "<{} name='{}' mode='{}'>".format(
            self.__class__.__name__, self.name, self.mode)

    def __enter__(self):
        if not self.handle:
            raise ValueError("I/O operation on closed file.")

        return self

    def __exit__(self, *exc_info):
        self.close()

    @property
    def frames(self):
        return self._info.frames

    @property
    def samplerate(self):
        return self._info.samplerate

    @property
    def channels(self):
        return self._info.channels

    @property
    def sections(self):
        return self._info.sections

    @property
    def format(self):
        return (major_format_str(self._info.format),
                minor_format_str(self._info.format))


def open(filename, mode="r"):
    return SndFileWrapper(filename, mode)
