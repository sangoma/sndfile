from ._sndfile import lib, ffi


@ffi.def_extern()
def vio_get_filelen(user_data):
    fobj = ffi.from_handle(user_data)

    saved_pos = fobj.tell()
    end = fobj.seek(0, 2)
    fobj.seek(0, saved_pos)
    return end


@ffi.def_extern()
def vio_seek(offset, whence, user_data):
    fobj = ffi.from_handle(user_data)
    return fobj.seek(offset, whence)


@ffi.def_extern()
def vio_read(ptr, count, user_data):
    fobj = ffi.from_handle(user_data)
    buf = ffi.cast("char *", ptr)

    chunk = fobj.read(count)
    count = len(chunk)
    buf[0:count] = chunk
    return count


@ffi.def_extern()
def vio_write(ptr, count, user_data):
    fobj = ffi.from_handle(user_data)
    buf = ffi.cast("char *", ptr)

    return fobj.write(buf[0:count])


@ffi.def_extern()
def vio_tell(user_data):
    fobj = ffi.from_handle(user_data)
    return fobj.tell()


def get_vio_table():
    return ffi.new(
        "SF_VIRTUAL_IO *", {
            'get_filelen': lib.vio_get_filelen,
            'seek': lib.vio_seek,
            'read': lib.vio_read,
            'write': lib.vio_write,
            'tell': lib.vio_tell
        })
