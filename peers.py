class Peers:
    peer_ids = {1: ":50051", 2: ":50052", 3: ":50053"}

    @staticmethod
    def get_peers():
        return ["localhost" + port for port in Peers.peer_ids.values()]

    @staticmethod
    def verify_peer_id(node_id):
        if node_id not in Peers.peer_ids:
            raise ValueError(f"Invalid node id: {node_id}")

    @staticmethod
    def get_peer_target(node_id):
        Peers.verify_peer_id(node_id)
        return f"localhost{Peers.peer_ids[node_id]}"
