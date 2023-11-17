"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*
Defines the structure of protobuf message containing generic response to a command
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _EnumResultGeneric:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumResultGenericEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumResultGeneric.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESULT_UNKNOWN: _EnumResultGeneric.ValueType
    RESULT_SUCCESS: _EnumResultGeneric.ValueType
    RESULT_ILL_FORMED: _EnumResultGeneric.ValueType
    RESULT_NOT_SUPPORTED: _EnumResultGeneric.ValueType
    RESULT_ARGUMENT_OUT_OF_BOUNDS: _EnumResultGeneric.ValueType
    RESULT_ARGUMENT_INVALID: _EnumResultGeneric.ValueType

class EnumResultGeneric(_EnumResultGeneric, metaclass=_EnumResultGenericEnumTypeWrapper): ...

RESULT_UNKNOWN: EnumResultGeneric.ValueType
RESULT_SUCCESS: EnumResultGeneric.ValueType
RESULT_ILL_FORMED: EnumResultGeneric.ValueType
RESULT_NOT_SUPPORTED: EnumResultGeneric.ValueType
RESULT_ARGUMENT_OUT_OF_BOUNDS: EnumResultGeneric.ValueType
RESULT_ARGUMENT_INVALID: EnumResultGeneric.ValueType
global___EnumResultGeneric = EnumResultGeneric

class ResponseGeneric(google.protobuf.message.Message):
    """
    Generic Response used across most response / notification messages

    @ref EnumResultGeneric
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULT_FIELD_NUMBER: builtins.int
    result: global___EnumResultGeneric.ValueType
    " Generic pass/fail/error info"

    def __init__(self, *, result: global___EnumResultGeneric.ValueType | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["result", b"result"]) -> None: ...

global___ResponseGeneric = ResponseGeneric
