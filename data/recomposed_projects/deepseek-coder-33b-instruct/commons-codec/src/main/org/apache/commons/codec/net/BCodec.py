from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.net.RFC1522Codec import *


class BCodec(StringDecoder, StringEncoder, RFC1522Codec):

    __decodingPolicy: CodecPolicy = None
    __charset: str = None

    __DECODING_POLICY_DEFAULT: CodecPolicy = CodecPolicy.LENIENT

    def _doDecoding(self, bytes: typing.List[int]) -> typing.List[int]:

        if bytes is None:
            return None

        return Base64(
            0, BaseNCodec.getChunkSeparator(), False, self.__decodingPolicy
        ).decode0(bytes)

    def _doEncoding(self, bytes: typing.List[int]) -> typing.List[int]:

        if bytes is None:
            return None

        # Convert list of integers to bytes
        byte_array = bytes.tobytes()

        # Use Base64 to encode the bytes
        encoded_bytes = Base64.encodeBase640(byte_array)

        # Convert the encoded bytes back to a list of integers
        encoded_list = list(encoded_bytes)

        return encoded_list

    def _getEncoding(self) -> str:

        return "B"

    def getDefaultCharset(self) -> str:

        return self.__charset

    def getCharset(self) -> str:

        return self.__charset

    def decode1(self, value: typing.Any) -> typing.Any:

        if value is None:
            return None
        if isinstance(value, str):
            return self.decode0(value)
        raise DecoderException(
            "Objects of type "
            + type(value).__name__
            + " cannot be decoded using BCodec",
            None,
        )

    def encode3(self, value: typing.Any) -> typing.Any:

        if value is None:
            return None
        if isinstance(value, str):
            return self.encode2(value)
        raise EncoderException(
            "Objects of type "
            + type(value).__name__
            + " cannot be encoded using BCodec",
            None,
        )

    def decode0(self, value: str) -> str:

        if value is None:
            return None
        try:
            return self.decodeText(value)
        except UnsupportedEncodingException as e:
            raise DecoderException(e.getMessage(), e)
        except ValueError as e:
            raise DecoderException(e.getMessage(), e)

    def encode2(self, strSource: str) -> str:

        if strSource is None:
            return None
        return self.encode0(strSource, self.getCharset())

    def encode1(self, strSource: str, sourceCharset: str) -> str:

        if strSource is None:
            return None
        try:
            return self.encodeText1(strSource, sourceCharset)
        except UnsupportedEncodingException as e:
            raise EncoderException(e.getMessage(), e)

    def encode0(self, strSource: str, sourceCharset: str) -> str:

        if strSource is None:
            return None

        # Assuming that the method encodeText0 is defined in the RFC1522Codec class
        # If it's not, you need to import it from the correct module
        return self.encodeText0(strSource, sourceCharset)

    def isStrictDecoding(self) -> bool:

        return self.__decodingPolicy == CodecPolicy.STRICT

    @staticmethod
    def BCodec2(charsetName: str) -> BCodec:

        return BCodec.BCodec1(charsetName)

    def __init__(self, charset: str, decodingPolicy: CodecPolicy) -> None:

        self.__charset = charset
        self.__decodingPolicy = decodingPolicy

    @staticmethod
    def BCodec1(charset: str) -> BCodec:

        return BCodec(charset, BCodec.__DECODING_POLICY_DEFAULT)

    @staticmethod
    def BCodec0() -> BCodec:

        return BCodec.BCodec1(StandardCharsets.UTF_8)
