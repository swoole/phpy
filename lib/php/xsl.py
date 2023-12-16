import phpy

CLONE_AUTO = 0
CLONE_NEVER = -1
CLONE_ALWAYS = 1
SECPREF_NONE = 0
SECPREF_READ_FILE = 2
SECPREF_WRITE_FILE = 4
SECPREF_CREATE_DIRECTORY = 8
SECPREF_READ_NETWORK = 16
SECPREF_WRITE_NETWORK = 32
SECPREF_DEFAULT = 44
LIBXSLT_VERSION = 10134
LIBXSLT_DOTTED_VERSION = "1.1.34"
LIBEXSLT_VERSION = 820
LIBEXSLT_DOTTED_VERSION = "1.1.34"




class XSLTProcessor():

    def importStylesheet(self, _stylesheet):
        return self.__this.call(f"importStylesheet", _stylesheet)

    def transformToDoc(self, _document, _return_class=None):
        return self.__this.call(f"transformToDoc", _document, _return_class)

    def transformToUri(self, _document, _uri):
        return self.__this.call(f"transformToUri", _document, _uri)

    def transformToXml(self, _document):
        return self.__this.call(f"transformToXml", _document)

    def setParameter(self, _namespace, _name, _value=None):
        return self.__this.call(f"setParameter", _namespace, _name, _value)

    def getParameter(self, _namespace, _name):
        return self.__this.call(f"getParameter", _namespace, _name)

    def removeParameter(self, _namespace, _name):
        return self.__this.call(f"removeParameter", _namespace, _name)

    def hasExsltSupport(self):
        return self.__this.call(f"hasExsltSupport", )

    def registerPHPFunctions(self, _functions=None):
        return self.__this.call(f"registerPHPFunctions", _functions)

    def setProfiling(self, _filename):
        return self.__this.call(f"setProfiling", _filename)

    def setSecurityPrefs(self, _preferences):
        return self.__this.call(f"setSecurityPrefs", _preferences)

    def getSecurityPrefs(self):
        return self.__this.call(f"getSecurityPrefs", )

    def __init__(self):
        self.__this = phpy.Object(f'XSLTProcessor')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

