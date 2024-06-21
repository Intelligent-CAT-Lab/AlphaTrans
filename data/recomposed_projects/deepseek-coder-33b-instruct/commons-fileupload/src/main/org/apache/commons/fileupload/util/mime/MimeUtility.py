from __future__ import annotations
import re
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

            if encoding.upper() == MimeUtility.__BASE64_ENCODING_MARKER:
                Base64Decoder.decode(encodedData, out)
            elif encoding.upper() == MimeUtility.__QUOTEDPRINTABLE_ENCODING_MARKER:
                QuotedPrintableDecoder.decode(encodedData, out)
            else:
                raise ValueError("Unknown RFC 2047 encoding: " + encoding)

            decodedData = out.getvalue()
            return decodedData.decode(MimeUtility.__javaCharset(charset))
        except Exception as e:
            raise ValueError("Invalid RFC 2047 encoding") from e

    def __init__(self) -> None:

        self.__MIME2JAVA = {}
        self.__LINEAR_WHITESPACE = " \t\r\n"
        self.__ENCODED_TOKEN_FINISHER = "?="
        self.__ENCODED_TOKEN_MARKER = "=?"
        self.__QUOTEDPRINTABLE_ENCODING_MARKER = "Q"
        self.__BASE64_ENCODING_MARKER = "B"
        self.__US_ASCII_CHARSET = "US-ASCII"
