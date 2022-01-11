from concurrent import futures

import grpc

import eager.eager_pb2_grpc


class General:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver


class Last:
    def __init__(self, leader):
        self.leader = leader


class EagerServicer(eager.eager_pb2_grpc.EagerServicer):

class Node:
    def __init__(self, value, nodes):
        self.value = value   # int
        self.nodes = nodes   # list of ints

        if len(nodes) < 2:
            send_finish(Last(leader=self.value))

        self.receiver = nodes[nodes.index(self.value) + 1]
        self.servicer = EagerServicer(self)

    def send_message(self, message):

    def send_finish(self, message):

    def serve(self):
        server = grpc.server(futures.TheadPoolExecutor(max_workers=10))




if __name__ == "__main__":
