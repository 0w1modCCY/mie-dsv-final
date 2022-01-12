import argparse
from concurrent import futures

import grpc

import eager_pb2
import eager_pb2_grpc
from data_logger import Logger as log

def to_string(array):
    string = "" + array[0]
    array.pop(0)
    for node in array:
        string = ", " + node


class General:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver


class Last:
    def __init__(self, leader):
        self.leader = leader


class EagerServicer(eager_pb2_grpc.EagerServicer):
    def __init__(self, node):
        super(EagerServicer, self).__init__()
        self.node = node

    def Send(self, request, context):
        log.log_sent(self.node.value, self.node.receiver)

        return eager_pb2.Empty()

    def End(self, request, context):
        log.log_finish(self.node.value)

        return eager_pb2.Empty()


class Node:
    def __init__(self, value, nodes):
        self.next = None
        self.value = value  # int
        self.nodes = nodes  # list of ints
        self.servicer = EagerServicer(self)

        if len(nodes) < 2:
            self.send_finish(self.value)

        self.receiver = nodes[nodes.index(self.value) + 1]

    def send_message(self, sender, receiver, nodes):
        with grpc.insecure_channel('localhost:' + str(50280)) as channel:
            stub = eager_pb2_grpc.EagerStub(channel)
            stub.Send(eager_pb2.General(sender=sender, receiver=receiver, nodes=nodes))

    def send_finish(self, leader):
        with grpc.insecure_channel('localhost:' + str(50280)) as channel:
            stub = eager_pb2_grpc.EagerStub(channel)
            stub.End(eager_pb2.Last(leader=leader))

    def serve(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        eager_pb2_grpc.add_EagerServicer_to_server(self.servicer, server)
        server.add_insecure_port('[::]:' + str(50280))
        server.start()

        if self.value < self.receiver:
            self.nodes.remove(self.receiver)

        if len(self.nodes) == 2:
            self.receiver = self.nodes[1]
            self.next = self.nodes[0]

        else:
            index = self.nodes.index(self.value)
            self.receiver = self.nodes[index + 1]
            self.next = self.nodes[index + 1]

        self.send_message(self.receiver, self.next, to_string(self.nodes))

        server.stop(None)
        exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Node creation')
    parser.add_argument("-v", "--value", required=True, type=int, help="Node value")
    parser.add_argument("-n", "--nodes", nargs='*', required=True, help="Nodes left in the topology")
    args = vars(parser.parse_args())

    value = args['value']
    n = args['nodes'][0]
    nodes = n.split(',')

    Node = Node(value, nodes)
    Node.serve()
