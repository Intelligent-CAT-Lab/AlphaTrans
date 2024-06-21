from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *


class DefaultFileItemTest(unittest.TestCase):

    RUSSIAN_STUFF_WIN1251: typing.List[int] = []

    RUSSIAN_STUFF_KOI8R: typing.List[int] = []

    RUSSIAN_STUFF_UTF8: typing.List[int] = []

    RUSSIAN_STUFF_UNICODE: typing.List[int] = []

    SWISS_GERMAN_STUFF_UTF8: typing.List[int] = []

    SWISS_GERMAN_STUFF_ISO8859_1: typing.List[int] = []

    SWISS_GERMAN_STUFF_UNICODE: typing.List[int] = []

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
