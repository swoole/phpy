from php import swoole


def on_receive(serv, fd, tid, data):
    print(serv)
    print(data)
    s.send(fd, "Swoole: " + data)


s = swoole.Server("127.0.0.1", 9501)
s.on('receive', on_receive)
s.start()
