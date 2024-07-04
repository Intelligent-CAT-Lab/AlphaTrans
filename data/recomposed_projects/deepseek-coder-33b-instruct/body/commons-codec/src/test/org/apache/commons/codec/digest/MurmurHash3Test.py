from __future__ import annotations
import re
import random
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.digest.MurmurHash3 import *


class MurmurHash3Test(unittest.TestCase):

    __RANDOM_BYTES: typing.List[int] = None

    __RANDOM_INTS: typing.List[int] = [
        46,
        246,
        249,
        184,
        247,
        84,
        99,
        144,
        62,
        77,
        195,
        220,
        92,
        20,
        150,
        159,
        38,
        40,
        124,
        252,
        185,
        28,
        63,
        13,
        213,
        172,
        85,
        198,
        118,
        74,
        109,
        157,
        132,
        216,
        76,
        177,
        173,
        23,
        140,
        86,
        146,
        95,
        54,
        176,
        114,
        179,
        234,
        174,
        183,
        141,
        122,
        12,
        60,
        116,
        200,
        142,
        6,
        167,
        59,
        240,
        33,
        29,
        165,
        111,
        243,
        30,
        219,
        110,
        255,
        53,
        32,
        35,
        64,
        225,
        96,
        152,
        70,
        41,
        133,
        80,
        244,
        127,
        57,
        199,
        5,
        164,
        151,
        49,
        26,
        180,
        203,
        83,
        108,
        39,
        126,
        208,
        42,
        206,
        178,
        19,
        69,
        223,
        71,
        231,
        250,
        125,
        211,
        232,
        189,
        55,
        44,
        82,
        48,
        221,
        43,
        192,
        241,
        103,
        155,
        27,
        51,
        163,
        21,
        169,
        91,
        94,
        217,
        191,
        78,
        72,
        93,
        102,
        104,
        105,
        8,
        113,
        100,
        143,
        89,
        245,
        227,
        120,
        160,
        251,
        153,
        145,
        45,
        218,
        168,
        233,
        229,
        253,
        67,
        22,
        182,
        98,
        137,
        128,
        135,
        11,
        214,
        66,
        73,
        171,
        188,
        170,
        131,
        207,
        79,
        106,
        24,
        75,
        237,
        194,
        7,
        129,
        215,
        81,
        248,
        242,
        16,
        25,
        136,
        147,
        156,
        97,
        52,
        10,
        181,
        17,
        205,
        58,
        101,
        68,
        230,
        1,
        37,
        0,
        222,
        88,
        130,
        148,
        224,
        47,
        50,
        197,
        34,
        212,
        196,
        209,
        14,
        36,
        139,
        228,
        154,
        31,
        175,
        202,
        236,
        161,
        3,
        162,
        190,
        254,
        134,
        119,
        4,
        61,
        65,
        117,
        186,
        107,
        204,
        9,
        187,
        201,
        90,
        149,
        226,
        56,
        239,
        238,
        235,
        112,
        87,
        18,
        121,
        115,
        138,
        123,
        210,
        2,
        193,
        166,
        158,
        15,
    ]
    __TEST_HASH64: str = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor"
        + " incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis"
        + " nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        + " Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu"
        + " fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in"
        + " culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde"
        + " omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam"
        + " rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto"
        + " beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit"
        + " aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui"
        + " ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum"
        + " quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius"
        + " modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut"
        + " enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit"
        + " laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure"
        + " reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur,"
        + " vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
    )

    @staticmethod
    def run_static_init():
        MurmurHash3Test.__RANDOM_BYTES = [0] * len(MurmurHash3Test.__RANDOM_INTS)
        for i in range(len(MurmurHash3Test.__RANDOM_BYTES)):
            MurmurHash3Test.__RANDOM_BYTES[i] = MurmurHash3Test.__RANDOM_INTS[i]

    def testIncrementalHashWithUnprocessedBytesAndHugeLengthArray(self) -> None:

        unprocessedSize = 3
        hugeLength = 2**31 - 1 - 2
        self.assertTrue(
            "This should overflow to negative", unprocessedSize + hugeLength < 4
        )

        bytes = None
        try:
            bytes = [0] * hugeLength
        except MemoryError:
            pass
        self.assertTrue(
            "Cannot allocate array of length " + str(hugeLength), bytes is not None
        )

        inc = IncrementalHash32x86()
        inc.start(0)
        inc.add(bytes, 0, unprocessedSize)
        inc.add(bytes, 0, hugeLength)

    def testIncrementalHash32x86(self) -> None:

        bytes = [0] * 1023
        for i in range(len(bytes)):
            bytes[i] = random.randint(0, 255)

        seeds = [-567, 0, 6787990]
        for seed in seeds:
            self.__assertIncrementalHash32x86(bytes, seed, [0, 0])
            self.__assertIncrementalHash32x86(bytes, seed, [1, 1, 1, 1, 1, 1, 1, 1, 1])
            self.__assertIncrementalHash32x86(bytes, seed, [1, 4])
            self.__assertIncrementalHash32x86(bytes, seed, [2, 4])
            self.__assertIncrementalHash32x86(bytes, seed, [3, 4])
            self.__assertIncrementalHash32x86(bytes, seed, [4, 1])
            self.__assertIncrementalHash32x86(bytes, seed, [4, 2])
            self.__assertIncrementalHash32x86(bytes, seed, [4, 3])
            self.__assertIncrementalHash32x86(bytes, seed, [4, 16, 64])
            for i in range(10):
                self.__assertIncrementalHash32x86(
                    bytes, seed, self.__createRandomBlocks(len(bytes))
                )

    def testIncrementalHash32(self) -> None:

        bytes = [0] * 1023
        for i in range(1023):
            bytes[i] = random.randint(0, 255)

        for seed in [-567, 0, 6787990]:
            self.__assertIncrementalHash32(bytes, seed, [0, 0])
            self.__assertIncrementalHash32(bytes, seed, [1, 1, 1, 1, 1, 1, 1, 1, 1])
            self.__assertIncrementalHash32(bytes, seed, [1, 4])
            self.__assertIncrementalHash32(bytes, seed, [2, 4])
            self.__assertIncrementalHash32(bytes, seed, [3, 4])
            self.__assertIncrementalHash32(bytes, seed, [4, 1])
            self.__assertIncrementalHash32(bytes, seed, [4, 2])
            self.__assertIncrementalHash32(bytes, seed, [4, 3])
            self.__assertIncrementalHash32(bytes, seed, [4, 16, 64])
            for i in range(10):
                self.__assertIncrementalHash32x86(
                    bytes, seed, self.__createRandomBlocks(len(bytes))
                )

    def testHash128x64WithOffsetLengthAndNegativeSeed(self) -> None:

        pass  # LLM could not translate this method

    def testHash128x64WithOffsetLengthAndSeed(self) -> None:

        pass  # LLM could not translate this method

    def testHash128x64(self) -> None:

        pass  # LLM could not translate this method

    def testHash128String(self) -> None:

        seed = 104729
        minSize = 1
        maxSize = 11
        codePoints = 112956
        chars = [""] * ((maxSize - minSize) * 2)
        for i in range(1000):
            pos = 0
            size = random.randint(minSize, maxSize)
            for j in range(size):
                codePoint = random.randint(codePoints)
                chars[pos : pos + len(chr(codePoint))] = chr(codePoint)
                pos += len(chr(codePoint))
            text = "".join(chars[:pos])
            bytes = StringUtils.getBytesUtf8(text)
            h1 = MurmurHash3.hash1282(bytes, 0, len(bytes), seed)
            h2 = MurmurHash3.hash1281(text)
            self.assertEqual(h1, h2)

    def testHash128WithOffsetLengthAndNegativeSeed(self) -> None:

        pass  # LLM could not translate this method

    def testHash128WithOffsetLengthAndSeed(self) -> None:

        pass  # LLM could not translate this method

    def testHash128(self) -> None:

        pass  # LLM could not translate this method

    def testHash64InNotEqualToHash128(self) -> None:

        for i in range(32):
            bytes = self.__RANDOM_BYTES[:i]
            h1 = MurmurHash3.hash643(bytes)
            hash = MurmurHash3.hash1280(bytes)
            self.assertNotEqual(
                "Did not expect hash64 to match upper bits of hash128", hash[0], h1
            )
            self.assertNotEqual(
                "Did not expect hash64 to match lower bits of hash128", hash[1], h1
            )

    def testHash64WithPrimitives(self) -> None:

        offset = 0
        seed = 104729

        iters = 1000
        shortBuffer = bytearray(MurmurHash3.SHORT_BYTES)
        intBuffer = bytearray(MurmurHash3.INTEGER_BYTES)
        longBuffer = bytearray(MurmurHash3.LONG_BYTES)
        shortBytes = shortBuffer
        intBytes = intBuffer
        longBytes = longBuffer
        for i in range(iters):
            ln = random.getrandbits(64)
            in_ = ln >> 3
            sn = ln >> 5
            shortBuffer[0:2] = sn.to_bytes(2, "little")
            self.assertEqual(
                MurmurHash3.hash645(shortBytes, offset, len(shortBytes), seed),
                MurmurHash3.hash642(sn),
            )
            intBuffer[0:4] = in_.to_bytes(4, "little")
            self.assertEqual(
                MurmurHash3.hash645(intBytes, offset, len(intBytes), seed),
                MurmurHash3.hash641(in_),
            )
            longBuffer[0:8] = ln.to_bytes(8, "little")
            self.assertEqual(
                MurmurHash3.hash645(longBytes, offset, len(longBytes), seed),
                MurmurHash3.hash640(ln),
            )

    def testHash64WithOffsetAndLength(self) -> None:

        origin = StringUtils.getBytesUtf8(self.__TEST_HASH64)
        originOffset = [123] * (len(origin) + 150)
        originOffset[150:] = origin
        hash = MurmurHash3.hash644(originOffset, 150, len(origin))
        self.assertEqual(5785358552565094607, hash)

    def testHash64(self) -> None:

        origin = StringUtils.getBytesUtf8(self.__TEST_HASH64)
        hash = MurmurHash3.hash643(origin)
        self.assertEqual(5785358552565094607, hash)

    def testHash32x86WithTrailingNegativeSignedBytes(self) -> None:

        pass  # LLM could not translate this method

    def testHash32x86WithOffsetLengthAndSeed(self) -> None:

        pass  # LLM could not translate this method

    def testhash32x86(self) -> None:

        pass  # LLM could not translate this method

    def testHash32WithTrailingNegativeSignedBytesIsInvalid(self) -> None:

        pass  # LLM could not translate this method

    def testHash32String(self) -> None:

        seed = 104729
        minSize = 1
        maxSize = 11
        codePoints = 112956
        chars = [""] * ((maxSize - minSize) * 2)
        for i in range(1000):
            pos = 0
            size = random.randint(minSize, maxSize)
            for j in range(size):
                codePoint = random.randint(codePoints)
                chars[pos : pos + len(chars)] = [chr(codePoint)]
                pos += len(chars)
            text = "".join(chars)
            bytes = StringUtils.getBytesUtf8(text)
            h1 = MurmurHash3.hash328(bytes, 0, len(bytes), seed)
            h2 = MurmurHash3.hash325(text)
            self.assertEqual(h1, h2)

    def testHash32WithOffsetLengthAndSeed(self) -> None:

        pass  # LLM could not translate this method

    def testHash32WithLengthAndSeed(self) -> None:

        pass  # LLM could not translate this method

    def testHash32WithLength(self) -> None:

        pass  # LLM could not translate this method

    def testHash32(self) -> None:

        pass  # LLM could not translate this method

    def testHash32LongSeed(self) -> None:

        offset = 0
        seed = 104729

        length = MurmurHash3.LONG_BYTES
        buffer = bytearray(length)
        bytes = buffer
        data = self.__createLongTestData()
        for i in data:
            buffer[0:8] = i.to_bytes(8, "little")
            self.assertEqual(
                MurmurHash3.hash32x861(bytes, offset, length, seed),
                MurmurHash3.hash323(i, seed),
            )

    def testHash32Long(self) -> None:

        offset = 0
        seed = 104729

        length = MurmurHash3.LONG_BYTES
        buffer = bytearray(length)
        bytes = buffer
        data = self.__createLongTestData()
        for i in data:
            buffer[0:8] = i.to_bytes(8, byteorder="little")
            self.assertEqual(
                MurmurHash3.hash32x861(bytes, offset, length, seed),
                MurmurHash3.hash322(i),
            )

    def testHash32LongLongSeed(self) -> None:

        offset = 0
        seed = 104729

        length = MurmurHash3.LONG_BYTES * 2
        buffer = bytearray(length)
        bytes = buffer
        data = self.__createLongTestData()
        for i in data:
            for j in data:
                buffer[0:8] = i.to_bytes(8, "big")
                buffer[8:16] = j.to_bytes(8, "big")
                self.assertEqual(
                    MurmurHash3.hash32x861(bytes, offset, length, seed),
                    MurmurHash3.hash321(i, j, seed),
                )

    def testHash32LongLong(self) -> None:

        offset = 0
        seed = 104729

        length = MurmurHash3.LONG_BYTES * 2
        buffer = bytearray(length)
        bytes = buffer
        data = self.__createLongTestData()
        for i in data:
            for j in data:
                buffer[0:8] = i.to_bytes(8, "little")
                buffer[8:16] = j.to_bytes(8, "little")
                self.assertEqual(
                    MurmurHash3.hash32x861(bytes, offset, length, seed),
                    MurmurHash3.hash320(i, j),
                )

    @staticmethod
    def __createRandomBlocks(maxLength: int) -> typing.List[int]:

        blocks: typing.List[int] = [0] * 20
        count: int = 0
        length: int = 0

        while count < len(blocks) and length < maxLength:
            size: int = random.randint(1, 9)
            blocks[count] = size
            count += 1
            length += size

        return blocks[:count]

    @staticmethod
    def __assertIncrementalHash32x86(
        bytes: typing.List[int], seed: int, blocks: typing.List[int]
    ) -> None:

        offset = 0
        total = 0
        inc = IncrementalHash32x86()
        inc.start(seed)
        for block in blocks:
            total += block
            h1 = MurmurHash3.hash32x861(bytes, 0, total, seed)
            inc.add(bytes, offset, block)
            offset += block
            h2 = inc.end()
            assert h1 == h2, "Hashes differ"
            assert h1 == inc.end(), "Hashes differ after no additional data"

    @staticmethod
    def __assertIncrementalHash32(
        bytes: typing.List[int], seed: int, blocks: typing.List[int]
    ) -> None:

        offset = 0
        total = 0
        inc = IncrementalHash32x86()
        inc.start(seed)
        for block in blocks:
            total += block
            h1 = MurmurHash3.hash328(bytes, 0, total, seed)
            inc.add(bytes, offset, block)
            offset += block
            h2 = inc.end()
            assert h1 == h2, "Hashes differ"
            assert h1 == inc.end(), "Hashes differ after no additional data"

    @staticmethod
    def __negativeBytes(bytes: typing.List[int], start: int, length: int) -> bool:
        for i in range(start, start + length):
            if bytes[i] < 0:
                return True
        return False

    @staticmethod
    def __createLongTestData() -> typing.List[int]:

        data: typing.List[int] = [0] * 100
        data[0] = 0
        data[1] = -9223372036854775808
        data[2] = 9223372036854775807
        data[3] = -1
        for i in range(4, len(data)):
            data[i] = random.randint(-9223372036854775808, 9223372036854775807)
        return data


MurmurHash3Test.run_static_init()
