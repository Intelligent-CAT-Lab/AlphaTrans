# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.binary.Codec105ErrorInputStream import *
from src.main.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.Base64InputStream import *
import unittest
import sys
import typing
from typing import *
import io

# Imports End


class Base64InputStreamTest(unittest.TestCase):

    # Class Fields Begin
    __ENCODED_B64: str = "AAAA////"
    __CRLF: typing.List[int] = ""  # LLM could not translate field
    __LF: typing.List[int] = ""  # LLM could not translate field
    __STRING_FIXTURE: str = "Hello World"
    # Class Fields End

    # Class Methods Begin
    def testSkipWrongArgument(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(ENCODED_B64))
        with BaseNCodecInputStream(ins) as b64stream:
            b64stream.skip(-10)

    def testSkipToEnd(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(ENCODED_B64))
        with BaseNCodecInputStream.Base64InputStream0(ins) as b64stream:
            self.assertEqual(6, b64stream.skip(6))
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(-1, b64stream.read0())

    def testSkipPastEnd(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(ENCODED_B64))
        with BaseNCodecInputStream(ins) as b64stream:
            self.assertEqual(6, b64stream.skip(10))
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(-1, b64stream.read0())

    def testSkipNone(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(ENCODED_B64))
        with BaseNCodecInputStream(ins) as b64stream:
            actual_bytes = bytearray(6)
            self.assertEqual(b64stream.skip(0), 0)
            b64stream.read1(actual_bytes, 0, len(actual_bytes))
            self.assertEqual(actual_bytes, bytearray([0, 0, 0, 255, 255, 255]))
            self.assertEqual(b64stream.read0(), -1)

    def testSkipBig(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(ENCODED_B64))
        with BaseNCodecInputStream.Base64InputStream0(ins) as b64stream:
            self.assertEqual(6, b64stream.skip(sys.maxsize))
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(-1, b64stream.read0())

    def testReadOutOfBounds(self) -> None:

        pass  # LLM could not translate method body

    def testReadNull(self) -> None:

        pass  # LLM could not translate method body

    def testRead0(self) -> None:

        pass  # LLM could not translate method body

    def testMarkSupported(self) -> None:

        pass  # LLM could not translate method body

    def testBase64EmptyInputStreamPemChuckSize(self) -> None:

        pass  # LLM could not translate method body

    def testBase64EmptyInputStreamMimeChuckSize(self) -> None:

        self.__testBase64EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testAvailable(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(ENCODED_B64))
        with BaseNCodecInputStream(ins) as b64stream:
            self.assertEqual(1, b64stream.available())
            self.assertEqual(6, b64stream.skip(10))
            self.assertEqual(0, b64stream.available())
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(0, b64stream.available())

    def testInputStreamReader(self) -> None:

        pass  # LLM could not translate method body

    def testCodec101(self) -> None:

        pass  # LLM could not translate method body

    def testCodec105(self) -> None:

        pass  # LLM could not translate method body

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        pass  # LLM could not translate method body

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        pass  # LLM could not translate method body

    def __testBase64EmptyInputStream(self, chuckSize: int) -> None:

        emptyEncoded = b""
        emptyDecoded = b""
        self.__testByteByByte(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)

    # Class Methods End
