from php import redis

db = redis.Redis()
db.connect("127.0.0.1", 6379, -1)
db.set("key", "swoole")
print(db.get("key"))
