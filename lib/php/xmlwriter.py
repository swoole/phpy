import phpy



def open_uri(_uri):
    return phpy.call('xmlwriter_open_uri', _uri)


def open_memory():
    return phpy.call('xmlwriter_open_memory', )


def set_indent(_writer, _enable):
    return phpy.call('xmlwriter_set_indent', _writer, _enable)


def set_indent_string(_writer, _indentation):
    return phpy.call('xmlwriter_set_indent_string', _writer, _indentation)


def start_comment(_writer):
    return phpy.call('xmlwriter_start_comment', _writer)


def end_comment(_writer):
    return phpy.call('xmlwriter_end_comment', _writer)


def start_attribute(_writer, _name):
    return phpy.call('xmlwriter_start_attribute', _writer, _name)


def end_attribute(_writer):
    return phpy.call('xmlwriter_end_attribute', _writer)


def write_attribute(_writer, _name, _value):
    return phpy.call('xmlwriter_write_attribute', _writer, _name, _value)


def start_attribute_ns(_writer, _prefix, _name, _namespace):
    return phpy.call('xmlwriter_start_attribute_ns', _writer, _prefix, _name, _namespace)


def write_attribute_ns(_writer, _prefix, _name, _namespace, _value):
    return phpy.call('xmlwriter_write_attribute_ns', _writer, _prefix, _name, _namespace, _value)


def start_element(_writer, _name):
    return phpy.call('xmlwriter_start_element', _writer, _name)


def end_element(_writer):
    return phpy.call('xmlwriter_end_element', _writer)


def full_end_element(_writer):
    return phpy.call('xmlwriter_full_end_element', _writer)


def start_element_ns(_writer, _prefix, _name, _namespace):
    return phpy.call('xmlwriter_start_element_ns', _writer, _prefix, _name, _namespace)


def write_element(_writer, _name, _content=None):
    return phpy.call('xmlwriter_write_element', _writer, _name, _content)


def write_element_ns(_writer, _prefix, _name, _namespace, _content=None):
    return phpy.call('xmlwriter_write_element_ns', _writer, _prefix, _name, _namespace, _content)


def start_pi(_writer, _target):
    return phpy.call('xmlwriter_start_pi', _writer, _target)


def end_pi(_writer):
    return phpy.call('xmlwriter_end_pi', _writer)


def write_pi(_writer, _target, _content):
    return phpy.call('xmlwriter_write_pi', _writer, _target, _content)


def start_cdata(_writer):
    return phpy.call('xmlwriter_start_cdata', _writer)


def end_cdata(_writer):
    return phpy.call('xmlwriter_end_cdata', _writer)


def write_cdata(_writer, _content):
    return phpy.call('xmlwriter_write_cdata', _writer, _content)


def text(_writer, _content):
    return phpy.call('xmlwriter_text', _writer, _content)


def write_raw(_writer, _content):
    return phpy.call('xmlwriter_write_raw', _writer, _content)


def start_document(_writer, _version="1.0", _encoding=None, _standalone=None):
    return phpy.call('xmlwriter_start_document', _writer, _version, _encoding, _standalone)


def end_document(_writer):
    return phpy.call('xmlwriter_end_document', _writer)


def write_comment(_writer, _content):
    return phpy.call('xmlwriter_write_comment', _writer, _content)


def start_dtd(_writer, _qualified_name, _public_id=None, _system_id=None):
    return phpy.call('xmlwriter_start_dtd', _writer, _qualified_name, _public_id, _system_id)


def end_dtd(_writer):
    return phpy.call('xmlwriter_end_dtd', _writer)


def write_dtd(_writer, _name, _public_id=None, _system_id=None, _content=None):
    return phpy.call('xmlwriter_write_dtd', _writer, _name, _public_id, _system_id, _content)


def start_dtd_element(_writer, _qualified_name):
    return phpy.call('xmlwriter_start_dtd_element', _writer, _qualified_name)


def end_dtd_element(_writer):
    return phpy.call('xmlwriter_end_dtd_element', _writer)


def write_dtd_element(_writer, _name, _content):
    return phpy.call('xmlwriter_write_dtd_element', _writer, _name, _content)


def start_dtd_attlist(_writer, _name):
    return phpy.call('xmlwriter_start_dtd_attlist', _writer, _name)


def end_dtd_attlist(_writer):
    return phpy.call('xmlwriter_end_dtd_attlist', _writer)


def write_dtd_attlist(_writer, _name, _content):
    return phpy.call('xmlwriter_write_dtd_attlist', _writer, _name, _content)


def start_dtd_entity(_writer, _name, _is_param):
    return phpy.call('xmlwriter_start_dtd_entity', _writer, _name, _is_param)


def end_dtd_entity(_writer):
    return phpy.call('xmlwriter_end_dtd_entity', _writer)


def write_dtd_entity(_writer, _name, _content, _is_param=False, _public_id=None, _system_id=None, _notation_data=None):
    return phpy.call('xmlwriter_write_dtd_entity', _writer, _name, _content, _is_param, _public_id, _system_id, _notation_data)


def output_memory(_writer, _flush=True):
    return phpy.call('xmlwriter_output_memory', _writer, _flush)


def flush(_writer, _empty=True):
    return phpy.call('xmlwriter_flush', _writer, _empty)




class XMLWriter():

    def openUri(self, _uri):
        return self.__this.call(f"openUri", _uri)

    def openMemory(self):
        return self.__this.call(f"openMemory", )

    def setIndent(self, _enable):
        return self.__this.call(f"setIndent", _enable)

    def setIndentString(self, _indentation):
        return self.__this.call(f"setIndentString", _indentation)

    def startComment(self):
        return self.__this.call(f"startComment", )

    def endComment(self):
        return self.__this.call(f"endComment", )

    def startAttribute(self, _name):
        return self.__this.call(f"startAttribute", _name)

    def endAttribute(self):
        return self.__this.call(f"endAttribute", )

    def writeAttribute(self, _name, _value):
        return self.__this.call(f"writeAttribute", _name, _value)

    def startAttributeNs(self, _prefix, _name, _namespace):
        return self.__this.call(f"startAttributeNs", _prefix, _name, _namespace)

    def writeAttributeNs(self, _prefix, _name, _namespace, _value):
        return self.__this.call(f"writeAttributeNs", _prefix, _name, _namespace, _value)

    def startElement(self, _name):
        return self.__this.call(f"startElement", _name)

    def endElement(self):
        return self.__this.call(f"endElement", )

    def fullEndElement(self):
        return self.__this.call(f"fullEndElement", )

    def startElementNs(self, _prefix, _name, _namespace):
        return self.__this.call(f"startElementNs", _prefix, _name, _namespace)

    def writeElement(self, _name, _content=None):
        return self.__this.call(f"writeElement", _name, _content)

    def writeElementNs(self, _prefix, _name, _namespace, _content=None):
        return self.__this.call(f"writeElementNs", _prefix, _name, _namespace, _content)

    def startPi(self, _target):
        return self.__this.call(f"startPi", _target)

    def endPi(self):
        return self.__this.call(f"endPi", )

    def writePi(self, _target, _content):
        return self.__this.call(f"writePi", _target, _content)

    def startCdata(self):
        return self.__this.call(f"startCdata", )

    def endCdata(self):
        return self.__this.call(f"endCdata", )

    def writeCdata(self, _content):
        return self.__this.call(f"writeCdata", _content)

    def text(self, _content):
        return self.__this.call(f"text", _content)

    def writeRaw(self, _content):
        return self.__this.call(f"writeRaw", _content)

    def startDocument(self, _version="1.0", _encoding=None, _standalone=None):
        return self.__this.call(f"startDocument", _version, _encoding, _standalone)

    def endDocument(self):
        return self.__this.call(f"endDocument", )

    def writeComment(self, _content):
        return self.__this.call(f"writeComment", _content)

    def startDtd(self, _qualified_name, _public_id=None, _system_id=None):
        return self.__this.call(f"startDtd", _qualified_name, _public_id, _system_id)

    def endDtd(self):
        return self.__this.call(f"endDtd", )

    def writeDtd(self, _name, _public_id=None, _system_id=None, _content=None):
        return self.__this.call(f"writeDtd", _name, _public_id, _system_id, _content)

    def startDtdElement(self, _qualified_name):
        return self.__this.call(f"startDtdElement", _qualified_name)

    def endDtdElement(self):
        return self.__this.call(f"endDtdElement", )

    def writeDtdElement(self, _name, _content):
        return self.__this.call(f"writeDtdElement", _name, _content)

    def startDtdAttlist(self, _name):
        return self.__this.call(f"startDtdAttlist", _name)

    def endDtdAttlist(self):
        return self.__this.call(f"endDtdAttlist", )

    def writeDtdAttlist(self, _name, _content):
        return self.__this.call(f"writeDtdAttlist", _name, _content)

    def startDtdEntity(self, _name, _is_param):
        return self.__this.call(f"startDtdEntity", _name, _is_param)

    def endDtdEntity(self):
        return self.__this.call(f"endDtdEntity", )

    def writeDtdEntity(self, _name, _content, _is_param=False, _public_id=None, _system_id=None, _notation_data=None):
        return self.__this.call(f"writeDtdEntity", _name, _content, _is_param, _public_id, _system_id, _notation_data)

    def outputMemory(self, _flush=True):
        return self.__this.call(f"outputMemory", _flush)

    def flush(self, _empty=True):
        return self.__this.call(f"flush", _empty)

    def __init__(self):
        self.__this = phpy.Object(f'XMLWriter')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

