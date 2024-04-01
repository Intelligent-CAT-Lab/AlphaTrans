# Imports Begin
from src.main.org.apache.commons.codec.binary.BinaryCodec import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
import unittest
import typing
from typing import *

# Imports End


class BinaryCodecTest(unittest.TestCase):

    # Class Fields Begin
    __CHARSET_UTF8: str = ""  # LLM could not translate field
    __BIT_0: int = ""  # LLM could not translate field
    __BIT_1: int = 2
    __BIT_2: int = 0x04
    __BIT_3: int = 0x08
    __BIT_4: int = 0x10
    __BIT_5: int = 0x20
    __BIT_6: int = 0x40
    __BIT_7: int = 0x80
    # Class Fields End

    # Class Methods Begin
    def testEncodeObject(self) -> None:

        pass  # LLM could not translate method body

    def testEncodeObjectException(self) -> None:

        try:
            self.encode1("")
        except EncoderException:
            return
        self.fail("Expected EncoderException")

    def testEncodeObjectNull(self) -> None:

        obj = bytearray(0)
        self.assertEqual(0, len(self.encode1(obj)))

    def testToAsciiString(self) -> None:

        pass  # LLM could not translate method body

    def testToAsciiChars(self) -> None:

        pass  # LLM could not translate method body

    def testToAsciiBytes(self) -> None:

        pass  # LLM could not translate method body

    def testEncodeByteArray(self) -> None:

        pass  # LLM could not translate method body

    def testFromAsciiByteArray(self) -> None:

        pass  # LLM could not translate method body

    def testFromAsciiCharArray(self) -> None:

        pass  # LLM could not translate method body

    def testToByteArrayFromString(self) -> None:

        pass  # LLM could not translate method body

    def testDecodeByteArray(self) -> None:

        pass  # LLM could not translate method body

    def testDecodeObject(self) -> None:

        pass  # LLM could not translate method body

    def testDecodeObjectException(self) -> None:

        try:
            self.instance.decode1(object())
        except DecoderException:
            return
        self.fail("Expected DecoderException")

    def tearDown(self) -> None:

        self.instance = None

    def setUp(self) -> None:

        self.instance = BinaryCodec()

    def assertDecodeObject(self, bits: typing.List[int], encodeMe: str) -> None:

        decoded: bytes = self.decode1(encodeMe)
        assert decoded == bits
        if encodeMe is None:
            decoded = self.decode0(None)
        else:
            decoded = self.decode1(encodeMe.encode(self.__CHARSET_UTF8))
        assert decoded == bits
        if encodeMe is None:
            decoded = self.decode1(None)
        else:
            decoded = self.decode1(encodeMe.encode(self.__CHARSET_UTF8))
        assert decoded == bits

    # Class Methods End
