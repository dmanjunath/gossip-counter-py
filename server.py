import grpc
from concurrent import futures
import sys
import gossip_pb2, gossip_pb2_grpc
from peers import Peers

class GossipServiceServicer(gossip_pb2_grpc.GossipServiceServicer):
    def __init__(self):
        self.counter = 0

    def Increment(self, request, context):
        self.counter += 1
        return gossip_pb2.IncrementResponse(success=True)

    def GetGossipCount(self, request, context):
        return gossip_pb2.GetCountResponse(count=self.counter)

def serve(node_id):
    Peers.verify_peer_id(node_id)
    port = Peers.peer_ids[node_id]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gossip_pb2_grpc.add_GossipServiceServicer_to_server(GossipServiceServicer(), server)
    server.add_insecure_port(f'[::]{port}')
    server.start()
    print(f"Server listening at [::]{port}")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <node_id>")
        sys.exit(1)

    node_id = int(sys.argv[1])
    serve(node_id)
