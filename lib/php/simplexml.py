import phpy



def simplexml_load_file(_filename, _class_name="SimpleXMLElement", _options=0, _namespace_or_prefix="", _is_prefix=False):
    return phpy.call('simplexml_load_file', _filename, _class_name, _options, _namespace_or_prefix, _is_prefix)


def simplexml_load_string(_data, _class_name="SimpleXMLElement", _options=0, _namespace_or_prefix="", _is_prefix=False):
    return phpy.call('simplexml_load_string', _data, _class_name, _options, _namespace_or_prefix, _is_prefix)


def simplexml_import_dom(_node, _class_name="SimpleXMLElement"):
    return phpy.call('simplexml_import_dom', _node, _class_name)




def SimpleXMLElement():

    def xpath(self, _expression):
        return self.__this.call(f"xpath", _expression)

    def registerXPathNamespace(self, _prefix, _namespace):
        return self.__this.call(f"registerXPathNamespace", _prefix, _namespace)

    def asXML(self, _filename=None):
        return self.__this.call(f"asXML", _filename)

    def saveXML(self, _filename=None):
        return self.__this.call(f"saveXML", _filename)

    def getNamespaces(self, _recursive=False):
        return self.__this.call(f"getNamespaces", _recursive)

    def getDocNamespaces(self, _recursive=False, _from_root=True):
        return self.__this.call(f"getDocNamespaces", _recursive, _from_root)

    def children(self, _namespace_or_prefix=None, _is_prefix=False):
        return self.__this.call(f"children", _namespace_or_prefix, _is_prefix)

    def attributes(self, _namespace_or_prefix=None, _is_prefix=False):
        return self.__this.call(f"attributes", _namespace_or_prefix, _is_prefix)

    def __init__(self, _data, _options=0, _data_is_u_r_l=False, _namespace_or_prefix="", _is_prefix=False):
        self.__this = phpy.Object(f'SimpleXMLElement', _data, _options, _data_is_u_r_l, _namespace_or_prefix, _is_prefix)

    def addChild(self, _qualified_name, _value=None, _namespace=None):
        return self.__this.call(f"addChild", _qualified_name, _value, _namespace)

    def addAttribute(self, _qualified_name, _value, _namespace=None):
        return self.__this.call(f"addAttribute", _qualified_name, _value, _namespace)

    def getName(self):
        return self.__this.call(f"getName", )

    def __toString(self):
        return self.__this.call(f"__toString", )

    def count(self):
        return self.__this.call(f"count", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )


def SimpleXMLIterator():

    def xpath(self, _expression):
        return self.__this.call(f"xpath", _expression)

    def registerXPathNamespace(self, _prefix, _namespace):
        return self.__this.call(f"registerXPathNamespace", _prefix, _namespace)

    def asXML(self, _filename=None):
        return self.__this.call(f"asXML", _filename)

    def saveXML(self, _filename=None):
        return self.__this.call(f"saveXML", _filename)

    def getNamespaces(self, _recursive=False):
        return self.__this.call(f"getNamespaces", _recursive)

    def getDocNamespaces(self, _recursive=False, _from_root=True):
        return self.__this.call(f"getDocNamespaces", _recursive, _from_root)

    def children(self, _namespace_or_prefix=None, _is_prefix=False):
        return self.__this.call(f"children", _namespace_or_prefix, _is_prefix)

    def attributes(self, _namespace_or_prefix=None, _is_prefix=False):
        return self.__this.call(f"attributes", _namespace_or_prefix, _is_prefix)

    def __init__(self, _data, _options=0, _data_is_u_r_l=False, _namespace_or_prefix="", _is_prefix=False):
        self.__this = phpy.Object(f'SimpleXMLIterator', _data, _options, _data_is_u_r_l, _namespace_or_prefix, _is_prefix)

    def addChild(self, _qualified_name, _value=None, _namespace=None):
        return self.__this.call(f"addChild", _qualified_name, _value, _namespace)

    def addAttribute(self, _qualified_name, _value, _namespace=None):
        return self.__this.call(f"addAttribute", _qualified_name, _value, _namespace)

    def getName(self):
        return self.__this.call(f"getName", )

    def __toString(self):
        return self.__this.call(f"__toString", )

    def count(self):
        return self.__this.call(f"count", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )


