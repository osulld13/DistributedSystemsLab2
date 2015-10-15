import sys
import socket
import threadpool
import os

# global threadpool for server
server_thread_pool = threadpool.ThreadPool(40)

port_num = int(sys.argv[1])

def create_server_socket():
    # create socket  and initialise to localhost:8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", port_num)

    print "starting up on %s port %s\n" % server_address

    # bind socket to server address and wait for incoming connections4
    sock.bind(server_address)
    sock.listen(1)

    while True:
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
        data = connection.recv(1024)
        print "received message: %s" % data

        # Respond to the appropriate message
        if data == "KILL_SERVICE\n":
            # Kill service
            response = "Killing Service\n"
            connection.sendall("%s" % response)
            os._exit(0)
        elif data[0:4] == "HELO" and data[-1] == '\n':
            # Respond to HELO message
            # Construct the appropriate response
            response = data
            response += "IP:[" + socket.gethostbyname(socket.gethostname()) + "]\n"
            response += "Port:[" + str(port_num) +"]\n"
            response += "StudentID:[12308492]\n"
            connection.sendall("%s" % response)

    finally:
        connection.close()

if __name__ == '__main__':
    create_server_socket()
    #wait for threads to complete
    server_thread_pool.wait_completion()
