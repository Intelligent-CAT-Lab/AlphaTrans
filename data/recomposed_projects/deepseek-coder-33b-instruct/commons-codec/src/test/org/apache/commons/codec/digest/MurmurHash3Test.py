from __future__ import annotations
import re
import random
from dataclasses import field
import sys
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.digest.MurmurHash3 import *


class MurmurHash3Test(unittest.TestCase):

    __RANDOM_BYTES: typing.List[int] = None
    __RANDOM_INTS: typing.List[int] = None  # LLM could not translate this field

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

    def testIncrementalHashWithUnprocessedBytesAndHugeLengthArray(self) -> None:

        unprocessed_size: int = 3
        huge_length: int = sys.maxsize - 2
        assert unprocessed_size + huge_length < 4, "This should overflow to negative"

        bytes: typing.Optional[bytes] = None
        try:
            bytes = bytearray(huge_length)
        except MemoryError:
            pass
        assert bytes is not None, "Cannot allocate array of length " + str(huge_length)

        inc: IncrementalHash32x86 = IncrementalHash32x86()
        inc.start(0)
        inc.add(bytes, 0, unprocessed_size)
        inc.add(bytes, 0, huge_length)

    def testIncrementalHash32x86(self) -> None:

        def assertIncrementalHash32x86(
            bytes: typing.List[int], seed: int, *blocks: int
        ) -> None:
            pass

        def createRandomBlocks(maxLength: int) -> typing.List[int]:
            pass

        bytes = [0] * 1023
        for seed in [-567, 0, 6787990]:
            assertIncrementalHash32x86(bytes, seed, 0, 0)
            assertIncrementalHash32x86(bytes, seed, 1, 1, 1, 1, 1, 1, 1, 1)
            assertIncrementalHash32x86(bytes, seed, 1, 4)
            assertIncrementalHash32x86(bytes, seed, 2, 4)
            assertIncrementalHash32x86(bytes, seed, 3, 4)
            assertIncrementalHash32x86(bytes, seed, 4, 1)
            assertIncrementalHash32x86(bytes, seed, 4, 2)
            assertIncrementalHash32x86(bytes, seed, 4, 3)
            assertIncrementalHash32x86(bytes, seed, 4, 16, 64)
            for _ in range(10):
                assertIncrementalHash32x86(bytes, seed, createRandomBlocks(len(bytes)))

    def testIncrementalHash32(self) -> None:

        bytes = [0] * 1023
        for _ in range(len(bytes)):
            bytes[_] = random.randint(0, 255)

        for seed in [-567, 0, 6787990]:
            self.__assertIncrementalHash32(bytes, seed, 0, 0)
            self.__assertIncrementalHash32(bytes, seed, 1, 1, 1, 1, 1, 1, 1, 1)
            self.__assertIncrementalHash32(bytes, seed, 1, 4)
            self.__assertIncrementalHash32(bytes, seed, 2, 4)
            self.__assertIncrementalHash32(bytes, seed, 3, 4)
            self.__assertIncrementalHash32(bytes, seed, 4, 1)
            self.__assertIncrementalHash32(bytes, seed, 4, 2)
            self.__assertIncrementalHash32(bytes, seed, 4, 3)
            self.__assertIncrementalHash32(bytes, seed, 4, 16, 64)
            for _ in range(10):
                self.__assertIncrementalHash32x86(
                    bytes, seed, self.__createRandomBlocks(len(bytes))
                )

    @staticmethod
    def __assertIncrementalHash32(
        bytes: typing.List[int], seed: int, *blocks: int
    ) -> None:
        pass

    @staticmethod
    def __assertIncrementalHash32x86(
        bytes: typing.List[int], seed: int, blocks: typing.List[int]
    ) -> None:
        pass

    @staticmethod
    def __createRandomBlocks(maxLength: int) -> typing.List[int]:
        pass

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
        chars = [None] * ((maxSize - minSize) * 2)
        for i in range(1000):
            pos = 0
            size = random.randint(minSize, maxSize)
            for j in range(size):
                codePoint = random.randint(0, codePoints)
                chars[pos : pos + len(chr(codePoint))] = chr(codePoint)
                pos += len(chr(codePoint))
            text = "".join(chars[:pos])
            bytes = StringUtils.getBytesUtf8(text)
            h1 = MurmurHash3.hash1282(bytes, 0, len(bytes), seed)
            h2 = MurmurHash3.hash1281(text)
            assert h1 == h2, f"Arrays are not equal. h1: {h1}, h2: {h2}"

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
            assert hash[0] != h1, "Did not expect hash64 to match upper bits of hash128"
            assert hash[1] != h1, "Did not expect hash64 to match lower bits of hash128"

    def testHash64WithPrimitives(self) -> None:

        offset = 0
        seed = 104729

        iters = 1000
        shortBuffer = bytearray(MurmurHash3.SHORT_BYTES)
        intBuffer = bytearray(MurmurHash3.INTEGER_BYTES)
        longBuffer = bytearray(MurmurHash3.LONG_BYTES)
        shortBytes = bytes(shortBuffer)
        intBytes = bytes(intBuffer)
        longBytes = bytes(longBuffer)
        for i in range(iters):
            ln = random.getrandbits(64)
            in_ = ln >> 3
            sn = (ln >> 5) & 0xFFFF
            shortBuffer[0:2] = sn.to_bytes(2, byteorder="big", signed=True)
            assert MurmurHash3.hash645(
                shortBytes, offset, len(shortBytes), seed
            ) == MurmurHash3.hash642(sn)
            intBuffer[0:4] = in_.to_bytes(4, byteorder="big", signed=True)
            assert MurmurHash3.hash645(
                intBytes, offset, len(intBytes), seed
            ) == MurmurHash3.hash641(in_)
            longBuffer[0:8] = ln.to_bytes(8, byteorder="big", signed=True)
            assert MurmurHash3.hash645(
                longBytes, offset, len(longBytes), seed
            ) == MurmurHash3.hash640(ln)

    def testHash64WithOffsetAndLength(self) -> None:

        origin = StringUtils.getBytesUtf8(self.__TEST_HASH64)
        originOffset = bytearray(b"\x7B" * (len(origin) + 150))
        originOffset[150 : 150 + len(origin)] = origin
        hash = MurmurHash3.hash644(originOffset, 150, len(origin))
        assert hash == 5785358552565094607

    def testHash64(self) -> None:

        origin: bytes = StringUtils.getBytesUtf8(self.__TEST_HASH64)
        hash: int = MurmurHash3.hash643(origin)
        assert hash == 5785358552565094607

    def testHash32x86WithTrailingNegativeSignedBytes(self) -> None:

        self.assertEqual(-43192051, MurmurHash3.hash32x861(bytearray([-1]), 0, 1, 0))
        self.assertEqual(
            -582037868, MurmurHash3.hash32x861(bytearray([0, -1]), 0, 2, 0)
        )
        self.assertEqual(
            922088087, MurmurHash3.hash32x861(bytearray([0, 0, -1]), 0, 3, 0)
        )
        self.assertEqual(
            -1309567588, MurmurHash3.hash32x861(bytearray([-1, 0]), 0, 2, 0)
        )
        self.assertEqual(
            -363779670, MurmurHash3.hash32x861(bytearray([-1, 0, 0]), 0, 3, 0)
        )
        self.assertEqual(
            -225068062, MurmurHash3.hash32x861(bytearray([0, -1, 0]), 0, 3, 0)
        )

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
        chars = [None] * ((maxSize - minSize) * 2)
        for i in range(1000):
            pos = 0
            size = random.randint(minSize, maxSize)
            for j in range(size):
                codePoint = random.randint(0, codePoints)
                chars[pos : pos + 1] = chr(codePoint)
                pos += 1
            text = "".join(chars[:pos])
            bytes = StringUtils.getBytesUtf8(text)
            h1 = MurmurHash3.hash328(bytes, 0, len(bytes), seed)
            h2 = MurmurHash3.hash325(text)
            assert h1 == h2

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
            buffer[0:8] = i.to_bytes(8, "big")
            assert MurmurHash3.hash32x861(
                bytes, offset, length, seed
            ) == MurmurHash3.hash323(i, seed)

    def testHash32Long(self) -> None:

        offset = 0
        seed = 104729

        length = MurmurHash3.LONG_BYTES
        buffer = bytearray(length)
        bytes = buffer
        data = self.__createLongTestData()
        for i in data:
            buffer[0:8] = i.to_bytes(8, "big")
            assert MurmurHash3.hash32x861(
                bytes, offset, length, seed
            ) == MurmurHash3.hash322(i)

    def testHash32LongLongSeed(self) -> None:

        offset = 0
        seed = 104729

        length = MurmurHash3.LONG_BYTES * 2
        buffer = bytearray(length)
        data = self.__createLongTestData()
        for i in data:
            for j in data:
                buffer[0:8] = i.to_bytes(8, "big")
                buffer[MurmurHash3.LONG_BYTES : MurmurHash3.LONG_BYTES + 8] = (
                    j.to_bytes(8, "big")
                )
                assert MurmurHash3.hash32x861(
                    buffer, offset, length, seed
                ) == MurmurHash3.hash321(i, j, seed)

    def testHash32LongLong(self) -> None:

        offset = 0
        seed = 104729

        length = MurmurHash3.LONG_BYTES * 2
        buffer = bytearray(length)
        bytes = buffer
        data = self.__createLongTestData()
        for i in data:
            for j in data:
                buffer[0:8] = i.to_bytes(8, byteorder="big", signed=True)
                buffer[MurmurHash3.LONG_BYTES : MurmurHash3.LONG_BYTES + 8] = (
                    j.to_bytes(8, byteorder="big", signed=True)
                )
                assert MurmurHash3.hash32x861(
                    bytes, offset, length, seed
                ) == MurmurHash3.hash320(i, j)

    @staticmethod
    def __createRandomBlocks(maxLength: int) -> typing.List[int]:

        blocks = [0] * 20
        count = 0
        length = 0
        while count < len(blocks) and length < maxLength:
            size = random.randint(1, 9)
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

        data = [0] * 100
        data[0] = 0
        data[1] = -9223372036854775808
        data[2] = 9223372036854775807
        data[3] = -1
        for i in range(4, len(data)):
            data[i] = random.randint(-9223372036854775808, 9223372036854775807)
        return data
