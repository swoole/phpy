import phpy

IMG_AVIF = 256
IMG_GIF = 1
IMG_JPG = 2
IMG_JPEG = 2
IMG_PNG = 4
IMG_WBMP = 8
IMG_XPM = 16
IMG_WEBP = 32
IMG_BMP = 64
IMG_TGA = 128
IMG_WEBP_LOSSLESS = 101
IMG_COLOR_TILED = -5
IMG_COLOR_STYLED = -2
IMG_COLOR_BRUSHED = -3
IMG_COLOR_STYLEDBRUSHED = -4
IMG_COLOR_TRANSPARENT = -6
IMG_ARC_ROUNDED = 0
IMG_ARC_PIE = 0
IMG_ARC_CHORD = 1
IMG_ARC_NOFILL = 2
IMG_ARC_EDGED = 4
IMG_GD2_RAW = 1
IMG_GD2_COMPRESSED = 2
IMG_FLIP_HORIZONTAL = 1
IMG_FLIP_VERTICAL = 2
IMG_FLIP_BOTH = 3
IMG_EFFECT_REPLACE = 0
IMG_EFFECT_ALPHABLEND = 1
IMG_EFFECT_NORMAL = 2
IMG_EFFECT_OVERLAY = 3
IMG_EFFECT_MULTIPLY = 4
IMG_CROP_DEFAULT = 0
IMG_CROP_TRANSPARENT = 1
IMG_CROP_BLACK = 2
IMG_CROP_WHITE = 3
IMG_CROP_SIDES = 4
IMG_CROP_THRESHOLD = 5
IMG_BELL = 1
IMG_BESSEL = 2
IMG_BILINEAR_FIXED = 3
IMG_BICUBIC = 4
IMG_BICUBIC_FIXED = 5
IMG_BLACKMAN = 6
IMG_BOX = 7
IMG_BSPLINE = 8
IMG_CATMULLROM = 9
IMG_GAUSSIAN = 10
IMG_GENERALIZED_CUBIC = 11
IMG_HERMITE = 12
IMG_HAMMING = 13
IMG_HANNING = 14
IMG_MITCHELL = 15
IMG_POWER = 17
IMG_QUADRATIC = 18
IMG_SINC = 19
IMG_NEAREST_NEIGHBOUR = 16
IMG_WEIGHTED4 = 21
IMG_TRIANGLE = 20
IMG_AFFINE_TRANSLATE = 0
IMG_AFFINE_SCALE = 1
IMG_AFFINE_ROTATE = 2
IMG_AFFINE_SHEAR_HORIZONTAL = 3
IMG_AFFINE_SHEAR_VERTICAL = 4
BUNDLED = 1
IMG_FILTER_NEGATE = 0
IMG_FILTER_GRAYSCALE = 1
IMG_FILTER_BRIGHTNESS = 2
IMG_FILTER_CONTRAST = 3
IMG_FILTER_COLORIZE = 4
IMG_FILTER_EDGEDETECT = 5
IMG_FILTER_GAUSSIAN_BLUR = 7
IMG_FILTER_SELECTIVE_BLUR = 8
IMG_FILTER_EMBOSS = 6
IMG_FILTER_MEAN_REMOVAL = 9
IMG_FILTER_SMOOTH = 10
IMG_FILTER_PIXELATE = 11
IMG_FILTER_SCATTER = 12
VERSION = "2.0.35"
MAJOR_VERSION = 2
MINOR_VERSION = 0
RELEASE_VERSION = 35
EXTRA_VERSION = ""
PNG_NO_FILTER = 0
PNG_FILTER_NONE = 8
PNG_FILTER_SUB = 16
PNG_FILTER_UP = 32
PNG_FILTER_AVG = 64
PNG_FILTER_PAETH = 128
PNG_ALL_FILTERS = 248


def info():
    return phpy.call('gd_info', )


def imageloadfont(_filename):
    return phpy.call('imageloadfont', _filename)


def imagesetstyle(_image, _style):
    return phpy.call('imagesetstyle', _image, _style)


def imagecreatetruecolor(_width, _height):
    return phpy.call('imagecreatetruecolor', _width, _height)


def imageistruecolor(_image):
    return phpy.call('imageistruecolor', _image)


def imagetruecolortopalette(_image, _dither, _num_colors):
    return phpy.call('imagetruecolortopalette', _image, _dither, _num_colors)


def imagepalettetotruecolor(_image):
    return phpy.call('imagepalettetotruecolor', _image)


def imagecolormatch(_image1, _image2):
    return phpy.call('imagecolormatch', _image1, _image2)


def imagesetthickness(_image, _thickness):
    return phpy.call('imagesetthickness', _image, _thickness)


def imagefilledellipse(_image, _center_x, _center_y, _width, _height, _color):
    return phpy.call('imagefilledellipse', _image, _center_x, _center_y, _width, _height, _color)


def imagefilledarc(_image, _center_x, _center_y, _width, _height, _start_angle, _end_angle, _color, _style):
    return phpy.call('imagefilledarc', _image, _center_x, _center_y, _width, _height, _start_angle, _end_angle, _color, _style)


def imagealphablending(_image, _enable):
    return phpy.call('imagealphablending', _image, _enable)


def imagesavealpha(_image, _enable):
    return phpy.call('imagesavealpha', _image, _enable)


def imagelayereffect(_image, _effect):
    return phpy.call('imagelayereffect', _image, _effect)


def imagecolorallocatealpha(_image, _red, _green, _blue, _alpha):
    return phpy.call('imagecolorallocatealpha', _image, _red, _green, _blue, _alpha)


def imagecolorresolvealpha(_image, _red, _green, _blue, _alpha):
    return phpy.call('imagecolorresolvealpha', _image, _red, _green, _blue, _alpha)


def imagecolorclosestalpha(_image, _red, _green, _blue, _alpha):
    return phpy.call('imagecolorclosestalpha', _image, _red, _green, _blue, _alpha)


def imagecolorexactalpha(_image, _red, _green, _blue, _alpha):
    return phpy.call('imagecolorexactalpha', _image, _red, _green, _blue, _alpha)


def imagecopyresampled(_dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _dst_width, _dst_height, _src_width, _src_height):
    return phpy.call('imagecopyresampled', _dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _dst_width, _dst_height, _src_width, _src_height)


def imagerotate(_image, _angle, _background_color, _ignore_transparent=False):
    return phpy.call('imagerotate', _image, _angle, _background_color, _ignore_transparent)


def imagesettile(_image, _tile):
    return phpy.call('imagesettile', _image, _tile)


def imagesetbrush(_image, _brush):
    return phpy.call('imagesetbrush', _image, _brush)


def imagecreate(_width, _height):
    return phpy.call('imagecreate', _width, _height)


def imagetypes():
    return phpy.call('imagetypes', )


def imagecreatefromstring(_data):
    return phpy.call('imagecreatefromstring', _data)


def imagecreatefromgif(_filename):
    return phpy.call('imagecreatefromgif', _filename)


def imagecreatefromjpeg(_filename):
    return phpy.call('imagecreatefromjpeg', _filename)


def imagecreatefrompng(_filename):
    return phpy.call('imagecreatefrompng', _filename)


def imagecreatefromwebp(_filename):
    return phpy.call('imagecreatefromwebp', _filename)


def imagecreatefromxbm(_filename):
    return phpy.call('imagecreatefromxbm', _filename)


def imagecreatefromwbmp(_filename):
    return phpy.call('imagecreatefromwbmp', _filename)


def imagecreatefromgd(_filename):
    return phpy.call('imagecreatefromgd', _filename)


def imagecreatefromgd2(_filename):
    return phpy.call('imagecreatefromgd2', _filename)


def imagecreatefromgd2part(_filename, _x, _y, _width, _height):
    return phpy.call('imagecreatefromgd2part', _filename, _x, _y, _width, _height)


def imagecreatefrombmp(_filename):
    return phpy.call('imagecreatefrombmp', _filename)


def imagecreatefromtga(_filename):
    return phpy.call('imagecreatefromtga', _filename)


def imagexbm(_image, _filename, _foreground_color=None):
    return phpy.call('imagexbm', _image, _filename, _foreground_color)


def imagegif(_image, _file=None):
    return phpy.call('imagegif', _image, _file)


def imagepng(_image, _file=None, _quality=-1, _filters=-1):
    return phpy.call('imagepng', _image, _file, _quality, _filters)


def imagewebp(_image, _file=None, _quality=-1):
    return phpy.call('imagewebp', _image, _file, _quality)


def imagejpeg(_image, _file=None, _quality=-1):
    return phpy.call('imagejpeg', _image, _file, _quality)


def imagewbmp(_image, _file=None, _foreground_color=None):
    return phpy.call('imagewbmp', _image, _file, _foreground_color)


def imagegd(_image, _file=None):
    return phpy.call('imagegd', _image, _file)


def imagegd2(_image, _file=None, _chunk_size=None, _mode=None):
    return phpy.call('imagegd2', _image, _file, _chunk_size, _mode)


def imagebmp(_image, _file=None, _compressed=True):
    return phpy.call('imagebmp', _image, _file, _compressed)


def imagedestroy(_image):
    return phpy.call('imagedestroy', _image)


def imagecolorallocate(_image, _red, _green, _blue):
    return phpy.call('imagecolorallocate', _image, _red, _green, _blue)


def imagepalettecopy(_dst, _src):
    return phpy.call('imagepalettecopy', _dst, _src)


def imagecolorat(_image, _x, _y):
    return phpy.call('imagecolorat', _image, _x, _y)


def imagecolorclosest(_image, _red, _green, _blue):
    return phpy.call('imagecolorclosest', _image, _red, _green, _blue)


def imagecolorclosesthwb(_image, _red, _green, _blue):
    return phpy.call('imagecolorclosesthwb', _image, _red, _green, _blue)


def imagecolordeallocate(_image, _color):
    return phpy.call('imagecolordeallocate', _image, _color)


def imagecolorresolve(_image, _red, _green, _blue):
    return phpy.call('imagecolorresolve', _image, _red, _green, _blue)


def imagecolorexact(_image, _red, _green, _blue):
    return phpy.call('imagecolorexact', _image, _red, _green, _blue)


def imagecolorset(_image, _color, _red, _green, _blue, _alpha=0):
    return phpy.call('imagecolorset', _image, _color, _red, _green, _blue, _alpha)


def imagecolorsforindex(_image, _color):
    return phpy.call('imagecolorsforindex', _image, _color)


def imagegammacorrect(_image, _input_gamma, _output_gamma):
    return phpy.call('imagegammacorrect', _image, _input_gamma, _output_gamma)


def imagesetpixel(_image, _x, _y, _color):
    return phpy.call('imagesetpixel', _image, _x, _y, _color)


def imageline(_image, _x1, _y1, _x2, _y2, _color):
    return phpy.call('imageline', _image, _x1, _y1, _x2, _y2, _color)


def imagedashedline(_image, _x1, _y1, _x2, _y2, _color):
    return phpy.call('imagedashedline', _image, _x1, _y1, _x2, _y2, _color)


def imagerectangle(_image, _x1, _y1, _x2, _y2, _color):
    return phpy.call('imagerectangle', _image, _x1, _y1, _x2, _y2, _color)


def imagefilledrectangle(_image, _x1, _y1, _x2, _y2, _color):
    return phpy.call('imagefilledrectangle', _image, _x1, _y1, _x2, _y2, _color)


def imagearc(_image, _center_x, _center_y, _width, _height, _start_angle, _end_angle, _color):
    return phpy.call('imagearc', _image, _center_x, _center_y, _width, _height, _start_angle, _end_angle, _color)


def imageellipse(_image, _center_x, _center_y, _width, _height, _color):
    return phpy.call('imageellipse', _image, _center_x, _center_y, _width, _height, _color)


def imagefilltoborder(_image, _x, _y, _border_color, _color):
    return phpy.call('imagefilltoborder', _image, _x, _y, _border_color, _color)


def imagefill(_image, _x, _y, _color):
    return phpy.call('imagefill', _image, _x, _y, _color)


def imagecolorstotal(_image):
    return phpy.call('imagecolorstotal', _image)


def imagecolortransparent(_image, _color=None):
    return phpy.call('imagecolortransparent', _image, _color)


def imageinterlace(_image, _enable=None):
    return phpy.call('imageinterlace', _image, _enable)


def imagepolygon(_image, _points, _num_points_or_color, _color=None):
    return phpy.call('imagepolygon', _image, _points, _num_points_or_color, _color)


def imageopenpolygon(_image, _points, _num_points_or_color, _color=None):
    return phpy.call('imageopenpolygon', _image, _points, _num_points_or_color, _color)


def imagefilledpolygon(_image, _points, _num_points_or_color, _color=None):
    return phpy.call('imagefilledpolygon', _image, _points, _num_points_or_color, _color)


def imagefontwidth(_font):
    return phpy.call('imagefontwidth', _font)


def imagefontheight(_font):
    return phpy.call('imagefontheight', _font)


def imagechar(_image, _font, _x, _y, _char, _color):
    return phpy.call('imagechar', _image, _font, _x, _y, _char, _color)


def imagecharup(_image, _font, _x, _y, _char, _color):
    return phpy.call('imagecharup', _image, _font, _x, _y, _char, _color)


def imagestring(_image, _font, _x, _y, _string, _color):
    return phpy.call('imagestring', _image, _font, _x, _y, _string, _color)


def imagestringup(_image, _font, _x, _y, _string, _color):
    return phpy.call('imagestringup', _image, _font, _x, _y, _string, _color)


def imagecopy(_dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _src_width, _src_height):
    return phpy.call('imagecopy', _dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _src_width, _src_height)


def imagecopymerge(_dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _src_width, _src_height, _pct):
    return phpy.call('imagecopymerge', _dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _src_width, _src_height, _pct)


def imagecopymergegray(_dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _src_width, _src_height, _pct):
    return phpy.call('imagecopymergegray', _dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _src_width, _src_height, _pct)


def imagecopyresized(_dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _dst_width, _dst_height, _src_width, _src_height):
    return phpy.call('imagecopyresized', _dst_image, _src_image, _dst_x, _dst_y, _src_x, _src_y, _dst_width, _dst_height, _src_width, _src_height)


def imagesx(_image):
    return phpy.call('imagesx', _image)


def imagesy(_image):
    return phpy.call('imagesy', _image)


def imagesetclip(_image, _x1, _y1, _x2, _y2):
    return phpy.call('imagesetclip', _image, _x1, _y1, _x2, _y2)


def imagegetclip(_image):
    return phpy.call('imagegetclip', _image)


def imageftbbox(_size, _angle, _font_filename, _string, _options=[]):
    return phpy.call('imageftbbox', _size, _angle, _font_filename, _string, _options)


def imagefttext(_image, _size, _angle, _x, _y, _color, _font_filename, _text, _options=[]):
    return phpy.call('imagefttext', _image, _size, _angle, _x, _y, _color, _font_filename, _text, _options)


def imagettfbbox(_size, _angle, _font_filename, _string, _options=[]):
    return phpy.call('imagettfbbox', _size, _angle, _font_filename, _string, _options)


def imagettftext(_image, _size, _angle, _x, _y, _color, _font_filename, _text, _options=[]):
    return phpy.call('imagettftext', _image, _size, _angle, _x, _y, _color, _font_filename, _text, _options)


def imagefilter(_image, _filter, _args=None):
    return phpy.call('imagefilter', _image, _filter, _args)


def imageconvolution(_image, _matrix, _divisor, _offset):
    return phpy.call('imageconvolution', _image, _matrix, _divisor, _offset)


def imageflip(_image, _mode):
    return phpy.call('imageflip', _image, _mode)


def imageantialias(_image, _enable):
    return phpy.call('imageantialias', _image, _enable)


def imagecrop(_image, _rectangle):
    return phpy.call('imagecrop', _image, _rectangle)


def imagecropauto(_image, _mode=0, _threshold=0.5, _color=-1):
    return phpy.call('imagecropauto', _image, _mode, _threshold, _color)


def imagescale(_image, _width, _height=-1, _mode=3):
    return phpy.call('imagescale', _image, _width, _height, _mode)


def imageaffine(_image, _affine, _clip=None):
    return phpy.call('imageaffine', _image, _affine, _clip)


def imageaffinematrixget(_type, _options):
    return phpy.call('imageaffinematrixget', _type, _options)


def imageaffinematrixconcat(_matrix1, _matrix2):
    return phpy.call('imageaffinematrixconcat', _matrix1, _matrix2)


def imagegetinterpolation(_image):
    return phpy.call('imagegetinterpolation', _image)


def imagesetinterpolation(_image, _method=3):
    return phpy.call('imagesetinterpolation', _image, _method)


def imageresolution(_image, _resolution_x=None, _resolution_y=None):
    return phpy.call('imageresolution', _image, _resolution_x, _resolution_y)




class GdImage():


    def __init__(self):
        self.__this = phpy.Object(f'GdImage')


class GdFont():


    def __init__(self):
        self.__this = phpy.Object(f'GdFont')


