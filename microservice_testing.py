import zmq


context = zmq.Context() # creates the ZeroMQ environment that the program needs.

socket = context.socket(zmq.REP) # I reply to requests

socket.bind("tcp://*:5555") # open port 5555

print("Message sender running...")


while True:
    r_message = socket.recv_string() # wait here until a request arrives
    print(f"Got request:{r_message}")

    sent_message = "This is a message from CS361"
    socket.send_string(sent_message) # send the reply
