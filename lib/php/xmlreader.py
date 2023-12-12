import phpy





def XMLReader():
    NONE = 0
    ELEMENT = 1
    ATTRIBUTE = 2
    TEXT = 3
    CDATA = 4
    ENTITY_REF = 5
    ENTITY = 6
    PI = 7
    COMMENT = 8
    DOC = 9
    DOC_TYPE = 10
    DOC_FRAGMENT = 11
    NOTATION = 12
    WHITESPACE = 13
    SIGNIFICANT_WHITESPACE = 14
    END_ELEMENT = 15
    END_ENTITY = 16
    XML_DECLARATION = 17
    LOADDTD = 1
    DEFAULTATTRS = 2
    VALIDATE = 3
    SUBST_ENTITIES = 4

    def close(self):
        return self.__this.call(f"close", )

    def getAttribute(self, _name):
        return self.__this.call(f"getAttribute", _name)

    def getAttributeNo(self, _index):
        return self.__this.call(f"getAttributeNo", _index)

    def getAttributeNs(self, _name, _namespace):
        return self.__this.call(f"getAttributeNs", _name, _namespace)

    def getParserProperty(self, _property):
        return self.__this.call(f"getParserProperty", _property)

    def isValid(self):
        return self.__this.call(f"isValid", )

    def lookupNamespace(self, _prefix):
        return self.__this.call(f"lookupNamespace", _prefix)

    def moveToAttribute(self, _name):
        return self.__this.call(f"moveToAttribute", _name)

    def moveToAttributeNo(self, _index):
        return self.__this.call(f"moveToAttributeNo", _index)

    def moveToAttributeNs(self, _name, _namespace):
        return self.__this.call(f"moveToAttributeNs", _name, _namespace)

    def moveToElement(self):
        return self.__this.call(f"moveToElement", )

    def moveToFirstAttribute(self):
        return self.__this.call(f"moveToFirstAttribute", )

    def moveToNextAttribute(self):
        return self.__this.call(f"moveToNextAttribute", )

    def read(self):
        return self.__this.call(f"read", )

    def next(self, _name=None):
        return self.__this.call(f"next", _name)

    def open(_uri, _encoding=None, _flags=0):
        return phpy.call(f"XMLReader::open", _uri, _encoding, _flags)

    def readInnerXml(self):
        return self.__this.call(f"readInnerXml", )

    def readOuterXml(self):
        return self.__this.call(f"readOuterXml", )

    def readString(self):
        return self.__this.call(f"readString", )

    def setSchema(self, _filename):
        return self.__this.call(f"setSchema", _filename)

    def setParserProperty(self, _property, _value):
        return self.__this.call(f"setParserProperty", _property, _value)

    def setRelaxNGSchema(self, _filename):
        return self.__this.call(f"setRelaxNGSchema", _filename)

    def setRelaxNGSchemaSource(self, _source):
        return self.__this.call(f"setRelaxNGSchemaSource", _source)

    def XML(_source, _encoding=None, _flags=0):
        return phpy.call(f"XMLReader::XML", _source, _encoding, _flags)

    def expand(self, _base_node=None):
        return self.__this.call(f"expand", _base_node)


