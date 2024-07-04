from __future__ import annotations
import re
from io import StringIO
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class RFC1522Codec(ABC):

    _PREFIX: str = "=?"
    _POSTFIX: str = "?="
    _SEP: str = "?"

    def _decodeText(self, text: str) -> str:

        if text is None:
            return None

        if not text.startswith(self._PREFIX) or not text.endswith(self._POSTFIX):
            raise DecoderException(
                "RFC 1522 violation: malformed encoded content", None
            )

        terminator = len(text) - 2
        from_ = 2
        to = text.find(self._SEP, from_)

        if to == terminator:
            raise DecoderException("RFC 1522 violation: charset token not found", None)

        charset = text[from_:to]

        if charset == "":
            raise DecoderException("RFC 1522 violation: charset not specified", None)

        from_ = to + 1
        to = text.find(self._SEP, from_)

        if to == terminator:
            raise DecoderException("RFC 1522 violation: encoding token not found", None)

        encoding = text[from_:to]

        if not self._getEncoding().lower() == encoding.lower():
            raise DecoderException(
                "This codec cannot decode " + encoding + " encoded content", None
            )

        from_ = to + 1
        to = text.find(self._SEP, from_)
        data = StringUtils.getBytesUsAscii(text[from_:to])
        data = self._doDecoding(data)

        return str(data, charset)

    def _encodeText1(self, text: str, charsetName: str) -> str:
        if text is None:
            return None
        return self._encodeText0(text, charsetName)

    def _encodeText0(self, text: str, charset: str) -> str:
        if text is None:
            return None
        buffer = io.StringIO()
        buffer.write(self._PREFIX)
        buffer.write(charset)
        buffer.write(self._SEP)
        buffer.write(self._getEncoding())
        buffer.write(self._SEP)
        buffer.write(
            StringUtils.newStringUsAscii(self._doEncoding(text.encode(charset)))
        )
        buffer.write(self._POSTFIX)
        return buffer.getvalue()

    def _doDecoding(self, bytes: typing.List[int]) -> typing.List[int]:
        raise NotImplementedError("Subclass must implement abstract method")

    def _doEncoding(self, bytes: typing.List[int]) -> typing.List[int]:
        raise NotImplementedError("Subclass must implement abstract method")

    def _getEncoding(self) -> str:
        pass
