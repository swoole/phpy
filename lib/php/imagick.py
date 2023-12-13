import phpy





class ImagickException():


    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ImagickException', _message, _code, _previous)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getFile(self):
        return self.__this.call(f"getFile", )

    def getLine(self):
        return self.__this.call(f"getLine", )

    def getTrace(self):
        return self.__this.call(f"getTrace", )

    def getPrevious(self):
        return self.__this.call(f"getPrevious", )

    def getTraceAsString(self):
        return self.__this.call(f"getTraceAsString", )

    def __str__(self):
        return self.__this.call(f"__toString", )


class ImagickDrawException():


    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ImagickDrawException', _message, _code, _previous)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getFile(self):
        return self.__this.call(f"getFile", )

    def getLine(self):
        return self.__this.call(f"getLine", )

    def getTrace(self):
        return self.__this.call(f"getTrace", )

    def getPrevious(self):
        return self.__this.call(f"getPrevious", )

    def getTraceAsString(self):
        return self.__this.call(f"getTraceAsString", )

    def __str__(self):
        return self.__this.call(f"__toString", )


class ImagickPixelIteratorException():


    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ImagickPixelIteratorException', _message, _code, _previous)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getFile(self):
        return self.__this.call(f"getFile", )

    def getLine(self):
        return self.__this.call(f"getLine", )

    def getTrace(self):
        return self.__this.call(f"getTrace", )

    def getPrevious(self):
        return self.__this.call(f"getPrevious", )

    def getTraceAsString(self):
        return self.__this.call(f"getTraceAsString", )

    def __str__(self):
        return self.__this.call(f"__toString", )


class ImagickPixelException():


    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ImagickPixelException', _message, _code, _previous)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getFile(self):
        return self.__this.call(f"getFile", )

    def getLine(self):
        return self.__this.call(f"getLine", )

    def getTrace(self):
        return self.__this.call(f"getTrace", )

    def getPrevious(self):
        return self.__this.call(f"getPrevious", )

    def getTraceAsString(self):
        return self.__this.call(f"getTraceAsString", )

    def __str__(self):
        return self.__this.call(f"__toString", )


class ImagickKernelException():


    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ImagickKernelException', _message, _code, _previous)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getFile(self):
        return self.__this.call(f"getFile", )

    def getLine(self):
        return self.__this.call(f"getLine", )

    def getTrace(self):
        return self.__this.call(f"getTrace", )

    def getPrevious(self):
        return self.__this.call(f"getPrevious", )

    def getTraceAsString(self):
        return self.__this.call(f"getTraceAsString", )

    def __str__(self):
        return self.__this.call(f"__toString", )


class Imagick():
    COLOR_BLACK = 11
    COLOR_BLUE = 12
    COLOR_CYAN = 13
    COLOR_GREEN = 14
    COLOR_RED = 15
    COLOR_YELLOW = 16
    COLOR_MAGENTA = 17
    COLOR_ALPHA = 18
    COLOR_FUZZ = 19
    IMAGICK_EXTNUM = 30600
    IMAGICK_EXTVER = "3.6.0"
    QUANTUM_RANGE = 65535
    USE_ZEND_MM = 0
    COMPOSITE_DEFAULT = 54
    COMPOSITE_UNDEFINED = 0
    COMPOSITE_NO = 52
    COMPOSITE_ATOP = 2
    COMPOSITE_BLEND = 3
    COMPOSITE_BUMPMAP = 5
    COMPOSITE_CLEAR = 7
    COMPOSITE_COLORBURN = 8
    COMPOSITE_COLORDODGE = 9
    COMPOSITE_COLORIZE = 10
    COMPOSITE_COPYBLACK = 11
    COMPOSITE_COPYBLUE = 12
    COMPOSITE_COPY = 13
    COMPOSITE_COPYCYAN = 14
    COMPOSITE_COPYGREEN = 15
    COMPOSITE_COPYMAGENTA = 16
    COMPOSITE_COPYALPHA = 17
    COMPOSITE_COPYOPACITY = 17
    COMPOSITE_COPYRED = 18
    COMPOSITE_COPYYELLOW = 19
    COMPOSITE_DARKEN = 20
    COMPOSITE_DSTATOP = 28
    COMPOSITE_DST = 29
    COMPOSITE_DSTIN = 30
    COMPOSITE_DSTOUT = 31
    COMPOSITE_DSTOVER = 32
    COMPOSITE_DIFFERENCE = 22
    COMPOSITE_DISPLACE = 23
    COMPOSITE_DISSOLVE = 24
    COMPOSITE_EXCLUSION = 33
    COMPOSITE_HARDLIGHT = 34
    COMPOSITE_HUE = 36
    COMPOSITE_IN = 37
    COMPOSITE_LIGHTEN = 39
    COMPOSITE_LUMINIZE = 44
    COMPOSITE_MODULATE = 48
    COMPOSITE_MULTIPLY = 51
    COMPOSITE_OUT = 53
    COMPOSITE_OVER = 54
    COMPOSITE_OVERLAY = 55
    COMPOSITE_PLUS = 58
    COMPOSITE_REPLACE = 59
    COMPOSITE_SATURATE = 60
    COMPOSITE_SCREEN = 61
    COMPOSITE_SOFTLIGHT = 62
    COMPOSITE_SRCATOP = 63
    COMPOSITE_SRC = 64
    COMPOSITE_SRCIN = 65
    COMPOSITE_SRCOUT = 66
    COMPOSITE_SRCOVER = 67
    COMPOSITE_THRESHOLD = 68
    COMPOSITE_XOR = 70
    COMPOSITE_CHANGEMASK = 6
    COMPOSITE_LINEARLIGHT = 43
    COMPOSITE_DISTORT = 25
    COMPOSITE_BLUR = 4
    COMPOSITE_PEGTOPLIGHT = 56
    COMPOSITE_VIVIDLIGHT = 69
    COMPOSITE_PINLIGHT = 57
    COMPOSITE_LINEARDODGE = 42
    COMPOSITE_LINEARBURN = 41
    COMPOSITE_MATHEMATICS = 45
    COMPOSITE_MODULUSADD = 49
    COMPOSITE_MODULUSSUBTRACT = 50
    COMPOSITE_MINUSDST = 46
    COMPOSITE_DIVIDEDST = 26
    COMPOSITE_DIVIDESRC = 27
    COMPOSITE_MINUSSRC = 47
    COMPOSITE_DARKENINTENSITY = 21
    COMPOSITE_LIGHTENINTENSITY = 40
    COMPOSITE_HARDMIX = 35
    COMPOSITE_STEREO = 71
    COMPOSITE_FREEZE = 72
    COMPOSITE_INTERPOLATE = 73
    COMPOSITE_NEGATE = 74
    COMPOSITE_REFLECT = 75
    COMPOSITE_SOFTBURN = 76
    COMPOSITE_SOFTDODGE = 77
    COMPOSITE_STAMP = 78
    COMPOSITE_RMSE = 79
    MONTAGEMODE_FRAME = 1
    MONTAGEMODE_UNFRAME = 2
    MONTAGEMODE_CONCATENATE = 3
    STYLE_NORMAL = 1
    STYLE_ITALIC = 2
    STYLE_OBLIQUE = 3
    STYLE_ANY = 4
    STYLE_BOLD = 5
    FILTER_UNDEFINED = 0
    FILTER_POINT = 1
    FILTER_BOX = 2
    FILTER_TRIANGLE = 3
    FILTER_HERMITE = 4
    FILTER_HANNING = 5
    FILTER_HANN = 5
    FILTER_HAMMING = 6
    FILTER_BLACKMAN = 7
    FILTER_GAUSSIAN = 8
    FILTER_QUADRATIC = 9
    FILTER_CUBIC = 10
    FILTER_CATROM = 11
    FILTER_MITCHELL = 12
    FILTER_LANCZOS = 22
    FILTER_BESSEL = 13
    FILTER_SINC = 14
    FILTER_KAISER = 16
    FILTER_WELSH = 17
    FILTER_WELCH = 17
    FILTER_PARZEN = 18
    FILTER_LAGRANGE = 21
    FILTER_SENTINEL = 32
    FILTER_BOHMAN = 19
    FILTER_BARTLETT = 20
    FILTER_JINC = 13
    FILTER_SINCFAST = 15
    FILTER_ROBIDOUX = 26
    FILTER_LANCZOSSHARP = 23
    FILTER_LANCZOS2 = 24
    FILTER_LANCZOS2SHARP = 25
    FILTER_ROBIDOUXSHARP = 27
    FILTER_COSINE = 28
    FILTER_SPLINE = 29
    FILTER_LANCZOSRADIUS = 30
    FILTER_CUBIC_SPLINE = 31
    IMGTYPE_UNDEFINED = 0
    IMGTYPE_BILEVEL = 1
    IMGTYPE_GRAYSCALE = 2
    IMGTYPE_GRAYSCALEALPHA = 3
    IMGTYPE_GRAYSCALEMATTE = 3
    IMGTYPE_PALETTE = 4
    IMGTYPE_PALETTEMATTE = 5
    IMGTYPE_PALETTEALPHA = 5
    IMGTYPE_TRUECOLOR = 6
    IMGTYPE_TRUECOLORALPHA = 7
    IMGTYPE_TRUECOLORMATTE = 7
    IMGTYPE_COLORSEPARATION = 8
    IMGTYPE_COLORSEPARATIONALPHA = 9
    IMGTYPE_COLORSEPARATIONMATTE = 9
    IMGTYPE_OPTIMIZE = 10
    IMGTYPE_PALETTEBILEVELALPHA = 11
    IMGTYPE_PALETTEBILEVELMATTE = 11
    RESOLUTION_UNDEFINED = 0
    RESOLUTION_PIXELSPERINCH = 1
    RESOLUTION_PIXELSPERCENTIMETER = 2
    COMPRESSION_UNDEFINED = 0
    COMPRESSION_NO = 16
    COMPRESSION_BZIP = 3
    COMPRESSION_FAX = 7
    COMPRESSION_GROUP4 = 8
    COMPRESSION_JPEG = 12
    COMPRESSION_JPEG2000 = 11
    COMPRESSION_LOSSLESSJPEG = 13
    COMPRESSION_LZW = 15
    COMPRESSION_RLE = 19
    COMPRESSION_ZIP = 20
    COMPRESSION_DXT1 = 4
    COMPRESSION_DXT3 = 5
    COMPRESSION_DXT5 = 6
    COMPRESSION_ZIPS = 21
    COMPRESSION_PIZ = 17
    COMPRESSION_PXR24 = 18
    COMPRESSION_B44 = 2
    COMPRESSION_B44A = 1
    COMPRESSION_LZMA = 14
    COMPRESSION_JBIG1 = 9
    COMPRESSION_JBIG2 = 10
    COMPRESSION_ZSTD = 22
    COMPRESSION_WEBP = 23
    COMPRESSION_DWAA = 24
    COMPRESSION_DWAB = 25
    PAINT_POINT = 1
    PAINT_REPLACE = 2
    PAINT_FLOODFILL = 3
    PAINT_FILLTOBORDER = 4
    PAINT_RESET = 5
    GRAVITY_NORTHWEST = 1
    GRAVITY_NORTH = 2
    GRAVITY_NORTHEAST = 3
    GRAVITY_WEST = 4
    GRAVITY_CENTER = 5
    GRAVITY_EAST = 6
    GRAVITY_SOUTHWEST = 7
    GRAVITY_SOUTH = 8
    GRAVITY_SOUTHEAST = 9
    GRAVITY_FORGET = 0
    STRETCH_NORMAL = 1
    STRETCH_ULTRACONDENSED = 2
    STRETCH_EXTRACONDENSED = 3
    STRETCH_CONDENSED = 4
    STRETCH_SEMICONDENSED = 5
    STRETCH_SEMIEXPANDED = 6
    STRETCH_EXPANDED = 7
    STRETCH_EXTRAEXPANDED = 8
    STRETCH_ULTRAEXPANDED = 9
    STRETCH_ANY = 10
    ALIGN_UNDEFINED = 0
    ALIGN_LEFT = 1
    ALIGN_CENTER = 2
    ALIGN_RIGHT = 3
    DECORATION_NO = 1
    DECORATION_UNDERLINE = 2
    DECORATION_OVERLINE = 3
    DECORATION_LINETROUGH = 4
    DECORATION_LINETHROUGH = 4
    NOISE_UNIFORM = 1
    NOISE_GAUSSIAN = 2
    NOISE_MULTIPLICATIVEGAUSSIAN = 3
    NOISE_IMPULSE = 4
    NOISE_LAPLACIAN = 5
    NOISE_POISSON = 6
    NOISE_RANDOM = 7
    CHANNEL_UNDEFINED = 0
    CHANNEL_RED = 1
    CHANNEL_GRAY = 1
    CHANNEL_CYAN = 1
    CHANNEL_GREEN = 2
    CHANNEL_MAGENTA = 2
    CHANNEL_BLUE = 4
    CHANNEL_YELLOW = 4
    CHANNEL_ALPHA = 16
    CHANNEL_OPACITY = 16
    CHANNEL_BLACK = 8
    CHANNEL_INDEX = 32
    CHANNEL_ALL = 134217727
    CHANNEL_DEFAULT = 134217727
    CHANNEL_RGBA = 23
    CHANNEL_TRUEALPHA = 256
    CHANNEL_RGBS = 512
    CHANNEL_GRAY_CHANNELS = 1024
    CHANNEL_SYNC = 131072
    CHANNEL_READ_MASK = 64
    CHANNEL_WRITE_MASK = 128
    CHANNEL_META = 256
    CHANNEL_COMPOSITE_MASK = 512
    CHANNEL_COMPOSITES = 31
    METRIC_ABSOLUTEERRORMETRIC = 1
    METRIC_MEANABSOLUTEERROR = 3
    METRIC_MEANERRORPERPIXELMETRIC = 4
    METRIC_MEANSQUAREERROR = 5
    METRIC_PEAKABSOLUTEERROR = 7
    METRIC_PEAKSIGNALTONOISERATIO = 8
    METRIC_ROOTMEANSQUAREDERROR = 10
    METRIC_NORMALIZEDCROSSCORRELATIONERRORMETRIC = 6
    METRIC_FUZZERROR = 2
    METRIC_PERCEPTUALHASH_ERROR = 9
    METRIC_STRUCTURAL_SIMILARITY_ERROR = 11
    METRIC_STRUCTURAL_DISSIMILARITY_ERROR = 12
    PIXEL_CHAR = 1
    PIXELSTORAGE_CHAR = 1
    PIXEL_DOUBLE = 2
    PIXELSTORAGE_DOUBLE = 2
    PIXEL_FLOAT = 3
    PIXELSTORAGE_FLOAT = 3
    PIXEL_LONG = 4
    PIXELSTORAGE_LONG = 4
    PIXEL_QUANTUM = 6
    PIXELSTORAGE_QUANTUM = 6
    PIXEL_SHORT = 7
    PIXELSTORAGE_SHORT = 7
    EVALUATE_UNDEFINED = 0
    EVALUATE_ADD = 2
    EVALUATE_AND = 4
    EVALUATE_DIVIDE = 6
    EVALUATE_LEFTSHIFT = 11
    EVALUATE_MAX = 13
    EVALUATE_MIN = 16
    EVALUATE_MULTIPLY = 18
    EVALUATE_OR = 19
    EVALUATE_RIGHTSHIFT = 22
    EVALUATE_SET = 24
    EVALUATE_SUBTRACT = 26
    EVALUATE_XOR = 32
    EVALUATE_POW = 21
    EVALUATE_LOG = 12
    EVALUATE_THRESHOLD = 29
    EVALUATE_THRESHOLDBLACK = 28
    EVALUATE_THRESHOLDWHITE = 30
    EVALUATE_GAUSSIANNOISE = 8
    EVALUATE_IMPULSENOISE = 9
    EVALUATE_LAPLACIANNOISE = 10
    EVALUATE_MULTIPLICATIVENOISE = 17
    EVALUATE_POISSONNOISE = 20
    EVALUATE_UNIFORMNOISE = 31
    EVALUATE_COSINE = 5
    EVALUATE_SINE = 25
    EVALUATE_ADDMODULUS = 3
    EVALUATE_MEAN = 14
    EVALUATE_ABS = 1
    EVALUATE_EXPONENTIAL = 7
    EVALUATE_MEDIAN = 15
    EVALUATE_SUM = 27
    EVALUATE_ROOT_MEAN_SQUARE = 23
    EVALUATE_INVERSE_LOG = 33
    COLORSPACE_UNDEFINED = 0
    COLORSPACE_RGB = 21
    COLORSPACE_GRAY = 3
    COLORSPACE_TRANSPARENT = 24
    COLORSPACE_OHTA = 18
    COLORSPACE_XYZ = 26
    COLORSPACE_YCBCR = 27
    COLORSPACE_YCC = 28
    COLORSPACE_YIQ = 30
    COLORSPACE_YPBPR = 31
    COLORSPACE_YUV = 32
    COLORSPACE_CMYK = 2
    COLORSPACE_SRGB = 23
    COLORSPACE_HSB = 6
    COLORSPACE_HSL = 8
    COLORSPACE_HWB = 10
    COLORSPACE_LOG = 15
    COLORSPACE_CMY = 1
    COLORSPACE_LUV = 17
    COLORSPACE_HCL = 4
    COLORSPACE_LCH = 12
    COLORSPACE_LMS = 16
    COLORSPACE_LCHAB = 13
    COLORSPACE_LCHUV = 14
    COLORSPACE_SCRGB = 22
    COLORSPACE_HSI = 7
    COLORSPACE_HSV = 9
    COLORSPACE_HCLP = 5
    COLORSPACE_YDBDR = 29
    COLORSPACE_REC601YCBCR = 19
    COLORSPACE_REC709YCBCR = 20
    COLORSPACE_XYY = 25
    COLORSPACE_LINEARGRAY = 33
    COLORSPACE_DISPLAYP3 = 35
    COLORSPACE_ADOBE98 = 36
    COLORSPACE_PROPHOTO = 37
    COLORSPACE_JZAZBZ = 34
    VIRTUALPIXELMETHOD_UNDEFINED = 0
    VIRTUALPIXELMETHOD_BACKGROUND = 1
    VIRTUALPIXELMETHOD_EDGE = 3
    VIRTUALPIXELMETHOD_MIRROR = 4
    VIRTUALPIXELMETHOD_TILE = 6
    VIRTUALPIXELMETHOD_TRANSPARENT = 7
    VIRTUALPIXELMETHOD_MASK = 8
    VIRTUALPIXELMETHOD_BLACK = 9
    VIRTUALPIXELMETHOD_GRAY = 10
    VIRTUALPIXELMETHOD_WHITE = 11
    VIRTUALPIXELMETHOD_HORIZONTALTILE = 12
    VIRTUALPIXELMETHOD_VERTICALTILE = 13
    VIRTUALPIXELMETHOD_HORIZONTALTILEEDGE = 14
    VIRTUALPIXELMETHOD_VERTICALTILEEDGE = 15
    VIRTUALPIXELMETHOD_CHECKERTILE = 16
    VIRTUALPIXELMETHOD_DITHER = 2
    VIRTUALPIXELMETHOD_RANDOM = 5
    PREVIEW_UNDEFINED = 0
    PREVIEW_ROTATE = 1
    PREVIEW_SHEAR = 2
    PREVIEW_ROLL = 3
    PREVIEW_HUE = 4
    PREVIEW_SATURATION = 5
    PREVIEW_BRIGHTNESS = 6
    PREVIEW_GAMMA = 7
    PREVIEW_SPIFF = 8
    PREVIEW_DULL = 9
    PREVIEW_GRAYSCALE = 10
    PREVIEW_QUANTIZE = 11
    PREVIEW_DESPECKLE = 12
    PREVIEW_REDUCENOISE = 13
    PREVIEW_ADDNOISE = 14
    PREVIEW_SHARPEN = 15
    PREVIEW_BLUR = 16
    PREVIEW_THRESHOLD = 17
    PREVIEW_EDGEDETECT = 18
    PREVIEW_SPREAD = 19
    PREVIEW_SOLARIZE = 20
    PREVIEW_SHADE = 21
    PREVIEW_RAISE = 22
    PREVIEW_SEGMENT = 23
    PREVIEW_SWIRL = 24
    PREVIEW_IMPLODE = 25
    PREVIEW_WAVE = 26
    PREVIEW_OILPAINT = 27
    PREVIEW_CHARCOALDRAWING = 28
    PREVIEW_JPEG = 29
    RENDERINGINTENT_UNDEFINED = 0
    RENDERINGINTENT_SATURATION = 1
    RENDERINGINTENT_PERCEPTUAL = 2
    RENDERINGINTENT_ABSOLUTE = 3
    RENDERINGINTENT_RELATIVE = 4
    INTERLACE_UNDEFINED = 0
    INTERLACE_NO = 1
    INTERLACE_LINE = 2
    INTERLACE_PLANE = 3
    INTERLACE_PARTITION = 4
    INTERLACE_GIF = 5
    INTERLACE_JPEG = 6
    INTERLACE_PNG = 7
    FILLRULE_UNDEFINED = 0
    FILLRULE_EVENODD = 1
    FILLRULE_NONZERO = 2
    PATHUNITS_UNDEFINED = 0
    PATHUNITS_USERSPACE = 1
    PATHUNITS_USERSPACEONUSE = 2
    PATHUNITS_OBJECTBOUNDINGBOX = 3
    LINECAP_UNDEFINED = 0
    LINECAP_BUTT = 1
    LINECAP_ROUND = 2
    LINECAP_SQUARE = 3
    LINEJOIN_UNDEFINED = 0
    LINEJOIN_MITER = 1
    LINEJOIN_ROUND = 2
    LINEJOIN_BEVEL = 3
    RESOURCETYPE_UNDEFINED = 0
    RESOURCETYPE_AREA = 1
    RESOURCETYPE_DISK = 2
    RESOURCETYPE_FILE = 3
    RESOURCETYPE_MAP = 5
    RESOURCETYPE_MEMORY = 6
    RESOURCETYPE_TIME = 9
    RESOURCETYPE_THROTTLE = 8
    RESOURCETYPE_THREAD = 7
    RESOURCETYPE_WIDTH = 10
    RESOURCETYPE_HEIGHT = 4
    RESOURCETYPE_LISTLENGTH = 11
    DISPOSE_UNRECOGNIZED = 0
    DISPOSE_UNDEFINED = 0
    DISPOSE_NONE = 1
    DISPOSE_BACKGROUND = 2
    DISPOSE_PREVIOUS = 3
    INTERPOLATE_UNDEFINED = 0
    INTERPOLATE_AVERAGE = 1
    INTERPOLATE_BILINEAR = 5
    INTERPOLATE_INTEGER = 8
    INTERPOLATE_MESH = 9
    INTERPOLATE_SPLINE = 11
    INTERPOLATE_AVERAGE_9 = 2
    INTERPOLATE_AVERAGE_16 = 3
    INTERPOLATE_BLEND = 6
    INTERPOLATE_BACKGROUND_COLOR = 4
    INTERPOLATE_CATROM = 7
    INTERPOLATE_NEAREST_PIXEL = 10
    LAYERMETHOD_UNDEFINED = 0
    LAYERMETHOD_COALESCE = 1
    LAYERMETHOD_COMPAREANY = 2
    LAYERMETHOD_COMPARECLEAR = 3
    LAYERMETHOD_COMPAREOVERLAY = 4
    LAYERMETHOD_DISPOSE = 5
    LAYERMETHOD_OPTIMIZE = 6
    LAYERMETHOD_OPTIMIZEPLUS = 8
    LAYERMETHOD_OPTIMIZETRANS = 9
    LAYERMETHOD_COMPOSITE = 12
    LAYERMETHOD_OPTIMIZEIMAGE = 7
    LAYERMETHOD_REMOVEDUPS = 10
    LAYERMETHOD_REMOVEZERO = 11
    LAYERMETHOD_TRIMBOUNDS = 16
    ORIENTATION_UNDEFINED = 0
    ORIENTATION_TOPLEFT = 1
    ORIENTATION_TOPRIGHT = 2
    ORIENTATION_BOTTOMRIGHT = 3
    ORIENTATION_BOTTOMLEFT = 4
    ORIENTATION_LEFTTOP = 5
    ORIENTATION_RIGHTTOP = 6
    ORIENTATION_RIGHTBOTTOM = 7
    ORIENTATION_LEFTBOTTOM = 8
    DISTORTION_UNDEFINED = 0
    DISTORTION_AFFINE = 1
    DISTORTION_AFFINEPROJECTION = 2
    DISTORTION_ARC = 9
    DISTORTION_BILINEAR = 6
    DISTORTION_PERSPECTIVE = 4
    DISTORTION_PERSPECTIVEPROJECTION = 5
    DISTORTION_SCALEROTATETRANSLATE = 3
    DISTORTION_POLYNOMIAL = 8
    DISTORTION_POLAR = 10
    DISTORTION_DEPOLAR = 11
    DISTORTION_BARREL = 14
    DISTORTION_SHEPARDS = 16
    DISTORTION_SENTINEL = 18
    DISTORTION_RIGID_AFFINE = 19
    DISTORTION_BARRELINVERSE = 15
    DISTORTION_BILINEARFORWARD = 6
    DISTORTION_BILINEARREVERSE = 7
    DISTORTION_RESIZE = 17
    DISTORTION_CYLINDER2PLANE = 12
    DISTORTION_PLANE2CYLINDER = 13
    LAYERMETHOD_MERGE = 13
    LAYERMETHOD_FLATTEN = 14
    LAYERMETHOD_MOSAIC = 15
    ALPHACHANNEL_ACTIVATE = 1
    ALPHACHANNEL_ON = 10
    ALPHACHANNEL_SET = 13
    ALPHACHANNEL_UNDEFINED = 0
    ALPHACHANNEL_DISCRETE = 6
    ALPHACHANNEL_COPY = 4
    ALPHACHANNEL_DEACTIVATE = 5
    ALPHACHANNEL_EXTRACT = 8
    ALPHACHANNEL_OFF = 9
    ALPHACHANNEL_OPAQUE = 11
    ALPHACHANNEL_SHAPE = 14
    ALPHACHANNEL_TRANSPARENT = 15
    ALPHACHANNEL_ASSOCIATE = 2
    ALPHACHANNEL_DISSOCIATE = 7
    SPARSECOLORMETHOD_UNDEFINED = 0
    SPARSECOLORMETHOD_BARYCENTRIC = 1
    SPARSECOLORMETHOD_BILINEAR = 7
    SPARSECOLORMETHOD_POLYNOMIAL = 8
    SPARSECOLORMETHOD_SPEPARDS = 16
    SPARSECOLORMETHOD_VORONOI = 18
    SPARSECOLORMETHOD_INVERSE = 19
    SPARSECOLORMETHOD_MANHATTAN = 20
    DITHERMETHOD_UNDEFINED = 0
    DITHERMETHOD_NO = 1
    DITHERMETHOD_RIEMERSMA = 2
    DITHERMETHOD_FLOYDSTEINBERG = 3
    FUNCTION_UNDEFINED = 0
    FUNCTION_POLYNOMIAL = 3
    FUNCTION_SINUSOID = 4
    ALPHACHANNEL_BACKGROUND = 3
    FUNCTION_ARCSIN = 1
    FUNCTION_ARCTAN = 2
    ALPHACHANNEL_REMOVE = 12
    STATISTIC_GRADIENT = 1
    STATISTIC_MAXIMUM = 2
    STATISTIC_MEAN = 3
    STATISTIC_MEDIAN = 4
    STATISTIC_MINIMUM = 5
    STATISTIC_MODE = 6
    STATISTIC_NONPEAK = 7
    STATISTIC_STANDARD_DEVIATION = 9
    STATISTIC_ROOT_MEAN_SQUARE = 8
    STATISTIC_CONTRAST = 10
    MORPHOLOGY_CONVOLVE = 1
    MORPHOLOGY_CORRELATE = 2
    MORPHOLOGY_ERODE = 3
    MORPHOLOGY_DILATE = 4
    MORPHOLOGY_ERODE_INTENSITY = 5
    MORPHOLOGY_DILATE_INTENSITY = 6
    MORPHOLOGY_DISTANCE = 21
    MORPHOLOGY_OPEN = 8
    MORPHOLOGY_CLOSE = 9
    MORPHOLOGY_OPEN_INTENSITY = 10
    MORPHOLOGY_CLOSE_INTENSITY = 11
    MORPHOLOGY_SMOOTH = 12
    MORPHOLOGY_EDGE_IN = 13
    MORPHOLOGY_EDGE_OUT = 14
    MORPHOLOGY_EDGE = 15
    MORPHOLOGY_TOP_HAT = 16
    MORPHOLOGY_BOTTOM_HAT = 17
    MORPHOLOGY_HIT_AND_MISS = 18
    MORPHOLOGY_THINNING = 19
    MORPHOLOGY_THICKEN = 20
    MORPHOLOGY_VORONOI = 22
    MORPHOLOGY_ITERATIVE = 7
    KERNEL_UNITY = 1
    KERNEL_GAUSSIAN = 2
    KERNEL_DIFFERENCE_OF_GAUSSIANS = 3
    KERNEL_LAPLACIAN_OF_GAUSSIANS = 4
    KERNEL_BLUR = 5
    KERNEL_COMET = 6
    KERNEL_LAPLACIAN = 8
    KERNEL_SOBEL = 9
    KERNEL_FREI_CHEN = 10
    KERNEL_ROBERTS = 11
    KERNEL_PREWITT = 12
    KERNEL_COMPASS = 13
    KERNEL_KIRSCH = 14
    KERNEL_DIAMOND = 15
    KERNEL_SQUARE = 16
    KERNEL_RECTANGLE = 17
    KERNEL_OCTAGON = 18
    KERNEL_DISK = 19
    KERNEL_PLUS = 20
    KERNEL_CROSS = 21
    KERNEL_RING = 22
    KERNEL_PEAKS = 23
    KERNEL_EDGES = 24
    KERNEL_CORNERS = 25
    KERNEL_DIAGONALS = 26
    KERNEL_LINE_ENDS = 27
    KERNEL_LINE_JUNCTIONS = 28
    KERNEL_RIDGES = 29
    KERNEL_CONVEX_HULL = 30
    KERNEL_THIN_SE = 31
    KERNEL_SKELETON = 32
    KERNEL_CHEBYSHEV = 33
    KERNEL_MANHATTAN = 34
    KERNEL_OCTAGONAL = 35
    KERNEL_EUCLIDEAN = 36
    KERNEL_USER_DEFINED = 37
    KERNEL_BINOMIAL = 7
    DIRECTION_LEFT_TO_RIGHT = 2
    DIRECTION_RIGHT_TO_LEFT = 1
    NORMALIZE_KERNEL_NONE = 0
    NORMALIZE_KERNEL_VALUE = 8192
    NORMALIZE_KERNEL_CORRELATE = 65536
    NORMALIZE_KERNEL_PERCENT = 4096
    PIXELMASK_READ = 1
    PIXELMASK_WRITE = 2
    PIXELMASK_COMPOSITE = 4
    AUTO_THRESHOLD_KAPUR = 1
    AUTO_THRESHOLD_OTSU = 2
    AUTO_THRESHOLD_TRIANGLE = 3
    COMPLEX_OPERATOR_ADD = 1
    COMPLEX_OPERATOR_CONJUGATE = 2
    COMPLEX_OPERATOR_DIVIDE = 3
    COMPLEX_OPERATOR_MAGNITUDEPHASE = 4
    COMPLEX_OPERATOR_MULTIPLY = 5
    COMPLEX_OPERATOR_REALIMAGINARY = 6
    COMPLEX_OPERATOR_SUBTRACT = 7


    def optimizeImageLayers(self):
        return self.__this.call(f"optimizeImageLayers", )

    def compareImageLayers(self, _metric):
        return self.__this.call(f"compareImageLayers", _metric)

    def pingImageBlob(self, _image):
        return self.__this.call(f"pingImageBlob", _image)

    def pingImageFile(self, _filehandle, _filename=None):
        return self.__this.call(f"pingImageFile", _filehandle, _filename)

    def transposeImage(self):
        return self.__this.call(f"transposeImage", )

    def transverseImage(self):
        return self.__this.call(f"transverseImage", )

    def trimImage(self, _fuzz):
        return self.__this.call(f"trimImage", _fuzz)

    def waveImage(self, _amplitude, _length):
        return self.__this.call(f"waveImage", _amplitude, _length)

    def vignetteImage(self, _black_point, _white_point, _x, _y):
        return self.__this.call(f"vignetteImage", _black_point, _white_point, _x, _y)

    def uniqueImageColors(self):
        return self.__this.call(f"uniqueImageColors", )

    def setImageMatte(self, _matte):
        return self.__this.call(f"setImageMatte", _matte)

    def adaptiveResizeImage(self, _columns, _rows, _bestfit=False, _legacy=False):
        return self.__this.call(f"adaptiveResizeImage", _columns, _rows, _bestfit, _legacy)

    def sketchImage(self, _radius, _sigma, _angle):
        return self.__this.call(f"sketchImage", _radius, _sigma, _angle)

    def shadeImage(self, _gray, _azimuth, _elevation):
        return self.__this.call(f"shadeImage", _gray, _azimuth, _elevation)

    def getSizeOffset(self):
        return self.__this.call(f"getSizeOffset", )

    def setSizeOffset(self, _columns, _rows, _offset):
        return self.__this.call(f"setSizeOffset", _columns, _rows, _offset)

    def adaptiveBlurImage(self, _radius, _sigma, _channel=134217727):
        return self.__this.call(f"adaptiveBlurImage", _radius, _sigma, _channel)

    def contrastStretchImage(self, _black_point, _white_point, _channel=134217727):
        return self.__this.call(f"contrastStretchImage", _black_point, _white_point, _channel)

    def adaptiveSharpenImage(self, _radius, _sigma, _channel=134217727):
        return self.__this.call(f"adaptiveSharpenImage", _radius, _sigma, _channel)

    def randomThresholdImage(self, _low, _high, _channel=134217727):
        return self.__this.call(f"randomThresholdImage", _low, _high, _channel)

    def roundCornersImage(self, _x_rounding, _y_rounding, _stroke_width=10, _displace=5, _size_correction=-6):
        return self.__this.call(f"roundCornersImage", _x_rounding, _y_rounding, _stroke_width, _displace, _size_correction)

    def roundCorners(self, _x_rounding, _y_rounding, _stroke_width=10, _displace=5, _size_correction=-6):
        return self.__this.call(f"roundCorners", _x_rounding, _y_rounding, _stroke_width, _displace, _size_correction)

    def setIteratorIndex(self, _index):
        return self.__this.call(f"setIteratorIndex", _index)

    def getIteratorIndex(self):
        return self.__this.call(f"getIteratorIndex", )

    def setImageAlpha(self, _alpha):
        return self.__this.call(f"setImageAlpha", _alpha)

    def polaroidImage(self, _settings, _angle):
        return self.__this.call(f"polaroidImage", _settings, _angle)

    def getImageProperty(self, _name):
        return self.__this.call(f"getImageProperty", _name)

    def setImageProperty(self, _name, _value):
        return self.__this.call(f"setImageProperty", _name, _value)

    def deleteImageProperty(self, _name):
        return self.__this.call(f"deleteImageProperty", _name)

    def identifyFormat(self, _format):
        return self.__this.call(f"identifyFormat", _format)

    def setImageInterpolateMethod(self, _method):
        return self.__this.call(f"setImageInterpolateMethod", _method)

    def getImageInterpolateMethod(self):
        return self.__this.call(f"getImageInterpolateMethod", )

    def linearStretchImage(self, _black_point, _white_point):
        return self.__this.call(f"linearStretchImage", _black_point, _white_point)

    def getImageLength(self):
        return self.__this.call(f"getImageLength", )

    def extentImage(self, _width, _height, _x, _y):
        return self.__this.call(f"extentImage", _width, _height, _x, _y)

    def getImageOrientation(self):
        return self.__this.call(f"getImageOrientation", )

    def setImageOrientation(self, _orientation):
        return self.__this.call(f"setImageOrientation", _orientation)

    def clutImage(self, _lookup_table, _channel=134217727):
        return self.__this.call(f"clutImage", _lookup_table, _channel)

    def getImageProperties(self, _pattern="*", _include_values=True):
        return self.__this.call(f"getImageProperties", _pattern, _include_values)

    def getImageProfiles(self, _pattern="*", _include_values=True):
        return self.__this.call(f"getImageProfiles", _pattern, _include_values)

    def distortImage(self, _distortion, _arguments, _bestfit):
        return self.__this.call(f"distortImage", _distortion, _arguments, _bestfit)

    def writeImageFile(self, _filehandle, _format=None):
        return self.__this.call(f"writeImageFile", _filehandle, _format)

    def writeImagesFile(self, _filehandle, _format=None):
        return self.__this.call(f"writeImagesFile", _filehandle, _format)

    def resetImagePage(self, _page):
        return self.__this.call(f"resetImagePage", _page)

    def animateImages(self, _x_server):
        return self.__this.call(f"animateImages", _x_server)

    def setFont(self, _font):
        return self.__this.call(f"setFont", _font)

    def getFont(self):
        return self.__this.call(f"getFont", )

    def setPointSize(self, _point_size):
        return self.__this.call(f"setPointSize", _point_size)

    def getPointSize(self):
        return self.__this.call(f"getPointSize", )

    def mergeImageLayers(self, _layermethod):
        return self.__this.call(f"mergeImageLayers", _layermethod)

    def setImageAlphaChannel(self, _alphachannel):
        return self.__this.call(f"setImageAlphaChannel", _alphachannel)

    def floodfillPaintImage(self, _fill_color, _fuzz, _border_color, _x, _y, _invert, _channel=134217727):
        return self.__this.call(f"floodfillPaintImage", _fill_color, _fuzz, _border_color, _x, _y, _invert, _channel)

    def opaquePaintImage(self, _target_color, _fill_color, _fuzz, _invert, _channel=134217727):
        return self.__this.call(f"opaquePaintImage", _target_color, _fill_color, _fuzz, _invert, _channel)

    def transparentPaintImage(self, _target_color, _alpha, _fuzz, _invert):
        return self.__this.call(f"transparentPaintImage", _target_color, _alpha, _fuzz, _invert)

    def liquidRescaleImage(self, _width, _height, _delta_x, _rigidity):
        return self.__this.call(f"liquidRescaleImage", _width, _height, _delta_x, _rigidity)

    def encipherImage(self, _passphrase):
        return self.__this.call(f"encipherImage", _passphrase)

    def decipherImage(self, _passphrase):
        return self.__this.call(f"decipherImage", _passphrase)

    def setGravity(self, _gravity):
        return self.__this.call(f"setGravity", _gravity)

    def getGravity(self):
        return self.__this.call(f"getGravity", )

    def getImageChannelRange(self, _channel):
        return self.__this.call(f"getImageChannelRange", _channel)

    def getImageAlphaChannel(self):
        return self.__this.call(f"getImageAlphaChannel", )

    def getImageChannelDistortions(self, _reference_image, _metric, _channel=134217727):
        return self.__this.call(f"getImageChannelDistortions", _reference_image, _metric, _channel)

    def setImageGravity(self, _gravity):
        return self.__this.call(f"setImageGravity", _gravity)

    def getImageGravity(self):
        return self.__this.call(f"getImageGravity", )

    def importImagePixels(self, _x, _y, _width, _height, _map, _pixelstorage, _pixels):
        return self.__this.call(f"importImagePixels", _x, _y, _width, _height, _map, _pixelstorage, _pixels)

    def deskewImage(self, _threshold):
        return self.__this.call(f"deskewImage", _threshold)

    def segmentImage(self, _colorspace, _cluster_threshold, _smooth_threshold, _verbose=False):
        return self.__this.call(f"segmentImage", _colorspace, _cluster_threshold, _smooth_threshold, _verbose)

    def sparseColorImage(self, _sparsecolormethod, _arguments, _channel=134217727):
        return self.__this.call(f"sparseColorImage", _sparsecolormethod, _arguments, _channel)

    def remapImage(self, _replacement, _dither_method):
        return self.__this.call(f"remapImage", _replacement, _dither_method)

    def houghLineImage(self, _width, _height, _threshold):
        return self.__this.call(f"houghLineImage", _width, _height, _threshold)

    def exportImagePixels(self, _x, _y, _width, _height, _map, _pixelstorage):
        return self.__this.call(f"exportImagePixels", _x, _y, _width, _height, _map, _pixelstorage)

    def getImageChannelKurtosis(self, _channel=134217727):
        return self.__this.call(f"getImageChannelKurtosis", _channel)

    def functionImage(self, _function, _parameters, _channel=134217727):
        return self.__this.call(f"functionImage", _function, _parameters, _channel)

    def transformImageColorspace(self, _colorspace):
        return self.__this.call(f"transformImageColorspace", _colorspace)

    def haldClutImage(self, _clut, _channel=134217727):
        return self.__this.call(f"haldClutImage", _clut, _channel)

    def autoLevelImage(self, _channel=134217727):
        return self.__this.call(f"autoLevelImage", _channel)

    def blueShiftImage(self, _factor=1.5):
        return self.__this.call(f"blueShiftImage", _factor)

    def getImageArtifact(self, _artifact):
        return self.__this.call(f"getImageArtifact", _artifact)

    def setImageArtifact(self, _artifact, _value):
        return self.__this.call(f"setImageArtifact", _artifact, _value)

    def deleteImageArtifact(self, _artifact):
        return self.__this.call(f"deleteImageArtifact", _artifact)

    def getColorspace(self):
        return self.__this.call(f"getColorspace", )

    def setColorspace(self, _colorspace):
        return self.__this.call(f"setColorspace", _colorspace)

    def clampImage(self, _channel=134217727):
        return self.__this.call(f"clampImage", _channel)

    def smushImages(self, _stack, _offset):
        return self.__this.call(f"smushImages", _stack, _offset)

    def __init__(self, _files=None):
        self.__this = phpy.Object(f'Imagick', _files)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def count(self, _mode=0):
        return self.__this.call(f"count", _mode)

    def getPixelIterator(self):
        return self.__this.call(f"getPixelIterator", )

    def getPixelRegionIterator(self, _x, _y, _columns, _rows):
        return self.__this.call(f"getPixelRegionIterator", _x, _y, _columns, _rows)

    def readImage(self, _filename):
        return self.__this.call(f"readImage", _filename)

    def readImages(self, _filenames):
        return self.__this.call(f"readImages", _filenames)

    def readImageBlob(self, _image, _filename=None):
        return self.__this.call(f"readImageBlob", _image, _filename)

    def setImageFormat(self, _format):
        return self.__this.call(f"setImageFormat", _format)

    def scaleImage(self, _columns, _rows, _bestfit=False, _legacy=False):
        return self.__this.call(f"scaleImage", _columns, _rows, _bestfit, _legacy)

    def writeImage(self, _filename=None):
        return self.__this.call(f"writeImage", _filename)

    def writeImages(self, _filename, _adjoin):
        return self.__this.call(f"writeImages", _filename, _adjoin)

    def blurImage(self, _radius, _sigma, _channel=134217727):
        return self.__this.call(f"blurImage", _radius, _sigma, _channel)

    def thumbnailImage(self, _columns, _rows, _bestfit=False, _fill=False, _legacy=False):
        return self.__this.call(f"thumbnailImage", _columns, _rows, _bestfit, _fill, _legacy)

    def cropThumbnailImage(self, _width, _height, _legacy=False):
        return self.__this.call(f"cropThumbnailImage", _width, _height, _legacy)

    def getImageFilename(self):
        return self.__this.call(f"getImageFilename", )

    def setImageFilename(self, _filename):
        return self.__this.call(f"setImageFilename", _filename)

    def getImageFormat(self):
        return self.__this.call(f"getImageFormat", )

    def getImageMimeType(self):
        return self.__this.call(f"getImageMimeType", )

    def removeImage(self):
        return self.__this.call(f"removeImage", )

    def destroy(self):
        return self.__this.call(f"destroy", )

    def clear(self):
        return self.__this.call(f"clear", )

    def clone(self):
        return self.__this.call(f"clone", )

    def getImageSize(self):
        return self.__this.call(f"getImageSize", )

    def getImageBlob(self):
        return self.__this.call(f"getImageBlob", )

    def getImagesBlob(self):
        return self.__this.call(f"getImagesBlob", )

    def setFirstIterator(self):
        return self.__this.call(f"setFirstIterator", )

    def setLastIterator(self):
        return self.__this.call(f"setLastIterator", )

    def resetIterator(self):
        return self.__this.call(f"resetIterator", )

    def previousImage(self):
        return self.__this.call(f"previousImage", )

    def nextImage(self):
        return self.__this.call(f"nextImage", )

    def hasPreviousImage(self):
        return self.__this.call(f"hasPreviousImage", )

    def hasNextImage(self):
        return self.__this.call(f"hasNextImage", )

    def setImageIndex(self, _index):
        return self.__this.call(f"setImageIndex", _index)

    def getImageIndex(self):
        return self.__this.call(f"getImageIndex", )

    def commentImage(self, _comment):
        return self.__this.call(f"commentImage", _comment)

    def cropImage(self, _width, _height, _x, _y):
        return self.__this.call(f"cropImage", _width, _height, _x, _y)

    def labelImage(self, _label):
        return self.__this.call(f"labelImage", _label)

    def getImageGeometry(self):
        return self.__this.call(f"getImageGeometry", )

    def drawImage(self, _drawing):
        return self.__this.call(f"drawImage", _drawing)

    def setImageCompressionQuality(self, _quality):
        return self.__this.call(f"setImageCompressionQuality", _quality)

    def getImageCompressionQuality(self):
        return self.__this.call(f"getImageCompressionQuality", )

    def setImageCompression(self, _compression):
        return self.__this.call(f"setImageCompression", _compression)

    def getImageCompression(self):
        return self.__this.call(f"getImageCompression", )

    def annotateImage(self, _settings, _x, _y, _angle, _text):
        return self.__this.call(f"annotateImage", _settings, _x, _y, _angle, _text)

    def compositeImage(self, _composite_image, _composite, _x, _y, _channel=134217727):
        return self.__this.call(f"compositeImage", _composite_image, _composite, _x, _y, _channel)

    def modulateImage(self, _brightness, _saturation, _hue):
        return self.__this.call(f"modulateImage", _brightness, _saturation, _hue)

    def getImageColors(self):
        return self.__this.call(f"getImageColors", )

    def montageImage(self, _settings, _tile_geometry, _thumbnail_geometry, _monatgemode, _frame):
        return self.__this.call(f"montageImage", _settings, _tile_geometry, _thumbnail_geometry, _monatgemode, _frame)

    def identifyImage(self, _append_raw_output=False):
        return self.__this.call(f"identifyImage", _append_raw_output)

    def thresholdImage(self, _threshold, _channel=134217727):
        return self.__this.call(f"thresholdImage", _threshold, _channel)

    def adaptiveThresholdImage(self, _width, _height, _offset):
        return self.__this.call(f"adaptiveThresholdImage", _width, _height, _offset)

    def blackThresholdImage(self, _threshold_color):
        return self.__this.call(f"blackThresholdImage", _threshold_color)

    def whiteThresholdImage(self, _threshold_color):
        return self.__this.call(f"whiteThresholdImage", _threshold_color)

    def appendImages(self, _stack):
        return self.__this.call(f"appendImages", _stack)

    def charcoalImage(self, _radius, _sigma):
        return self.__this.call(f"charcoalImage", _radius, _sigma)

    def normalizeImage(self, _channel=134217727):
        return self.__this.call(f"normalizeImage", _channel)

    def oilPaintImage(self, _radius):
        return self.__this.call(f"oilPaintImage", _radius)

    def posterizeImage(self, _levels, _dither):
        return self.__this.call(f"posterizeImage", _levels, _dither)

    def raiseImage(self, _width, _height, _x, _y, _raise):
        return self.__this.call(f"raiseImage", _width, _height, _x, _y, _raise)

    def resampleImage(self, _x_resolution, _y_resolution, _filter, _blur):
        return self.__this.call(f"resampleImage", _x_resolution, _y_resolution, _filter, _blur)

    def resizeImage(self, _columns, _rows, _filter, _blur, _bestfit=False, _legacy=False):
        return self.__this.call(f"resizeImage", _columns, _rows, _filter, _blur, _bestfit, _legacy)

    def rollImage(self, _x, _y):
        return self.__this.call(f"rollImage", _x, _y)

    def rotateImage(self, _background_color, _degrees):
        return self.__this.call(f"rotateImage", _background_color, _degrees)

    def sampleImage(self, _columns, _rows):
        return self.__this.call(f"sampleImage", _columns, _rows)

    def solarizeImage(self, _threshold):
        return self.__this.call(f"solarizeImage", _threshold)

    def shadowImage(self, _opacity, _sigma, _x, _y):
        return self.__this.call(f"shadowImage", _opacity, _sigma, _x, _y)

    def setImageBackgroundColor(self, _background_color):
        return self.__this.call(f"setImageBackgroundColor", _background_color)

    def setImageChannelMask(self, _channel):
        return self.__this.call(f"setImageChannelMask", _channel)

    def setImageCompose(self, _compose):
        return self.__this.call(f"setImageCompose", _compose)

    def setImageDelay(self, _delay):
        return self.__this.call(f"setImageDelay", _delay)

    def setImageDepth(self, _depth):
        return self.__this.call(f"setImageDepth", _depth)

    def setImageGamma(self, _gamma):
        return self.__this.call(f"setImageGamma", _gamma)

    def setImageIterations(self, _iterations):
        return self.__this.call(f"setImageIterations", _iterations)

    def setImageMatteColor(self, _matte_color):
        return self.__this.call(f"setImageMatteColor", _matte_color)

    def setImagePage(self, _width, _height, _x, _y):
        return self.__this.call(f"setImagePage", _width, _height, _x, _y)

    def setImageProgressMonitor(self, _filename):
        return self.__this.call(f"setImageProgressMonitor", _filename)

    def setProgressMonitor(self, _callback):
        return self.__this.call(f"setProgressMonitor", _callback)

    def setImageResolution(self, _x_resolution, _y_resolution):
        return self.__this.call(f"setImageResolution", _x_resolution, _y_resolution)

    def setImageScene(self, _scene):
        return self.__this.call(f"setImageScene", _scene)

    def setImageTicksPerSecond(self, _ticks_per_second):
        return self.__this.call(f"setImageTicksPerSecond", _ticks_per_second)

    def setImageType(self, _image_type):
        return self.__this.call(f"setImageType", _image_type)

    def setImageUnits(self, _units):
        return self.__this.call(f"setImageUnits", _units)

    def sharpenImage(self, _radius, _sigma, _channel=134217727):
        return self.__this.call(f"sharpenImage", _radius, _sigma, _channel)

    def shaveImage(self, _columns, _rows):
        return self.__this.call(f"shaveImage", _columns, _rows)

    def shearImage(self, _background_color, _x_shear, _y_shear):
        return self.__this.call(f"shearImage", _background_color, _x_shear, _y_shear)

    def spliceImage(self, _width, _height, _x, _y):
        return self.__this.call(f"spliceImage", _width, _height, _x, _y)

    def pingImage(self, _filename):
        return self.__this.call(f"pingImage", _filename)

    def readImageFile(self, _filehandle, _filename=None):
        return self.__this.call(f"readImageFile", _filehandle, _filename)

    def displayImage(self, _servername):
        return self.__this.call(f"displayImage", _servername)

    def displayImages(self, _servername):
        return self.__this.call(f"displayImages", _servername)

    def spreadImage(self, _radius):
        return self.__this.call(f"spreadImage", _radius)

    def swirlImage(self, _degrees):
        return self.__this.call(f"swirlImage", _degrees)

    def stripImage(self):
        return self.__this.call(f"stripImage", )

    def queryFormats(_pattern="*"):
        return phpy.call(f"Imagick::queryFormats", _pattern)

    def queryFonts(_pattern="*"):
        return phpy.call(f"Imagick::queryFonts", _pattern)

    def queryFontMetrics(self, _settings, _text, _multiline=None):
        return self.__this.call(f"queryFontMetrics", _settings, _text, _multiline)

    def steganoImage(self, _watermark, _offset):
        return self.__this.call(f"steganoImage", _watermark, _offset)

    def addNoiseImage(self, _noise, _channel=134217727):
        return self.__this.call(f"addNoiseImage", _noise, _channel)

    def addNoiseImageWithAttenuate(self, _noise, _attenuate, _channel=134217727):
        return self.__this.call(f"addNoiseImageWithAttenuate", _noise, _attenuate, _channel)

    def motionBlurImage(self, _radius, _sigma, _angle, _channel=134217727):
        return self.__this.call(f"motionBlurImage", _radius, _sigma, _angle, _channel)

    def morphImages(self, _number_frames):
        return self.__this.call(f"morphImages", _number_frames)

    def minifyImage(self):
        return self.__this.call(f"minifyImage", )

    def affineTransformImage(self, _settings):
        return self.__this.call(f"affineTransformImage", _settings)

    def averageImages(self):
        return self.__this.call(f"averageImages", )

    def borderImage(self, _border_color, _width, _height):
        return self.__this.call(f"borderImage", _border_color, _width, _height)

    def borderImageWithComposite(self, _border_color, _width, _height, _composite):
        return self.__this.call(f"borderImageWithComposite", _border_color, _width, _height, _composite)

    def calculateCrop(_original_width, _original_height, _desired_width, _desired_height, _legacy=False):
        return phpy.call(f"Imagick::calculateCrop", _original_width, _original_height, _desired_width, _desired_height, _legacy)

    def chopImage(self, _width, _height, _x, _y):
        return self.__this.call(f"chopImage", _width, _height, _x, _y)

    def clipImage(self):
        return self.__this.call(f"clipImage", )

    def clipPathImage(self, _pathname, _inside):
        return self.__this.call(f"clipPathImage", _pathname, _inside)

    def clipImagePath(self, _pathname, _inside):
        return self.__this.call(f"clipImagePath", _pathname, _inside)

    def coalesceImages(self):
        return self.__this.call(f"coalesceImages", )

    def colorizeImage(self, _colorize_color, _opacity_color, _legacy=False):
        return self.__this.call(f"colorizeImage", _colorize_color, _opacity_color, _legacy)

    def compareImageChannels(self, _reference, _channel, _metric):
        return self.__this.call(f"compareImageChannels", _reference, _channel, _metric)

    def compareImages(self, _reference, _metric):
        return self.__this.call(f"compareImages", _reference, _metric)

    def contrastImage(self, _sharpen):
        return self.__this.call(f"contrastImage", _sharpen)

    def combineImages(self, _colorspace):
        return self.__this.call(f"combineImages", _colorspace)

    def convolveImage(self, _kernel, _channel=134217727):
        return self.__this.call(f"convolveImage", _kernel, _channel)

    def cycleColormapImage(self, _displace):
        return self.__this.call(f"cycleColormapImage", _displace)

    def deconstructImages(self):
        return self.__this.call(f"deconstructImages", )

    def despeckleImage(self):
        return self.__this.call(f"despeckleImage", )

    def edgeImage(self, _radius):
        return self.__this.call(f"edgeImage", _radius)

    def embossImage(self, _radius, _sigma):
        return self.__this.call(f"embossImage", _radius, _sigma)

    def enhanceImage(self):
        return self.__this.call(f"enhanceImage", )

    def equalizeImage(self):
        return self.__this.call(f"equalizeImage", )

    def evaluateImage(self, _evaluate, _constant, _channel=134217727):
        return self.__this.call(f"evaluateImage", _evaluate, _constant, _channel)

    def evaluateImages(self, _evaluate):
        return self.__this.call(f"evaluateImages", _evaluate)

    def flattenImages(self):
        return self.__this.call(f"flattenImages", )

    def flipImage(self):
        return self.__this.call(f"flipImage", )

    def flopImage(self):
        return self.__this.call(f"flopImage", )

    def forwardFourierTransformImage(self, _magnitude):
        return self.__this.call(f"forwardFourierTransformImage", _magnitude)

    def frameImage(self, _matte_color, _width, _height, _inner_bevel, _outer_bevel):
        return self.__this.call(f"frameImage", _matte_color, _width, _height, _inner_bevel, _outer_bevel)

    def frameImageWithComposite(self, _matte_color, _width, _height, _inner_bevel, _outer_bevel, _composite):
        return self.__this.call(f"frameImageWithComposite", _matte_color, _width, _height, _inner_bevel, _outer_bevel, _composite)

    def fxImage(self, _expression, _channel=134217727):
        return self.__this.call(f"fxImage", _expression, _channel)

    def gammaImage(self, _gamma, _channel=134217727):
        return self.__this.call(f"gammaImage", _gamma, _channel)

    def gaussianBlurImage(self, _radius, _sigma, _channel=134217727):
        return self.__this.call(f"gaussianBlurImage", _radius, _sigma, _channel)

    def getImageBackgroundColor(self):
        return self.__this.call(f"getImageBackgroundColor", )

    def getImageBluePrimary(self):
        return self.__this.call(f"getImageBluePrimary", )

    def getImageBorderColor(self):
        return self.__this.call(f"getImageBorderColor", )

    def getImageChannelDepth(self, _channel):
        return self.__this.call(f"getImageChannelDepth", _channel)

    def getImageChannelDistortion(self, _reference, _channel, _metric):
        return self.__this.call(f"getImageChannelDistortion", _reference, _channel, _metric)

    def getImageChannelMean(self, _channel):
        return self.__this.call(f"getImageChannelMean", _channel)

    def getImageChannelStatistics(self):
        return self.__this.call(f"getImageChannelStatistics", )

    def getImageColormapColor(self, _index):
        return self.__this.call(f"getImageColormapColor", _index)

    def getImageColorspace(self):
        return self.__this.call(f"getImageColorspace", )

    def getImageCompose(self):
        return self.__this.call(f"getImageCompose", )

    def getImageDelay(self):
        return self.__this.call(f"getImageDelay", )

    def getImageDepth(self):
        return self.__this.call(f"getImageDepth", )

    def getImageDistortion(self, _reference, _metric):
        return self.__this.call(f"getImageDistortion", _reference, _metric)

    def getImageDispose(self):
        return self.__this.call(f"getImageDispose", )

    def getImageGamma(self):
        return self.__this.call(f"getImageGamma", )

    def getImageGreenPrimary(self):
        return self.__this.call(f"getImageGreenPrimary", )

    def getImageHeight(self):
        return self.__this.call(f"getImageHeight", )

    def getImageHistogram(self):
        return self.__this.call(f"getImageHistogram", )

    def getImageInterlaceScheme(self):
        return self.__this.call(f"getImageInterlaceScheme", )

    def getImageIterations(self):
        return self.__this.call(f"getImageIterations", )

    def getImagePage(self):
        return self.__this.call(f"getImagePage", )

    def getImagePixelColor(self, _x, _y):
        return self.__this.call(f"getImagePixelColor", _x, _y)

    def setImagePixelColor(self, _x, _y, _color):
        return self.__this.call(f"setImagePixelColor", _x, _y, _color)

    def getImageProfile(self, _name):
        return self.__this.call(f"getImageProfile", _name)

    def getImageRedPrimary(self):
        return self.__this.call(f"getImageRedPrimary", )

    def getImageRenderingIntent(self):
        return self.__this.call(f"getImageRenderingIntent", )

    def getImageResolution(self):
        return self.__this.call(f"getImageResolution", )

    def getImageScene(self):
        return self.__this.call(f"getImageScene", )

    def getImageSignature(self):
        return self.__this.call(f"getImageSignature", )

    def getImageTicksPerSecond(self):
        return self.__this.call(f"getImageTicksPerSecond", )

    def getImageType(self):
        return self.__this.call(f"getImageType", )

    def getImageUnits(self):
        return self.__this.call(f"getImageUnits", )

    def getImageVirtualPixelMethod(self):
        return self.__this.call(f"getImageVirtualPixelMethod", )

    def getImageWhitePoint(self):
        return self.__this.call(f"getImageWhitePoint", )

    def getImageWidth(self):
        return self.__this.call(f"getImageWidth", )

    def getNumberImages(self):
        return self.__this.call(f"getNumberImages", )

    def getImageTotalInkDensity(self):
        return self.__this.call(f"getImageTotalInkDensity", )

    def getImageRegion(self, _width, _height, _x, _y):
        return self.__this.call(f"getImageRegion", _width, _height, _x, _y)

    def implodeImage(self, _radius):
        return self.__this.call(f"implodeImage", _radius)

    def inverseFourierTransformImage(self, _complement, _magnitude):
        return self.__this.call(f"inverseFourierTransformImage", _complement, _magnitude)

    def levelImage(self, _black_point, _gamma, _white_point, _channel=134217727):
        return self.__this.call(f"levelImage", _black_point, _gamma, _white_point, _channel)

    def magnifyImage(self):
        return self.__this.call(f"magnifyImage", )

    def negateImage(self, _gray, _channel=134217727):
        return self.__this.call(f"negateImage", _gray, _channel)

    def previewImages(self, _preview):
        return self.__this.call(f"previewImages", _preview)

    def profileImage(self, _name, _profile):
        return self.__this.call(f"profileImage", _name, _profile)

    def quantizeImage(self, _number_colors, _colorspace, _tree_depth, _dither, _measure_error):
        return self.__this.call(f"quantizeImage", _number_colors, _colorspace, _tree_depth, _dither, _measure_error)

    def quantizeImages(self, _number_colors, _colorspace, _tree_depth, _dither, _measure_error):
        return self.__this.call(f"quantizeImages", _number_colors, _colorspace, _tree_depth, _dither, _measure_error)

    def removeImageProfile(self, _name):
        return self.__this.call(f"removeImageProfile", _name)

    def separateImageChannel(self, _channel):
        return self.__this.call(f"separateImageChannel", _channel)

    def sepiaToneImage(self, _threshold):
        return self.__this.call(f"sepiaToneImage", _threshold)

    def setImageBluePrimary(self, _x, _y):
        return self.__this.call(f"setImageBluePrimary", _x, _y)

    def setImageBorderColor(self, _border_color):
        return self.__this.call(f"setImageBorderColor", _border_color)

    def setImageChannelDepth(self, _channel, _depth):
        return self.__this.call(f"setImageChannelDepth", _channel, _depth)

    def setImageColormapColor(self, _index, _color):
        return self.__this.call(f"setImageColormapColor", _index, _color)

    def setImageColorspace(self, _colorspace):
        return self.__this.call(f"setImageColorspace", _colorspace)

    def setImageDispose(self, _dispose):
        return self.__this.call(f"setImageDispose", _dispose)

    def setImageExtent(self, _columns, _rows):
        return self.__this.call(f"setImageExtent", _columns, _rows)

    def setImageGreenPrimary(self, _x, _y):
        return self.__this.call(f"setImageGreenPrimary", _x, _y)

    def setImageInterlaceScheme(self, _interlace):
        return self.__this.call(f"setImageInterlaceScheme", _interlace)

    def setImageProfile(self, _name, _profile):
        return self.__this.call(f"setImageProfile", _name, _profile)

    def setImageRedPrimary(self, _x, _y):
        return self.__this.call(f"setImageRedPrimary", _x, _y)

    def setImageRenderingIntent(self, _rendering_intent):
        return self.__this.call(f"setImageRenderingIntent", _rendering_intent)

    def setImageVirtualPixelMethod(self, _method):
        return self.__this.call(f"setImageVirtualPixelMethod", _method)

    def setImageWhitePoint(self, _x, _y):
        return self.__this.call(f"setImageWhitePoint", _x, _y)

    def sigmoidalContrastImage(self, _sharpen, _alpha, _beta, _channel=134217727):
        return self.__this.call(f"sigmoidalContrastImage", _sharpen, _alpha, _beta, _channel)

    def stereoImage(self, _offset_image):
        return self.__this.call(f"stereoImage", _offset_image)

    def textureImage(self, _texture):
        return self.__this.call(f"textureImage", _texture)

    def tintImage(self, _tint_color, _opacity_color, _legacy=False):
        return self.__this.call(f"tintImage", _tint_color, _opacity_color, _legacy)

    def unsharpMaskImage(self, _radius, _sigma, _amount, _threshold, _channel=134217727):
        return self.__this.call(f"unsharpMaskImage", _radius, _sigma, _amount, _threshold, _channel)

    def getImage(self):
        return self.__this.call(f"getImage", )

    def addImage(self, _image):
        return self.__this.call(f"addImage", _image)

    def setImage(self, _image):
        return self.__this.call(f"setImage", _image)

    def newImage(self, _columns, _rows, _background_color, _format=None):
        return self.__this.call(f"newImage", _columns, _rows, _background_color, _format)

    def newPseudoImage(self, _columns, _rows, _pseudo_format):
        return self.__this.call(f"newPseudoImage", _columns, _rows, _pseudo_format)

    def getCompression(self):
        return self.__this.call(f"getCompression", )

    def getCompressionQuality(self):
        return self.__this.call(f"getCompressionQuality", )

    def getCopyright():
        return phpy.call(f"Imagick::getCopyright", )

    def getConfigureOptions(_pattern="*"):
        return phpy.call(f"Imagick::getConfigureOptions", _pattern)

    def getFeatures():
        return phpy.call(f"Imagick::getFeatures", )

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getFormat(self):
        return self.__this.call(f"getFormat", )

    def getHomeURL():
        return phpy.call(f"Imagick::getHomeURL", )

    def getInterlaceScheme(self):
        return self.__this.call(f"getInterlaceScheme", )

    def getOption(self, _key):
        return self.__this.call(f"getOption", _key)

    def getPackageName():
        return phpy.call(f"Imagick::getPackageName", )

    def getPage(self):
        return self.__this.call(f"getPage", )

    def getQuantum():
        return phpy.call(f"Imagick::getQuantum", )

    def getHdriEnabled():
        return phpy.call(f"Imagick::getHdriEnabled", )

    def getQuantumDepth():
        return phpy.call(f"Imagick::getQuantumDepth", )

    def getQuantumRange():
        return phpy.call(f"Imagick::getQuantumRange", )

    def getReleaseDate():
        return phpy.call(f"Imagick::getReleaseDate", )

    def getResource(_type):
        return phpy.call(f"Imagick::getResource", _type)

    def getResourceLimit(_type):
        return phpy.call(f"Imagick::getResourceLimit", _type)

    def getSamplingFactors(self):
        return self.__this.call(f"getSamplingFactors", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getVersion():
        return phpy.call(f"Imagick::getVersion", )

    def setBackgroundColor(self, _background_color):
        return self.__this.call(f"setBackgroundColor", _background_color)

    def setCompression(self, _compression):
        return self.__this.call(f"setCompression", _compression)

    def setCompressionQuality(self, _quality):
        return self.__this.call(f"setCompressionQuality", _quality)

    def setFilename(self, _filename):
        return self.__this.call(f"setFilename", _filename)

    def setFormat(self, _format):
        return self.__this.call(f"setFormat", _format)

    def setInterlaceScheme(self, _interlace):
        return self.__this.call(f"setInterlaceScheme", _interlace)

    def setOption(self, _key, _value):
        return self.__this.call(f"setOption", _key, _value)

    def setPage(self, _width, _height, _x, _y):
        return self.__this.call(f"setPage", _width, _height, _x, _y)

    def setResourceLimit(_type, _limit):
        return phpy.call(f"Imagick::setResourceLimit", _type, _limit)

    def setResolution(self, _x_resolution, _y_resolution):
        return self.__this.call(f"setResolution", _x_resolution, _y_resolution)

    def setSamplingFactors(self, _factors):
        return self.__this.call(f"setSamplingFactors", _factors)

    def setSize(self, _columns, _rows):
        return self.__this.call(f"setSize", _columns, _rows)

    def setType(self, _imgtype):
        return self.__this.call(f"setType", _imgtype)

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def current(self):
        return self.__this.call(f"current", )

    def brightnessContrastImage(self, _brightness, _contrast, _channel=134217727):
        return self.__this.call(f"brightnessContrastImage", _brightness, _contrast, _channel)

    def colorMatrixImage(self, _color_matrix):
        return self.__this.call(f"colorMatrixImage", _color_matrix)

    def selectiveBlurImage(self, _radius, _sigma, _threshold, _channel=134217727):
        return self.__this.call(f"selectiveBlurImage", _radius, _sigma, _threshold, _channel)

    def rotationalBlurImage(self, _angle, _channel=134217727):
        return self.__this.call(f"rotationalBlurImage", _angle, _channel)

    def statisticImage(self, _type, _width, _height, _channel=134217727):
        return self.__this.call(f"statisticImage", _type, _width, _height, _channel)

    def subimageMatch(self, _image, _offset=None, _similarity=None, _threshold=0, _metric=0):
        return self.__this.call(f"subimageMatch", _image, _offset, _similarity, _threshold, _metric)

    def similarityImage(self, _image, _offset=None, _similarity=None, _threshold=0, _metric=0):
        return self.__this.call(f"similarityImage", _image, _offset, _similarity, _threshold, _metric)

    def setRegistry(_key, _value):
        return phpy.call(f"Imagick::setRegistry", _key, _value)

    def getRegistry(_key):
        return phpy.call(f"Imagick::getRegistry", _key)

    def listRegistry():
        return phpy.call(f"Imagick::listRegistry", )

    def morphology(self, _morphology, _iterations, _kernel, _channel=134217727):
        return self.__this.call(f"morphology", _morphology, _iterations, _kernel, _channel)

    def setAntialias(self, _antialias):
        return self.__this.call(f"setAntialias", _antialias)

    def getAntialias(self):
        return self.__this.call(f"getAntialias", )

    def colorDecisionListImage(self, _color_correction_collection):
        return self.__this.call(f"colorDecisionListImage", _color_correction_collection)

    def optimizeImageTransparency(self):
        return self.__this.call(f"optimizeImageTransparency", )

    def autoGammaImage(self, _channel=134217727):
        return self.__this.call(f"autoGammaImage", _channel)

    def autoOrient(self):
        return self.__this.call(f"autoOrient", )

    def autoOrientate(self):
        return self.__this.call(f"autoOrientate", )

    def compositeImageGravity(self, _image, _composite_constant, _gravity):
        return self.__this.call(f"compositeImageGravity", _image, _composite_constant, _gravity)

    def localContrastImage(self, _radius, _strength):
        return self.__this.call(f"localContrastImage", _radius, _strength)

    def identifyImageType(self):
        return self.__this.call(f"identifyImageType", )

    def getImageMask(self, _pixelmask):
        return self.__this.call(f"getImageMask", _pixelmask)

    def setImageMask(self, _clip_mask, _pixelmask):
        return self.__this.call(f"setImageMask", _clip_mask, _pixelmask)

    def cannyEdgeImage(self, _radius, _sigma, _lower_percent, _upper_percent):
        return self.__this.call(f"cannyEdgeImage", _radius, _sigma, _lower_percent, _upper_percent)

    def setSeed(_seed):
        return phpy.call(f"Imagick::setSeed", _seed)

    def waveletDenoiseImage(self, _threshold, _softness):
        return self.__this.call(f"waveletDenoiseImage", _threshold, _softness)

    def meanShiftImage(self, _width, _height, _color_distance):
        return self.__this.call(f"meanShiftImage", _width, _height, _color_distance)

    def kmeansImage(self, _number_colors, _max_iterations, _tolerance):
        return self.__this.call(f"kmeansImage", _number_colors, _max_iterations, _tolerance)

    def rangeThresholdImage(self, _low_black, _low_white, _high_white, _high_black):
        return self.__this.call(f"rangeThresholdImage", _low_black, _low_white, _high_white, _high_black)

    def autoThresholdImage(self, _auto_threshold_method):
        return self.__this.call(f"autoThresholdImage", _auto_threshold_method)

    def bilateralBlurImage(self, _radius, _sigma, _intensity_sigma, _spatial_sigma):
        return self.__this.call(f"bilateralBlurImage", _radius, _sigma, _intensity_sigma, _spatial_sigma)

    def claheImage(self, _width, _height, _number_bins, _clip_limit):
        return self.__this.call(f"claheImage", _width, _height, _number_bins, _clip_limit)

    def channelFxImage(self, _expression):
        return self.__this.call(f"channelFxImage", _expression)

    def colorThresholdImage(self, _start_color, _stop_color):
        return self.__this.call(f"colorThresholdImage", _start_color, _stop_color)

    def complexImages(self, _complex_operator):
        return self.__this.call(f"complexImages", _complex_operator)

    def interpolativeResizeImage(self, _columns, _rows, _interpolate):
        return self.__this.call(f"interpolativeResizeImage", _columns, _rows, _interpolate)

    def levelImageColors(self, _black_color, _white_color, _invert):
        return self.__this.call(f"levelImageColors", _black_color, _white_color, _invert)

    def levelizeImage(self, _black_point, _gamma, _white_point):
        return self.__this.call(f"levelizeImage", _black_point, _gamma, _white_point)

    def orderedDitherImage(self, _dither_format):
        return self.__this.call(f"orderedDitherImage", _dither_format)

    def whiteBalanceImage(self):
        return self.__this.call(f"whiteBalanceImage", )


class ImagickDraw():


    def resetVectorGraphics(self):
        return self.__this.call(f"resetVectorGraphics", )

    def getTextKerning(self):
        return self.__this.call(f"getTextKerning", )

    def setTextKerning(self, _kerning):
        return self.__this.call(f"setTextKerning", _kerning)

    def getTextInterwordSpacing(self):
        return self.__this.call(f"getTextInterwordSpacing", )

    def setTextInterwordSpacing(self, _spacing):
        return self.__this.call(f"setTextInterwordSpacing", _spacing)

    def getTextInterlineSpacing(self):
        return self.__this.call(f"getTextInterlineSpacing", )

    def setTextInterlineSpacing(self, _spacing):
        return self.__this.call(f"setTextInterlineSpacing", _spacing)

    def __init__(self):
        self.__this = phpy.Object(f'ImagickDraw', )

    def setFillColor(self, _fill_color):
        return self.__this.call(f"setFillColor", _fill_color)

    def setFillAlpha(self, _alpha):
        return self.__this.call(f"setFillAlpha", _alpha)

    def setResolution(self, _resolution_x, _resolution_y):
        return self.__this.call(f"setResolution", _resolution_x, _resolution_y)

    def setStrokeColor(self, _color):
        return self.__this.call(f"setStrokeColor", _color)

    def setStrokeAlpha(self, _alpha):
        return self.__this.call(f"setStrokeAlpha", _alpha)

    def setStrokeWidth(self, _width):
        return self.__this.call(f"setStrokeWidth", _width)

    def clear(self):
        return self.__this.call(f"clear", )

    def circle(self, _origin_x, _origin_y, _perimeter_x, _perimeter_y):
        return self.__this.call(f"circle", _origin_x, _origin_y, _perimeter_x, _perimeter_y)

    def annotation(self, _x, _y, _text):
        return self.__this.call(f"annotation", _x, _y, _text)

    def setTextAntialias(self, _antialias):
        return self.__this.call(f"setTextAntialias", _antialias)

    def setTextEncoding(self, _encoding):
        return self.__this.call(f"setTextEncoding", _encoding)

    def setFont(self, _font_name):
        return self.__this.call(f"setFont", _font_name)

    def setFontFamily(self, _font_family):
        return self.__this.call(f"setFontFamily", _font_family)

    def setFontSize(self, _point_size):
        return self.__this.call(f"setFontSize", _point_size)

    def setFontStyle(self, _style):
        return self.__this.call(f"setFontStyle", _style)

    def setFontWeight(self, _weight):
        return self.__this.call(f"setFontWeight", _weight)

    def getFont(self):
        return self.__this.call(f"getFont", )

    def getFontFamily(self):
        return self.__this.call(f"getFontFamily", )

    def getFontSize(self):
        return self.__this.call(f"getFontSize", )

    def getFontStyle(self):
        return self.__this.call(f"getFontStyle", )

    def getFontWeight(self):
        return self.__this.call(f"getFontWeight", )

    def destroy(self):
        return self.__this.call(f"destroy", )

    def rectangle(self, _top_left_x, _top_left_y, _bottom_right_x, _bottom_right_y):
        return self.__this.call(f"rectangle", _top_left_x, _top_left_y, _bottom_right_x, _bottom_right_y)

    def roundRectangle(self, _top_left_x, _top_left_y, _bottom_right_x, _bottom_right_y, _rounding_x, _rounding_y):
        return self.__this.call(f"roundRectangle", _top_left_x, _top_left_y, _bottom_right_x, _bottom_right_y, _rounding_x, _rounding_y)

    def ellipse(self, _origin_x, _origin_y, _radius_x, _radius_y, _angle_start, _angle_end):
        return self.__this.call(f"ellipse", _origin_x, _origin_y, _radius_x, _radius_y, _angle_start, _angle_end)

    def skewX(self, _degrees):
        return self.__this.call(f"skewX", _degrees)

    def skewY(self, _degrees):
        return self.__this.call(f"skewY", _degrees)

    def translate(self, _x, _y):
        return self.__this.call(f"translate", _x, _y)

    def line(self, _start_x, _start_y, _end_x, _end_y):
        return self.__this.call(f"line", _start_x, _start_y, _end_x, _end_y)

    def arc(self, _start_x, _start_y, _end_x, _end_y, _start_angle, _end_angle):
        return self.__this.call(f"arc", _start_x, _start_y, _end_x, _end_y, _start_angle, _end_angle)

    def alpha(self, _x, _y, _paint):
        return self.__this.call(f"alpha", _x, _y, _paint)

    def polygon(self, _coordinates):
        return self.__this.call(f"polygon", _coordinates)

    def point(self, _x, _y):
        return self.__this.call(f"point", _x, _y)

    def getTextDecoration(self):
        return self.__this.call(f"getTextDecoration", )

    def getTextEncoding(self):
        return self.__this.call(f"getTextEncoding", )

    def getFontStretch(self):
        return self.__this.call(f"getFontStretch", )

    def setFontStretch(self, _stretch):
        return self.__this.call(f"setFontStretch", _stretch)

    def setStrokeAntialias(self, _enabled):
        return self.__this.call(f"setStrokeAntialias", _enabled)

    def setTextAlignment(self, _align):
        return self.__this.call(f"setTextAlignment", _align)

    def setTextDecoration(self, _decoration):
        return self.__this.call(f"setTextDecoration", _decoration)

    def setTextUnderColor(self, _under_color):
        return self.__this.call(f"setTextUnderColor", _under_color)

    def setViewbox(self, _left_x, _top_y, _right_x, _bottom_y):
        return self.__this.call(f"setViewbox", _left_x, _top_y, _right_x, _bottom_y)

    def clone(self):
        return self.__this.call(f"clone", )

    def affine(self, _affine):
        return self.__this.call(f"affine", _affine)

    def bezier(self, _coordinates):
        return self.__this.call(f"bezier", _coordinates)

    def composite(self, _composite, _x, _y, _width, _height, _image):
        return self.__this.call(f"composite", _composite, _x, _y, _width, _height, _image)

    def color(self, _x, _y, _paint):
        return self.__this.call(f"color", _x, _y, _paint)

    def comment(self, _comment):
        return self.__this.call(f"comment", _comment)

    def getClipPath(self):
        return self.__this.call(f"getClipPath", )

    def getClipRule(self):
        return self.__this.call(f"getClipRule", )

    def getClipUnits(self):
        return self.__this.call(f"getClipUnits", )

    def getFillColor(self):
        return self.__this.call(f"getFillColor", )

    def getFillOpacity(self):
        return self.__this.call(f"getFillOpacity", )

    def getFillRule(self):
        return self.__this.call(f"getFillRule", )

    def getGravity(self):
        return self.__this.call(f"getGravity", )

    def getStrokeAntialias(self):
        return self.__this.call(f"getStrokeAntialias", )

    def getStrokeColor(self):
        return self.__this.call(f"getStrokeColor", )

    def getStrokeDashArray(self):
        return self.__this.call(f"getStrokeDashArray", )

    def getStrokeDashOffset(self):
        return self.__this.call(f"getStrokeDashOffset", )

    def getStrokeLineCap(self):
        return self.__this.call(f"getStrokeLineCap", )

    def getStrokeLineJoin(self):
        return self.__this.call(f"getStrokeLineJoin", )

    def getStrokeMiterLimit(self):
        return self.__this.call(f"getStrokeMiterLimit", )

    def getStrokeOpacity(self):
        return self.__this.call(f"getStrokeOpacity", )

    def getStrokeWidth(self):
        return self.__this.call(f"getStrokeWidth", )

    def getTextAlignment(self):
        return self.__this.call(f"getTextAlignment", )

    def getTextAntialias(self):
        return self.__this.call(f"getTextAntialias", )

    def getVectorGraphics(self):
        return self.__this.call(f"getVectorGraphics", )

    def getTextUnderColor(self):
        return self.__this.call(f"getTextUnderColor", )

    def pathClose(self):
        return self.__this.call(f"pathClose", )

    def pathCurveToAbsolute(self, _x1, _y1, _x2, _y2, _x, _y):
        return self.__this.call(f"pathCurveToAbsolute", _x1, _y1, _x2, _y2, _x, _y)

    def pathCurveToRelative(self, _x1, _y1, _x2, _y2, _x, _y):
        return self.__this.call(f"pathCurveToRelative", _x1, _y1, _x2, _y2, _x, _y)

    def pathCurveToQuadraticBezierAbsolute(self, _x1, _y1, _x_end, _y):
        return self.__this.call(f"pathCurveToQuadraticBezierAbsolute", _x1, _y1, _x_end, _y)

    def pathCurveToQuadraticBezierRelative(self, _x1, _y1, _x_end, _y):
        return self.__this.call(f"pathCurveToQuadraticBezierRelative", _x1, _y1, _x_end, _y)

    def pathCurveToQuadraticBezierSmoothAbsolute(self, _x, _y):
        return self.__this.call(f"pathCurveToQuadraticBezierSmoothAbsolute", _x, _y)

    def pathCurveToQuadraticBezierSmoothRelative(self, _x, _y):
        return self.__this.call(f"pathCurveToQuadraticBezierSmoothRelative", _x, _y)

    def pathCurveToSmoothAbsolute(self, _x2, _y2, _x, _y):
        return self.__this.call(f"pathCurveToSmoothAbsolute", _x2, _y2, _x, _y)

    def pathCurveToSmoothRelative(self, _x2, _y2, _x, _y):
        return self.__this.call(f"pathCurveToSmoothRelative", _x2, _y2, _x, _y)

    def pathEllipticArcAbsolute(self, _rx, _ry, _x_axis_rotation, _large_arc, _sweep, _x, _y):
        return self.__this.call(f"pathEllipticArcAbsolute", _rx, _ry, _x_axis_rotation, _large_arc, _sweep, _x, _y)

    def pathEllipticArcRelative(self, _rx, _ry, _x_axis_rotation, _large_arc, _sweep, _x, _y):
        return self.__this.call(f"pathEllipticArcRelative", _rx, _ry, _x_axis_rotation, _large_arc, _sweep, _x, _y)

    def pathFinish(self):
        return self.__this.call(f"pathFinish", )

    def pathLineToAbsolute(self, _x, _y):
        return self.__this.call(f"pathLineToAbsolute", _x, _y)

    def pathLineToRelative(self, _x, _y):
        return self.__this.call(f"pathLineToRelative", _x, _y)

    def pathLineToHorizontalAbsolute(self, _x):
        return self.__this.call(f"pathLineToHorizontalAbsolute", _x)

    def pathLineToHorizontalRelative(self, _x):
        return self.__this.call(f"pathLineToHorizontalRelative", _x)

    def pathLineToVerticalAbsolute(self, _y):
        return self.__this.call(f"pathLineToVerticalAbsolute", _y)

    def pathLineToVerticalRelative(self, _y):
        return self.__this.call(f"pathLineToVerticalRelative", _y)

    def pathMoveToAbsolute(self, _x, _y):
        return self.__this.call(f"pathMoveToAbsolute", _x, _y)

    def pathMoveToRelative(self, _x, _y):
        return self.__this.call(f"pathMoveToRelative", _x, _y)

    def pathStart(self):
        return self.__this.call(f"pathStart", )

    def polyline(self, _coordinates):
        return self.__this.call(f"polyline", _coordinates)

    def popClipPath(self):
        return self.__this.call(f"popClipPath", )

    def popDefs(self):
        return self.__this.call(f"popDefs", )

    def popPattern(self):
        return self.__this.call(f"popPattern", )

    def pushClipPath(self, _clip_mask_id):
        return self.__this.call(f"pushClipPath", _clip_mask_id)

    def pushDefs(self):
        return self.__this.call(f"pushDefs", )

    def pushPattern(self, _pattern_id, _x, _y, _width, _height):
        return self.__this.call(f"pushPattern", _pattern_id, _x, _y, _width, _height)

    def render(self):
        return self.__this.call(f"render", )

    def rotate(self, _degrees):
        return self.__this.call(f"rotate", _degrees)

    def scale(self, _x, _y):
        return self.__this.call(f"scale", _x, _y)

    def setClipPath(self, _clip_mask):
        return self.__this.call(f"setClipPath", _clip_mask)

    def setClipRule(self, _fillrule):
        return self.__this.call(f"setClipRule", _fillrule)

    def setClipUnits(self, _pathunits):
        return self.__this.call(f"setClipUnits", _pathunits)

    def setFillOpacity(self, _opacity):
        return self.__this.call(f"setFillOpacity", _opacity)

    def setFillPatternUrl(self, _fill_url):
        return self.__this.call(f"setFillPatternUrl", _fill_url)

    def setFillRule(self, _fillrule):
        return self.__this.call(f"setFillRule", _fillrule)

    def setGravity(self, _gravity):
        return self.__this.call(f"setGravity", _gravity)

    def setStrokePatternUrl(self, _stroke_url):
        return self.__this.call(f"setStrokePatternUrl", _stroke_url)

    def setStrokeDashOffset(self, _dash_offset):
        return self.__this.call(f"setStrokeDashOffset", _dash_offset)

    def setStrokeLineCap(self, _linecap):
        return self.__this.call(f"setStrokeLineCap", _linecap)

    def setStrokeLineJoin(self, _linejoin):
        return self.__this.call(f"setStrokeLineJoin", _linejoin)

    def setStrokeMiterLimit(self, _miterlimit):
        return self.__this.call(f"setStrokeMiterLimit", _miterlimit)

    def setStrokeOpacity(self, _opacity):
        return self.__this.call(f"setStrokeOpacity", _opacity)

    def setVectorGraphics(self, _xml):
        return self.__this.call(f"setVectorGraphics", _xml)

    def pop(self):
        return self.__this.call(f"pop", )

    def push(self):
        return self.__this.call(f"push", )

    def setStrokeDashArray(self, _dashes):
        return self.__this.call(f"setStrokeDashArray", _dashes)

    def getOpacity(self):
        return self.__this.call(f"getOpacity", )

    def setOpacity(self, _opacity):
        return self.__this.call(f"setOpacity", _opacity)

    def getFontResolution(self):
        return self.__this.call(f"getFontResolution", )

    def setFontResolution(self, _x, _y):
        return self.__this.call(f"setFontResolution", _x, _y)

    def getBorderColor(self):
        return self.__this.call(f"getBorderColor", )

    def setBorderColor(self, _color):
        return self.__this.call(f"setBorderColor", _color)

    def setDensity(self, _density):
        return self.__this.call(f"setDensity", _density)

    def getDensity(self):
        return self.__this.call(f"getDensity", )

    def getTextDirection(self):
        return self.__this.call(f"getTextDirection", )

    def setTextDirection(self, _direction):
        return self.__this.call(f"setTextDirection", _direction)


class ImagickPixelIterator():


    def __init__(self, _imagick):
        self.__this = phpy.Object(f'ImagickPixelIterator', _imagick)

    def clear(self):
        return self.__this.call(f"clear", )

    def getPixelIterator(_imagick):
        return phpy.call(f"ImagickPixelIterator::getPixelIterator", _imagick)

    def getPixelRegionIterator(_imagick, _x, _y, _columns, _rows):
        return phpy.call(f"ImagickPixelIterator::getPixelRegionIterator", _imagick, _x, _y, _columns, _rows)

    def destroy(self):
        return self.__this.call(f"destroy", )

    def getCurrentIteratorRow(self):
        return self.__this.call(f"getCurrentIteratorRow", )

    def getIteratorRow(self):
        return self.__this.call(f"getIteratorRow", )

    def getNextIteratorRow(self):
        return self.__this.call(f"getNextIteratorRow", )

    def getPreviousIteratorRow(self):
        return self.__this.call(f"getPreviousIteratorRow", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def current(self):
        return self.__this.call(f"current", )

    def newPixelIterator(self, _imagick):
        return self.__this.call(f"newPixelIterator", _imagick)

    def newPixelRegionIterator(self, _imagick, _x, _y, _columns, _rows):
        return self.__this.call(f"newPixelRegionIterator", _imagick, _x, _y, _columns, _rows)

    def resetIterator(self):
        return self.__this.call(f"resetIterator", )

    def setIteratorFirstRow(self):
        return self.__this.call(f"setIteratorFirstRow", )

    def setIteratorLastRow(self):
        return self.__this.call(f"setIteratorLastRow", )

    def setIteratorRow(self, _row):
        return self.__this.call(f"setIteratorRow", _row)

    def syncIterator(self):
        return self.__this.call(f"syncIterator", )

    def valid(self):
        return self.__this.call(f"valid", )


class ImagickPixel():


    def __init__(self, _color=None):
        self.__this = phpy.Object(f'ImagickPixel', _color)

    def clear(self):
        return self.__this.call(f"clear", )

    def destroy(self):
        return self.__this.call(f"destroy", )

    def getColor(self, _normalized=0):
        return self.__this.call(f"getColor", _normalized)

    def getColorAsString(self):
        return self.__this.call(f"getColorAsString", )

    def getColorCount(self):
        return self.__this.call(f"getColorCount", )

    def getColorQuantum(self):
        return self.__this.call(f"getColorQuantum", )

    def getColorValue(self, _color):
        return self.__this.call(f"getColorValue", _color)

    def getColorValueQuantum(self, _color):
        return self.__this.call(f"getColorValueQuantum", _color)

    def getHSL(self):
        return self.__this.call(f"getHSL", )

    def getIndex(self):
        return self.__this.call(f"getIndex", )

    def isPixelSimilar(self, _color, _fuzz):
        return self.__this.call(f"isPixelSimilar", _color, _fuzz)

    def isPixelSimilarQuantum(self, _color, _fuzz_quantum_range_scaled_by_square_root_of_three):
        return self.__this.call(f"isPixelSimilarQuantum", _color, _fuzz_quantum_range_scaled_by_square_root_of_three)

    def isSimilar(self, _color, _fuzz_quantum_range_scaled_by_square_root_of_three):
        return self.__this.call(f"isSimilar", _color, _fuzz_quantum_range_scaled_by_square_root_of_three)

    def setColor(self, _color):
        return self.__this.call(f"setColor", _color)

    def setColorCount(self, _color_count):
        return self.__this.call(f"setColorCount", _color_count)

    def setColorValue(self, _color, _value):
        return self.__this.call(f"setColorValue", _color, _value)

    def setColorValueQuantum(self, _color, _value):
        return self.__this.call(f"setColorValueQuantum", _color, _value)

    def setHSL(self, _hue, _saturation, _luminosity):
        return self.__this.call(f"setHSL", _hue, _saturation, _luminosity)

    def setIndex(self, _index):
        return self.__this.call(f"setIndex", _index)

    def setColorFromPixel(self, _pixel):
        return self.__this.call(f"setColorFromPixel", _pixel)


class ImagickKernel():


    def addKernel(self, _kernel):
        return self.__this.call(f"addKernel", _kernel)

    def addUnityKernel(self, _scale):
        return self.__this.call(f"addUnityKernel", _scale)

    def fromBuiltin(_kernel, _shape):
        return phpy.call(f"ImagickKernel::fromBuiltin", _kernel, _shape)

    def fromMatrix(_matrix, _origin):
        return phpy.call(f"ImagickKernel::fromMatrix", _matrix, _origin)

    def getMatrix(self):
        return self.__this.call(f"getMatrix", )

    def scale(self, _scale, _normalize_kernel=None):
        return self.__this.call(f"scale", _scale, _normalize_kernel)

    def separate(self):
        return self.__this.call(f"separate", )

    def __init__(self):
        self.__this = phpy.Object(f'ImagickKernel')


