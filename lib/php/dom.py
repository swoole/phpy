import phpy

XML_ELEMENT_NODE = 1
XML_ATTRIBUTE_NODE = 2
XML_TEXT_NODE = 3
XML_CDATA_SECTION_NODE = 4
XML_ENTITY_REF_NODE = 5
XML_ENTITY_NODE = 6
XML_PI_NODE = 7
XML_COMMENT_NODE = 8
XML_DOCUMENT_NODE = 9
XML_DOCUMENT_TYPE_NODE = 10
XML_DOCUMENT_FRAG_NODE = 11
XML_NOTATION_NODE = 12
XML_HTML_DOCUMENT_NODE = 13
XML_DTD_NODE = 14
XML_ELEMENT_DECL_NODE = 15
XML_ATTRIBUTE_DECL_NODE = 16
XML_ENTITY_DECL_NODE = 17
XML_NAMESPACE_DECL_NODE = 18
XML_LOCAL_NAMESPACE = 18
XML_ATTRIBUTE_CDATA = 1
XML_ATTRIBUTE_ID = 2
XML_ATTRIBUTE_IDREF = 3
XML_ATTRIBUTE_IDREFS = 4
XML_ATTRIBUTE_ENTITY = 6
XML_ATTRIBUTE_NMTOKEN = 7
XML_ATTRIBUTE_NMTOKENS = 8
XML_ATTRIBUTE_ENUMERATION = 9
XML_ATTRIBUTE_NOTATION = 10
PHP_ERR = 0
INDEX_SIZE_ERR = 1
DOMSTRING_SIZE_ERR = 2
HIERARCHY_REQUEST_ERR = 3
WRONG_DOCUMENT_ERR = 4
INVALID_CHARACTER_ERR = 5
NO_DATA_ALLOWED_ERR = 6
NO_MODIFICATION_ALLOWED_ERR = 7
NOT_FOUND_ERR = 8
NOT_SUPPORTED_ERR = 9
INUSE_ATTRIBUTE_ERR = 10
INVALID_STATE_ERR = 11
SYNTAX_ERR = 12
INVALID_MODIFICATION_ERR = 13
NAMESPACE_ERR = 14
INVALID_ACCESS_ERR = 15
VALIDATION_ERR = 16


def import_simplexml(_node):
    return phpy.call('dom_import_simplexml', _node)




class DOMException():

    code = 0

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'DOMException', _message, _code, _previous)

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


class DOMParentNode():


    def append(self, _nodes=None):
        return self.__this.call(f"append", _nodes)

    def prepend(self, _nodes=None):
        return self.__this.call(f"prepend", _nodes)

    def __init__(self):
        self.__this = phpy.Object(f'DOMParentNode')


class DOMChildNode():


    def remove(self):
        return self.__this.call(f"remove", )

    def before(self, _nodes=None):
        return self.__this.call(f"before", _nodes)

    def after(self, _nodes=None):
        return self.__this.call(f"after", _nodes)

    def replaceWith(self, _nodes=None):
        return self.__this.call(f"replaceWith", _nodes)

    def __init__(self):
        self.__this = phpy.Object(f'DOMChildNode')


class DOMImplementation():


    def getFeature(self, _feature, _version):
        return self.__this.call(f"getFeature", _feature, _version)

    def hasFeature(self, _feature, _version):
        return self.__this.call(f"hasFeature", _feature, _version)

    def createDocumentType(self, _qualified_name, _public_id="", _system_id=""):
        return self.__this.call(f"createDocumentType", _qualified_name, _public_id, _system_id)

    def createDocument(self, _namespace=None, _qualified_name="", _doctype=None):
        return self.__this.call(f"createDocument", _namespace, _qualified_name, _doctype)

    def __init__(self):
        self.__this = phpy.Object(f'DOMImplementation')


class DOMNode():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)

    def __init__(self):
        self.__this = phpy.Object(f'DOMNode')


class DOMNameSpaceNode():

    nodeName = None
    nodeValue = None
    nodeType = None
    prefix = None
    localName = None
    namespaceURI = None
    ownerDocument = None
    parentNode = None

    def __init__(self):
        self.__this = phpy.Object(f'DOMNameSpaceNode')


class DOMDocumentFragment():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    firstElementChild = None
    lastElementChild = None
    childElementCount = None

    def __init__(self):
        self.__this = phpy.Object(f'DOMDocumentFragment', )

    def appendXML(self, _data):
        return self.__this.call(f"appendXML", _data)

    def append(self, _nodes=None):
        return self.__this.call(f"append", _nodes)

    def prepend(self, _nodes=None):
        return self.__this.call(f"prepend", _nodes)

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)


class DOMDocument():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    doctype = None
    implementation = None
    documentElement = None
    actualEncoding = None
    encoding = None
    xmlEncoding = None
    standalone = None
    xmlStandalone = None
    version = None
    xmlVersion = None
    strictErrorChecking = None
    documentURI = None
    config = None
    formatOutput = None
    validateOnParse = None
    resolveExternals = None
    preserveWhiteSpace = None
    recover = None
    substituteEntities = None
    firstElementChild = None
    lastElementChild = None
    childElementCount = None

    def __init__(self, _version="1.0", _encoding=""):
        self.__this = phpy.Object(f'DOMDocument', _version, _encoding)

    def createAttribute(self, _local_name):
        return self.__this.call(f"createAttribute", _local_name)

    def createAttributeNS(self, _namespace, _qualified_name):
        return self.__this.call(f"createAttributeNS", _namespace, _qualified_name)

    def createCDATASection(self, _data):
        return self.__this.call(f"createCDATASection", _data)

    def createComment(self, _data):
        return self.__this.call(f"createComment", _data)

    def createDocumentFragment(self):
        return self.__this.call(f"createDocumentFragment", )

    def createElement(self, _local_name, _value=""):
        return self.__this.call(f"createElement", _local_name, _value)

    def createElementNS(self, _namespace, _qualified_name, _value=""):
        return self.__this.call(f"createElementNS", _namespace, _qualified_name, _value)

    def createEntityReference(self, _name):
        return self.__this.call(f"createEntityReference", _name)

    def createProcessingInstruction(self, _target, _data=""):
        return self.__this.call(f"createProcessingInstruction", _target, _data)

    def createTextNode(self, _data):
        return self.__this.call(f"createTextNode", _data)

    def getElementById(self, _element_id):
        return self.__this.call(f"getElementById", _element_id)

    def getElementsByTagName(self, _qualified_name):
        return self.__this.call(f"getElementsByTagName", _qualified_name)

    def getElementsByTagNameNS(self, _namespace, _local_name):
        return self.__this.call(f"getElementsByTagNameNS", _namespace, _local_name)

    def importNode(self, _node, _deep=False):
        return self.__this.call(f"importNode", _node, _deep)

    def load(self, _filename, _options=0):
        return self.__this.call(f"load", _filename, _options)

    def loadXML(self, _source, _options=0):
        return self.__this.call(f"loadXML", _source, _options)

    def normalizeDocument(self):
        return self.__this.call(f"normalizeDocument", )

    def registerNodeClass(self, _base_class, _extended_class):
        return self.__this.call(f"registerNodeClass", _base_class, _extended_class)

    def save(self, _filename, _options=0):
        return self.__this.call(f"save", _filename, _options)

    def loadHTML(self, _source, _options=0):
        return self.__this.call(f"loadHTML", _source, _options)

    def loadHTMLFile(self, _filename, _options=0):
        return self.__this.call(f"loadHTMLFile", _filename, _options)

    def saveHTML(self, _node=None):
        return self.__this.call(f"saveHTML", _node)

    def saveHTMLFile(self, _filename):
        return self.__this.call(f"saveHTMLFile", _filename)

    def saveXML(self, _node=None, _options=0):
        return self.__this.call(f"saveXML", _node, _options)

    def schemaValidate(self, _filename, _flags=0):
        return self.__this.call(f"schemaValidate", _filename, _flags)

    def schemaValidateSource(self, _source, _flags=0):
        return self.__this.call(f"schemaValidateSource", _source, _flags)

    def relaxNGValidate(self, _filename):
        return self.__this.call(f"relaxNGValidate", _filename)

    def relaxNGValidateSource(self, _source):
        return self.__this.call(f"relaxNGValidateSource", _source)

    def validate(self):
        return self.__this.call(f"validate", )

    def xinclude(self, _options=0):
        return self.__this.call(f"xinclude", _options)

    def adoptNode(self, _node):
        return self.__this.call(f"adoptNode", _node)

    def append(self, _nodes=None):
        return self.__this.call(f"append", _nodes)

    def prepend(self, _nodes=None):
        return self.__this.call(f"prepend", _nodes)

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)


class DOMNodeList():

    length = None

    def count(self):
        return self.__this.call(f"count", )

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def item(self, _index):
        return self.__this.call(f"item", _index)

    def __init__(self):
        self.__this = phpy.Object(f'DOMNodeList')


class DOMNamedNodeMap():

    length = None

    def getNamedItem(self, _qualified_name):
        return self.__this.call(f"getNamedItem", _qualified_name)

    def getNamedItemNS(self, _namespace, _local_name):
        return self.__this.call(f"getNamedItemNS", _namespace, _local_name)

    def item(self, _index):
        return self.__this.call(f"item", _index)

    def count(self):
        return self.__this.call(f"count", )

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def __init__(self):
        self.__this = phpy.Object(f'DOMNamedNodeMap')


class DOMCharacterData():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    data = None
    length = None
    previousElementSibling = None
    nextElementSibling = None

    def appendData(self, _data):
        return self.__this.call(f"appendData", _data)

    def substringData(self, _offset, _count):
        return self.__this.call(f"substringData", _offset, _count)

    def insertData(self, _offset, _data):
        return self.__this.call(f"insertData", _offset, _data)

    def deleteData(self, _offset, _count):
        return self.__this.call(f"deleteData", _offset, _count)

    def replaceData(self, _offset, _count, _data):
        return self.__this.call(f"replaceData", _offset, _count, _data)

    def replaceWith(self, _nodes=None):
        return self.__this.call(f"replaceWith", _nodes)

    def remove(self):
        return self.__this.call(f"remove", )

    def before(self, _nodes=None):
        return self.__this.call(f"before", _nodes)

    def after(self, _nodes=None):
        return self.__this.call(f"after", _nodes)

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)

    def __init__(self):
        self.__this = phpy.Object(f'DOMCharacterData')


class DOMAttr():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    name = None
    specified = True
    value = None
    ownerElement = None
    schemaTypeInfo = None

    def __init__(self, _name, _value=""):
        self.__this = phpy.Object(f'DOMAttr', _name, _value)

    def isId(self):
        return self.__this.call(f"isId", )

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)


class DOMElement():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    tagName = None
    schemaTypeInfo = None
    firstElementChild = None
    lastElementChild = None
    childElementCount = None
    previousElementSibling = None
    nextElementSibling = None

    def __init__(self, _qualified_name, _value=None, _namespace=""):
        self.__this = phpy.Object(f'DOMElement', _qualified_name, _value, _namespace)

    def getAttribute(self, _qualified_name):
        return self.__this.call(f"getAttribute", _qualified_name)

    def getAttributeNS(self, _namespace, _local_name):
        return self.__this.call(f"getAttributeNS", _namespace, _local_name)

    def getAttributeNode(self, _qualified_name):
        return self.__this.call(f"getAttributeNode", _qualified_name)

    def getAttributeNodeNS(self, _namespace, _local_name):
        return self.__this.call(f"getAttributeNodeNS", _namespace, _local_name)

    def getElementsByTagName(self, _qualified_name):
        return self.__this.call(f"getElementsByTagName", _qualified_name)

    def getElementsByTagNameNS(self, _namespace, _local_name):
        return self.__this.call(f"getElementsByTagNameNS", _namespace, _local_name)

    def hasAttribute(self, _qualified_name):
        return self.__this.call(f"hasAttribute", _qualified_name)

    def hasAttributeNS(self, _namespace, _local_name):
        return self.__this.call(f"hasAttributeNS", _namespace, _local_name)

    def removeAttribute(self, _qualified_name):
        return self.__this.call(f"removeAttribute", _qualified_name)

    def removeAttributeNS(self, _namespace, _local_name):
        return self.__this.call(f"removeAttributeNS", _namespace, _local_name)

    def removeAttributeNode(self, _attr):
        return self.__this.call(f"removeAttributeNode", _attr)

    def setAttribute(self, _qualified_name, _value):
        return self.__this.call(f"setAttribute", _qualified_name, _value)

    def setAttributeNS(self, _namespace, _qualified_name, _value):
        return self.__this.call(f"setAttributeNS", _namespace, _qualified_name, _value)

    def setAttributeNode(self, _attr):
        return self.__this.call(f"setAttributeNode", _attr)

    def setAttributeNodeNS(self, _attr):
        return self.__this.call(f"setAttributeNodeNS", _attr)

    def setIdAttribute(self, _qualified_name, _is_id):
        return self.__this.call(f"setIdAttribute", _qualified_name, _is_id)

    def setIdAttributeNS(self, _namespace, _qualified_name, _is_id):
        return self.__this.call(f"setIdAttributeNS", _namespace, _qualified_name, _is_id)

    def setIdAttributeNode(self, _attr, _is_id):
        return self.__this.call(f"setIdAttributeNode", _attr, _is_id)

    def remove(self):
        return self.__this.call(f"remove", )

    def before(self, _nodes=None):
        return self.__this.call(f"before", _nodes)

    def after(self, _nodes=None):
        return self.__this.call(f"after", _nodes)

    def replaceWith(self, _nodes=None):
        return self.__this.call(f"replaceWith", _nodes)

    def append(self, _nodes=None):
        return self.__this.call(f"append", _nodes)

    def prepend(self, _nodes=None):
        return self.__this.call(f"prepend", _nodes)

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)


class DOMText():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    data = None
    length = None
    previousElementSibling = None
    nextElementSibling = None
    wholeText = None

    def __init__(self, _data=""):
        self.__this = phpy.Object(f'DOMText', _data)

    def isWhitespaceInElementContent(self):
        return self.__this.call(f"isWhitespaceInElementContent", )

    def isElementContentWhitespace(self):
        return self.__this.call(f"isElementContentWhitespace", )

    def splitText(self, _offset):
        return self.__this.call(f"splitText", _offset)

    def appendData(self, _data):
        return self.__this.call(f"appendData", _data)

    def substringData(self, _offset, _count):
        return self.__this.call(f"substringData", _offset, _count)

    def insertData(self, _offset, _data):
        return self.__this.call(f"insertData", _offset, _data)

    def deleteData(self, _offset, _count):
        return self.__this.call(f"deleteData", _offset, _count)

    def replaceData(self, _offset, _count, _data):
        return self.__this.call(f"replaceData", _offset, _count, _data)

    def replaceWith(self, _nodes=None):
        return self.__this.call(f"replaceWith", _nodes)

    def remove(self):
        return self.__this.call(f"remove", )

    def before(self, _nodes=None):
        return self.__this.call(f"before", _nodes)

    def after(self, _nodes=None):
        return self.__this.call(f"after", _nodes)

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)


class DOMComment():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    data = None
    length = None
    previousElementSibling = None
    nextElementSibling = None

    def __init__(self, _data=""):
        self.__this = phpy.Object(f'DOMComment', _data)

    def appendData(self, _data):
        return self.__this.call(f"appendData", _data)

    def substringData(self, _offset, _count):
        return self.__this.call(f"substringData", _offset, _count)

    def insertData(self, _offset, _data):
        return self.__this.call(f"insertData", _offset, _data)

    def deleteData(self, _offset, _count):
        return self.__this.call(f"deleteData", _offset, _count)

    def replaceData(self, _offset, _count, _data):
        return self.__this.call(f"replaceData", _offset, _count, _data)

    def replaceWith(self, _nodes=None):
        return self.__this.call(f"replaceWith", _nodes)

    def remove(self):
        return self.__this.call(f"remove", )

    def before(self, _nodes=None):
        return self.__this.call(f"before", _nodes)

    def after(self, _nodes=None):
        return self.__this.call(f"after", _nodes)

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)


class DOMCdataSection():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    data = None
    length = None
    previousElementSibling = None
    nextElementSibling = None
    wholeText = None

    def __init__(self, _data):
        self.__this = phpy.Object(f'DOMCdataSection', _data)

    def isWhitespaceInElementContent(self):
        return self.__this.call(f"isWhitespaceInElementContent", )

    def isElementContentWhitespace(self):
        return self.__this.call(f"isElementContentWhitespace", )

    def splitText(self, _offset):
        return self.__this.call(f"splitText", _offset)

    def appendData(self, _data):
        return self.__this.call(f"appendData", _data)

    def substringData(self, _offset, _count):
        return self.__this.call(f"substringData", _offset, _count)

    def insertData(self, _offset, _data):
        return self.__this.call(f"insertData", _offset, _data)

    def deleteData(self, _offset, _count):
        return self.__this.call(f"deleteData", _offset, _count)

    def replaceData(self, _offset, _count, _data):
        return self.__this.call(f"replaceData", _offset, _count, _data)

    def replaceWith(self, _nodes=None):
        return self.__this.call(f"replaceWith", _nodes)

    def remove(self):
        return self.__this.call(f"remove", )

    def before(self, _nodes=None):
        return self.__this.call(f"before", _nodes)

    def after(self, _nodes=None):
        return self.__this.call(f"after", _nodes)

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)


class DOMDocumentType():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    name = None
    entities = None
    notations = None
    publicId = None
    systemId = None
    internalSubset = None

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)

    def __init__(self):
        self.__this = phpy.Object(f'DOMDocumentType')


class DOMNotation():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    publicId = None
    systemId = None

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)

    def __init__(self):
        self.__this = phpy.Object(f'DOMNotation')


class DOMEntity():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    publicId = None
    systemId = None
    notationName = None
    actualEncoding = None
    encoding = None
    version = None

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)

    def __init__(self):
        self.__this = phpy.Object(f'DOMEntity')


class DOMEntityReference():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None

    def __init__(self, _name):
        self.__this = phpy.Object(f'DOMEntityReference', _name)

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)


class DOMProcessingInstruction():

    nodeName = None
    nodeValue = None
    nodeType = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None
    baseURI = None
    textContent = None
    target = None
    data = None

    def __init__(self, _name, _value=""):
        self.__this = phpy.Object(f'DOMProcessingInstruction', _name, _value)

    def appendChild(self, _node):
        return self.__this.call(f"appendChild", _node)

    def C14N(self, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14N", _exclusive, _with_comments, _xpath, _ns_prefixes)

    def C14NFile(self, _uri, _exclusive=False, _with_comments=False, _xpath=None, _ns_prefixes=None):
        return self.__this.call(f"C14NFile", _uri, _exclusive, _with_comments, _xpath, _ns_prefixes)

    def cloneNode(self, _deep=False):
        return self.__this.call(f"cloneNode", _deep)

    def getLineNo(self):
        return self.__this.call(f"getLineNo", )

    def getNodePath(self):
        return self.__this.call(f"getNodePath", )

    def hasAttributes(self):
        return self.__this.call(f"hasAttributes", )

    def hasChildNodes(self):
        return self.__this.call(f"hasChildNodes", )

    def insertBefore(self, _node, _child=None):
        return self.__this.call(f"insertBefore", _node, _child)

    def isDefaultNamespace(self, _namespace):
        return self.__this.call(f"isDefaultNamespace", _namespace)

    def isSameNode(self, _other_node):
        return self.__this.call(f"isSameNode", _other_node)

    def isSupported(self, _feature, _version):
        return self.__this.call(f"isSupported", _feature, _version)

    def lookupNamespaceURI(self, _prefix):
        return self.__this.call(f"lookupNamespaceURI", _prefix)

    def lookupPrefix(self, _namespace):
        return self.__this.call(f"lookupPrefix", _namespace)

    def normalize(self):
        return self.__this.call(f"normalize", )

    def removeChild(self, _child):
        return self.__this.call(f"removeChild", _child)

    def replaceChild(self, _node, _child):
        return self.__this.call(f"replaceChild", _node, _child)


class DOMXPath():

    document = None
    registerNodeNamespaces = None

    def __init__(self, _document, _register_node_n_s=True):
        self.__this = phpy.Object(f'DOMXPath', _document, _register_node_n_s)

    def evaluate(self, _expression, _context_node=None, _register_node_n_s=True):
        return self.__this.call(f"evaluate", _expression, _context_node, _register_node_n_s)

    def query(self, _expression, _context_node=None, _register_node_n_s=True):
        return self.__this.call(f"query", _expression, _context_node, _register_node_n_s)

    def registerNamespace(self, _prefix, _namespace):
        return self.__this.call(f"registerNamespace", _prefix, _namespace)

    def registerPhpFunctions(self, _restrict=None):
        return self.__this.call(f"registerPhpFunctions", _restrict)


