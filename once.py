
from bge import logic as gl

from oscpy.client import OSCClient
from oscpy.server import OSCThreadServer

def on_action(action):
    gl.action = 1 if action == 1 else -1
    gl.action_new = 1

def on_reset(*args):
    gl.reset = args
    gl.num_reset = 0

def osc_server_init():
    gl.server = OSCThreadServer()
    gl.server.listen('localhost', port=8001, default=True)
    # Les callbacks du serveur
    gl.server.bind(b'/action', on_action)
    gl.server.bind(b'/reset', on_reset)

def main():
    print("Lancement de once.py ...")

    gl.action = 0
    gl.action_new = 0
    gl.reset = 0
    gl.num_reset = 0
    gl.server = None

    osc_server_init()
    # Un client pour envoyer sur la même machine
    gl.client = OSCClient(b'localhost', 8003)

main()
