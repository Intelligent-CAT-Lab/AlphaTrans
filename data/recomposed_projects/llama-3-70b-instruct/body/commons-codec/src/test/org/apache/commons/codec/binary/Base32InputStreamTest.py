from __future__ import annotations
import re
import os
from io import BytesIO
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.binary.Base32InputStream import *
from src.test.org.apache.commons.codec.binary.Base32TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.test.org.apache.commons.codec.binary.Codec105ErrorInputStream import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base32InputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"
    __LF: typing.List[int] = [10]
    __CRLF: typing.List[int] = [13, 10]
    __ENCODED_FOO: str = "MZXW6==="

    def testSkipWrongArgument(self) -> None:

        pass  # LLM could not translate this method

    def testSkipToEnd(self) -> None:

        pass  # LLM could not translate this method

    def testSkipPastEnd(self) -> None:

        pass  # LLM could not translate this method

    def testSkipBig(self) -> None:

        pass  # LLM could not translate this method

    def testSkipNone(self) -> None:

        pass  # LLM could not translate this method

    def testReadOutOfBounds(self) -> None:

        pass  # LLM could not translate this method

    def testReadNull(self) -> None:

        pass  # LLM could not translate this method

    def testRead0(self) -> None:

        pass  # LLM could not translate this method

    def testMarkSupported(self) -> None:

        pass  # LLM could not translate this method

    def testBase32EmptyInputStreamPemChuckSize(self) -> None:
        self.__testBase32EmptyInputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase32EmptyInputStreamMimeChuckSize(self) -> None:
        self.__testBase32EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testAvailable(self) -> None:

        pass  # LLM could not translate this method

    def testCodec105(self) -> None:

        pass  # LLM could not translate this method

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
        in_ = Base32InputStream.Base32InputStream2(
            io.BytesIO(decoded), True, chunkSize, separator
        )
        output: typing.List[int] = [0] * len(encoded)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]

        self.assertEqual(-1, in_.read(1)[0], "EOF")
        self.assertEqual(-1, in_.read(1)[0], "Still EOF")
        self.assertListEqual(encoded, output, "Streaming base32 encode")

        in_.close()

        in_ = Base32InputStream.Base32InputStream0(io.BytesIO(encoded))
        output = [0] * len(decoded)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]

        self.assertEqual(-1, in_.read(1)[0], "EOF")
        self.assertEqual(-1, in_.read(1)[0], "Still EOF")
        self.assertListEqual(decoded, output, "Streaming base32 decode")

        in_.close()

        in_ = io.BytesIO(decoded)
        for i in range(10):
            in_ = Base32InputStream.Base32InputStream2(in_, True, chunkSize, separator)
            in_ = Base32InputStream.Base32InputStream1(in_, False)
        output = [0] * len(decoded)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]

        self.assertEqual(-1, in_.read(1)[0], "EOF")
        self.assertEqual(-1, in_.read(1)[0], "Still EOF")
        self.assertListEqual(decoded, output, "Streaming base32 wrap-wrap-wrap!")

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        pass  # LLM could not translate this method

    def __testBase32EmptyInputStream(self, chuckSize: int) -> None:

        pass  # LLM could not translate this method
