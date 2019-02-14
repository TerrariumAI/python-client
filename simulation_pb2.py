# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simulation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simulation.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10simulation.proto\x12\x02pb\")\n\x11SpawnAgentRequest\x12\t\n\x01X\x18\x01 \x01(\x05\x12\t\n\x01Y\x18\x02 \x01(\x05\"\x1e\n\x10SpawnAgentResult\x12\n\n\x02Id\x18\x01 \x01(\t\"%\n\x17\x41gentObservationRequest\x12\n\n\x02Id\x18\x01 \x01(\t\"V\n\x16\x41gentObservationResult\x12\r\n\x05\x41live\x18\x01 \x01(\x08\x12\r\n\x05\x43\x65lls\x18\x02 \x03(\t\x12\x0e\n\x06\x45nergy\x18\x03 \x01(\x05\x12\x0e\n\x06Health\x18\x04 \x01(\x05\"C\n\x12\x41gentActionRequest\x12\n\n\x02Id\x18\x01 \x01(\t\x12\x0e\n\x06\x41\x63tion\x18\x02 \x01(\t\x12\x11\n\tDirection\x18\x03 \x01(\t\"\'\n\x11\x41gentActionResult\x12\x12\n\nSuccessful\x18\x01 \x01(\x08\"\x13\n\x11ResetWorldRequest\"\x12\n\x10ResetWorldResult\"\x11\n\x0fSpectateRequest\"4\n\nCellUpdate\x12\t\n\x01X\x18\x01 \x01(\x05\x12\t\n\x01Y\x18\x02 \x01(\x05\x12\x10\n\x08Occupant\x18\x03 \x01(\t2\xca\x02\n\nSimulation\x12;\n\nSpawnAgent\x12\x15.pb.SpawnAgentRequest\x1a\x14.pb.SpawnAgentResult\"\x00\x12M\n\x10\x41gentObservation\x12\x1b.pb.AgentObservationRequest\x1a\x1a.pb.AgentObservationResult\"\x00\x12>\n\x0b\x41gentAction\x12\x16.pb.AgentActionRequest\x1a\x15.pb.AgentActionResult\"\x00\x12;\n\nResetWorld\x12\x15.pb.ResetWorldRequest\x1a\x14.pb.ResetWorldResult\"\x00\x12\x33\n\x08Spectate\x12\x13.pb.SpectateRequest\x1a\x0e.pb.CellUpdate\"\x00\x30\x01\x62\x06proto3')
)




_SPAWNAGENTREQUEST = _descriptor.Descriptor(
  name='SpawnAgentRequest',
  full_name='pb.SpawnAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='X', full_name='pb.SpawnAgentRequest.X', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Y', full_name='pb.SpawnAgentRequest.Y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=65,
)


_SPAWNAGENTRESULT = _descriptor.Descriptor(
  name='SpawnAgentResult',
  full_name='pb.SpawnAgentResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='pb.SpawnAgentResult.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=97,
)


_AGENTOBSERVATIONREQUEST = _descriptor.Descriptor(
  name='AgentObservationRequest',
  full_name='pb.AgentObservationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='pb.AgentObservationRequest.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=136,
)


_AGENTOBSERVATIONRESULT = _descriptor.Descriptor(
  name='AgentObservationResult',
  full_name='pb.AgentObservationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Alive', full_name='pb.AgentObservationResult.Alive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Cells', full_name='pb.AgentObservationResult.Cells', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Energy', full_name='pb.AgentObservationResult.Energy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Health', full_name='pb.AgentObservationResult.Health', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=224,
)


_AGENTACTIONREQUEST = _descriptor.Descriptor(
  name='AgentActionRequest',
  full_name='pb.AgentActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='pb.AgentActionRequest.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Action', full_name='pb.AgentActionRequest.Action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Direction', full_name='pb.AgentActionRequest.Direction', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=293,
)


_AGENTACTIONRESULT = _descriptor.Descriptor(
  name='AgentActionResult',
  full_name='pb.AgentActionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Successful', full_name='pb.AgentActionResult.Successful', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=334,
)


_RESETWORLDREQUEST = _descriptor.Descriptor(
  name='ResetWorldRequest',
  full_name='pb.ResetWorldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=355,
)


_RESETWORLDRESULT = _descriptor.Descriptor(
  name='ResetWorldResult',
  full_name='pb.ResetWorldResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=375,
)


_SPECTATEREQUEST = _descriptor.Descriptor(
  name='SpectateRequest',
  full_name='pb.SpectateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=377,
  serialized_end=394,
)


_CELLUPDATE = _descriptor.Descriptor(
  name='CellUpdate',
  full_name='pb.CellUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='X', full_name='pb.CellUpdate.X', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Y', full_name='pb.CellUpdate.Y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Occupant', full_name='pb.CellUpdate.Occupant', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=396,
  serialized_end=448,
)

DESCRIPTOR.message_types_by_name['SpawnAgentRequest'] = _SPAWNAGENTREQUEST
DESCRIPTOR.message_types_by_name['SpawnAgentResult'] = _SPAWNAGENTRESULT
DESCRIPTOR.message_types_by_name['AgentObservationRequest'] = _AGENTOBSERVATIONREQUEST
DESCRIPTOR.message_types_by_name['AgentObservationResult'] = _AGENTOBSERVATIONRESULT
DESCRIPTOR.message_types_by_name['AgentActionRequest'] = _AGENTACTIONREQUEST
DESCRIPTOR.message_types_by_name['AgentActionResult'] = _AGENTACTIONRESULT
DESCRIPTOR.message_types_by_name['ResetWorldRequest'] = _RESETWORLDREQUEST
DESCRIPTOR.message_types_by_name['ResetWorldResult'] = _RESETWORLDRESULT
DESCRIPTOR.message_types_by_name['SpectateRequest'] = _SPECTATEREQUEST
DESCRIPTOR.message_types_by_name['CellUpdate'] = _CELLUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpawnAgentRequest = _reflection.GeneratedProtocolMessageType('SpawnAgentRequest', (_message.Message,), dict(
  DESCRIPTOR = _SPAWNAGENTREQUEST,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.SpawnAgentRequest)
  ))
_sym_db.RegisterMessage(SpawnAgentRequest)

SpawnAgentResult = _reflection.GeneratedProtocolMessageType('SpawnAgentResult', (_message.Message,), dict(
  DESCRIPTOR = _SPAWNAGENTRESULT,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.SpawnAgentResult)
  ))
_sym_db.RegisterMessage(SpawnAgentResult)

AgentObservationRequest = _reflection.GeneratedProtocolMessageType('AgentObservationRequest', (_message.Message,), dict(
  DESCRIPTOR = _AGENTOBSERVATIONREQUEST,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.AgentObservationRequest)
  ))
_sym_db.RegisterMessage(AgentObservationRequest)

AgentObservationResult = _reflection.GeneratedProtocolMessageType('AgentObservationResult', (_message.Message,), dict(
  DESCRIPTOR = _AGENTOBSERVATIONRESULT,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.AgentObservationResult)
  ))
_sym_db.RegisterMessage(AgentObservationResult)

AgentActionRequest = _reflection.GeneratedProtocolMessageType('AgentActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _AGENTACTIONREQUEST,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.AgentActionRequest)
  ))
_sym_db.RegisterMessage(AgentActionRequest)

AgentActionResult = _reflection.GeneratedProtocolMessageType('AgentActionResult', (_message.Message,), dict(
  DESCRIPTOR = _AGENTACTIONRESULT,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.AgentActionResult)
  ))
_sym_db.RegisterMessage(AgentActionResult)

ResetWorldRequest = _reflection.GeneratedProtocolMessageType('ResetWorldRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESETWORLDREQUEST,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.ResetWorldRequest)
  ))
_sym_db.RegisterMessage(ResetWorldRequest)

ResetWorldResult = _reflection.GeneratedProtocolMessageType('ResetWorldResult', (_message.Message,), dict(
  DESCRIPTOR = _RESETWORLDRESULT,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.ResetWorldResult)
  ))
_sym_db.RegisterMessage(ResetWorldResult)

SpectateRequest = _reflection.GeneratedProtocolMessageType('SpectateRequest', (_message.Message,), dict(
  DESCRIPTOR = _SPECTATEREQUEST,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.SpectateRequest)
  ))
_sym_db.RegisterMessage(SpectateRequest)

CellUpdate = _reflection.GeneratedProtocolMessageType('CellUpdate', (_message.Message,), dict(
  DESCRIPTOR = _CELLUPDATE,
  __module__ = 'simulation_pb2'
  # @@protoc_insertion_point(class_scope:pb.CellUpdate)
  ))
_sym_db.RegisterMessage(CellUpdate)



_SIMULATION = _descriptor.ServiceDescriptor(
  name='Simulation',
  full_name='pb.Simulation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=451,
  serialized_end=781,
  methods=[
  _descriptor.MethodDescriptor(
    name='SpawnAgent',
    full_name='pb.Simulation.SpawnAgent',
    index=0,
    containing_service=None,
    input_type=_SPAWNAGENTREQUEST,
    output_type=_SPAWNAGENTRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AgentObservation',
    full_name='pb.Simulation.AgentObservation',
    index=1,
    containing_service=None,
    input_type=_AGENTOBSERVATIONREQUEST,
    output_type=_AGENTOBSERVATIONRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AgentAction',
    full_name='pb.Simulation.AgentAction',
    index=2,
    containing_service=None,
    input_type=_AGENTACTIONREQUEST,
    output_type=_AGENTACTIONRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ResetWorld',
    full_name='pb.Simulation.ResetWorld',
    index=3,
    containing_service=None,
    input_type=_RESETWORLDREQUEST,
    output_type=_RESETWORLDRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Spectate',
    full_name='pb.Simulation.Spectate',
    index=4,
    containing_service=None,
    input_type=_SPECTATEREQUEST,
    output_type=_CELLUPDATE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMULATION)

DESCRIPTOR.services_by_name['Simulation'] = _SIMULATION

# @@protoc_insertion_point(module_scope)
