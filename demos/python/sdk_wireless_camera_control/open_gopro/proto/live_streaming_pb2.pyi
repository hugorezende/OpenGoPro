"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*
Defines the structure of protobuf messages for working with Live Streams
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _EnumLens:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumLensEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumLens.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LENS_WIDE: _EnumLens.ValueType
    LENS_LINEAR: _EnumLens.ValueType
    LENS_SUPERVIEW: _EnumLens.ValueType

class EnumLens(_EnumLens, metaclass=_EnumLensEnumTypeWrapper): ...

LENS_WIDE: EnumLens.ValueType
LENS_LINEAR: EnumLens.ValueType
LENS_SUPERVIEW: EnumLens.ValueType
global___EnumLens = EnumLens

class _EnumLiveStreamError:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumLiveStreamErrorEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumLiveStreamError.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LIVE_STREAM_ERROR_NONE: _EnumLiveStreamError.ValueType
    " No error (success)"
    LIVE_STREAM_ERROR_NETWORK: _EnumLiveStreamError.ValueType
    " General network error during the stream"
    LIVE_STREAM_ERROR_CREATESTREAM: _EnumLiveStreamError.ValueType
    " Startup error: bad URL or valid with live stream server"
    LIVE_STREAM_ERROR_OUTOFMEMORY: _EnumLiveStreamError.ValueType
    " Not enough memory on camera to complete task"
    LIVE_STREAM_ERROR_INPUTSTREAM: _EnumLiveStreamError.ValueType
    " Failed to get stream from low level camera system"
    LIVE_STREAM_ERROR_INTERNET: _EnumLiveStreamError.ValueType
    " No internet access detected on startup of streamer"
    LIVE_STREAM_ERROR_OSNETWORK: _EnumLiveStreamError.ValueType
    " Error occured in linux networking stack. usually means the server closed the connection"
    LIVE_STREAM_ERROR_SELECTEDNETWORKTIMEOUT: _EnumLiveStreamError.ValueType
    " Timed out attemping to connect to the wifi network when attemping live stream"
    LIVE_STREAM_ERROR_SSL_HANDSHAKE: _EnumLiveStreamError.ValueType
    " SSL handshake failed (commonly caused due to incorrect time / time zone)"
    LIVE_STREAM_ERROR_CAMERA_BLOCKED: _EnumLiveStreamError.ValueType
    " Low level camera system rejected attempt to start live stream"
    LIVE_STREAM_ERROR_UNKNOWN: _EnumLiveStreamError.ValueType
    " Unknown"
    LIVE_STREAM_ERROR_SD_CARD_FULL: _EnumLiveStreamError.ValueType
    " Can not perform livestream because sd card is full"
    LIVE_STREAM_ERROR_SD_CARD_REMOVED: _EnumLiveStreamError.ValueType
    " Livestream stopped because sd card was removed"

class EnumLiveStreamError(_EnumLiveStreamError, metaclass=_EnumLiveStreamErrorEnumTypeWrapper): ...

LIVE_STREAM_ERROR_NONE: EnumLiveStreamError.ValueType
" No error (success)"
LIVE_STREAM_ERROR_NETWORK: EnumLiveStreamError.ValueType
" General network error during the stream"
LIVE_STREAM_ERROR_CREATESTREAM: EnumLiveStreamError.ValueType
" Startup error: bad URL or valid with live stream server"
LIVE_STREAM_ERROR_OUTOFMEMORY: EnumLiveStreamError.ValueType
" Not enough memory on camera to complete task"
LIVE_STREAM_ERROR_INPUTSTREAM: EnumLiveStreamError.ValueType
" Failed to get stream from low level camera system"
LIVE_STREAM_ERROR_INTERNET: EnumLiveStreamError.ValueType
" No internet access detected on startup of streamer"
LIVE_STREAM_ERROR_OSNETWORK: EnumLiveStreamError.ValueType
" Error occured in linux networking stack. usually means the server closed the connection"
LIVE_STREAM_ERROR_SELECTEDNETWORKTIMEOUT: EnumLiveStreamError.ValueType
" Timed out attemping to connect to the wifi network when attemping live stream"
LIVE_STREAM_ERROR_SSL_HANDSHAKE: EnumLiveStreamError.ValueType
" SSL handshake failed (commonly caused due to incorrect time / time zone)"
LIVE_STREAM_ERROR_CAMERA_BLOCKED: EnumLiveStreamError.ValueType
" Low level camera system rejected attempt to start live stream"
LIVE_STREAM_ERROR_UNKNOWN: EnumLiveStreamError.ValueType
" Unknown"
LIVE_STREAM_ERROR_SD_CARD_FULL: EnumLiveStreamError.ValueType
" Can not perform livestream because sd card is full"
LIVE_STREAM_ERROR_SD_CARD_REMOVED: EnumLiveStreamError.ValueType
" Livestream stopped because sd card was removed"
global___EnumLiveStreamError = EnumLiveStreamError

class _EnumLiveStreamStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumLiveStreamStatusEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumLiveStreamStatus.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LIVE_STREAM_STATE_IDLE: _EnumLiveStreamStatus.ValueType
    " Initial status. Livestream has not yet been configured"
    LIVE_STREAM_STATE_CONFIG: _EnumLiveStreamStatus.ValueType
    " Livestream is being configured"
    LIVE_STREAM_STATE_READY: _EnumLiveStreamStatus.ValueType
    "\n    Livestream has finished configuration and is ready to start streaming\n    "
    LIVE_STREAM_STATE_STREAMING: _EnumLiveStreamStatus.ValueType
    " Livestream is actively streaming"
    LIVE_STREAM_STATE_COMPLETE_STAY_ON: _EnumLiveStreamStatus.ValueType
    " Live stream is exiting. No errors occured."
    LIVE_STREAM_STATE_FAILED_STAY_ON: _EnumLiveStreamStatus.ValueType
    " Live stream is exiting. An error occurred."
    LIVE_STREAM_STATE_RECONNECTING: _EnumLiveStreamStatus.ValueType
    " An error occurred during livestream and stream is attempting to reconnect."

class EnumLiveStreamStatus(_EnumLiveStreamStatus, metaclass=_EnumLiveStreamStatusEnumTypeWrapper): ...

LIVE_STREAM_STATE_IDLE: EnumLiveStreamStatus.ValueType
" Initial status. Livestream has not yet been configured"
LIVE_STREAM_STATE_CONFIG: EnumLiveStreamStatus.ValueType
" Livestream is being configured"
LIVE_STREAM_STATE_READY: EnumLiveStreamStatus.ValueType
"\nLivestream has finished configuration and is ready to start streaming\n"
LIVE_STREAM_STATE_STREAMING: EnumLiveStreamStatus.ValueType
" Livestream is actively streaming"
LIVE_STREAM_STATE_COMPLETE_STAY_ON: EnumLiveStreamStatus.ValueType
" Live stream is exiting. No errors occured."
LIVE_STREAM_STATE_FAILED_STAY_ON: EnumLiveStreamStatus.ValueType
" Live stream is exiting. An error occurred."
LIVE_STREAM_STATE_RECONNECTING: EnumLiveStreamStatus.ValueType
" An error occurred during livestream and stream is attempting to reconnect."
global___EnumLiveStreamStatus = EnumLiveStreamStatus

class _EnumRegisterLiveStreamStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumRegisterLiveStreamStatusEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumRegisterLiveStreamStatus.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    REGISTER_LIVE_STREAM_STATUS_STATUS: _EnumRegisterLiveStreamStatus.ValueType
    REGISTER_LIVE_STREAM_STATUS_ERROR: _EnumRegisterLiveStreamStatus.ValueType
    REGISTER_LIVE_STREAM_STATUS_MODE: _EnumRegisterLiveStreamStatus.ValueType
    REGISTER_LIVE_STREAM_STATUS_BITRATE: _EnumRegisterLiveStreamStatus.ValueType

class EnumRegisterLiveStreamStatus(
    _EnumRegisterLiveStreamStatus, metaclass=_EnumRegisterLiveStreamStatusEnumTypeWrapper
): ...

REGISTER_LIVE_STREAM_STATUS_STATUS: EnumRegisterLiveStreamStatus.ValueType
REGISTER_LIVE_STREAM_STATUS_ERROR: EnumRegisterLiveStreamStatus.ValueType
REGISTER_LIVE_STREAM_STATUS_MODE: EnumRegisterLiveStreamStatus.ValueType
REGISTER_LIVE_STREAM_STATUS_BITRATE: EnumRegisterLiveStreamStatus.ValueType
global___EnumRegisterLiveStreamStatus = EnumRegisterLiveStreamStatus

class _EnumWindowSize:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumWindowSizeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumWindowSize.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    WINDOW_SIZE_480: _EnumWindowSize.ValueType
    WINDOW_SIZE_720: _EnumWindowSize.ValueType
    WINDOW_SIZE_1080: _EnumWindowSize.ValueType

class EnumWindowSize(_EnumWindowSize, metaclass=_EnumWindowSizeEnumTypeWrapper): ...

WINDOW_SIZE_480: EnumWindowSize.ValueType
WINDOW_SIZE_720: EnumWindowSize.ValueType
WINDOW_SIZE_1080: EnumWindowSize.ValueType
global___EnumWindowSize = EnumWindowSize

class NotifyLiveStreamStatus(google.protobuf.message.Message):
    """*
    Live Stream status

    Sent either:
      - as a syncrhonous response to initial @ref RequestGetLiveStreamStatus
      - as asynchronous notifications registered for via @ref RequestGetLiveStreamStatus
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LIVE_STREAM_STATUS_FIELD_NUMBER: builtins.int
    LIVE_STREAM_ERROR_FIELD_NUMBER: builtins.int
    LIVE_STREAM_ENCODE_FIELD_NUMBER: builtins.int
    LIVE_STREAM_BITRATE_FIELD_NUMBER: builtins.int
    LIVE_STREAM_WINDOW_SIZE_SUPPORTED_ARRAY_FIELD_NUMBER: builtins.int
    LIVE_STREAM_ENCODE_SUPPORTED_FIELD_NUMBER: builtins.int
    LIVE_STREAM_MAX_LENS_UNSUPPORTED_FIELD_NUMBER: builtins.int
    LIVE_STREAM_MINIMUM_STREAM_BITRATE_FIELD_NUMBER: builtins.int
    LIVE_STREAM_MAXIMUM_STREAM_BITRATE_FIELD_NUMBER: builtins.int
    LIVE_STREAM_LENS_SUPPORTED_FIELD_NUMBER: builtins.int
    LIVE_STREAM_LENS_SUPPORTED_ARRAY_FIELD_NUMBER: builtins.int
    live_stream_status: global___EnumLiveStreamStatus.ValueType
    " Live stream status"
    live_stream_error: global___EnumLiveStreamError.ValueType
    " Live stream error"
    live_stream_encode: builtins.bool
    " Is live stream encoding?"
    live_stream_bitrate: builtins.int
    " Live stream bitrate (Kbps)"

    @property
    def live_stream_window_size_supported_array(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___EnumWindowSize.ValueType]:
        """
        List  of supported resolutions returned when live stream is registered or requested

        1. register  --> camera
        2. register response (with capabilities) --> mobile
        3. async notifications (without capabilities) --> mobile
        """
    live_stream_encode_supported: builtins.bool
    " Does the camera support encoding while live streaming?"
    live_stream_max_lens_unsupported: builtins.bool
    " Is the Max Lens feature NOT supported?"
    live_stream_minimum_stream_bitrate: builtins.int
    " Camera-defined minimum bitrate (static) (Kbps)"
    live_stream_maximum_stream_bitrate: builtins.int
    " Camera-defined maximum bitrate (static) (Kbps)"
    live_stream_lens_supported: builtins.bool
    " Does camera support setting lens for live streaming?"

    @property
    def live_stream_lens_supported_array(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___EnumLens.ValueType]:
        """Array of supported lenses for live streaming"""
    def __init__(
        self,
        *,
        live_stream_status: global___EnumLiveStreamStatus.ValueType | None = ...,
        live_stream_error: global___EnumLiveStreamError.ValueType | None = ...,
        live_stream_encode: builtins.bool | None = ...,
        live_stream_bitrate: builtins.int | None = ...,
        live_stream_window_size_supported_array: collections.abc.Iterable[global___EnumWindowSize.ValueType]
        | None = ...,
        live_stream_encode_supported: builtins.bool | None = ...,
        live_stream_max_lens_unsupported: builtins.bool | None = ...,
        live_stream_minimum_stream_bitrate: builtins.int | None = ...,
        live_stream_maximum_stream_bitrate: builtins.int | None = ...,
        live_stream_lens_supported: builtins.bool | None = ...,
        live_stream_lens_supported_array: collections.abc.Iterable[global___EnumLens.ValueType] | None = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "live_stream_bitrate",
            b"live_stream_bitrate",
            "live_stream_encode",
            b"live_stream_encode",
            "live_stream_encode_supported",
            b"live_stream_encode_supported",
            "live_stream_error",
            b"live_stream_error",
            "live_stream_lens_supported",
            b"live_stream_lens_supported",
            "live_stream_max_lens_unsupported",
            b"live_stream_max_lens_unsupported",
            "live_stream_maximum_stream_bitrate",
            b"live_stream_maximum_stream_bitrate",
            "live_stream_minimum_stream_bitrate",
            b"live_stream_minimum_stream_bitrate",
            "live_stream_status",
            b"live_stream_status",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "live_stream_bitrate",
            b"live_stream_bitrate",
            "live_stream_encode",
            b"live_stream_encode",
            "live_stream_encode_supported",
            b"live_stream_encode_supported",
            "live_stream_error",
            b"live_stream_error",
            "live_stream_lens_supported",
            b"live_stream_lens_supported",
            "live_stream_lens_supported_array",
            b"live_stream_lens_supported_array",
            "live_stream_max_lens_unsupported",
            b"live_stream_max_lens_unsupported",
            "live_stream_maximum_stream_bitrate",
            b"live_stream_maximum_stream_bitrate",
            "live_stream_minimum_stream_bitrate",
            b"live_stream_minimum_stream_bitrate",
            "live_stream_status",
            b"live_stream_status",
            "live_stream_window_size_supported_array",
            b"live_stream_window_size_supported_array",
        ],
    ) -> None: ...

global___NotifyLiveStreamStatus = NotifyLiveStreamStatus

class RequestGetLiveStreamStatus(google.protobuf.message.Message):
    """*
    Get the current livestream status (and optionally register for future status changes)

    Both current status and future status changes are sent via @ref NotifyLiveStreamStatus
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTER_LIVE_STREAM_STATUS_FIELD_NUMBER: builtins.int
    UNREGISTER_LIVE_STREAM_STATUS_FIELD_NUMBER: builtins.int

    @property
    def register_live_stream_status(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        global___EnumRegisterLiveStreamStatus.ValueType
    ]:
        """Array of live stream statuses to be notified about"""
    @property
    def unregister_live_stream_status(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        global___EnumRegisterLiveStreamStatus.ValueType
    ]:
        """Array of live stream statuses to stop being notified about"""
    def __init__(
        self,
        *,
        register_live_stream_status: collections.abc.Iterable[global___EnumRegisterLiveStreamStatus.ValueType]
        | None = ...,
        unregister_live_stream_status: collections.abc.Iterable[global___EnumRegisterLiveStreamStatus.ValueType]
        | None = ...
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "register_live_stream_status",
            b"register_live_stream_status",
            "unregister_live_stream_status",
            b"unregister_live_stream_status",
        ],
    ) -> None: ...

global___RequestGetLiveStreamStatus = RequestGetLiveStreamStatus

class RequestSetLiveStreamMode(google.protobuf.message.Message):
    """*
    Configure lives streaming

    The current livestream status can be queried via @ref RequestGetLiveStreamStatus

    TODO What is the response?
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    URL_FIELD_NUMBER: builtins.int
    ENCODE_FIELD_NUMBER: builtins.int
    WINDOW_SIZE_FIELD_NUMBER: builtins.int
    CERT_FIELD_NUMBER: builtins.int
    MINIMUM_BITRATE_FIELD_NUMBER: builtins.int
    MAXIMUM_BITRATE_FIELD_NUMBER: builtins.int
    STARTING_BITRATE_FIELD_NUMBER: builtins.int
    LENS_FIELD_NUMBER: builtins.int
    url: builtins.str
    " RTMP(S) URL used for live stream"
    encode: builtins.bool
    " Save media to sdcard while streaming?"
    window_size: global___EnumWindowSize.ValueType
    " Live stream resolution"
    cert: builtins.bytes
    " Certificate for servers that require it"
    minimum_bitrate: builtins.int
    " Minimum desired bitrate (may or may not be honored)"
    maximum_bitrate: builtins.int
    " Maximum desired bitrate (may or may not be honored)"
    starting_bitrate: builtins.int
    " Starting bitrate"
    lens: global___EnumLens.ValueType
    " Lens to use for live stream (see NotifyLiveStreamStatus.live_stream_lens_supported)"

    def __init__(
        self,
        *,
        url: builtins.str | None = ...,
        encode: builtins.bool | None = ...,
        window_size: global___EnumWindowSize.ValueType | None = ...,
        cert: builtins.bytes | None = ...,
        minimum_bitrate: builtins.int | None = ...,
        maximum_bitrate: builtins.int | None = ...,
        starting_bitrate: builtins.int | None = ...,
        lens: global___EnumLens.ValueType | None = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "cert",
            b"cert",
            "encode",
            b"encode",
            "lens",
            b"lens",
            "maximum_bitrate",
            b"maximum_bitrate",
            "minimum_bitrate",
            b"minimum_bitrate",
            "starting_bitrate",
            b"starting_bitrate",
            "url",
            b"url",
            "window_size",
            b"window_size",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "cert",
            b"cert",
            "encode",
            b"encode",
            "lens",
            b"lens",
            "maximum_bitrate",
            b"maximum_bitrate",
            "minimum_bitrate",
            b"minimum_bitrate",
            "starting_bitrate",
            b"starting_bitrate",
            "url",
            b"url",
            "window_size",
            b"window_size",
        ],
    ) -> None: ...

global___RequestSetLiveStreamMode = RequestSetLiveStreamMode
