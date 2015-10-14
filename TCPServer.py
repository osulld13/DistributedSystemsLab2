import sys
import socket
import threadpool

# global threadpool for server
server_thread_pool = threadpool.ThreadPool(40)

# get local ip with following function
# socket.gethostbyname(socket.gethostname())

def create_server_socket():
    # create socket  and initialise to localhost:8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8000)

    print "starting up on %s port %s\n" % server_address

    # bind socket to server address and wait for incoming connections4
    sock.bind(server_address)
    sock.listen(1)

    while True:
        print "waiting for a connection\n"
        # sock.accept returns a 2 element tuple
        connection, client_address = sock.accept()
        # Hand the client interaction off to a seperate thread
        server_thread_pool.add_task(
            start_client_interaction,
            connection,
            client_address
        )


def start_client_interaction(connection, client_address):
    try:
        data = connection.recv(16)
        print "received message: %s" % data
        print "sending back message"
        connection.sendall("message received")

    finally:
        connection.close()

if __name__ == '__main__':
    create_server_socket()
