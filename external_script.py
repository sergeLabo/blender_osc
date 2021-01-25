
from oscpy.client import OSCClient
from oscpy.server import OSCThreadServer


def on_result(arg):
    print("waouh ...", arg)

server = OSCThreadServer()
server.listen('localhost', port=8003, default=True)
server.bind(b'/result', on_result)

client = OSCClient(b'localhost', 8001)

toto = 0
while 1:
    if toto % 2 == 0:
        client.send_message(b'/action', [toto])
    else:
        client.send_message(b'/reset', [toto])
    toto += 1
