#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import test_urls

context = zmq.Context()

#  Socket to talk to server
print("Connecting to image scraper server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Encode the list of URLs into a byte string and send
print(f"Sending data …")
data = test_urls.test_list().encode()
socket.send(data)

#  Get the reply.
message = socket.recv()
print(f"Received reply [ {message} ]")