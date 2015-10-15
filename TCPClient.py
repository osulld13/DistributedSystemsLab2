import socket
import sys
import threadpool

from random import randint

# this is a multithreaded client program that was used to test
# the server code

client_thread_pool = threadpool.ThreadPool(20)

# A list containing a series of potential server messages for testing
messages = [
    "HELO\n",
    "HELO tesasdfasdft \n",
    "KILL_SERVICE\n",
    "A message for testing\n",
    "Another message for testing\n",
]

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
    # Send random message from global list of messages
    message = messages[randint(0, 4)]

    # create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8000)
    sock.connect(server_address)

    # send message
    sock.send(message)

    # receive and print response
    data = sock.recv(1024)
    print data

    # close socket
    sock.close()

if __name__ == '__main__':
    # Main line for program
    # Create 20 tasks that send messages to the server
    for x in range(0, int(sys.argv[1])):
        client_thread_pool.add_task(
            connect_to_server_auto
        )
    # wait for threads to complete before finishing program
    client_thread_pool.wait_completion()
