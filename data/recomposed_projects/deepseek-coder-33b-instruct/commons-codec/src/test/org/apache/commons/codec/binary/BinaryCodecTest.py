from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.BinaryCodec import *


class BinaryCodecTest(unittest.TestCase):

    __BIT_7: int = 0x80

    __BIT_6: int = 0x40

    __BIT_5: int = 0x20

    __BIT_4: int = 0x10

    __BIT_3: int = 0x08

    __BIT_2: int = 0x04

    __BIT_1: int = 0x02

    __BIT_0: int = 0x01

    __CHARSET_UTF8: str = "UTF-8"

    def testEncodeObject(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeObjectException(self) -> None:

        try:
            BinaryCodec().encode1("")
        except EncoderException:
            return
        assert False, "Expected EncoderException"

    def testEncodeObjectNull(self) -> None:

        obj = bytearray(0)
        result = BinaryCodec.encode1(obj)
        self.assertEqual(0, len(result))

    def testToAsciiString(self) -> None:

        pass  # LLM could not translate this method

    def testToAsciiChars(self) -> None:

        pass  # LLM could not translate this method

    def testToAsciiBytes(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeByteArray(self) -> None:

        pass  # LLM could not translate this method

    def testFromAsciiByteArray(self) -> None:

        pass  # LLM could not translate this method

    def testFromAsciiCharArray(self) -> None:

        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii1([])))

        bits = bytearray(1)
        decoded = BinaryCodec.fromAscii1(list("00000000"))
        self.assertEqual(bits, decoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.fromAscii1(list("00000001"))
        self.assertEqual(bits, decoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.fromAscii1(list("00000011"))
        self.assertEqual(bits, decoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.fromAscii1(list("00000111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.fromAscii1(list("00001111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.fromAscii1(list("00011111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.fromAscii1(list("00111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.fromAscii1(list("01111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("11111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000011111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000000111111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000001111111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000011111111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0000111111111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0001111111111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0011111111111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("0111111111111111"))
        self.assertEqual(bits, decoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.fromAscii1(list("1111111111111111"))
        self.assertEqual(bits, decoded)

        self.assertEqual(0, len(BinaryCodec.fromAscii1(None)))

    def testToByteArrayFromString(self) -> None:

        bits = bytearray(1)
        decoded = BinaryCodec.toByteArray(self, "00000000")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = BinaryCodec.toByteArray(self, "00000001")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = BinaryCodec.toByteArray(self, "00000011")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = BinaryCodec.toByteArray(self, "00000111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = BinaryCodec.toByteArray(self, "00001111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = BinaryCodec.toByteArray(self, "00011111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = BinaryCodec.toByteArray(self, "00111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = BinaryCodec.toByteArray(self, "01111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "11111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "0000000011111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "0000000111111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "0000001111111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "0000011111111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "0000111111111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "0001111111111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "0011111111111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "0111111111111111")
        assert bytes(bits) == bytes(decoded)

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = BinaryCodec.toByteArray(self, "1111111111111111")
        assert bytes(bits) == bytes(decoded)

        assert BinaryCodec.toByteArray(self, None).__len__() == 0

    def testDecodeByteArray(self) -> None:

        bits = bytearray(1)
        decoded = self.decode0("00000000".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        decoded = self.decode0("00000001".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        decoded = self.decode0("00000011".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        decoded = self.decode0("00000111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        decoded = self.decode0("00001111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        decoded = self.decode0("00011111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        decoded = self.decode0("00111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        decoded = self.decode0("01111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("11111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("0000000011111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("0000000111111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("0000001111111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("0000011111111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("0000111111111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("0001111111111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("0011111111111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("0111111111111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        decoded = self.decode0("1111111111111111".encode(self.__CHARSET_UTF8))
        assert bytes(bits) == decoded

    def testDecodeObject(self) -> None:

        bits = bytearray(1)
        self.assertDecodeObject(bits, "00000000")

        bits = bytearray(1)
        bits[0] = self.__BIT_0
        self.assertDecodeObject(bits, "00000001")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1
        self.assertDecodeObject(bits, "00000011")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        self.assertDecodeObject(bits, "00000111")

        bits = bytearray(1)
        bits[0] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        self.assertDecodeObject(bits, "00001111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        self.assertDecodeObject(bits, "00011111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        self.assertDecodeObject(bits, "00111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        self.assertDecodeObject(bits, "01111111")

        bits = bytearray(1)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "11111111")

        bits = bytearray(2)
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000011111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000000111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000001111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000011111111111")

        bits = bytearray(2)
        bits[1] = self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0000111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0001111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0011111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "0111111111111111")

        bits = bytearray(2)
        bits[1] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        bits[0] = (
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        )
        self.assertDecodeObject(bits, "1111111111111111")

        self.assertDecodeObject(bytearray(0), None)

    def testDecodeObjectException(self) -> None:

        try:
            self.instance.decode1(object())
        except DecoderException:
            return
        assert False, "Expected DecoderException"

    def tearDown(self) -> None:

        self.instance = None

    def setUp(self) -> None:

        self.instance = BinaryCodec()

    def assertDecodeObject(self, bits: typing.List[int], encodeMe: str) -> None:

        pass  # LLM could not translate this method
