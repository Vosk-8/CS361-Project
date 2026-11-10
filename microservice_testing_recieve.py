import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)  # I make requests

socket.connect("tcp://localhost:5555") #connects to set port

socket.send_string("Requesting message from message service...") # send the request

reply = socket.recv_string() # wait for reply

print(reply)