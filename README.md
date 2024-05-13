## gossip-counter-py

#### Overview
Build a distributed counter such that a message can be sent to any counter node and the count will be incremented across all nodes.

There will be 3 node servers as well as a client script that can send a increment request to one of the 3 node servers. The data model and logic for how the node servers replicate this data amongst themselves is what you'll modify and entirely up to you.

You can decide the constraints and trade offs of the system, favoring higher consistency or availability and the behavior of network partitions. There's no right answer here, different use cases could warrant different criteria.

Things to note:
- Right now all nodes in this system can accept incoming requests, if you want to add a leader, that's your choice
- Assume all peer servers are trusted

#### Dependencies
- python3

#### Setup
Create a virtualenv
```
python3 -m venv .
source bin/activate
pip3 install -r requirements.txt
```

Generate protocol buffer files
```
python -m grpc_tools.protoc -I. --python_out=./ --grpc_python_out=./ gossip.proto
```

#### Running
Open two new tabs
```
# tab 1
# node id can be 1-3
python3 server.py <node-id>

# tab 2
# node id can be 1-3
# action can be 'increment' or 'getCount'
python3 client.py <node-id> <action>
```