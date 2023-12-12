import phpy





class Redis():
    REDIS_NOT_FOUND = 0
    REDIS_STRING = 1
    REDIS_SET = 2
    REDIS_LIST = 3
    REDIS_ZSET = 4
    REDIS_HASH = 5
    REDIS_STREAM = 6
    PIPELINE = 2
    ATOMIC = 0
    MULTI = 1
    OPT_SERIALIZER = 1
    OPT_PREFIX = 2
    OPT_READ_TIMEOUT = 3
    OPT_TCP_KEEPALIVE = 6
    OPT_COMPRESSION = 7
    OPT_REPLY_LITERAL = 8
    OPT_COMPRESSION_LEVEL = 9
    OPT_NULL_MULTIBULK_AS_NULL = 10
    SERIALIZER_NONE = 0
    SERIALIZER_PHP = 1
    SERIALIZER_JSON = 4
    COMPRESSION_NONE = 0
    OPT_SCAN = 4
    SCAN_RETRY = 1
    SCAN_NORETRY = 0
    SCAN_PREFIX = 2
    SCAN_NOPREFIX = 3
    AFTER = "after"
    BEFORE = "before"
    OPT_MAX_RETRIES = 11
    OPT_BACKOFF_ALGORITHM = 12
    BACKOFF_ALGORITHM_DEFAULT = 0
    BACKOFF_ALGORITHM_CONSTANT = 6
    BACKOFF_ALGORITHM_UNIFORM = 5
    BACKOFF_ALGORITHM_EXPONENTIAL = 4
    BACKOFF_ALGORITHM_FULL_JITTER = 2
    BACKOFF_ALGORITHM_EQUAL_JITTER = 3
    BACKOFF_ALGORITHM_DECORRELATED_JITTER = 1
    OPT_BACKOFF_BASE = 13
    OPT_BACKOFF_CAP = 14

    def __init__(self):
        self.__this = phpy.Object(f'Redis', )

    def _prefix(self, _key):
        return self.__this.call(f"_prefix", _key)

    def _serialize(self, _value):
        return self.__this.call(f"_serialize", _value)

    def _unserialize(self, _value):
        return self.__this.call(f"_unserialize", _value)

    def _pack(self, _value):
        return self.__this.call(f"_pack", _value)

    def _unpack(self, _value):
        return self.__this.call(f"_unpack", _value)

    def _compress(self, _value):
        return self.__this.call(f"_compress", _value)

    def _uncompress(self, _value):
        return self.__this.call(f"_uncompress", _value)

    def acl(self, _subcmd, _args=None):
        return self.__this.call(f"acl", _subcmd, _args)

    def append(self, _key, _value):
        return self.__this.call(f"append", _key, _value)

    def auth(self, _auth):
        return self.__this.call(f"auth", _auth)

    def bgSave(self):
        return self.__this.call(f"bgSave", )

    def bgrewriteaof(self):
        return self.__this.call(f"bgrewriteaof", )

    def bitcount(self, _key):
        return self.__this.call(f"bitcount", _key)

    def bitop(self, _operation, _ret_key, _key, _other_keys=None):
        return self.__this.call(f"bitop", _operation, _ret_key, _key, _other_keys)

    def bitpos(self, _key, _bit, _start=None, _end=None):
        return self.__this.call(f"bitpos", _key, _bit, _start, _end)

    def blPop(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"blPop", _key, _timeout_or_key, _extra_args)

    def brPop(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"brPop", _key, _timeout_or_key, _extra_args)

    def brpoplpush(self, _src, _dst, _timeout):
        return self.__this.call(f"brpoplpush", _src, _dst, _timeout)

    def bzPopMax(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"bzPopMax", _key, _timeout_or_key, _extra_args)

    def bzPopMin(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"bzPopMin", _key, _timeout_or_key, _extra_args)

    def clearLastError(self):
        return self.__this.call(f"clearLastError", )

    def client(self, _cmd, _args=None):
        return self.__this.call(f"client", _cmd, _args)

    def close(self):
        return self.__this.call(f"close", )

    def command(self, _args=None):
        return self.__this.call(f"command", _args)

    def config(self, _cmd, _key, _value=None):
        return self.__this.call(f"config", _cmd, _key, _value)

    def connect(self, _host, _port=None, _timeout=None, _retry_interval=None):
        return self.__this.call(f"connect", _host, _port, _timeout, _retry_interval)

    def dbSize(self):
        return self.__this.call(f"dbSize", )

    def debug(self, _key):
        return self.__this.call(f"debug", _key)

    def decr(self, _key):
        return self.__this.call(f"decr", _key)

    def decrBy(self, _key, _value):
        return self.__this.call(f"decrBy", _key, _value)

    def _del(self, _key, _other_keys=None):
        return self.__this.call(f"del", _key, _other_keys)

    def discard(self):
        return self.__this.call(f"discard", )

    def dump(self, _key):
        return self.__this.call(f"dump", _key)

    def echo(self, _msg):
        return self.__this.call(f"echo", _msg)

    def eval(self, _script, _args=None, _num_keys=None):
        return self.__this.call(f"eval", _script, _args, _num_keys)

    def evalsha(self, _script_sha, _args=None, _num_keys=None):
        return self.__this.call(f"evalsha", _script_sha, _args, _num_keys)

    def exec(self):
        return self.__this.call(f"exec", )

    def exists(self, _key, _other_keys=None):
        return self.__this.call(f"exists", _key, _other_keys)

    def expire(self, _key, _timeout):
        return self.__this.call(f"expire", _key, _timeout)

    def expireAt(self, _key, _timestamp):
        return self.__this.call(f"expireAt", _key, _timestamp)

    def flushAll(self, _async=None):
        return self.__this.call(f"flushAll", _async)

    def flushDB(self, _async=None):
        return self.__this.call(f"flushDB", _async)

    def geoadd(self, _key, _lng, _lat, _member, _other_triples=None):
        return self.__this.call(f"geoadd", _key, _lng, _lat, _member, _other_triples)

    def geodist(self, _key, _src, _dst, _unit=None):
        return self.__this.call(f"geodist", _key, _src, _dst, _unit)

    def geohash(self, _key, _member, _other_members=None):
        return self.__this.call(f"geohash", _key, _member, _other_members)

    def geopos(self, _key, _member, _other_members=None):
        return self.__this.call(f"geopos", _key, _member, _other_members)

    def georadius(self, _key, _lng, _lan, _radius, _unit, _opts=None):
        return self.__this.call(f"georadius", _key, _lng, _lan, _radius, _unit, _opts)

    def georadius_ro(self, _key, _lng, _lan, _radius, _unit, _opts=None):
        return self.__this.call(f"georadius_ro", _key, _lng, _lan, _radius, _unit, _opts)

    def georadiusbymember(self, _key, _member, _radius, _unit, _opts=None):
        return self.__this.call(f"georadiusbymember", _key, _member, _radius, _unit, _opts)

    def georadiusbymember_ro(self, _key, _member, _radius, _unit, _opts=None):
        return self.__this.call(f"georadiusbymember_ro", _key, _member, _radius, _unit, _opts)

    def get(self, _key):
        return self.__this.call(f"get", _key)

    def getAuth(self):
        return self.__this.call(f"getAuth", )

    def getBit(self, _key, _offset):
        return self.__this.call(f"getBit", _key, _offset)

    def getDBNum(self):
        return self.__this.call(f"getDBNum", )

    def getHost(self):
        return self.__this.call(f"getHost", )

    def getLastError(self):
        return self.__this.call(f"getLastError", )

    def getMode(self):
        return self.__this.call(f"getMode", )

    def getOption(self, _option):
        return self.__this.call(f"getOption", _option)

    def getPersistentID(self):
        return self.__this.call(f"getPersistentID", )

    def getPort(self):
        return self.__this.call(f"getPort", )

    def getRange(self, _key, _start, _end):
        return self.__this.call(f"getRange", _key, _start, _end)

    def getReadTimeout(self):
        return self.__this.call(f"getReadTimeout", )

    def getSet(self, _key, _value):
        return self.__this.call(f"getSet", _key, _value)

    def getTimeout(self):
        return self.__this.call(f"getTimeout", )

    def hDel(self, _key, _member, _other_members=None):
        return self.__this.call(f"hDel", _key, _member, _other_members)

    def hExists(self, _key, _member):
        return self.__this.call(f"hExists", _key, _member)

    def hGet(self, _key, _member):
        return self.__this.call(f"hGet", _key, _member)

    def hGetAll(self, _key):
        return self.__this.call(f"hGetAll", _key)

    def hIncrBy(self, _key, _member, _value):
        return self.__this.call(f"hIncrBy", _key, _member, _value)

    def hIncrByFloat(self, _key, _member, _value):
        return self.__this.call(f"hIncrByFloat", _key, _member, _value)

    def hKeys(self, _key):
        return self.__this.call(f"hKeys", _key)

    def hLen(self, _key):
        return self.__this.call(f"hLen", _key)

    def hMget(self, _key, _keys):
        return self.__this.call(f"hMget", _key, _keys)

    def hMset(self, _key, _pairs):
        return self.__this.call(f"hMset", _key, _pairs)

    def hSet(self, _key, _member, _value):
        return self.__this.call(f"hSet", _key, _member, _value)

    def hSetNx(self, _key, _member, _value):
        return self.__this.call(f"hSetNx", _key, _member, _value)

    def hStrLen(self, _key, _member):
        return self.__this.call(f"hStrLen", _key, _member)

    def hVals(self, _key):
        return self.__this.call(f"hVals", _key)

    def hscan(self, _str_key, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"hscan", _str_key, _i_iterator, _str_pattern, _i_count)

    def incr(self, _key):
        return self.__this.call(f"incr", _key)

    def incrBy(self, _key, _value):
        return self.__this.call(f"incrBy", _key, _value)

    def incrByFloat(self, _key, _value):
        return self.__this.call(f"incrByFloat", _key, _value)

    def info(self, _option=None):
        return self.__this.call(f"info", _option)

    def isConnected(self):
        return self.__this.call(f"isConnected", )

    def keys(self, _pattern):
        return self.__this.call(f"keys", _pattern)

    def lInsert(self, _key, _position, _pivot, _value):
        return self.__this.call(f"lInsert", _key, _position, _pivot, _value)

    def lLen(self, _key):
        return self.__this.call(f"lLen", _key)

    def lPop(self, _key):
        return self.__this.call(f"lPop", _key)

    def lPush(self, _key, _value):
        return self.__this.call(f"lPush", _key, _value)

    def lPushx(self, _key, _value):
        return self.__this.call(f"lPushx", _key, _value)

    def lSet(self, _key, _index, _value):
        return self.__this.call(f"lSet", _key, _index, _value)

    def lastSave(self):
        return self.__this.call(f"lastSave", )

    def lindex(self, _key, _index):
        return self.__this.call(f"lindex", _key, _index)

    def lrange(self, _key, _start, _end):
        return self.__this.call(f"lrange", _key, _start, _end)

    def lrem(self, _key, _value, _count):
        return self.__this.call(f"lrem", _key, _value, _count)

    def ltrim(self, _key, _start, _stop):
        return self.__this.call(f"ltrim", _key, _start, _stop)

    def mget(self, _keys):
        return self.__this.call(f"mget", _keys)

    def migrate(self, _host, _port, _key, _db, _timeout, _copy=None, _replace=None):
        return self.__this.call(f"migrate", _host, _port, _key, _db, _timeout, _copy, _replace)

    def move(self, _key, _dbindex):
        return self.__this.call(f"move", _key, _dbindex)

    def mset(self, _pairs):
        return self.__this.call(f"mset", _pairs)

    def msetnx(self, _pairs):
        return self.__this.call(f"msetnx", _pairs)

    def multi(self, _mode=None):
        return self.__this.call(f"multi", _mode)

    def object(self, _field, _key):
        return self.__this.call(f"object", _field, _key)

    def pconnect(self, _host, _port=None, _timeout=None):
        return self.__this.call(f"pconnect", _host, _port, _timeout)

    def persist(self, _key):
        return self.__this.call(f"persist", _key)

    def pexpire(self, _key, _timestamp):
        return self.__this.call(f"pexpire", _key, _timestamp)

    def pexpireAt(self, _key, _timestamp):
        return self.__this.call(f"pexpireAt", _key, _timestamp)

    def pfadd(self, _key, _elements):
        return self.__this.call(f"pfadd", _key, _elements)

    def pfcount(self, _key):
        return self.__this.call(f"pfcount", _key)

    def pfmerge(self, _dstkey, _keys):
        return self.__this.call(f"pfmerge", _dstkey, _keys)

    def ping(self):
        return self.__this.call(f"ping", )

    def pipeline(self):
        return self.__this.call(f"pipeline", )

    def psetex(self, _key, _expire, _value):
        return self.__this.call(f"psetex", _key, _expire, _value)

    def psubscribe(self, _patterns, _callback):
        return self.__this.call(f"psubscribe", _patterns, _callback)

    def pttl(self, _key):
        return self.__this.call(f"pttl", _key)

    def publish(self, _channel, _message):
        return self.__this.call(f"publish", _channel, _message)

    def pubsub(self, _cmd, _args=None):
        return self.__this.call(f"pubsub", _cmd, _args)

    def punsubscribe(self, _pattern, _other_patterns=None):
        return self.__this.call(f"punsubscribe", _pattern, _other_patterns)

    def rPop(self, _key):
        return self.__this.call(f"rPop", _key)

    def rPush(self, _key, _value):
        return self.__this.call(f"rPush", _key, _value)

    def rPushx(self, _key, _value):
        return self.__this.call(f"rPushx", _key, _value)

    def randomKey(self):
        return self.__this.call(f"randomKey", )

    def rawcommand(self, _cmd, _args=None):
        return self.__this.call(f"rawcommand", _cmd, _args)

    def rename(self, _key, _newkey):
        return self.__this.call(f"rename", _key, _newkey)

    def renameNx(self, _key, _newkey):
        return self.__this.call(f"renameNx", _key, _newkey)

    def restore(self, _ttl, _key, _value):
        return self.__this.call(f"restore", _ttl, _key, _value)

    def role(self):
        return self.__this.call(f"role", )

    def rpoplpush(self, _src, _dst):
        return self.__this.call(f"rpoplpush", _src, _dst)

    def sAdd(self, _key, _value):
        return self.__this.call(f"sAdd", _key, _value)

    def sAddArray(self, _key, _options):
        return self.__this.call(f"sAddArray", _key, _options)

    def sDiff(self, _key, _other_keys=None):
        return self.__this.call(f"sDiff", _key, _other_keys)

    def sDiffStore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sDiffStore", _dst, _key, _other_keys)

    def sInter(self, _key, _other_keys=None):
        return self.__this.call(f"sInter", _key, _other_keys)

    def sInterStore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sInterStore", _dst, _key, _other_keys)

    def sMembers(self, _key):
        return self.__this.call(f"sMembers", _key)

    def sMisMember(self, _key, _member, _other_members=None):
        return self.__this.call(f"sMisMember", _key, _member, _other_members)

    def sMove(self, _src, _dst, _value):
        return self.__this.call(f"sMove", _src, _dst, _value)

    def sPop(self, _key):
        return self.__this.call(f"sPop", _key)

    def sRandMember(self, _key, _count=None):
        return self.__this.call(f"sRandMember", _key, _count)

    def sUnion(self, _key, _other_keys=None):
        return self.__this.call(f"sUnion", _key, _other_keys)

    def sUnionStore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sUnionStore", _dst, _key, _other_keys)

    def save(self):
        return self.__this.call(f"save", )

    def scan(self, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"scan", _i_iterator, _str_pattern, _i_count)

    def scard(self, _key):
        return self.__this.call(f"scard", _key)

    def script(self, _cmd, _args=None):
        return self.__this.call(f"script", _cmd, _args)

    def select(self, _dbindex):
        return self.__this.call(f"select", _dbindex)

    def set(self, _key, _value, _opts=None):
        return self.__this.call(f"set", _key, _value, _opts)

    def setBit(self, _key, _offset, _value):
        return self.__this.call(f"setBit", _key, _offset, _value)

    def setOption(self, _option, _value):
        return self.__this.call(f"setOption", _option, _value)

    def setRange(self, _key, _offset, _value):
        return self.__this.call(f"setRange", _key, _offset, _value)

    def setex(self, _key, _expire, _value):
        return self.__this.call(f"setex", _key, _expire, _value)

    def setnx(self, _key, _value):
        return self.__this.call(f"setnx", _key, _value)

    def sismember(self, _key, _value):
        return self.__this.call(f"sismember", _key, _value)

    def slaveof(self, _host=None, _port=None):
        return self.__this.call(f"slaveof", _host, _port)

    def slowlog(self, _arg, _option=None):
        return self.__this.call(f"slowlog", _arg, _option)

    def sort(self, _key, _options=None):
        return self.__this.call(f"sort", _key, _options)

    def sortAsc(self, _key, _pattern=None, _get=None, _start=None, _end=None, _get_list=None):
        return self.__this.call(f"sortAsc", _key, _pattern, _get, _start, _end, _get_list)

    def sortAscAlpha(self, _key, _pattern=None, _get=None, _start=None, _end=None, _get_list=None):
        return self.__this.call(f"sortAscAlpha", _key, _pattern, _get, _start, _end, _get_list)

    def sortDesc(self, _key, _pattern=None, _get=None, _start=None, _end=None, _get_list=None):
        return self.__this.call(f"sortDesc", _key, _pattern, _get, _start, _end, _get_list)

    def sortDescAlpha(self, _key, _pattern=None, _get=None, _start=None, _end=None, _get_list=None):
        return self.__this.call(f"sortDescAlpha", _key, _pattern, _get, _start, _end, _get_list)

    def srem(self, _key, _member, _other_members=None):
        return self.__this.call(f"srem", _key, _member, _other_members)

    def sscan(self, _str_key, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"sscan", _str_key, _i_iterator, _str_pattern, _i_count)

    def strlen(self, _key):
        return self.__this.call(f"strlen", _key)

    def subscribe(self, _channels, _callback):
        return self.__this.call(f"subscribe", _channels, _callback)

    def swapdb(self, _srcdb, _dstdb):
        return self.__this.call(f"swapdb", _srcdb, _dstdb)

    def time(self):
        return self.__this.call(f"time", )

    def ttl(self, _key):
        return self.__this.call(f"ttl", _key)

    def type(self, _key):
        return self.__this.call(f"type", _key)

    def unlink(self, _key, _other_keys=None):
        return self.__this.call(f"unlink", _key, _other_keys)

    def unsubscribe(self, _channel, _other_channels=None):
        return self.__this.call(f"unsubscribe", _channel, _other_channels)

    def unwatch(self):
        return self.__this.call(f"unwatch", )

    def wait(self, _numslaves, _timeout):
        return self.__this.call(f"wait", _numslaves, _timeout)

    def watch(self, _key, _other_keys=None):
        return self.__this.call(f"watch", _key, _other_keys)

    def xack(self, _str_key, _str_group, _arr_ids):
        return self.__this.call(f"xack", _str_key, _str_group, _arr_ids)

    def xadd(self, _str_key, _str_id, _arr_fields, _i_maxlen=None, _boo_approximate=None):
        return self.__this.call(f"xadd", _str_key, _str_id, _arr_fields, _i_maxlen, _boo_approximate)

    def xclaim(self, _str_key, _str_group, _str_consumer, _i_min_idle, _arr_ids, _arr_opts=None):
        return self.__this.call(f"xclaim", _str_key, _str_group, _str_consumer, _i_min_idle, _arr_ids, _arr_opts)

    def xdel(self, _str_key, _arr_ids):
        return self.__this.call(f"xdel", _str_key, _arr_ids)

    def xgroup(self, _str_operation, _str_key=None, _str_arg1=None, _str_arg2=None, _str_arg3=None):
        return self.__this.call(f"xgroup", _str_operation, _str_key, _str_arg1, _str_arg2, _str_arg3)

    def xinfo(self, _str_cmd, _str_key=None, _str_group=None):
        return self.__this.call(f"xinfo", _str_cmd, _str_key, _str_group)

    def xlen(self, _key):
        return self.__this.call(f"xlen", _key)

    def xpending(self, _str_key, _str_group, _str_start=None, _str_end=None, _i_count=None, _str_consumer=None):
        return self.__this.call(f"xpending", _str_key, _str_group, _str_start, _str_end, _i_count, _str_consumer)

    def xrange(self, _str_key, _str_start, _str_end, _i_count=None):
        return self.__this.call(f"xrange", _str_key, _str_start, _str_end, _i_count)

    def xread(self, _arr_streams, _i_count=None, _i_block=None):
        return self.__this.call(f"xread", _arr_streams, _i_count, _i_block)

    def xreadgroup(self, _str_group, _str_consumer, _arr_streams, _i_count=None, _i_block=None):
        return self.__this.call(f"xreadgroup", _str_group, _str_consumer, _arr_streams, _i_count, _i_block)

    def xrevrange(self, _str_key, _str_start, _str_end, _i_count=None):
        return self.__this.call(f"xrevrange", _str_key, _str_start, _str_end, _i_count)

    def xtrim(self, _str_key, _i_maxlen, _boo_approximate=None):
        return self.__this.call(f"xtrim", _str_key, _i_maxlen, _boo_approximate)

    def zAdd(self, _key, _score, _value, _extra_args=None):
        return self.__this.call(f"zAdd", _key, _score, _value, _extra_args)

    def zCard(self, _key):
        return self.__this.call(f"zCard", _key)

    def zCount(self, _key, _min, _max):
        return self.__this.call(f"zCount", _key, _min, _max)

    def zIncrBy(self, _key, _value, _member):
        return self.__this.call(f"zIncrBy", _key, _value, _member)

    def zLexCount(self, _key, _min, _max):
        return self.__this.call(f"zLexCount", _key, _min, _max)

    def zPopMax(self, _key):
        return self.__this.call(f"zPopMax", _key)

    def zPopMin(self, _key):
        return self.__this.call(f"zPopMin", _key)

    def zRange(self, _key, _start, _end, _scores=None):
        return self.__this.call(f"zRange", _key, _start, _end, _scores)

    def zRangeByLex(self, _key, _min, _max, _offset=None, _limit=None):
        return self.__this.call(f"zRangeByLex", _key, _min, _max, _offset, _limit)

    def zRangeByScore(self, _key, _start, _end, _options=None):
        return self.__this.call(f"zRangeByScore", _key, _start, _end, _options)

    def zRank(self, _key, _member):
        return self.__this.call(f"zRank", _key, _member)

    def zRem(self, _key, _member, _other_members=None):
        return self.__this.call(f"zRem", _key, _member, _other_members)

    def zRemRangeByLex(self, _key, _min, _max):
        return self.__this.call(f"zRemRangeByLex", _key, _min, _max)

    def zRemRangeByRank(self, _key, _start, _end):
        return self.__this.call(f"zRemRangeByRank", _key, _start, _end)

    def zRemRangeByScore(self, _key, _min, _max):
        return self.__this.call(f"zRemRangeByScore", _key, _min, _max)

    def zRevRange(self, _key, _start, _end, _scores=None):
        return self.__this.call(f"zRevRange", _key, _start, _end, _scores)

    def zRevRangeByLex(self, _key, _min, _max, _offset=None, _limit=None):
        return self.__this.call(f"zRevRangeByLex", _key, _min, _max, _offset, _limit)

    def zRevRangeByScore(self, _key, _start, _end, _options=None):
        return self.__this.call(f"zRevRangeByScore", _key, _start, _end, _options)

    def zRevRank(self, _key, _member):
        return self.__this.call(f"zRevRank", _key, _member)

    def zScore(self, _key, _member):
        return self.__this.call(f"zScore", _key, _member)

    def zinterstore(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zinterstore", _key, _keys, _weights, _aggregate)

    def zscan(self, _str_key, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"zscan", _str_key, _i_iterator, _str_pattern, _i_count)

    def zunionstore(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zunionstore", _key, _keys, _weights, _aggregate)

    def delete(self, _key, _other_keys=None):
        return self.__this.call(f"delete", _key, _other_keys)

    def evaluate(self, _script, _args=None, _num_keys=None):
        return self.__this.call(f"evaluate", _script, _args, _num_keys)

    def evaluateSha(self, _script_sha, _args=None, _num_keys=None):
        return self.__this.call(f"evaluateSha", _script_sha, _args, _num_keys)

    def getKeys(self, _pattern):
        return self.__this.call(f"getKeys", _pattern)

    def getMultiple(self, _keys):
        return self.__this.call(f"getMultiple", _keys)

    def lGet(self, _key, _index):
        return self.__this.call(f"lGet", _key, _index)

    def lGetRange(self, _key, _start, _end):
        return self.__this.call(f"lGetRange", _key, _start, _end)

    def lRemove(self, _key, _value, _count):
        return self.__this.call(f"lRemove", _key, _value, _count)

    def lSize(self, _key):
        return self.__this.call(f"lSize", _key)

    def listTrim(self, _key, _start, _stop):
        return self.__this.call(f"listTrim", _key, _start, _stop)

    def open(self, _host, _port=None, _timeout=None, _retry_interval=None):
        return self.__this.call(f"open", _host, _port, _timeout, _retry_interval)

    def popen(self, _host, _port=None, _timeout=None):
        return self.__this.call(f"popen", _host, _port, _timeout)

    def renameKey(self, _key, _newkey):
        return self.__this.call(f"renameKey", _key, _newkey)

    def sContains(self, _key, _value):
        return self.__this.call(f"sContains", _key, _value)

    def sGetMembers(self, _key):
        return self.__this.call(f"sGetMembers", _key)

    def sRemove(self, _key, _member, _other_members=None):
        return self.__this.call(f"sRemove", _key, _member, _other_members)

    def sSize(self, _key):
        return self.__this.call(f"sSize", _key)

    def sendEcho(self, _msg):
        return self.__this.call(f"sendEcho", _msg)

    def setTimeout(self, _key, _timeout):
        return self.__this.call(f"setTimeout", _key, _timeout)

    def substr(self, _key, _start, _end):
        return self.__this.call(f"substr", _key, _start, _end)

    def zDelete(self, _key, _member, _other_members=None):
        return self.__this.call(f"zDelete", _key, _member, _other_members)

    def zDeleteRangeByRank(self, _key, _min, _max):
        return self.__this.call(f"zDeleteRangeByRank", _key, _min, _max)

    def zDeleteRangeByScore(self, _key, _min, _max):
        return self.__this.call(f"zDeleteRangeByScore", _key, _min, _max)

    def zInter(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zInter", _key, _keys, _weights, _aggregate)

    def zRemove(self, _key, _member, _other_members=None):
        return self.__this.call(f"zRemove", _key, _member, _other_members)

    def zRemoveRangeByScore(self, _key, _min, _max):
        return self.__this.call(f"zRemoveRangeByScore", _key, _min, _max)

    def zReverseRange(self, _key, _start, _end, _scores=None):
        return self.__this.call(f"zReverseRange", _key, _start, _end, _scores)

    def zSize(self, _key):
        return self.__this.call(f"zSize", _key)

    def zUnion(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zUnion", _key, _keys, _weights, _aggregate)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RedisArray():

    def __call(self, _function_name, _arguments):
        return self.__this.call(f"__call", _function_name, _arguments)

    def __init__(self, _name_or_hosts, _options=None):
        self.__this = phpy.Object(f'RedisArray', _name_or_hosts, _options)

    def _continuum(self):
        return self.__this.call(f"_continuum", )

    def _distributor(self):
        return self.__this.call(f"_distributor", )

    def _function(self):
        return self.__this.call(f"_function", )

    def _hosts(self):
        return self.__this.call(f"_hosts", )

    def _instance(self, _host):
        return self.__this.call(f"_instance", _host)

    def _rehash(self, _callable=None):
        return self.__this.call(f"_rehash", _callable)

    def _target(self, _key):
        return self.__this.call(f"_target", _key)

    def bgsave(self):
        return self.__this.call(f"bgsave", )

    def _del(self, _keys):
        return self.__this.call(f"del", _keys)

    def discard(self):
        return self.__this.call(f"discard", )

    def exec(self):
        return self.__this.call(f"exec", )

    def flushall(self, _async=None):
        return self.__this.call(f"flushall", _async)

    def flushdb(self, _async=None):
        return self.__this.call(f"flushdb", _async)

    def getOption(self, _opt):
        return self.__this.call(f"getOption", _opt)

    def hscan(self, _str_key, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"hscan", _str_key, _i_iterator, _str_pattern, _i_count)

    def info(self):
        return self.__this.call(f"info", )

    def keys(self, _pattern):
        return self.__this.call(f"keys", _pattern)

    def mget(self, _keys):
        return self.__this.call(f"mget", _keys)

    def mset(self, _pairs):
        return self.__this.call(f"mset", _pairs)

    def multi(self, _host, _mode=None):
        return self.__this.call(f"multi", _host, _mode)

    def ping(self):
        return self.__this.call(f"ping", )

    def save(self):
        return self.__this.call(f"save", )

    def scan(self, _iterator, _node, _pattern=None, _count=None):
        return self.__this.call(f"scan", _iterator, _node, _pattern, _count)

    def select(self, _index):
        return self.__this.call(f"select", _index)

    def setOption(self, _opt, _value):
        return self.__this.call(f"setOption", _opt, _value)

    def sscan(self, _str_key, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"sscan", _str_key, _i_iterator, _str_pattern, _i_count)

    def unlink(self):
        return self.__this.call(f"unlink", )

    def unwatch(self):
        return self.__this.call(f"unwatch", )

    def zscan(self, _str_key, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"zscan", _str_key, _i_iterator, _str_pattern, _i_count)

    def delete(self, _keys):
        return self.__this.call(f"delete", _keys)

    def getMultiple(self, _keys):
        return self.__this.call(f"getMultiple", _keys)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RedisCluster():
    REDIS_NOT_FOUND = 0
    REDIS_STRING = 1
    REDIS_SET = 2
    REDIS_LIST = 3
    REDIS_ZSET = 4
    REDIS_HASH = 5
    REDIS_STREAM = 6
    ATOMIC = 0
    MULTI = 1
    OPT_SERIALIZER = 1
    OPT_PREFIX = 2
    OPT_READ_TIMEOUT = 3
    OPT_TCP_KEEPALIVE = 6
    OPT_COMPRESSION = 7
    OPT_REPLY_LITERAL = 8
    OPT_COMPRESSION_LEVEL = 9
    OPT_NULL_MULTIBULK_AS_NULL = 10
    SERIALIZER_NONE = 0
    SERIALIZER_PHP = 1
    SERIALIZER_JSON = 4
    COMPRESSION_NONE = 0
    OPT_SCAN = 4
    SCAN_RETRY = 1
    SCAN_NORETRY = 0
    SCAN_PREFIX = 2
    SCAN_NOPREFIX = 3
    AFTER = "after"
    BEFORE = "before"
    OPT_SLAVE_FAILOVER = 5
    FAILOVER_NONE = 0
    FAILOVER_ERROR = 1
    FAILOVER_DISTRIBUTE = 2
    FAILOVER_DISTRIBUTE_SLAVES = 3
    OPT_MAX_RETRIES = 11
    OPT_BACKOFF_ALGORITHM = 12
    BACKOFF_ALGORITHM_DEFAULT = 0
    BACKOFF_ALGORITHM_CONSTANT = 6
    BACKOFF_ALGORITHM_UNIFORM = 5
    BACKOFF_ALGORITHM_EXPONENTIAL = 4
    BACKOFF_ALGORITHM_FULL_JITTER = 2
    BACKOFF_ALGORITHM_EQUAL_JITTER = 3
    BACKOFF_ALGORITHM_DECORRELATED_JITTER = 1
    OPT_BACKOFF_BASE = 13
    OPT_BACKOFF_CAP = 14

    def __init__(self, _name, _seeds=None, _timeout=None, _read_timeout=None, _persistent=None, _auth=None):
        self.__this = phpy.Object(f'RedisCluster', _name, _seeds, _timeout, _read_timeout, _persistent, _auth)

    def _masters(self):
        return self.__this.call(f"_masters", )

    def _prefix(self, _key):
        return self.__this.call(f"_prefix", _key)

    def _redir(self):
        return self.__this.call(f"_redir", )

    def _serialize(self, _value):
        return self.__this.call(f"_serialize", _value)

    def _unserialize(self, _value):
        return self.__this.call(f"_unserialize", _value)

    def _compress(self, _value):
        return self.__this.call(f"_compress", _value)

    def _uncompress(self, _value):
        return self.__this.call(f"_uncompress", _value)

    def _pack(self, _value):
        return self.__this.call(f"_pack", _value)

    def _unpack(self, _value):
        return self.__this.call(f"_unpack", _value)

    def acl(self, _key_or_address, _subcmd, _args=None):
        return self.__this.call(f"acl", _key_or_address, _subcmd, _args)

    def append(self, _key, _value):
        return self.__this.call(f"append", _key, _value)

    def bgrewriteaof(self, _key_or_address):
        return self.__this.call(f"bgrewriteaof", _key_or_address)

    def bgsave(self, _key_or_address):
        return self.__this.call(f"bgsave", _key_or_address)

    def bitcount(self, _key):
        return self.__this.call(f"bitcount", _key)

    def bitop(self, _operation, _ret_key, _key, _other_keys=None):
        return self.__this.call(f"bitop", _operation, _ret_key, _key, _other_keys)

    def bitpos(self, _key, _bit, _start=None, _end=None):
        return self.__this.call(f"bitpos", _key, _bit, _start, _end)

    def blpop(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"blpop", _key, _timeout_or_key, _extra_args)

    def brpop(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"brpop", _key, _timeout_or_key, _extra_args)

    def brpoplpush(self, _src, _dst, _timeout):
        return self.__this.call(f"brpoplpush", _src, _dst, _timeout)

    def clearlasterror(self):
        return self.__this.call(f"clearlasterror", )

    def bzpopmax(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"bzpopmax", _key, _timeout_or_key, _extra_args)

    def bzpopmin(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"bzpopmin", _key, _timeout_or_key, _extra_args)

    def client(self, _key_or_address, _arg=None, _other_args=None):
        return self.__this.call(f"client", _key_or_address, _arg, _other_args)

    def close(self):
        return self.__this.call(f"close", )

    def cluster(self, _key_or_address, _arg=None, _other_args=None):
        return self.__this.call(f"cluster", _key_or_address, _arg, _other_args)

    def command(self, _args=None):
        return self.__this.call(f"command", _args)

    def config(self, _key_or_address, _arg=None, _other_args=None):
        return self.__this.call(f"config", _key_or_address, _arg, _other_args)

    def dbsize(self, _key_or_address):
        return self.__this.call(f"dbsize", _key_or_address)

    def decr(self, _key):
        return self.__this.call(f"decr", _key)

    def decrby(self, _key, _value):
        return self.__this.call(f"decrby", _key, _value)

    def _del(self, _key, _other_keys=None):
        return self.__this.call(f"del", _key, _other_keys)

    def discard(self):
        return self.__this.call(f"discard", )

    def dump(self, _key):
        return self.__this.call(f"dump", _key)

    def echo(self, _msg):
        return self.__this.call(f"echo", _msg)

    def eval(self, _script, _args=None, _num_keys=None):
        return self.__this.call(f"eval", _script, _args, _num_keys)

    def evalsha(self, _script_sha, _args=None, _num_keys=None):
        return self.__this.call(f"evalsha", _script_sha, _args, _num_keys)

    def exec(self):
        return self.__this.call(f"exec", )

    def exists(self, _key):
        return self.__this.call(f"exists", _key)

    def expire(self, _key, _timeout):
        return self.__this.call(f"expire", _key, _timeout)

    def expireat(self, _key, _timestamp):
        return self.__this.call(f"expireat", _key, _timestamp)

    def flushall(self, _key_or_address, _async=None):
        return self.__this.call(f"flushall", _key_or_address, _async)

    def flushdb(self, _key_or_address, _async=None):
        return self.__this.call(f"flushdb", _key_or_address, _async)

    def geoadd(self, _key, _lng, _lat, _member, _other_triples=None):
        return self.__this.call(f"geoadd", _key, _lng, _lat, _member, _other_triples)

    def geodist(self, _key, _src, _dst, _unit=None):
        return self.__this.call(f"geodist", _key, _src, _dst, _unit)

    def geohash(self, _key, _member, _other_members=None):
        return self.__this.call(f"geohash", _key, _member, _other_members)

    def geopos(self, _key, _member, _other_members=None):
        return self.__this.call(f"geopos", _key, _member, _other_members)

    def georadius(self, _key, _lng, _lan, _radius, _unit, _opts=None):
        return self.__this.call(f"georadius", _key, _lng, _lan, _radius, _unit, _opts)

    def georadius_ro(self, _key, _lng, _lan, _radius, _unit, _opts=None):
        return self.__this.call(f"georadius_ro", _key, _lng, _lan, _radius, _unit, _opts)

    def georadiusbymember(self, _key, _member, _radius, _unit, _opts=None):
        return self.__this.call(f"georadiusbymember", _key, _member, _radius, _unit, _opts)

    def georadiusbymember_ro(self, _key, _member, _radius, _unit, _opts=None):
        return self.__this.call(f"georadiusbymember_ro", _key, _member, _radius, _unit, _opts)

    def get(self, _key):
        return self.__this.call(f"get", _key)

    def getbit(self, _key, _offset):
        return self.__this.call(f"getbit", _key, _offset)

    def getlasterror(self):
        return self.__this.call(f"getlasterror", )

    def getmode(self):
        return self.__this.call(f"getmode", )

    def getoption(self, _option):
        return self.__this.call(f"getoption", _option)

    def getrange(self, _key, _start, _end):
        return self.__this.call(f"getrange", _key, _start, _end)

    def getset(self, _key, _value):
        return self.__this.call(f"getset", _key, _value)

    def hdel(self, _key, _member, _other_members=None):
        return self.__this.call(f"hdel", _key, _member, _other_members)

    def hexists(self, _key, _member):
        return self.__this.call(f"hexists", _key, _member)

    def hget(self, _key, _member):
        return self.__this.call(f"hget", _key, _member)

    def hgetall(self, _key):
        return self.__this.call(f"hgetall", _key)

    def hincrby(self, _key, _member, _value):
        return self.__this.call(f"hincrby", _key, _member, _value)

    def hincrbyfloat(self, _key, _member, _value):
        return self.__this.call(f"hincrbyfloat", _key, _member, _value)

    def hkeys(self, _key):
        return self.__this.call(f"hkeys", _key)

    def hlen(self, _key):
        return self.__this.call(f"hlen", _key)

    def hmget(self, _key, _keys):
        return self.__this.call(f"hmget", _key, _keys)

    def hmset(self, _key, _pairs):
        return self.__this.call(f"hmset", _key, _pairs)

    def hscan(self, _str_key, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"hscan", _str_key, _i_iterator, _str_pattern, _i_count)

    def hset(self, _key, _member, _value):
        return self.__this.call(f"hset", _key, _member, _value)

    def hsetnx(self, _key, _member, _value):
        return self.__this.call(f"hsetnx", _key, _member, _value)

    def hstrlen(self, _key, _member):
        return self.__this.call(f"hstrlen", _key, _member)

    def hvals(self, _key):
        return self.__this.call(f"hvals", _key)

    def incr(self, _key):
        return self.__this.call(f"incr", _key)

    def incrby(self, _key, _value):
        return self.__this.call(f"incrby", _key, _value)

    def incrbyfloat(self, _key, _value):
        return self.__this.call(f"incrbyfloat", _key, _value)

    def info(self, _key_or_address, _option=None):
        return self.__this.call(f"info", _key_or_address, _option)

    def keys(self, _pattern):
        return self.__this.call(f"keys", _pattern)

    def lastsave(self, _key_or_address):
        return self.__this.call(f"lastsave", _key_or_address)

    def lget(self, _key, _index):
        return self.__this.call(f"lget", _key, _index)

    def lindex(self, _key, _index):
        return self.__this.call(f"lindex", _key, _index)

    def linsert(self, _key, _position, _pivot, _value):
        return self.__this.call(f"linsert", _key, _position, _pivot, _value)

    def llen(self, _key):
        return self.__this.call(f"llen", _key)

    def lpop(self, _key):
        return self.__this.call(f"lpop", _key)

    def lpush(self, _key, _value):
        return self.__this.call(f"lpush", _key, _value)

    def lpushx(self, _key, _value):
        return self.__this.call(f"lpushx", _key, _value)

    def lrange(self, _key, _start, _end):
        return self.__this.call(f"lrange", _key, _start, _end)

    def lrem(self, _key, _value):
        return self.__this.call(f"lrem", _key, _value)

    def lset(self, _key, _index, _value):
        return self.__this.call(f"lset", _key, _index, _value)

    def ltrim(self, _key, _start, _stop):
        return self.__this.call(f"ltrim", _key, _start, _stop)

    def mget(self, _keys):
        return self.__this.call(f"mget", _keys)

    def mset(self, _pairs):
        return self.__this.call(f"mset", _pairs)

    def msetnx(self, _pairs):
        return self.__this.call(f"msetnx", _pairs)

    def multi(self):
        return self.__this.call(f"multi", )

    def object(self, _field, _key):
        return self.__this.call(f"object", _field, _key)

    def persist(self, _key):
        return self.__this.call(f"persist", _key)

    def pexpire(self, _key, _timestamp):
        return self.__this.call(f"pexpire", _key, _timestamp)

    def pexpireat(self, _key, _timestamp):
        return self.__this.call(f"pexpireat", _key, _timestamp)

    def pfadd(self, _key, _elements):
        return self.__this.call(f"pfadd", _key, _elements)

    def pfcount(self, _key):
        return self.__this.call(f"pfcount", _key)

    def pfmerge(self, _dstkey, _keys):
        return self.__this.call(f"pfmerge", _dstkey, _keys)

    def ping(self, _key_or_address):
        return self.__this.call(f"ping", _key_or_address)

    def psetex(self, _key, _expire, _value):
        return self.__this.call(f"psetex", _key, _expire, _value)

    def psubscribe(self, _patterns, _callback):
        return self.__this.call(f"psubscribe", _patterns, _callback)

    def pttl(self, _key):
        return self.__this.call(f"pttl", _key)

    def publish(self, _channel, _message):
        return self.__this.call(f"publish", _channel, _message)

    def pubsub(self, _key_or_address, _arg=None, _other_args=None):
        return self.__this.call(f"pubsub", _key_or_address, _arg, _other_args)

    def punsubscribe(self, _pattern, _other_patterns=None):
        return self.__this.call(f"punsubscribe", _pattern, _other_patterns)

    def randomkey(self, _key_or_address):
        return self.__this.call(f"randomkey", _key_or_address)

    def rawcommand(self, _cmd, _args=None):
        return self.__this.call(f"rawcommand", _cmd, _args)

    def rename(self, _key, _newkey):
        return self.__this.call(f"rename", _key, _newkey)

    def renamenx(self, _key, _newkey):
        return self.__this.call(f"renamenx", _key, _newkey)

    def restore(self, _ttl, _key, _value):
        return self.__this.call(f"restore", _ttl, _key, _value)

    def role(self):
        return self.__this.call(f"role", )

    def rpop(self, _key):
        return self.__this.call(f"rpop", _key)

    def rpoplpush(self, _src, _dst):
        return self.__this.call(f"rpoplpush", _src, _dst)

    def rpush(self, _key, _value):
        return self.__this.call(f"rpush", _key, _value)

    def rpushx(self, _key, _value):
        return self.__this.call(f"rpushx", _key, _value)

    def sadd(self, _key, _value):
        return self.__this.call(f"sadd", _key, _value)

    def saddarray(self, _key, _options):
        return self.__this.call(f"saddarray", _key, _options)

    def save(self, _key_or_address):
        return self.__this.call(f"save", _key_or_address)

    def scan(self, _i_iterator, _str_node, _str_pattern=None, _i_count=None):
        return self.__this.call(f"scan", _i_iterator, _str_node, _str_pattern, _i_count)

    def scard(self, _key):
        return self.__this.call(f"scard", _key)

    def script(self, _key_or_address, _arg=None, _other_args=None):
        return self.__this.call(f"script", _key_or_address, _arg, _other_args)

    def sdiff(self, _key, _other_keys=None):
        return self.__this.call(f"sdiff", _key, _other_keys)

    def sdiffstore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sdiffstore", _dst, _key, _other_keys)

    def set(self, _key, _value, _opts=None):
        return self.__this.call(f"set", _key, _value, _opts)

    def setbit(self, _key, _offset, _value):
        return self.__this.call(f"setbit", _key, _offset, _value)

    def setex(self, _key, _expire, _value):
        return self.__this.call(f"setex", _key, _expire, _value)

    def setnx(self, _key, _value):
        return self.__this.call(f"setnx", _key, _value)

    def setoption(self, _option, _value):
        return self.__this.call(f"setoption", _option, _value)

    def setrange(self, _key, _offset, _value):
        return self.__this.call(f"setrange", _key, _offset, _value)

    def sinter(self, _key, _other_keys=None):
        return self.__this.call(f"sinter", _key, _other_keys)

    def sinterstore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sinterstore", _dst, _key, _other_keys)

    def sismember(self, _key, _value):
        return self.__this.call(f"sismember", _key, _value)

    def slowlog(self, _key_or_address, _arg=None, _other_args=None):
        return self.__this.call(f"slowlog", _key_or_address, _arg, _other_args)

    def smembers(self, _key):
        return self.__this.call(f"smembers", _key)

    def smove(self, _src, _dst, _value):
        return self.__this.call(f"smove", _src, _dst, _value)

    def sort(self, _key, _options=None):
        return self.__this.call(f"sort", _key, _options)

    def spop(self, _key):
        return self.__this.call(f"spop", _key)

    def srandmember(self, _key, _count=None):
        return self.__this.call(f"srandmember", _key, _count)

    def srem(self, _key, _value):
        return self.__this.call(f"srem", _key, _value)

    def sscan(self, _str_key, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"sscan", _str_key, _i_iterator, _str_pattern, _i_count)

    def strlen(self, _key):
        return self.__this.call(f"strlen", _key)

    def subscribe(self, _channels, _callback):
        return self.__this.call(f"subscribe", _channels, _callback)

    def sunion(self, _key, _other_keys=None):
        return self.__this.call(f"sunion", _key, _other_keys)

    def sunionstore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sunionstore", _dst, _key, _other_keys)

    def time(self):
        return self.__this.call(f"time", )

    def ttl(self, _key):
        return self.__this.call(f"ttl", _key)

    def type(self, _key):
        return self.__this.call(f"type", _key)

    def unsubscribe(self, _channel, _other_channels=None):
        return self.__this.call(f"unsubscribe", _channel, _other_channels)

    def unlink(self, _key, _other_keys=None):
        return self.__this.call(f"unlink", _key, _other_keys)

    def unwatch(self):
        return self.__this.call(f"unwatch", )

    def watch(self, _key, _other_keys=None):
        return self.__this.call(f"watch", _key, _other_keys)

    def xack(self, _str_key, _str_group, _arr_ids):
        return self.__this.call(f"xack", _str_key, _str_group, _arr_ids)

    def xadd(self, _str_key, _str_id, _arr_fields, _i_maxlen=None, _boo_approximate=None):
        return self.__this.call(f"xadd", _str_key, _str_id, _arr_fields, _i_maxlen, _boo_approximate)

    def xclaim(self, _str_key, _str_group, _str_consumer, _i_min_idle, _arr_ids, _arr_opts=None):
        return self.__this.call(f"xclaim", _str_key, _str_group, _str_consumer, _i_min_idle, _arr_ids, _arr_opts)

    def xdel(self, _str_key, _arr_ids):
        return self.__this.call(f"xdel", _str_key, _arr_ids)

    def xgroup(self, _str_operation, _str_key=None, _str_arg1=None, _str_arg2=None, _str_arg3=None):
        return self.__this.call(f"xgroup", _str_operation, _str_key, _str_arg1, _str_arg2, _str_arg3)

    def xinfo(self, _str_cmd, _str_key=None, _str_group=None):
        return self.__this.call(f"xinfo", _str_cmd, _str_key, _str_group)

    def xlen(self, _key):
        return self.__this.call(f"xlen", _key)

    def xpending(self, _str_key, _str_group, _str_start=None, _str_end=None, _i_count=None, _str_consumer=None):
        return self.__this.call(f"xpending", _str_key, _str_group, _str_start, _str_end, _i_count, _str_consumer)

    def xrange(self, _str_key, _str_start, _str_end, _i_count=None):
        return self.__this.call(f"xrange", _str_key, _str_start, _str_end, _i_count)

    def xread(self, _arr_streams, _i_count=None, _i_block=None):
        return self.__this.call(f"xread", _arr_streams, _i_count, _i_block)

    def xreadgroup(self, _str_group, _str_consumer, _arr_streams, _i_count=None, _i_block=None):
        return self.__this.call(f"xreadgroup", _str_group, _str_consumer, _arr_streams, _i_count, _i_block)

    def xrevrange(self, _str_key, _str_start, _str_end, _i_count=None):
        return self.__this.call(f"xrevrange", _str_key, _str_start, _str_end, _i_count)

    def xtrim(self, _str_key, _i_maxlen, _boo_approximate=None):
        return self.__this.call(f"xtrim", _str_key, _i_maxlen, _boo_approximate)

    def zadd(self, _key, _score, _value, _extra_args=None):
        return self.__this.call(f"zadd", _key, _score, _value, _extra_args)

    def zcard(self, _key):
        return self.__this.call(f"zcard", _key)

    def zcount(self, _key, _min, _max):
        return self.__this.call(f"zcount", _key, _min, _max)

    def zincrby(self, _key, _value, _member):
        return self.__this.call(f"zincrby", _key, _value, _member)

    def zinterstore(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zinterstore", _key, _keys, _weights, _aggregate)

    def zlexcount(self, _key, _min, _max):
        return self.__this.call(f"zlexcount", _key, _min, _max)

    def zpopmax(self, _key):
        return self.__this.call(f"zpopmax", _key)

    def zpopmin(self, _key):
        return self.__this.call(f"zpopmin", _key)

    def zrange(self, _key, _start, _end, _scores=None):
        return self.__this.call(f"zrange", _key, _start, _end, _scores)

    def zrangebylex(self, _key, _min, _max, _offset=None, _limit=None):
        return self.__this.call(f"zrangebylex", _key, _min, _max, _offset, _limit)

    def zrangebyscore(self, _key, _start, _end, _options=None):
        return self.__this.call(f"zrangebyscore", _key, _start, _end, _options)

    def zrank(self, _key, _member):
        return self.__this.call(f"zrank", _key, _member)

    def zrem(self, _key, _member, _other_members=None):
        return self.__this.call(f"zrem", _key, _member, _other_members)

    def zremrangebylex(self, _key, _min, _max):
        return self.__this.call(f"zremrangebylex", _key, _min, _max)

    def zremrangebyrank(self, _key, _min, _max):
        return self.__this.call(f"zremrangebyrank", _key, _min, _max)

    def zremrangebyscore(self, _key, _min, _max):
        return self.__this.call(f"zremrangebyscore", _key, _min, _max)

    def zrevrange(self, _key, _start, _end, _scores=None):
        return self.__this.call(f"zrevrange", _key, _start, _end, _scores)

    def zrevrangebylex(self, _key, _min, _max, _offset=None, _limit=None):
        return self.__this.call(f"zrevrangebylex", _key, _min, _max, _offset, _limit)

    def zrevrangebyscore(self, _key, _start, _end, _options=None):
        return self.__this.call(f"zrevrangebyscore", _key, _start, _end, _options)

    def zrevrank(self, _key, _member):
        return self.__this.call(f"zrevrank", _key, _member)

    def zscan(self, _str_key, _i_iterator, _str_pattern=None, _i_count=None):
        return self.__this.call(f"zscan", _str_key, _i_iterator, _str_pattern, _i_count)

    def zscore(self, _key, _member):
        return self.__this.call(f"zscore", _key, _member)

    def zunionstore(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zunionstore", _key, _keys, _weights, _aggregate)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RedisSentinel():

    def __init__(self, _host, _port=None, _timeout=None, _persistent=None, _retry_interval=None, _read_timeout=None):
        self.__this = phpy.Object(f'RedisSentinel', _host, _port, _timeout, _persistent, _retry_interval, _read_timeout)

    def ckquorum(self, _value):
        return self.__this.call(f"ckquorum", _value)

    def failover(self, _value):
        return self.__this.call(f"failover", _value)

    def flushconfig(self):
        return self.__this.call(f"flushconfig", )

    def getMasterAddrByName(self, _value):
        return self.__this.call(f"getMasterAddrByName", _value)

    def master(self, _value):
        return self.__this.call(f"master", _value)

    def masters(self):
        return self.__this.call(f"masters", )

    def ping(self):
        return self.__this.call(f"ping", )

    def reset(self, _value):
        return self.__this.call(f"reset", _value)

    def sentinels(self, _value):
        return self.__this.call(f"sentinels", _value)

    def slaves(self, _value):
        return self.__this.call(f"slaves", _value)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RedisException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'RedisException', _message, _code, _previous)

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

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RedisClusterException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'RedisClusterException', _message, _code, _previous)

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

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

