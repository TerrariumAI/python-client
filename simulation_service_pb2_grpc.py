# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import simulation_service_pb2 as simulation__service__pb2


class SimulationServiceStub(object):
  """Service to manage simulation
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateAgent = channel.unary_unary(
        '/v1.SimulationService/CreateAgent',
        request_serializer=simulation__service__pb2.CreateAgentRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.CreateAgentResponse.FromString,
        )
    self.GetEntity = channel.unary_unary(
        '/v1.SimulationService/GetEntity',
        request_serializer=simulation__service__pb2.GetEntityRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.GetEntityResponse.FromString,
        )
    self.DeleteAgent = channel.unary_unary(
        '/v1.SimulationService/DeleteAgent',
        request_serializer=simulation__service__pb2.DeleteAgentRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.DeleteAgentResponse.FromString,
        )
    self.ExecuteAgentAction = channel.unary_unary(
        '/v1.SimulationService/ExecuteAgentAction',
        request_serializer=simulation__service__pb2.ExecuteAgentActionRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.ExecuteAgentActionResponse.FromString,
        )
    self.GetAgentObservation = channel.unary_unary(
        '/v1.SimulationService/GetAgentObservation',
        request_serializer=simulation__service__pb2.GetAgentObservationRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.GetAgentObservationResponse.FromString,
        )
    self.ResetWorld = channel.unary_unary(
        '/v1.SimulationService/ResetWorld',
        request_serializer=simulation__service__pb2.ResetWorldRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.ResetWorldResponse.FromString,
        )
    self.CreateSpectator = channel.unary_stream(
        '/v1.SimulationService/CreateSpectator',
        request_serializer=simulation__service__pb2.CreateSpectatorRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.SpectateResponse.FromString,
        )
    self.SubscribeSpectatorToRegion = channel.unary_unary(
        '/v1.SimulationService/SubscribeSpectatorToRegion',
        request_serializer=simulation__service__pb2.SubscribeSpectatorToRegionRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.SubscribeSpectatorToRegionResponse.FromString,
        )
    self.UnsubscribeSpectatorFromRegion = channel.unary_unary(
        '/v1.SimulationService/UnsubscribeSpectatorFromRegion',
        request_serializer=simulation__service__pb2.UnsubscribeSpectatorFromRegionRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.UnsubscribeSpectatorFromRegionResponse.FromString,
        )
    self.CreateRemoteModel = channel.unary_stream(
        '/v1.SimulationService/CreateRemoteModel',
        request_serializer=simulation__service__pb2.CreateRemoteModelRequest.SerializeToString,
        response_deserializer=simulation__service__pb2.Observation.FromString,
        )


class SimulationServiceServicer(object):
  """Service to manage simulation
  """

  def CreateAgent(self, request, context):
    """Create new agent
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEntity(self, request, context):
    """Get data for an entity
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAgent(self, request, context):
    """Delete an agent
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecuteAgentAction(self, request, context):
    """Perform an action for an agent
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAgentObservation(self, request, context):
    """Get the observation for an agent
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetWorld(self, request, context):
    """Reset the world
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateSpectator(self, request, context):
    """Create a new spectator stream
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeSpectatorToRegion(self, request, context):
    """Subscribe the spectator of given id to a region
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnsubscribeSpectatorFromRegion(self, request, context):
    """Subscribe the spectator of given id to a region
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateRemoteModel(self, request, context):
    """Create a remote model
    Receives Agent Action Execution requests
    Returns observations
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimulationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateAgent': grpc.unary_unary_rpc_method_handler(
          servicer.CreateAgent,
          request_deserializer=simulation__service__pb2.CreateAgentRequest.FromString,
          response_serializer=simulation__service__pb2.CreateAgentResponse.SerializeToString,
      ),
      'GetEntity': grpc.unary_unary_rpc_method_handler(
          servicer.GetEntity,
          request_deserializer=simulation__service__pb2.GetEntityRequest.FromString,
          response_serializer=simulation__service__pb2.GetEntityResponse.SerializeToString,
      ),
      'DeleteAgent': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAgent,
          request_deserializer=simulation__service__pb2.DeleteAgentRequest.FromString,
          response_serializer=simulation__service__pb2.DeleteAgentResponse.SerializeToString,
      ),
      'ExecuteAgentAction': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteAgentAction,
          request_deserializer=simulation__service__pb2.ExecuteAgentActionRequest.FromString,
          response_serializer=simulation__service__pb2.ExecuteAgentActionResponse.SerializeToString,
      ),
      'GetAgentObservation': grpc.unary_unary_rpc_method_handler(
          servicer.GetAgentObservation,
          request_deserializer=simulation__service__pb2.GetAgentObservationRequest.FromString,
          response_serializer=simulation__service__pb2.GetAgentObservationResponse.SerializeToString,
      ),
      'ResetWorld': grpc.unary_unary_rpc_method_handler(
          servicer.ResetWorld,
          request_deserializer=simulation__service__pb2.ResetWorldRequest.FromString,
          response_serializer=simulation__service__pb2.ResetWorldResponse.SerializeToString,
      ),
      'CreateSpectator': grpc.unary_stream_rpc_method_handler(
          servicer.CreateSpectator,
          request_deserializer=simulation__service__pb2.CreateSpectatorRequest.FromString,
          response_serializer=simulation__service__pb2.SpectateResponse.SerializeToString,
      ),
      'SubscribeSpectatorToRegion': grpc.unary_unary_rpc_method_handler(
          servicer.SubscribeSpectatorToRegion,
          request_deserializer=simulation__service__pb2.SubscribeSpectatorToRegionRequest.FromString,
          response_serializer=simulation__service__pb2.SubscribeSpectatorToRegionResponse.SerializeToString,
      ),
      'UnsubscribeSpectatorFromRegion': grpc.unary_unary_rpc_method_handler(
          servicer.UnsubscribeSpectatorFromRegion,
          request_deserializer=simulation__service__pb2.UnsubscribeSpectatorFromRegionRequest.FromString,
          response_serializer=simulation__service__pb2.UnsubscribeSpectatorFromRegionResponse.SerializeToString,
      ),
      'CreateRemoteModel': grpc.unary_stream_rpc_method_handler(
          servicer.CreateRemoteModel,
          request_deserializer=simulation__service__pb2.CreateRemoteModelRequest.FromString,
          response_serializer=simulation__service__pb2.Observation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v1.SimulationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
