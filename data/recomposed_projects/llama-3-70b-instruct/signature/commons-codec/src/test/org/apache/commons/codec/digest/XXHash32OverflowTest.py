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
        hugeLength = Integer.MAX_VALUE - (unprocessedSize - 1)
        self.assertTrue(
            "This should overflow to negative",
            unprocessedSize + hugeLength < bufferSize,
        )

        bytes = None
        try:
            bytes = [0] * hugeLength
        except OutOfMemoryError:
            pass
        self.assertTrue("Cannot allocate array of length " + hugeLength, bytes != None)

        inc = XXHash32.XXHash321()
        inc.update1(bytes, 0, unprocessedSize)
        inc.update1(bytes, 0, hugeLength)
