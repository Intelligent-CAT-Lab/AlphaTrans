from __future__ import annotations
import re
import sys
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.binary.BaseNCodec import *


class NoOpBaseNCodec(BaseNCodec):

    def _isInAlphabet0(self, value: int) -> bool:
        return False

    def decode1(
        self, pArray: typing.List[int], i: int, length: int, context: Context
    ) -> None:
        pass

    def encode2(
        self, pArray: typing.List[int], i: int, length: int, context: Context
    ) -> None:
        pass

    def __init__(self) -> None:
        super().__init__(0, 0, 0, 0, 0, 0, None)


class BaseNCodecTest(unittest.TestCase):

    codec: BaseNCodec = None

    def testEnsureBufferSizeThrowsOnOverflow(self) -> None:

        ncodec = NoOpBaseNCodec()
        context = Context()

        length = 10
        context.buffer = bytearray(length)
        context.pos = length
        extra = sys.maxsize

        with self.assertRaises(OutOfMemoryError):
            ncodec.ensureBufferSize(extra, context)

    def testEnsureBufferSizeExpandsToBeyondMaxBufferSize(self) -> None:

        self.__assertEnsureBufferSizeExpandsToMaxBufferSize(True)

    def testEnsureBufferSizeExpandsToMaxBufferSize(self) -> None:

        # Call the static method
        self.__assertEnsureBufferSizeExpandsToMaxBufferSize(False)

    def testEnsureBufferSize(self) -> None:

        ncodec = NoOpBaseNCodec()
        context = Context()
        assert context.buffer is None, "Initial buffer should be null"

        context.pos = 76979
        context.readPos = 273
        ncodec._ensureBufferSize(0, context)
        assert context.buffer is not None, "buffer should be initialized"
        assert ncodec._getDefaultBufferSize() == len(
            context.buffer
        ), "buffer should be initialized to default size"
        assert context.pos == 0, "context position"
        assert context.readPos == 0, "context read position"

        ncodec._ensureBufferSize(1, context)
        assert ncodec._getDefaultBufferSize() == len(
            context.buffer
        ), "buffer should not expand unless required"

        length = len(context.buffer)
        context.pos = length
        extra = 1
        ncodec._ensureBufferSize(extra, context)
        assert len(context.buffer) >= length + extra, "buffer should expand"

        length = len(context.buffer)
        context.pos = length
        extra = length * 10
        ncodec._ensureBufferSize(extra, context)
        assert (
            len(context.buffer) >= length + extra
        ), "buffer should expand beyond double capacity"

    def testProvidePaddingByte(self) -> None:

        class NoOpBaseNCodec(BaseNCodec):
            def __init__(self):
                super().__init__(1, 0, 0, 0, 0, 0x25, None)

            def isInAlphabet0(self, b: bytes) -> bool:
                return b == b"O" or b == b"K"  # allow OK

            def encode2(
                self, pArray: bytearray, i: int, length: int, context: Context
            ) -> None:
                pass

            def decode1(
                self, pArray: bytearray, i: int, length: int, context: Context
            ) -> None:
                pass

        self.codec = NoOpBaseNCodec()

        actualPaddingByte = self.codec.pad

        self.assertEqual(0x25, actualPaddingByte)

    def testContainsAlphabetOrPad(self) -> None:

        assert not self.codec._containsAlphabetOrPad(None)
        assert not self.codec._containsAlphabetOrPad([])
        assert self.codec._containsAlphabetOrPad(list(b"OK"))
        assert self.codec._containsAlphabetOrPad(list(b"OK "))
        assert not self.codec._containsAlphabetOrPad(list(b"ok "))
        assert self.codec._containsAlphabetOrPad([self.codec._pad])

    def testIsInAlphabetString(self) -> None:

        self.assertTrue(self.codec.isInAlphabet2("OK"))
        self.assertTrue(self.codec.isInAlphabet2("O=K= \t\n\r"))

    def testIsInAlphabetByteArrayBoolean(self) -> None:

        assert self.codec.isInAlphabet1([], False)
        assert self.codec.isInAlphabet1([ord("O")], False)
        assert not self.codec.isInAlphabet1([ord("O"), ord(" ")], False)
        assert not self.codec.isInAlphabet1([ord(" ")], False)
        assert self.codec.isInAlphabet1([], True)
        assert self.codec.isInAlphabet1([ord("O")], True)
        assert self.codec.isInAlphabet1([ord("O"), ord(" ")], True)
        assert self.codec.isInAlphabet1([ord(" ")], True)

    def testIsInAlphabetByte(self) -> None:

        assert not self.codec.isInAlphabet0(0)
        assert not self.codec.isInAlphabet0(ord("a"))
        assert self.codec.isInAlphabet0(ord("O"))
        assert self.codec.isInAlphabet0(ord("K"))

    def testIsWhiteSpace(self) -> None:

        self.assertTrue(BaseNCodec._isWhiteSpace(ord(" ")))
        self.assertTrue(BaseNCodec._isWhiteSpace(ord("\n")))
        self.assertTrue(BaseNCodec._isWhiteSpace(ord("\r")))
        self.assertTrue(BaseNCodec._isWhiteSpace(ord("\t")))

    def testBaseNCodec(self) -> None:
        self.assertIsNotNone(self.codec)

    def testContextToString(self) -> None:

        context = Context()
        context.buffer = [0, 0, 0]
        context.currentLinePos = 13
        context.eof = True
        context.ibitWorkArea = 777
        context.lbitWorkArea = 999
        context.modulus = 5
        context.pos = 42
        context.readPos = 981
        text = context.toString()
        self.assertTrue(str([0, 0, 0]) in text)
        self.assertTrue("13" in text)
        self.assertTrue("true" in text)
        self.assertTrue("777" in text)
        self.assertTrue("999" in text)
        self.assertTrue("5" in text)
        self.assertTrue("42" in text)
        self.assertTrue("981" in text)

    def setUp(self) -> None:

        class NoOpBaseNCodec(BaseNCodec):
            def __init__(self):
                super().__init__(0, 0, 0, 0, 0, 0, None)

            def isInAlphabet0(self, b: byte) -> bool:
                return b == b"O" or b == b"K"  # allow OK

            def encode2(
                self, pArray: bytearray, i: int, length: int, context: Context
            ) -> None:
                pass

            def decode1(
                self, pArray: bytearray, i: int, length: int, context: Context
            ) -> None:
                pass

        self.codec = NoOpBaseNCodec()

    @staticmethod
    def getPresumableFreeMemory() -> int:

        import gc

        gc.collect()
        allocated_memory = gc.get_objects()
        presumable_free_memory = sys.getsizeof(allocated_memory)
        return presumable_free_memory

    @staticmethod
    def __assumeCanAllocateBufferSize(size: int) -> None:

        bytes = None
        try:
            bytes = bytearray(size)
        except MemoryError:
            pass
        assert bytes is not None, "Cannot allocate array of size: " + str(size)

    @staticmethod
    def __assertEnsureBufferSizeExpandsToMaxBufferSize(
        exceedMaxBufferSize: bool,
    ) -> None:

        length = 0

        presumableFreeMemory = BaseNCodecTest.getPresumableFreeMemory()
        estimatedMemory = (1 << 31) + 32 * 1024 + length
        assert (
            presumableFreeMemory > estimatedMemory
        ), "Not enough free memory for the test"

        max_int = (1 << 31) - 1
        max = min(max_int, BaseNCodec._MAX_BUFFER_SIZE)

        if exceedMaxBufferSize:
            BaseNCodecTest.__assumeCanAllocateBufferSize(max + 1)
            gc.collect()

        ncodec = NoOpBaseNCodec()
        context = Context()

        context.buffer = bytearray(length)
        context.pos = length
        extra = max - length
        if exceedMaxBufferSize:
            extra += 1
        ncodec._ensureBufferSize(extra, context)
        assert len(context.buffer) >= length + extra
