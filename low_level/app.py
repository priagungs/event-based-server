from __future__ import print_function

import signal
import pyuv
import os


def readFile(path):
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\..\\files\\' + path[1:]) as f:
        return f.read()

def on_read(client, data, error):
    if data is None:
        client.close()
        clients.remove(client)
        return
    data_str = str(data)
    content = readFile(data_str.split()[1])
    response = 'HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n{}'.format(len(content), content)
    client.write(bytes(response, 'utf-8'))


def on_connection(server, error):
    client = pyuv.TCP(server.loop)
    server.accept(client)
    clients.append(client)
    client.start_read(on_read)


def signal_cb(handle, signum):
    [c.close() for c in clients]
    signal_h.close()
    server.close()


print("PyUV version %s" % pyuv.__version__)

loop = pyuv.Loop.default_loop()
clients = []

server = pyuv.TCP(loop)
server.bind(("0.0.0.0", 1234))
server.listen(on_connection)

signal_h = pyuv.Signal(loop)
signal_h.start(signal_cb, signal.SIGINT)

loop.run()
print("Stopped!")
