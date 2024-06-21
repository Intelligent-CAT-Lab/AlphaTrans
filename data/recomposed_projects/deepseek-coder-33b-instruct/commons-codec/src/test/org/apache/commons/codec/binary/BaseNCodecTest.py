from __future__ import annotations
import re
import sys
import unittest
import pytest
import io
import typing
from typing import *
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

        # Your code here
        pass

    def __init__(self) -> None:

        super().__init__(0, 0, 0, 0, 0, 0, None)


class BaseNCodecTest(unittest.TestCase):

    def testEnsureBufferSizeThrowsOnOverflow(self) -> None:

        class Context:
            def __init__(self):
                self.buffer = None
                self.pos = None

        class NoOpBaseNCodec(BaseNCodec):
            def ensureBufferSize(self, extra: int, context: Context) -> None:
                if context.pos + extra < 0:
                    raise ValueError("Buffer overflow")
                else:
                    context.buffer = bytearray(context.pos + extra)
                    context.pos += extra

        ncodec = NoOpBaseNCodec()
        context = Context()

        length = 10
        context.buffer = bytearray(length)
        context.pos = length
        extra = sys.maxsize
        ncodec.ensureBufferSize(extra, context)

    def testEnsureBufferSizeExpandsToBeyondMaxBufferSize(self) -> None:

        self.__assertEnsureBufferSizeExpandsToMaxBufferSize(True)

    def testEnsureBufferSizeExpandsToMaxBufferSize(self) -> None:

        self.__assertEnsureBufferSizeExpandsToMaxBufferSize(False)

    def testEnsureBufferSize(self) -> None:

        ncodec = NoOpBaseNCodec()
        context = Context()
        assert context.buffer is None, "Initial buffer should be null"

        context.pos = 76979
        context.readPos = 273
        ncodec.ensureBufferSize(0, context)
        assert context.buffer is not None, "buffer should be initialized"
        assert (
            context.buffer.length == ncodec.getDefaultBufferSize()
        ), "buffer should be initialized to default size"
        assert context.pos == 0, "context position"
        assert context.readPos == 0, "context read position"

        ncodec.ensureBufferSize(1, context)
        assert (
            context.buffer.length == ncodec.getDefaultBufferSize()
        ), "buffer should not expand unless required"

        length = context.buffer.length
        context.pos = length
        extra = 1
        ncodec.ensureBufferSize(extra, context)
        assert context.buffer.length >= length + extra, "buffer should expand"

        length = context.buffer.length
        context.pos = length
        extra = length * 10
        ncodec.ensureBufferSize(extra, context)
        assert (
            context.buffer.length >= length + extra
        ), "buffer should expand beyond double capacity"

    def testProvidePaddingByte(self) -> None:

        class BaseNCodec(BaseNCodec):
            def __init__(
                self,
                pad: int,
                isInAlphabet0: Callable[[byte], bool],
                encode2: Callable[[byte, int, int, Context], None],
                decode1: Callable[[byte, int, int, Context], None],
            ):
                super().__init__(1, 0, 0, 0, 0, pad, None)
                self.isInAlphabet0 = isInAlphabet0
                self.encode2 = encode2
                self.decode1 = decode1

            def isInAlphabet(self, b: byte) -> bool:
                return self.isInAlphabet0(b)

            def encode(
                self, pArray: byte, i: int, length: int, context: Context
            ) -> None:
                self.encode2(pArray, i, length, context)

            def decode(
                self, pArray: byte, i: int, length: int, context: Context
            ) -> None:
                self.decode1(pArray, i, length, context)

        codec = BaseNCodec(
            0x25,
            lambda b: b == b"O" or b == b"K",
            lambda pArray, i, length, context: None,
            lambda pArray, i, length, context: None,
        )

        actualPaddingByte = codec.pad

        assert actualPaddingByte == 0x25

    def testContainsAlphabetOrPad(self) -> None:

        codec = BaseNCodec()

        assert not codec.containsAlphabetOrPad(None)
        assert not codec.containsAlphabetOrPad(b"")
        assert codec.containsAlphabetOrPad(b"OK")
        assert codec.containsAlphabetOrPad(b"OK ")
        assert not codec.containsAlphabetOrPad(b"ok ")
        assert codec.containsAlphabetOrPad(bytes([codec.pad]))

    def testIsInAlphabetString(self) -> None:

        codec = BaseNCodec()

        assert codec.isInAlphabet2("OK") == True
        assert codec.isInAlphabet2("O=K= \t\n\r") == True

    def testIsInAlphabetByteArrayBoolean(self) -> None:

        codec = BaseNCodec()

        assert codec.isInAlphabet1(bytearray(b""), False)
        assert codec.isInAlphabet1(bytearray(b"O"), False)
        assert not codec.isInAlphabet1(bytearray(b"O "), False)
        assert not codec.isInAlphabet1(bytearray(b" "), False)
        assert codec.isInAlphabet1(bytearray(b""), True)
        assert codec.isInAlphabet1(bytearray(b"O"), True)
        assert codec.isInAlphabet1(bytearray(b"O "), True)
        assert codec.isInAlphabet1(bytearray(b" "), True)

    def testIsInAlphabetByte(self) -> None:

        codec = BaseNCodec()

        assert not codec.isInAlphabet0(0)
        assert not codec.isInAlphabet0(ord("a"))
        assert codec.isInAlphabet0(ord("O"))
        assert codec.isInAlphabet0(ord("K"))

    def testIsWhiteSpace(self) -> None:

        assert BaseNCodec.isWhiteSpace(ord(" "))
        assert BaseNCodec.isWhiteSpace(ord("\n"))
        assert BaseNCodec.isWhiteSpace(ord("\r"))
        assert BaseNCodec.isWhiteSpace(ord("\t"))

    def testBaseNCodec(self) -> None:

        assert self.codec is not None

    def testContextToString(self) -> None:

        class Context:
            def __init__(self):
                self.buffer = bytearray(3)
                self.currentLinePos = 13
                self.eof = True
                self.ibitWorkArea = 777
                self.lbitWorkArea = 999
                self.modulus = 5
                self.pos = 42
                self.readPos = 981

            def toString(self):
                return f"[{', '.join(str(b) for b in self.buffer)}], {self.currentLinePos}, {self.eof}, {self.ibitWorkArea}, {self.lbitWorkArea}, {self.modulus}, {self.pos}, {self.readPos}"

        context = Context()
        text = context.toString()
        assert "[0, 0, 0]" in text
        assert "13" in text
        assert "True" in text
        assert "777" in text
        assert "999" in text
        assert "5" in text
        assert "42" in text
        assert "981" in text

    def setUp(self) -> None:

        class BaseNCodecSubclass(BaseNCodec):
            def __init__(self):
                super().__init__(0, 0, 0, 0, 0, 0, None)

            def isInAlphabet0(self, b: bytes) -> bool:
                return b == b"O" or b == b"K"

            def encode2(
                self, pArray: bytearray, i: int, length: int, context: Context
            ) -> None:
                pass

            def decode1(
                self, pArray: bytearray, i: int, length: int, context: Context
            ) -> None:
                pass

        self.codec = BaseNCodecSubclass()

    @staticmethod
    def getPresumableFreeMemory() -> int:

        import gc

        gc.collect()
        allocated_memory = gc.get_objects_allocated_memory()
        presumable_free_memory = gc.get_objects_max_memory() - allocated_memory
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

        max_value = (1 << 31) - 1

        if exceedMaxBufferSize:
            BaseNCodecTest.__assumeCanAllocateBufferSize(max_value + 1)
            import gc

            gc.collect()

        ncodec = NoOpBaseNCodec()
        context = Context()

        context.buffer = bytearray(length)
        context.pos = length
        extra = max_value - length
        if exceedMaxBufferSize:
            extra += 1
        ncodec.ensureBufferSize(extra, context)
        assert len(context.buffer) >= length + extra
