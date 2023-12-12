import phpy

VERSION = "1.14.2"
STABILITY = "stable"


def MongoDB\BSON\fromPHP(_value):
    return phpy.call('MongoDB\BSON\fromPHP', _value)


def MongoDB\BSON\toPHP(_bson, _typemap=None):
    return phpy.call('MongoDB\BSON\toPHP', _bson, _typemap)


def MongoDB\BSON\toJSON(_bson):
    return phpy.call('MongoDB\BSON\toJSON', _bson)


def MongoDB\BSON\toCanonicalExtendedJSON(_bson):
    return phpy.call('MongoDB\BSON\toCanonicalExtendedJSON', _bson)


def MongoDB\BSON\toRelaxedExtendedJSON(_bson):
    return phpy.call('MongoDB\BSON\toRelaxedExtendedJSON', _bson)


def MongoDB\BSON\fromJSON(_json):
    return phpy.call('MongoDB\BSON\fromJSON', _json)


def MongoDB\Driver\Monitoring\addSubscriber(_subscriber):
    return phpy.call('MongoDB\Driver\Monitoring\addSubscriber', _subscriber)


def MongoDB\Driver\Monitoring\removeSubscriber(_subscriber):
    return phpy.call('MongoDB\Driver\Monitoring\removeSubscriber', _subscriber)




def BSONSerializable():

    def bsonSerialize(self):
        return self.__this.call(f"bsonSerialize", )


def BSONUnserializable():

    def bsonUnserialize(self, _data):
        return self.__this.call(f"bsonUnserialize", _data)


def BSONBinaryInterface():

    def getData(self):
        return self.__this.call(f"getData", )

    def getType(self):
        return self.__this.call(f"getType", )

    def __toString(self):
        return self.__this.call(f"__toString", )


def BSONDecimal128Interface():

    def __toString(self):
        return self.__this.call(f"__toString", )


def BSONJavascriptInterface():

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getScope(self):
        return self.__this.call(f"getScope", )

    def __toString(self):
        return self.__this.call(f"__toString", )


def BSONObjectIdInterface():

    def getTimestamp(self):
        return self.__this.call(f"getTimestamp", )

    def __toString(self):
        return self.__this.call(f"__toString", )


def BSONRegexInterface():

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def getPattern(self):
        return self.__this.call(f"getPattern", )

    def __toString(self):
        return self.__this.call(f"__toString", )


def BSONTimestampInterface():

    def getIncrement(self):
        return self.__this.call(f"getIncrement", )

    def getTimestamp(self):
        return self.__this.call(f"getTimestamp", )

    def __toString(self):
        return self.__this.call(f"__toString", )


def BSONUTCDateTimeInterface():

    def toDateTime(self):
        return self.__this.call(f"toDateTime", )

    def __toString(self):
        return self.__this.call(f"__toString", )


def BSONBinary():
    TYPE_GENERIC = 0
    TYPE_FUNCTION = 1
    TYPE_OLD_BINARY = 2
    TYPE_OLD_UUID = 3
    TYPE_UUID = 4
    TYPE_MD5 = 5
    TYPE_ENCRYPTED = 6
    TYPE_COLUMN = 7
    TYPE_USER_DEFINED = 128

    def __init__(self, _data, _type):
        self.__this = phpy.Object(f'MongoDB\\BSON\\Binary', _data, _type)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\BSON\\Binary::__set_state", _properties)

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)

    def getData(self):
        return self.__this.call(f"getData", )

    def getType(self):
        return self.__this.call(f"getType", )


def BSONDBPointer():

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def BSONDecimal128():

    def __init__(self, _value):
        self.__this = phpy.Object(f'MongoDB\\BSON\\Decimal128', _value)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\BSON\\Decimal128::__set_state", _properties)

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def BSONInt64():

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def BSONJavascript():

    def __init__(self, _javascript, _scope=None):
        self.__this = phpy.Object(f'MongoDB\\BSON\\Javascript', _javascript, _scope)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\BSON\\Javascript::__set_state", _properties)

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getScope(self):
        return self.__this.call(f"getScope", )


def BSONMaxKey():

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\BSON\\MaxKey::__set_state", _properties)

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def BSONMinKey():

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\BSON\\MinKey::__set_state", _properties)

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def BSONObjectId():

    def __init__(self, _id=None):
        self.__this = phpy.Object(f'MongoDB\\BSON\\ObjectId', _id)

    def getTimestamp(self):
        return self.__this.call(f"getTimestamp", )

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\BSON\\ObjectId::__set_state", _properties)

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def BSONPersistable():

    def bsonUnserialize(self, _data):
        return self.__this.call(f"bsonUnserialize", _data)

    def bsonSerialize(self):
        return self.__this.call(f"bsonSerialize", )


def BSONRegex():

    def __init__(self, _pattern, _flags=None):
        self.__this = phpy.Object(f'MongoDB\\BSON\\Regex', _pattern, _flags)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\BSON\\Regex::__set_state", _properties)

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)

    def getPattern(self):
        return self.__this.call(f"getPattern", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )


def BSONSymbol():

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def BSONTimestamp():

    def __init__(self, _increment, _timestamp):
        self.__this = phpy.Object(f'MongoDB\\BSON\\Timestamp', _increment, _timestamp)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\BSON\\Timestamp::__set_state", _properties)

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)

    def getIncrement(self):
        return self.__this.call(f"getIncrement", )

    def getTimestamp(self):
        return self.__this.call(f"getTimestamp", )


def BSONUndefined():

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def BSONUTCDateTime():

    def __init__(self, _milliseconds=None):
        self.__this = phpy.Object(f'MongoDB\\BSON\\UTCDateTime', _milliseconds)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\BSON\\UTCDateTime::__set_state", _properties)

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)

    def toDateTime(self):
        return self.__this.call(f"toDateTime", )


def DriverCursorInterface():

    def getId(self):
        return self.__this.call(f"getId", )

    def getServer(self):
        return self.__this.call(f"getServer", )

    def isDead(self):
        return self.__this.call(f"isDead", )

    def setTypeMap(self, _typemap):
        return self.__this.call(f"setTypeMap", _typemap)

    def toArray(self):
        return self.__this.call(f"toArray", )


def DriverBulkWrite():

    def __init__(self, _options=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\BulkWrite', _options)

    def insert(self, _document):
        return self.__this.call(f"insert", _document)

    def update(self, _query, _new_obj, _update_options=None):
        return self.__this.call(f"update", _query, _new_obj, _update_options)

    def delete(self, _query, _delete_options=None):
        return self.__this.call(f"delete", _query, _delete_options)

    def count(self):
        return self.__this.call(f"count", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverClientEncryption():
    AEAD_AES_256_CBC_HMAC_SHA_512_DETERMINISTIC = "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic"
    AEAD_AES_256_CBC_HMAC_SHA_512_RANDOM = "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
    ALGORITHM_INDEXED = "Indexed"
    ALGORITHM_UNINDEXED = "Unindexed"
    QUERY_TYPE_EQUALITY = "equality"

    def __init__(self, _options=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\ClientEncryption', _options)

    def createDataKey(self, _kms_provider, _options=None):
        return self.__this.call(f"createDataKey", _kms_provider, _options)

    def encrypt(self, _value, _options=None):
        return self.__this.call(f"encrypt", _value, _options)

    def decrypt(self, _key_vault_client):
        return self.__this.call(f"decrypt", _key_vault_client)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverCommand():

    def __init__(self, _document, _options=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Command', _document, _options)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverCursor():

    def setTypeMap(self, _typemap):
        return self.__this.call(f"setTypeMap", _typemap)

    def toArray(self):
        return self.__this.call(f"toArray", )

    def getId(self):
        return self.__this.call(f"getId", )

    def getServer(self):
        return self.__this.call(f"getServer", )

    def isDead(self):
        return self.__this.call(f"isDead", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def valid(self):
        return self.__this.call(f"valid", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverCursorId():

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\Driver\\CursorId::__set_state", _properties)

    def __toString(self):
        return self.__this.call(f"__toString", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def DriverManager():

    def __init__(self, _uri=None, _options=None, _driver_options=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Manager', _uri, _options, _driver_options)

    def addSubscriber(self, _subscriber):
        return self.__this.call(f"addSubscriber", _subscriber)

    def createClientEncryption(self, _options):
        return self.__this.call(f"createClientEncryption", _options)

    def executeCommand(self, _db, _command, _options=None):
        return self.__this.call(f"executeCommand", _db, _command, _options)

    def executeReadCommand(self, _db, _command, _options=None):
        return self.__this.call(f"executeReadCommand", _db, _command, _options)

    def executeWriteCommand(self, _db, _command, _options=None):
        return self.__this.call(f"executeWriteCommand", _db, _command, _options)

    def executeReadWriteCommand(self, _db, _command, _options=None):
        return self.__this.call(f"executeReadWriteCommand", _db, _command, _options)

    def executeQuery(self, _namespace, _zquery, _options=None):
        return self.__this.call(f"executeQuery", _namespace, _zquery, _options)

    def executeBulkWrite(self, _namespace, _zbulk, _options=None):
        return self.__this.call(f"executeBulkWrite", _namespace, _zbulk, _options)

    def getEncryptedFieldsMap(self):
        return self.__this.call(f"getEncryptedFieldsMap", )

    def getReadConcern(self):
        return self.__this.call(f"getReadConcern", )

    def getReadPreference(self):
        return self.__this.call(f"getReadPreference", )

    def getServers(self):
        return self.__this.call(f"getServers", )

    def getWriteConcern(self):
        return self.__this.call(f"getWriteConcern", )

    def removeSubscriber(self, _subscriber):
        return self.__this.call(f"removeSubscriber", _subscriber)

    def selectServer(self, _read_preference=None):
        return self.__this.call(f"selectServer", _read_preference)

    def startSession(self, _options=None):
        return self.__this.call(f"startSession", _options)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverQuery():

    def __init__(self, _filter, _options=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Query', _filter, _options)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverReadConcern():
    LOCAL = "local"
    MAJORITY = "majority"
    LINEARIZABLE = "linearizable"
    AVAILABLE = "available"
    SNAPSHOT = "snapshot"

    def __init__(self, _level=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\ReadConcern', _level)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\Driver\\ReadConcern::__set_state", _properties)

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def getLevel(self):
        return self.__this.call(f"getLevel", )

    def isDefault(self):
        return self.__this.call(f"isDefault", )

    def bsonSerialize(self):
        return self.__this.call(f"bsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def DriverReadPreference():
    RP_PRIMARY = 1
    RP_PRIMARY_PREFERRED = 5
    RP_SECONDARY = 2
    RP_SECONDARY_PREFERRED = 6
    RP_NEAREST = 10
    NO_MAX_STALENESS = -1
    SMALLEST_MAX_STALENESS_SECONDS = 90
    PRIMARY = "primary"
    PRIMARY_PREFERRED = "primaryPreferred"
    SECONDARY = "secondary"
    SECONDARY_PREFERRED = "secondaryPreferred"
    NEAREST = "nearest"

    def __init__(self, _mode, _tag_sets=None, _options=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\ReadPreference', _mode, _tag_sets, _options)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\Driver\\ReadPreference::__set_state", _properties)

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def getHedge(self):
        return self.__this.call(f"getHedge", )

    def getMaxStalenessSeconds(self):
        return self.__this.call(f"getMaxStalenessSeconds", )

    def getMode(self):
        return self.__this.call(f"getMode", )

    def getModeString(self):
        return self.__this.call(f"getModeString", )

    def getTagSets(self):
        return self.__this.call(f"getTagSets", )

    def bsonSerialize(self):
        return self.__this.call(f"bsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def DriverServer():
    TYPE_UNKNOWN = 0
    TYPE_STANDALONE = 1
    TYPE_MONGOS = 2
    TYPE_POSSIBLE_PRIMARY = 3
    TYPE_RS_PRIMARY = 4
    TYPE_RS_SECONDARY = 5
    TYPE_RS_ARBITER = 6
    TYPE_RS_OTHER = 7
    TYPE_RS_GHOST = 8
    TYPE_LOAD_BALANCER = 9

    def executeCommand(self, _db, _command, _options=None):
        return self.__this.call(f"executeCommand", _db, _command, _options)

    def executeReadCommand(self, _db, _command, _options=None):
        return self.__this.call(f"executeReadCommand", _db, _command, _options)

    def executeWriteCommand(self, _db, _command, _options=None):
        return self.__this.call(f"executeWriteCommand", _db, _command, _options)

    def executeReadWriteCommand(self, _db, _command, _options=None):
        return self.__this.call(f"executeReadWriteCommand", _db, _command, _options)

    def executeQuery(self, _namespace, _zquery, _options=None):
        return self.__this.call(f"executeQuery", _namespace, _zquery, _options)

    def executeBulkWrite(self, _namespace, _zbulk, _options=None):
        return self.__this.call(f"executeBulkWrite", _namespace, _zbulk, _options)

    def getHost(self):
        return self.__this.call(f"getHost", )

    def getTags(self):
        return self.__this.call(f"getTags", )

    def getInfo(self):
        return self.__this.call(f"getInfo", )

    def getLatency(self):
        return self.__this.call(f"getLatency", )

    def getPort(self):
        return self.__this.call(f"getPort", )

    def getServerDescription(self):
        return self.__this.call(f"getServerDescription", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isPrimary(self):
        return self.__this.call(f"isPrimary", )

    def isSecondary(self):
        return self.__this.call(f"isSecondary", )

    def isArbiter(self):
        return self.__this.call(f"isArbiter", )

    def isHidden(self):
        return self.__this.call(f"isHidden", )

    def isPassive(self):
        return self.__this.call(f"isPassive", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverServerApi():
    V1 = "1"

    def __init__(self, _version, _strict=None, _deprecation_errors=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\ServerApi', _version, _strict, _deprecation_errors)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\Driver\\ServerApi::__set_state", _properties)

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def bsonSerialize(self):
        return self.__this.call(f"bsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def DriverServerDescription():
    TYPE_UNKNOWN = "Unknown"
    TYPE_STANDALONE = "Standalone"
    TYPE_MONGOS = "Mongos"
    TYPE_POSSIBLE_PRIMARY = "PossiblePrimary"
    TYPE_RS_PRIMARY = "RSPrimary"
    TYPE_RS_SECONDARY = "RSSecondary"
    TYPE_RS_ARBITER = "RSArbiter"
    TYPE_RS_OTHER = "RSOther"
    TYPE_RS_GHOST = "RSGhost"
    TYPE_LOAD_BALANCER = "LoadBalancer"

    def getHelloResponse(self):
        return self.__this.call(f"getHelloResponse", )

    def getHost(self):
        return self.__this.call(f"getHost", )

    def getLastUpdateTime(self):
        return self.__this.call(f"getLastUpdateTime", )

    def getPort(self):
        return self.__this.call(f"getPort", )

    def getRoundTripTime(self):
        return self.__this.call(f"getRoundTripTime", )

    def getType(self):
        return self.__this.call(f"getType", )


def DriverTopologyDescription():
    TYPE_UNKNOWN = "Unknown"
    TYPE_SINGLE = "Single"
    TYPE_SHARDED = "Sharded"
    TYPE_REPLICA_SET_NO_PRIMARY = "ReplicaSetNoPrimary"
    TYPE_REPLICA_SET_WITH_PRIMARY = "ReplicaSetWithPrimary"
    TYPE_LOAD_BALANCED = "LoadBalanced"

    def getServers(self):
        return self.__this.call(f"getServers", )

    def hasReadableServer(self, _read_preference=None):
        return self.__this.call(f"hasReadableServer", _read_preference)

    def hasWritableServer(self):
        return self.__this.call(f"hasWritableServer", )

    def getType(self):
        return self.__this.call(f"getType", )


def DriverSession():
    TRANSACTION_NONE = "none"
    TRANSACTION_STARTING = "starting"
    TRANSACTION_IN_PROGRESS = "in_progress"
    TRANSACTION_COMMITTED = "committed"
    TRANSACTION_ABORTED = "aborted"

    def abortTransaction(self):
        return self.__this.call(f"abortTransaction", )

    def advanceClusterTime(self, _cluster_time):
        return self.__this.call(f"advanceClusterTime", _cluster_time)

    def advanceOperationTime(self, _timestamp):
        return self.__this.call(f"advanceOperationTime", _timestamp)

    def commitTransaction(self):
        return self.__this.call(f"commitTransaction", )

    def endSession(self):
        return self.__this.call(f"endSession", )

    def getClusterTime(self):
        return self.__this.call(f"getClusterTime", )

    def getLogicalSessionId(self):
        return self.__this.call(f"getLogicalSessionId", )

    def getOperationTime(self):
        return self.__this.call(f"getOperationTime", )

    def getServer(self):
        return self.__this.call(f"getServer", )

    def getTransactionOptions(self):
        return self.__this.call(f"getTransactionOptions", )

    def getTransactionState(self):
        return self.__this.call(f"getTransactionState", )

    def isDirty(self):
        return self.__this.call(f"isDirty", )

    def isInTransaction(self):
        return self.__this.call(f"isInTransaction", )

    def startTransaction(self, _options=None):
        return self.__this.call(f"startTransaction", _options)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverWriteConcern():
    MAJORITY = "majority"

    def __init__(self, _w, _wtimeout=None, _journal=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\WriteConcern', _w, _wtimeout, _journal)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __set_state(_properties):
        return phpy.call(f"MongoDB\\Driver\\WriteConcern::__set_state", _properties)

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def getW(self):
        return self.__this.call(f"getW", )

    def getWtimeout(self):
        return self.__this.call(f"getWtimeout", )

    def getJournal(self):
        return self.__this.call(f"getJournal", )

    def isDefault(self):
        return self.__this.call(f"isDefault", )

    def bsonSerialize(self):
        return self.__this.call(f"bsonSerialize", )

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _serialized):
        return self.__this.call(f"unserialize", _serialized)


def DriverWriteConcernError():

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getInfo(self):
        return self.__this.call(f"getInfo", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverWriteError():

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getIndex(self):
        return self.__this.call(f"getIndex", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getInfo(self):
        return self.__this.call(f"getInfo", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverWriteResult():

    def getInsertedCount(self):
        return self.__this.call(f"getInsertedCount", )

    def getMatchedCount(self):
        return self.__this.call(f"getMatchedCount", )

    def getModifiedCount(self):
        return self.__this.call(f"getModifiedCount", )

    def getDeletedCount(self):
        return self.__this.call(f"getDeletedCount", )

    def getUpsertedCount(self):
        return self.__this.call(f"getUpsertedCount", )

    def getServer(self):
        return self.__this.call(f"getServer", )

    def getUpsertedIds(self):
        return self.__this.call(f"getUpsertedIds", )

    def getWriteConcernError(self):
        return self.__this.call(f"getWriteConcernError", )

    def getWriteErrors(self):
        return self.__this.call(f"getWriteErrors", )

    def isAcknowledged(self):
        return self.__this.call(f"isAcknowledged", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverExceptionException():

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionRuntimeException():

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\RuntimeException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionServerException():

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\ServerException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionConnectionException():

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\ConnectionException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionWriteException():

    def getWriteResult(self):
        return self.__this.call(f"getWriteResult", )

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\WriteException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionAuthenticationException():

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\AuthenticationException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionBulkWriteException():

    def getWriteResult(self):
        return self.__this.call(f"getWriteResult", )

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\BulkWriteException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionCommandException():

    def getResultDocument(self):
        return self.__this.call(f"getResultDocument", )

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\CommandException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionConnectionTimeoutException():

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\ConnectionTimeoutException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionEncryptionException():

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\EncryptionException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionExecutionTimeoutException():

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\ExecutionTimeoutException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionInvalidArgumentException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\InvalidArgumentException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionLogicException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\LogicException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionSSLConnectionException():

    def hasErrorLabel(self, _label):
        return self.__this.call(f"hasErrorLabel", _label)

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\SSLConnectionException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverExceptionUnexpectedValueException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'MongoDB\\Driver\\Exception\\UnexpectedValueException', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def DriverMonitoringCommandSubscriber():

    def commandStarted(self, _event):
        return self.__this.call(f"commandStarted", _event)

    def commandSucceeded(self, _event):
        return self.__this.call(f"commandSucceeded", _event)

    def commandFailed(self, _event):
        return self.__this.call(f"commandFailed", _event)


def DriverMonitoringCommandFailedEvent():

    def getCommandName(self):
        return self.__this.call(f"getCommandName", )

    def getError(self):
        return self.__this.call(f"getError", )

    def getDurationMicros(self):
        return self.__this.call(f"getDurationMicros", )

    def getOperationId(self):
        return self.__this.call(f"getOperationId", )

    def getReply(self):
        return self.__this.call(f"getReply", )

    def getRequestId(self):
        return self.__this.call(f"getRequestId", )

    def getServer(self):
        return self.__this.call(f"getServer", )

    def getServiceId(self):
        return self.__this.call(f"getServiceId", )

    def getServerConnectionId(self):
        return self.__this.call(f"getServerConnectionId", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringCommandStartedEvent():

    def getCommand(self):
        return self.__this.call(f"getCommand", )

    def getCommandName(self):
        return self.__this.call(f"getCommandName", )

    def getDatabaseName(self):
        return self.__this.call(f"getDatabaseName", )

    def getOperationId(self):
        return self.__this.call(f"getOperationId", )

    def getRequestId(self):
        return self.__this.call(f"getRequestId", )

    def getServer(self):
        return self.__this.call(f"getServer", )

    def getServiceId(self):
        return self.__this.call(f"getServiceId", )

    def getServerConnectionId(self):
        return self.__this.call(f"getServerConnectionId", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringCommandSucceededEvent():

    def getCommandName(self):
        return self.__this.call(f"getCommandName", )

    def getDurationMicros(self):
        return self.__this.call(f"getDurationMicros", )

    def getOperationId(self):
        return self.__this.call(f"getOperationId", )

    def getReply(self):
        return self.__this.call(f"getReply", )

    def getRequestId(self):
        return self.__this.call(f"getRequestId", )

    def getServer(self):
        return self.__this.call(f"getServer", )

    def getServiceId(self):
        return self.__this.call(f"getServiceId", )

    def getServerConnectionId(self):
        return self.__this.call(f"getServerConnectionId", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringSDAMSubscriber():

    def serverChanged(self, _event):
        return self.__this.call(f"serverChanged", _event)

    def serverClosed(self, _event):
        return self.__this.call(f"serverClosed", _event)

    def serverOpening(self, _event):
        return self.__this.call(f"serverOpening", _event)

    def serverHeartbeatFailed(self, _event):
        return self.__this.call(f"serverHeartbeatFailed", _event)

    def serverHeartbeatStarted(self, _event):
        return self.__this.call(f"serverHeartbeatStarted", _event)

    def serverHeartbeatSucceeded(self, _event):
        return self.__this.call(f"serverHeartbeatSucceeded", _event)

    def topologyChanged(self, _event):
        return self.__this.call(f"topologyChanged", _event)

    def topologyClosed(self, _event):
        return self.__this.call(f"topologyClosed", _event)

    def topologyOpening(self, _event):
        return self.__this.call(f"topologyOpening", _event)


def DriverMonitoringServerChangedEvent():

    def getHost(self):
        return self.__this.call(f"getHost", )

    def getPort(self):
        return self.__this.call(f"getPort", )

    def getNewDescription(self):
        return self.__this.call(f"getNewDescription", )

    def getPreviousDescription(self):
        return self.__this.call(f"getPreviousDescription", )

    def getTopologyId(self):
        return self.__this.call(f"getTopologyId", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringServerClosedEvent():

    def getHost(self):
        return self.__this.call(f"getHost", )

    def getPort(self):
        return self.__this.call(f"getPort", )

    def getTopologyId(self):
        return self.__this.call(f"getTopologyId", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringServerHeartbeatFailedEvent():

    def getDurationMicros(self):
        return self.__this.call(f"getDurationMicros", )

    def getError(self):
        return self.__this.call(f"getError", )

    def getHost(self):
        return self.__this.call(f"getHost", )

    def getPort(self):
        return self.__this.call(f"getPort", )

    def isAwaited(self):
        return self.__this.call(f"isAwaited", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringServerHeartbeatStartedEvent():

    def getHost(self):
        return self.__this.call(f"getHost", )

    def getPort(self):
        return self.__this.call(f"getPort", )

    def isAwaited(self):
        return self.__this.call(f"isAwaited", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringServerHeartbeatSucceededEvent():

    def getDurationMicros(self):
        return self.__this.call(f"getDurationMicros", )

    def getHost(self):
        return self.__this.call(f"getHost", )

    def getPort(self):
        return self.__this.call(f"getPort", )

    def getReply(self):
        return self.__this.call(f"getReply", )

    def isAwaited(self):
        return self.__this.call(f"isAwaited", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringServerOpeningEvent():

    def getHost(self):
        return self.__this.call(f"getHost", )

    def getPort(self):
        return self.__this.call(f"getPort", )

    def getTopologyId(self):
        return self.__this.call(f"getTopologyId", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringTopologyChangedEvent():

    def getNewDescription(self):
        return self.__this.call(f"getNewDescription", )

    def getPreviousDescription(self):
        return self.__this.call(f"getPreviousDescription", )

    def getTopologyId(self):
        return self.__this.call(f"getTopologyId", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringTopologyClosedEvent():

    def getTopologyId(self):
        return self.__this.call(f"getTopologyId", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


def DriverMonitoringTopologyOpeningEvent():

    def getTopologyId(self):
        return self.__this.call(f"getTopologyId", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )


