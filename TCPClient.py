import socket
import sys
import threadpool

# this is a multithreaded client program that was used to test
# the server code

client_thread_pool = threadpool.ThreadPool(20)

def connect_to_server_userin():
    user_in = raw_input("input your message:\n>> ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8000)
    sock.connect(server_address)

    sock.send(user_in)

    data = sock.recv(1024)
    print data

    sock.close()

# Sends test from the client
def connect_to_server_auto():
    user_in = "test message\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8000)
    sock.connect(server_address)

    sock.send(user_in)

    data = sock.recv(1024)
    print data

    sock.close()

if __name__ == '__main__':
    # Main line for program
    # Create 20 tasks that send messages to the server
    for x in range(0, 200):
        client_thread_pool.add_task(
            connect_to_server_auto
        )
