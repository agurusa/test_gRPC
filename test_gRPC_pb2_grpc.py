# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import test_gRPC_pb2 as test__gRPC__pb2


class test_gRPCStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeature = channel.unary_unary(
        '/test_gRPC.test_gRPC/GetFeature',
        request_serializer=test__gRPC__pb2.An_unexciting_request.SerializeToString,
        response_deserializer=test__gRPC__pb2.An_exciting_response.FromString,
        )


class test_gRPCServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetFeature(self, request, context):
    """simple RPC where client sends a request to a server using the stub and waits for a response to come back.
    rpc GetFeature(An_unexciting_request) returns (An_unexciting_request){}
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_test_gRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeature': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeature,
          request_deserializer=test__gRPC__pb2.An_unexciting_request.FromString,
          response_serializer=test__gRPC__pb2.An_exciting_response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'test_gRPC.test_gRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
