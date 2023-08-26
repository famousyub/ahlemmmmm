# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from common import minionn_onnx_pb2 as minionn__onnx__pb2


class MinioNNStub(object):
  """The service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Precomputation = channel.unary_unary(
        '/minionn.MinioNN/Precomputation',
        request_serializer=minionn__onnx__pb2.PrecomputationRequest.SerializeToString,
        response_deserializer=minionn__onnx__pb2.PrecomputationResponse.FromString,
        )
    self.Computation = channel.unary_unary(
        '/minionn.MinioNN/Computation',
        request_serializer=minionn__onnx__pb2.ComputationRequest.SerializeToString,
        response_deserializer=minionn__onnx__pb2.ComputationResponse.FromString,
        )


class MinioNNServicer(object):
  """The service definition.
  """

  def Precomputation(self, request, context):
    """Precomputation service - requests ONNX format, ~w
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Computation(self, request, context):
    """Computation message - sends ~u and x_s and receives y_s
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MinioNNServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Precomputation': grpc.unary_unary_rpc_method_handler(
          servicer.Precomputation,
          request_deserializer=minionn__onnx__pb2.PrecomputationRequest.FromString,
          response_serializer=minionn__onnx__pb2.PrecomputationResponse.SerializeToString,
      ),
      'Computation': grpc.unary_unary_rpc_method_handler(
          servicer.Computation,
          request_deserializer=minionn__onnx__pb2.ComputationRequest.FromString,
          response_serializer=minionn__onnx__pb2.ComputationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'minionn.MinioNN', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
