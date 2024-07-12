from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.XXHash32 import *


class XXHash32OverflowTest(unittest.TestCase):

    def testIncrementalHashWithUnprocessedBytesAndHugeLengthArray(self) -> None:

        bufferSize = 16
        unprocessedSize = bufferSize - 1
        hugeLength = (2**31) - 1 - (unprocessedSize - 1)
        assert (
            unprocessedSize + hugeLength < bufferSize
        ), "This should overflow to negative"

        bytes = None
        try:
            bytes = bytearray(hugeLength)
        except MemoryError:
            pass
        assert bytes is not None, "Cannot allocate array of length " + str(hugeLength)

        inc = XXHash32.XXHash321()
        inc.update1(bytes, 0, unprocessedSize)
        inc.update1(bytes, 0, hugeLength)
