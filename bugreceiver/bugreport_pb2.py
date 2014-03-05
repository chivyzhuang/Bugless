# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bugreport.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bugreport.proto',
  package='',
  serialized_pb='\n\x0f\x62ugreport.proto\"\x83\x02\n\tBugReport\x12 \n\x18phone_system_sdk_version\x18\x01 \x02(\x05\x12\x13\n\x0bphone_model\x18\x02 \x01(\t\x12\x15\n\rphone_product\x18\x03 \x01(\t\x12\x18\n\x10\x61pp_package_name\x18\x04 \x02(\t\x12\x18\n\x10\x61pp_version_code\x18\x05 \x02(\x05\x12\x0f\n\x07user_id\x18\x06 \x02(\t\x12\x1f\n\x04tags\x18\x07 \x03(\x0b\x32\x11.BugReport.BugTag\x1a\x42\n\x06\x42ugTag\x12\r\n\x05\x63ount\x18\x01 \x02(\x05\x12\x1c\n\x04type\x18\x02 \x02(\x0e\x32\x08.BugType:\x04JAVA\x12\x0b\n\x03tag\x18\x03 \x02(\t\"v\n\nReportFeed\x12\"\n\x05\x66\x65\x65\x64s\x18\x01 \x03(\x0b\x32\x13.ReportFeed.BugFeed\x1a\x44\n\x07\x42ugFeed\x12\x1c\n\x04type\x18\x01 \x02(\x0e\x32\x08.BugType:\x04JAVA\x12\x0b\n\x03tag\x18\x02 \x02(\t\x12\x0e\n\x06\x61nswer\x18\x03 \x02(\x08\"s\n\x07JavaBug\x12\x12\n\nbrief_info\x18\x01 \x02(\t\x12\x13\n\x0b\x64\x65tail_info\x18\x02 \x02(\t\x12\x0b\n\x03tag\x18\x03 \x02(\t\x12\x18\n\x10\x61pp_package_name\x18\x04 \x02(\t\x12\x18\n\x10\x61pp_version_code\x18\x05 \x02(\x05*+\n\x07\x42ugType\x12\x08\n\x04JAVA\x10\x00\x12\n\n\x06NATIVE\x10\x01\x12\n\n\x06KERNEL\x10\x02\x42+\n\x17\x63om.qasdk.message.modelB\x10\x42ugReportMessage')

_BUGTYPE = _descriptor.EnumDescriptor(
  name='BugType',
  full_name='BugType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JAVA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NATIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KERNEL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=518,
  serialized_end=561,
)

BugType = enum_type_wrapper.EnumTypeWrapper(_BUGTYPE)
JAVA = 0
NATIVE = 1
KERNEL = 2



_BUGREPORT_BUGTAG = _descriptor.Descriptor(
  name='BugTag',
  full_name='BugReport.BugTag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='BugReport.BugTag.count', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='BugReport.BugTag.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='BugReport.BugTag.tag', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=213,
  serialized_end=279,
)

_BUGREPORT = _descriptor.Descriptor(
  name='BugReport',
  full_name='BugReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone_system_sdk_version', full_name='BugReport.phone_system_sdk_version', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone_model', full_name='BugReport.phone_model', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone_product', full_name='BugReport.phone_product', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_package_name', full_name='BugReport.app_package_name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_version_code', full_name='BugReport.app_version_code', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='BugReport.user_id', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='BugReport.tags', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BUGREPORT_BUGTAG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=20,
  serialized_end=279,
)


_REPORTFEED_BUGFEED = _descriptor.Descriptor(
  name='BugFeed',
  full_name='ReportFeed.BugFeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ReportFeed.BugFeed.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='ReportFeed.BugFeed.tag', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer', full_name='ReportFeed.BugFeed.answer', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=331,
  serialized_end=399,
)

_REPORTFEED = _descriptor.Descriptor(
  name='ReportFeed',
  full_name='ReportFeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feeds', full_name='ReportFeed.feeds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REPORTFEED_BUGFEED, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=281,
  serialized_end=399,
)


_JAVABUG = _descriptor.Descriptor(
  name='JavaBug',
  full_name='JavaBug',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='brief_info', full_name='JavaBug.brief_info', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='detail_info', full_name='JavaBug.detail_info', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='JavaBug.tag', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_package_name', full_name='JavaBug.app_package_name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_version_code', full_name='JavaBug.app_version_code', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=401,
  serialized_end=516,
)

_BUGREPORT_BUGTAG.fields_by_name['type'].enum_type = _BUGTYPE
_BUGREPORT_BUGTAG.containing_type = _BUGREPORT;
_BUGREPORT.fields_by_name['tags'].message_type = _BUGREPORT_BUGTAG
_REPORTFEED_BUGFEED.fields_by_name['type'].enum_type = _BUGTYPE
_REPORTFEED_BUGFEED.containing_type = _REPORTFEED;
_REPORTFEED.fields_by_name['feeds'].message_type = _REPORTFEED_BUGFEED
DESCRIPTOR.message_types_by_name['BugReport'] = _BUGREPORT
DESCRIPTOR.message_types_by_name['ReportFeed'] = _REPORTFEED
DESCRIPTOR.message_types_by_name['JavaBug'] = _JAVABUG

class BugReport(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class BugTag(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _BUGREPORT_BUGTAG

    # @@protoc_insertion_point(class_scope:BugReport.BugTag)
  DESCRIPTOR = _BUGREPORT

  # @@protoc_insertion_point(class_scope:BugReport)

class ReportFeed(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class BugFeed(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _REPORTFEED_BUGFEED

    # @@protoc_insertion_point(class_scope:ReportFeed.BugFeed)
  DESCRIPTOR = _REPORTFEED

  # @@protoc_insertion_point(class_scope:ReportFeed)

class JavaBug(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JAVABUG

  # @@protoc_insertion_point(class_scope:JavaBug)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\027com.qasdk.message.modelB\020BugReportMessage')
# @@protoc_insertion_point(module_scope)