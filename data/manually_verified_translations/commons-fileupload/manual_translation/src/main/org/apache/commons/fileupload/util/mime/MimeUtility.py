from __future__ import annotations
import re
import os
from io import BytesIO
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *
from src.main.org.apache.commons.fileupload.util.mime.ParseException import *
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import *


class MimeUtility:

    __MIME2JAVA: typing.Dict[str, str] = {}

    __LINEAR_WHITESPACE: str = " \t\r\n"
    __ENCODED_TOKEN_FINISHER: str = "?="
    __ENCODED_TOKEN_MARKER: str = "=?"
    __QUOTEDPRINTABLE_ENCODING_MARKER: str = "Q"
    __BASE64_ENCODING_MARKER: str = "B"
    __US_ASCII_CHARSET: str = "US-ASCII"

    @staticmethod
    def run_static_init():
        MimeUtility.__MIME2JAVA = {
            "iso-2022-cn": "ISO2022CN",
            "iso-2022-kr": "ISO2022KR",
            "utf-8": "UTF8",
            "utf8": "UTF8",
            "ja_jp.iso2022-7": "ISO2022JP",
            "ja_jp.eucjp": "EUCJIS",
            "euc-kr": "KSC5601",
            "euckr": "KSC5601",
            "us-ascii": "ISO-8859-1",
            "x-us-ascii": "ISO-8859-1",
        }

    @staticmethod
    def decodeText(text: str) -> str:

        if text.find(MimeUtility.__ENCODED_TOKEN_MARKER) < 0:
            return text

        offset = 0
        endOffset = len(text)

        startWhiteSpace = -1
        endWhiteSpace = -1

        decodedText = []

        previousTokenEncoded = False

        while offset < endOffset:
            ch = text[offset]

            if MimeUtility.__LINEAR_WHITESPACE.find(ch) != -1:  # whitespace found
                startWhiteSpace = offset
                while offset < endOffset:
                    ch = text[offset]
                    if (
                        MimeUtility.__LINEAR_WHITESPACE.find(ch) != -1
                    ):  # whitespace found
                        offset += 1
                    else:
                        endWhiteSpace = offset
                        break
            else:
                wordStart = offset

                while offset < endOffset:
                    ch = text[offset]
                    if (
                        MimeUtility.__LINEAR_WHITESPACE.find(ch) == -1
                    ):  # not white space
                        offset += 1
                    else:
                        break
                word = text[wordStart:offset]
                if word.startswith(MimeUtility.__ENCODED_TOKEN_MARKER):
                    try:
                        decodedWord = MimeUtility.__decodeWord(word)

                        if not previousTokenEncoded and startWhiteSpace != -1:
                            decodedText.append(text[startWhiteSpace:endWhiteSpace])
                            startWhiteSpace = -1
                        previousTokenEncoded = True
                        decodedText.append(decodedWord)
                        continue

                    except ParseException:
                        pass
                if startWhiteSpace != -1:
                    decodedText.append(text[startWhiteSpace:endWhiteSpace])
                    startWhiteSpace = -1
                previousTokenEncoded = False
                decodedText.append(word)

        return "".join(decodedText)

    @staticmethod
    def __javaCharset(charset: str) -> str:
        if charset is None:
            return None

        mappedCharset = MimeUtility.__MIME2JAVA.get(charset.lower())
        if mappedCharset is None:
            return charset
        return mappedCharset

    @staticmethod
    def __decodeWord(word: str) -> str:

        if not word.startswith(MimeUtility.__ENCODED_TOKEN_MARKER):
            raise ParseException("Invalid RFC 2047 encoded-word: " + word)

        charsetPos = word.find("?", 2)
        if charsetPos == -1:
            raise ParseException("Missing charset in RFC 2047 encoded-word: " + word)

        charset = word[2:charsetPos].lower()

        encodingPos = word.find("?", charsetPos + 1)
        if encodingPos == -1:
            raise ParseException("Missing encoding in RFC 2047 encoded-word: " + word)

        encoding = word[charsetPos + 1 : encodingPos]

        encodedTextPos = word.find(
            MimeUtility.__ENCODED_TOKEN_FINISHER, encodingPos + 1
        )
        if encodedTextPos == -1:
            raise ParseException(
                "Missing encoded text in RFC 2047 encoded-word: " + word
            )

        encodedText = word[encodingPos + 1 : encodedTextPos]

        if len(encodedText) == 0:
            return ""

        try:
            out = io.BytesIO()

            encodedData = encodedText.encode(MimeUtility.__US_ASCII_CHARSET)

            if encoding == MimeUtility.__BASE64_ENCODING_MARKER:
                Base64Decoder.decode(encodedData, out)
            elif encoding == MimeUtility.__QUOTEDPRINTABLE_ENCODING_MARKER:
                QuotedPrintableDecoder.decode(encodedData, out)
            else:
                raise ValueError("Unknown RFC 2047 encoding: " + encoding)

            decodedData = out.getvalue()
            return decodedData.decode(MimeUtility.__javaCharset(charset))
        except IOError:
            raise ValueError("Invalid RFC 2047 encoding")

    def __init__(self) -> None:
        pass


MimeUtility.run_static_init()
