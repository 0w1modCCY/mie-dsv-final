# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import eager_pb2 as eager__pb2


class EagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Send = channel.unary_unary(
                '/Eager/Send',
                request_serializer=eager__pb2.General.SerializeToString,
                response_deserializer=eager__pb2.Empty.FromString,
                )
        self.End = channel.unary_unary(
                '/Eager/End',
                request_serializer=eager__pb2.Last.SerializeToString,
                response_deserializer=eager__pb2.Empty.FromString,
                )


class EagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Send(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def End(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Send': grpc.unary_unary_rpc_method_handler(
                    servicer.Send,
                    request_deserializer=eager__pb2.General.FromString,
                    response_serializer=eager__pb2.Empty.SerializeToString,
            ),
            'End': grpc.unary_unary_rpc_method_handler(
                    servicer.End,
                    request_deserializer=eager__pb2.Last.FromString,
                    response_serializer=eager__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Eager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Eager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Eager/Send',
            eager__pb2.General.SerializeToString,
            eager__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def End(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Eager/End',
            eager__pb2.Last.SerializeToString,
            eager__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
