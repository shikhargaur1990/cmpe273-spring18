import zmq
import threading
import sys
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sub = context.socket(zmq.SUB)
push = context.socket(zmq.PUSH)

# Define subscription and messages with prefix to accept.
sub.setsockopt_string(zmq.SUBSCRIBE, "1")
sub.connect("tcp://127.0.0.1:5681")

push.connect("tcp://127.0.0.1:5680")


class display(threading.Thread):
    def __init__(self):
      threading.Thread.__init__(self)
      print('User ['+sys.argv[1] +'] Connected to the chat server')
    
    def run(self):
        while(True):
            data=sub.recv()
            data=data.decode('utf-8').split(">>")
            if(data[1].strip()!=name):
                 print("\n"+data[1]+":"+data[2])
d=display()
d.start()

name=sys.argv[1]

while (True):
    message=input("["+name+"]>")
    data={'name':name,'message':message}
    push.send_json(data)