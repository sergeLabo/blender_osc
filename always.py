
from bge import logic as gl

def main():

    print("gl.reset =", gl.reset)
    print("gl.action =", gl.action)

    gl.client.send_message(b'/result', [1])


main()
