from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
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
    __CHARSET_UTF8: str = "utf-8"
    instance: BinaryCodec = None

    def testEncodeObject(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeObjectException(self) -> None:

        with pytest.raises(EncoderException):
            self.instance.encode1("")

    def testEncodeObjectNull(self) -> None:

        obj = bytearray(0)
        self.assertEqual(0, len(self.instance.encode1(obj)))

    def testToAsciiString(self) -> None:

        pass  # LLM could not translate this method

    def testToAsciiChars(self) -> None:

        pass  # LLM could not translate this method

    def testToAsciiBytes(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeByteArray(self) -> None:

        def encode0(raw: typing.List[int]) -> str:
            if raw is None:
                return ""
            return "".join([f"{i:08b}" for i in raw])

        bits = [0]
        l_encoded = encode0(bits)
        self.assertEqual("00000000", l_encoded)

        bits = [1]
        l_encoded = encode0(bits)
        self.assertEqual("00000001", l_encoded)

        bits = [3]
        l_encoded = encode0(bits)
        self.assertEqual("00000011", l_encoded)

        bits = [7]
        l_encoded = encode0(bits)
        self.assertEqual("00000111", l_encoded)

        bits = [15]
        l_encoded = encode0(bits)
        self.assertEqual("00001111", l_encoded)

        bits = [31]
        l_encoded = encode0(bits)
        self.assertEqual("00011111", l_encoded)

        bits = [63]
        l_encoded = encode0(bits)
        self.assertEqual("00111111", l_encoded)

        bits = [127]
        l_encoded = encode0(bits)
        self.assertEqual("01111111", l_encoded)

        bits = [255]
        l_encoded = encode0(bits)
        self.assertEqual("11111111", l_encoded)

        bits = [0, 0]
        l_encoded = encode0(bits)
        self.assertEqual("0000000000000000", l_encoded)

        bits = [0, 1]
        l_encoded = encode0(bits)
        self.assertEqual("0000000000000001", l_encoded)

        bits = [0, 3]
        l_encoded = encode0(bits)
        self.assertEqual("0000000000000011", l_encoded)

        bits = [0, 7]
        l_encoded = encode0(bits)
        self.assertEqual("0000000000000111", l_encoded)

        bits = [0, 15]
        l_encoded = encode0(bits)
        self.assertEqual("0000000000001111", l_encoded)

        bits = [0, 31]
        l_encoded = encode0(bits)
        self.assertEqual("0000000000011111", l_encoded)

        bits = [0, 63]
        l_encoded = encode0(bits)
        self.assertEqual("0000000000111111", l_encoded)

        bits = [0, 127]
        l_encoded = encode0(bits)
        self.assertEqual("0000000001111111", l_encoded)

        bits = [0, 255]
        l_encoded = encode0(bits)
        self.assertEqual("0000000011111111", l_encoded)

        bits = [255, 0]
        l_encoded = encode0(bits)
        self.assertEqual("0000000111111111", l_encoded)

        bits = [255, 1]
        l_encoded = encode0(bits)
        self.assertEqual("0000001111111111", l_encoded)

        bits = [255, 3]
        l_encoded = encode0(bits)
        self.assertEqual("0000011111111111", l_encoded)

        bits = [255, 7]
        l_encoded = encode0(bits)
        self.assertEqual("0000111111111111", l_encoded)

        bits = [255, 15]
        l_encoded = encode0(bits)
        self.assertEqual("0001111111111111", l_encoded)

        bits = [255, 31]
        l_encoded = encode0(bits)
        self.assertEqual("0011111111111111", l_encoded)

        bits = [255, 63]
        l_encoded = encode0(bits)
        self.assertEqual("0111111111111111", l_encoded)

        bits = [255, 255]
        l_encoded = encode0(bits)
        self.assertEqual("1111111111111111", l_encoded)

        self.assertEqual(0, len(encode0(None)))

    def testFromAsciiByteArray(self) -> None:

        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))
        self.assertEqual(0, len(BinaryCodec.fromAscii0([])))

        bits = [0]
        decoded = BinaryCodec.fromAscii0("00000000".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [self.__BIT_0]
        decoded = BinaryCodec.fromAscii0("00000001".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [self.__BIT_0 | self.__BIT_1]
        decoded = BinaryCodec.fromAscii0("00000011".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2]
        decoded = BinaryCodec.fromAscii0("00000111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3]
        decoded = BinaryCodec.fromAscii0("00001111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4
        ]
        decoded = BinaryCodec.fromAscii0("00011111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
        ]
        decoded = BinaryCodec.fromAscii0("00111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
        ]
        decoded = BinaryCodec.fromAscii0("01111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7
        ]
        decoded = BinaryCodec.fromAscii0("11111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            0,
        ]
        decoded = BinaryCodec.fromAscii0("0000000011111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0,
        ]
        decoded = BinaryCodec.fromAscii0("0000000111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1,
        ]
        decoded = BinaryCodec.fromAscii0("0000001111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2,
        ]
        decoded = BinaryCodec.fromAscii0("0000011111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3,
        ]
        decoded = BinaryCodec.fromAscii0("0000111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0 | self.__BIT_1 | self.__BIT_2 | self.__BIT_3 | self.__BIT_4,
        ]
        decoded = BinaryCodec.fromAscii0("0001111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5,
        ]
        decoded = BinaryCodec.fromAscii0("0011111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6,
        ]
        decoded = BinaryCodec.fromAscii0("0111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        bits = [
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
            self.__BIT_0
            | self.__BIT_1
            | self.__BIT_2
            | self.__BIT_3
            | self.__BIT_4
            | self.__BIT_5
            | self.__BIT_6
            | self.__BIT_7,
        ]
        decoded = BinaryCodec.fromAscii0("1111111111111111".encode(self.__CHARSET_UTF8))
        self.assertEqual(bytes(bits), bytes(decoded))

        self.assertEqual(0, len(BinaryCodec.fromAscii0(None)))

    def testFromAsciiCharArray(self) -> None:

        pass  # LLM could not translate this method

    def testToByteArrayFromString(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeByteArray(self) -> None:

        pass  # LLM could not translate this method

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

        with pytest.raises(DecoderException):
            self.instance.decode1(object())

    def tearDown(self) -> None:
        self.instance = None

    def setUp(self) -> None:
        self.instance = BinaryCodec()

    def assertDecodeObject(self, bits: typing.List[int], encodeMe: str) -> None:

        decoded = self.instance.decode1(encodeMe)
        self.assertEqual("".join(map(chr, bits)), "".join(map(chr, decoded)))

        if encodeMe is None:
            decoded = self.instance.decode0(None)
        else:
            decoded = self.instance.decode1(encodeMe.encode(self.__CHARSET_UTF8))
        self.assertEqual("".join(map(chr, bits)), "".join(map(chr, decoded)))

        if encodeMe is None:
            decoded = self.instance.decode1(None)
        else:
            decoded = self.instance.decode1(list(encodeMe))
        self.assertEqual("".join(map(chr, bits)), "".join(map(chr, decoded)))
