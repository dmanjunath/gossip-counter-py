import grpc
import sys
import gossip_pb2, gossip_pb2_grpc
from peers import Peers

def run(node_id, action):
    peer_target = Peers.get_peer_target(node_id)
    with grpc.insecure_channel(peer_target) as channel:
        stub = gossip_pb2_grpc.GossipServiceStub(channel)
        if action == "increment":
            response = stub.Increment(gossip_pb2.GossipMessage())
            print("Increment success:", response.success)
        elif action == "getCount":
            response = stub.GetGossipCount(gossip_pb2.GossipMessage())
            print("Gossip count:", response.count)
        else:
            print("Invalid action:", action)
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <node_id> <action>")
        sys.exit(1)

    node_id = int(sys.argv[1])
    action = sys.argv[2]
    run(node_id, action)
