import phpy

1_1 = 1
1_2 = 2
PERSISTENCE_SESSION = 1
PERSISTENCE_REQUEST = 2
FUNCTIONS_ALL = 999
ENCODED = 1
LITERAL = 2
RPC = 1
DOCUMENT = 2
ACTOR_NEXT = 1
ACTOR_NONE = 2
ACTOR_UNLIMATERECEIVER = 3
COMPRESSION_ACCEPT = 32
COMPRESSION_GZIP = 0
COMPRESSION_DEFLATE = 16
AUTHENTICATION_BASIC = 0
AUTHENTICATION_DIGEST = 1
UNKNOWN_TYPE = 999998
XSD_STRING = 101
XSD_BOOLEAN = 102
XSD_DECIMAL = 103
XSD_FLOAT = 104
XSD_DOUBLE = 105
XSD_DURATION = 106
XSD_DATETIME = 107
XSD_TIME = 108
XSD_DATE = 109
XSD_GYEARMONTH = 110
XSD_GYEAR = 111
XSD_GMONTHDAY = 112
XSD_GDAY = 113
XSD_GMONTH = 114
XSD_HEXBINARY = 115
XSD_BASE64BINARY = 116
XSD_ANYURI = 117
XSD_QNAME = 118
XSD_NOTATION = 119
XSD_NORMALIZEDSTRING = 120
XSD_TOKEN = 121
XSD_LANGUAGE = 122
XSD_NMTOKEN = 123
XSD_NAME = 124
XSD_NCNAME = 125
XSD_ID = 126
XSD_IDREF = 127
XSD_IDREFS = 128
XSD_ENTITY = 129
XSD_ENTITIES = 130
XSD_INTEGER = 131
XSD_NONPOSITIVEINTEGER = 132
XSD_NEGATIVEINTEGER = 133
XSD_LONG = 134
XSD_INT = 135
XSD_SHORT = 136
XSD_BYTE = 137
XSD_NONNEGATIVEINTEGER = 138
XSD_UNSIGNEDLONG = 139
XSD_UNSIGNEDINT = 140
XSD_UNSIGNEDSHORT = 141
XSD_UNSIGNEDBYTE = 142
XSD_POSITIVEINTEGER = 143
XSD_NMTOKENS = 144
XSD_ANYTYPE = 145
XSD_ANYXML = 147
APACHE_MAP = 200
ENC_OBJECT = 301
ENC_ARRAY = 300
XSD_1999_TIMEINSTANT = 401
XSD_NAMESPACE = "http://www.w3.org/2001/XMLSchema"
XSD_1999_NAMESPACE = "http://www.w3.org/1999/XMLSchema"
SINGLE_ELEMENT_ARRAYS = 1
WAIT_ONE_WAY_CALLS = 2
USE_XSI_ARRAY_TYPE = 4
WSDL_CACHE_NONE = 0
WSDL_CACHE_DISK = 1
WSDL_CACHE_MEMORY = 2
WSDL_CACHE_BOTH = 3
SSL_METHOD_TLS = 0
SSL_METHOD_SSLv2 = 1
SSL_METHOD_SSLv3 = 2
SSL_METHOD_SSLv23 = 3


def use_soap_error_handler(_enable=True):
    return phpy.call('use_soap_error_handler', _enable)


def is_soap_fault(_object):
    return phpy.call('is_soap_fault', _object)




def SoapClient():

    def __init__(self, _wsdl, _options=[]):
        self.__this = phpy.Object(f'SoapClient', _wsdl, _options)

    def __call(self, _name, _args):
        return self.__this.call(f"__call", _name, _args)

    def __soapCall(self, _name, _args, _options=None, _input_headers=None, _output_headers=None):
        return self.__this.call(f"__soapCall", _name, _args, _options, _input_headers, _output_headers)

    def __getFunctions(self):
        return self.__this.call(f"__getFunctions", )

    def __getTypes(self):
        return self.__this.call(f"__getTypes", )

    def __getLastRequest(self):
        return self.__this.call(f"__getLastRequest", )

    def __getLastResponse(self):
        return self.__this.call(f"__getLastResponse", )

    def __getLastRequestHeaders(self):
        return self.__this.call(f"__getLastRequestHeaders", )

    def __getLastResponseHeaders(self):
        return self.__this.call(f"__getLastResponseHeaders", )

    def __doRequest(self, _request, _location, _action, _version, _one_way=False):
        return self.__this.call(f"__doRequest", _request, _location, _action, _version, _one_way)

    def __setCookie(self, _name, _value=None):
        return self.__this.call(f"__setCookie", _name, _value)

    def __getCookies(self):
        return self.__this.call(f"__getCookies", )

    def __setSoapHeaders(self, _headers=None):
        return self.__this.call(f"__setSoapHeaders", _headers)

    def __setLocation(self, _location=None):
        return self.__this.call(f"__setLocation", _location)


def SoapVar():

    def __init__(self, _data, _encoding, _type_name=None, _type_namespace=None, _node_name=None, _node_namespace=None):
        self.__this = phpy.Object(f'SoapVar', _data, _encoding, _type_name, _type_namespace, _node_name, _node_namespace)


def SoapServer():

    def __init__(self, _wsdl, _options=[]):
        self.__this = phpy.Object(f'SoapServer', _wsdl, _options)

    def fault(self, _code, _string, _actor="", _details=None, _name=""):
        return self.__this.call(f"fault", _code, _string, _actor, _details, _name)

    def addSoapHeader(self, _header):
        return self.__this.call(f"addSoapHeader", _header)

    def setPersistence(self, _mode):
        return self.__this.call(f"setPersistence", _mode)

    def setClass(self, _class, _args=None):
        return self.__this.call(f"setClass", _class, _args)

    def setObject(self, _object):
        return self.__this.call(f"setObject", _object)

    def getFunctions(self):
        return self.__this.call(f"getFunctions", )

    def addFunction(self, _functions):
        return self.__this.call(f"addFunction", _functions)

    def handle(self, _request=None):
        return self.__this.call(f"handle", _request)


def SoapFault():

    def __init__(self, _code, _string, _actor=None, _details=None, _name=None, _header_fault=None):
        self.__this = phpy.Object(f'SoapFault', _code, _string, _actor, _details, _name, _header_fault)

    def __toString(self):
        return self.__this.call(f"__toString", )

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


def SoapParam():

    def __init__(self, _data, _name):
        self.__this = phpy.Object(f'SoapParam', _data, _name)


def SoapHeader():

    def __init__(self, _namespace, _name, _data=None, _must_understand=False, _actor=None):
        self.__this = phpy.Object(f'SoapHeader', _namespace, _name, _data, _must_understand, _actor)


