import phpy

USE_MBSTRING = 1


def tagname(_index):
    return phpy.call('exif_tagname', _index)


def read_data(_file, _required_sections=None, _as_arrays=False, _read_thumbnail=False):
    return phpy.call('exif_read_data', _file, _required_sections, _as_arrays, _read_thumbnail)


def thumbnail(_file, _width=None, _height=None, _image_type=None):
    return phpy.call('exif_thumbnail', _file, _width, _height, _image_type)


def imagetype(_filename):
    return phpy.call('exif_imagetype', _filename)




