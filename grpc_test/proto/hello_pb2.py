# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_test/proto/hello.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgrpc_test/proto/hello.proto\"\x1a\n\x05State\x12\x11\n\tIsSuccess\x18\x01 \x01(\x08\"\x18\n\x06\x62ookID\x12\x0e\n\x06\x62ookID\x18\x01 \x01(\x03\"\x1c\n\x08\x42ookname\x12\x10\n\x08\x42ookname\x18\x01 \x01(\t\"$\n\x04\x42ook\x12\x0e\n\x06\x62ookID\x18\x01 \x01(\x03\x12\x0c\n\x04Name\x18\x02 \x01(\t\"\x1f\n\x08\x42ookList\x12\x13\n\x04list\x18\x01 \x03(\x0b\x32\x05.Book2\x80\x01\n\x0b\x42ookManager\x12\x14\n\x03\x61\x64\x64\x12\x05.Book\x1a\x06.State\x12\x1b\n\tqueryByID\x12\x07.bookID\x1a\x05.Book\x12#\n\x0bqueryByName\x12\t.Bookname\x1a\t.BookList\x12\x19\n\x06\x64\x65lete\x12\x07.bookID\x1a\x06.Stateb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_test.proto.hello_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATE._serialized_start=31
  _STATE._serialized_end=57
  _BOOKID._serialized_start=59
  _BOOKID._serialized_end=83
  _BOOKNAME._serialized_start=85
  _BOOKNAME._serialized_end=113
  _BOOK._serialized_start=115
  _BOOK._serialized_end=151
  _BOOKLIST._serialized_start=153
  _BOOKLIST._serialized_end=184
  _BOOKMANAGER._serialized_start=187
  _BOOKMANAGER._serialized_end=315
# @@protoc_insertion_point(module_scope)