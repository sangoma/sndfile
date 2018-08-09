import io
import os
from array import array

from ._sndfile import ffi, lib
from .formats import major_format_str, minor_format_str
from .vio import get_vio_table


def _compute_mode(mode: str) -> int:
    result = 0
    for m in mode:
        if m == "r":
            result |= lib.SFM_READ
        elif m == "w":
            result |= lib.SFM_WRITE
        else:
            raise ValueError("Don't understand: {}".format(mode))
    return result


class SndFileBase:
    def __init__(self, handle, info):
        self._handle = handle
        self._info = info

    def close(self):
        if self._handle:
            lib.sf_close(self._handle)
            self._handle = None

    def read_frames(self, typecode, frames=-1):
        if not self._handle:
            raise ValueError("I/O operation on closed file.")

        if frames < 0:
            frames = self._info.frames

        if typecode in ("h", "i"):
            data = ffi.new("short[]", frames * self._info.channels)
            lib.sf_readf_short(self._handle, data, frames)
        elif typecode == "l":
            data = ffi.new("int[]", frames * self._info.channels)
            lib.sf_readf_int(self._handle, data, frames)
        elif typecode == "f":
            data = ffi.new("float[]", frames * self._info.channels)
            lib.sf_readf_float(self._handle, data, frames)
        elif typecode == "d":
            data = ffi.new("double[]", frames * self._info.channels)
            lib.sf_readf_double(self._handle, data, frames)
        else:
            raise ValueError("Bad typecode")

        return array(typecode, data)

    def __repr__(self):
        return "<{} at {}>".format(self.__class__.__name__, id(self._handle))

    def __enter__(self):
        if not self._handle:
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


class SndFileWrapper(SndFileBase):
    def __init__(self, name, mode='r'):
        sndfile_mode = _compute_mode(mode)
        info = ffi.new("SF_INFO *")
        handle = lib.sf_open(os.fsencode(name), sndfile_mode, info)

        if not handle:
            errmsg = ffi.string(lib.sf_strerror(handle))
            raise IOError("Failed to open {}: {}".format(
                name, errmsg.decode()))

        super().__init__(handle, info)
        self.mode = mode
        self.name = name

    def __repr__(self):
        return "<{} filename='{}' mode='{}'>".format(self.__class__.__name__,
                                                     self.name, self.mode)


class VirtualSndFile(SndFileBase):
    def __init__(self, fobj):
        if not fobj.seekable():
            raise ValueError("File must be seekable")

        if isinstance(fobj, io.BufferedWriter):
            self.mode, sndfile_mode = 'w', lib.SFM_WRITE
        elif isinstance(fobj, io.BufferedIOBase):
            self.mode, sndfile_mode = 'r', lib.SFM_READ
        else:
            raise ValueError("File object must be a BufferedIOBase object")

        info = ffi.new("SF_INFO *")
        self._user_data = ffi.new_handle(fobj)
        handle = lib.sf_open_virtual(get_vio_table(), sndfile_mode, info,
                                     self._user_data)

        if not handle:
            errmsg = ffi.string(lib.sf_strerror(handle))
            raise IOError("Failed to load bytes: {}".format(errmsg.decode()))

        super().__init__(handle, info)

    def __repr__(self):
        return "<{} mode='{}'>".format(self.__class__.__name__, self.mode)


def open(fp, mode="r"):
    if isinstance(fp, io.BufferedIOBase):
        return VirtualSndFile(fp)
    return SndFileWrapper(fp, mode)


def frombytes(data):
    return VirtualSndFile(io.BytesIO(data))
