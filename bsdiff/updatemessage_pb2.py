# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: updatemessage.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='updatemessage.proto',
  package='',
  serialized_pb='\n\x13updatemessage.proto\"1\n\x03\x41sk\x12\x14\n\x0cpackage_name\x18\x01 \x02(\t\x12\x14\n\x0cversion_code\x18\x02 \x02(\x05\"o\n\x06\x41nswer\x12\x12\n\nhas_update\x18\x01 \x02(\x08\x12\x0b\n\x03url\x18\x02 \x01(\t\x12 \n\x04type\x18\x03 \x01(\x0e\x32\x0b.UpdateType:\x05PATCH\x12\x11\n\tpatch_md5\x18\x04 \x01(\t\x12\x0f\n\x07\x61pk_md5\x18\x05 \x01(\t* \n\nUpdateType\x12\x07\n\x03\x41PK\x10\x00\x12\t\n\x05PATCH\x10\x01\x42(\n\x17\x63om.qasdk.message.modelB\rUpdateMessage')

_UPDATETYPE = _descriptor.EnumDescriptor(
  name='UpdateType',
  full_name='UpdateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='APK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PATCH', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=187,
  serialized_end=219,
)

UpdateType = enum_type_wrapper.EnumTypeWrapper(_UPDATETYPE)
APK = 0
PATCH = 1



_ASK = _descriptor.Descriptor(
  name='Ask',
  full_name='Ask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_name', full_name='Ask.package_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version_code', full_name='Ask.version_code', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=72,
)


_ANSWER = _descriptor.Descriptor(
  name='Answer',
  full_name='Answer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_update', full_name='Answer.has_update', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='Answer.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Answer.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patch_md5', full_name='Answer.patch_md5', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apk_md5', full_name='Answer.apk_md5', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=74,
  serialized_end=185,
)

_ANSWER.fields_by_name['type'].enum_type = _UPDATETYPE
DESCRIPTOR.message_types_by_name['Ask'] = _ASK
DESCRIPTOR.message_types_by_name['Answer'] = _ANSWER

class Ask(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ASK

  # @@protoc_insertion_point(class_scope:Ask)

class Answer(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ANSWER

  # @@protoc_insertion_point(class_scope:Answer)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\027com.qasdk.message.modelB\rUpdateMessage')
# @@protoc_insertion_point(module_scope)
