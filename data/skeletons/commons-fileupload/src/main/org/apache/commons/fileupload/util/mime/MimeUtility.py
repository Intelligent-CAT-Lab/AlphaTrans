from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import *
from src.main.org.apache.commons.fileupload.util.mime.ParseException import *
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *
import typing
from typing import *
import io

# Imports End


class MimeUtility:

    # Class Fields Begin
    __US_ASCII_CHARSET: str = None
    __BASE64_ENCODING_MARKER: str = None
    __QUOTEDPRINTABLE_ENCODING_MARKER: str = None
    __ENCODED_TOKEN_MARKER: str = None
    __ENCODED_TOKEN_FINISHER: str = None
    __LINEAR_WHITESPACE: str = None
    __MIME2JAVA: typing.Dict[str, str] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def decodeText(text: str) -> str:
        pass

    @staticmethod
    def __javaCharset(charset: str) -> str:
        pass

    @staticmethod
    def __decodeWord(word: str) -> str:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
