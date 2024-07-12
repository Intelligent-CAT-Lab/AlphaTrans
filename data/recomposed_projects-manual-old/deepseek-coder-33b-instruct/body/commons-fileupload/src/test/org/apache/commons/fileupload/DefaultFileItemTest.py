from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *


class DefaultFileItemTest:

    RUSSIAN_STUFF_WIN1251: List[int] = [
        0xC2,
        0xF1,
        0xE5,
        0xEC,
        0x5F,
        0xEF,
        0xF0,
        0xE8,
        0xE2,
        0xE5,
        0xF2,
    ]
    RUSSIAN_STUFF_KOI8R: List[int] = [
        0xF7,
        0xD3,
        0xC5,
        0xCD,
        0x5F,
        0xD0,
        0xD2,
        0xC9,
        0xD7,
        0xC5,
        0xD4,
    ]
    RUSSIAN_STUFF_UTF8: List[int] = [
        0xD0,
        0x92,
        0xD1,
        0x81,
        0xD0,
        0xB5,
        0xD0,
        0xBC,
        0x5F,
        0xD0,
        0xBF,
        0xD1,
        0x80,
        0xD0,
        0xB8,
        0xD0,
        0xB2,
        0xD0,
        0xB5,
        0xD1,
        0x82,
    ]
    RUSSIAN_STUFF_UNICODE: List[int] = [
        0x412,
        0x441,
        0x435,
        0x43C,
        0x5F,
        0x43F,
        0x440,
        0x438,
        0x432,
        0x435,
        0x442,
    ]
    SWISS_GERMAN_STUFF_UTF8: List[int] = [
        0x47,
        0x72,
        0xC3,
        0xBC,
        0x65,
        0x7A,
        0x69,
        0x5F,
        0x7A,
        0xC3,
        0xA4,
        0x6D,
        0xC3,
        0xA4,
    ]
    SWISS_GERMAN_STUFF_ISO8859_1: List[int] = [
        0x47,
        0x72,
        0xFC,
        0x65,
        0x7A,
        0x69,
        0x5F,
        0x7A,
        0xE4,
        0x6D,
        0xE4,
    ]
    SWISS_GERMAN_STUFF_UNICODE: List[int] = [
        0x47,
        0x72,
        0xFC,
        0x65,
        0x7A,
        0x69,
        0x5F,
        0x7A,
        0xE4,
        0x6D,
        0xE4,
    ]
    CHARSET_WIN1251: str = "Cp1251"
    CHARSET_KOI8_R: str = "KOI8_R"
    CHARSET_UTF8: str = "UTF-8"
    CHARSET_ASCII: str = "US-ASCII"
    CHARSET_ISO88591: str = "ISO-8859-1"
    __threshold: int = 16
    __fileContentType: str = "application/octet-stream"
    __textContentType: str = "text/plain"

    @staticmethod
    def __constructString(unicodeChars: typing.List[int]) -> str:

        buffer = ""
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer += chr(unicodeChar)
        return buffer
