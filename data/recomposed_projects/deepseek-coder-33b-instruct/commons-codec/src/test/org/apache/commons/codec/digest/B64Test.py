from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.digest.B64 import *


class B64Test(unittest.TestCase):

    def testB64from24bit(self) -> None:

        buffer = io.StringIO()
        b64from24bit(8, 16, 64, 2, buffer)
        b64from24bit(7, 77, 120, 4, buffer)
        assert buffer.getvalue() == "./spo/"

    def testB64T(self) -> None:

        # assertNotNull(new B64())
        # In Python, we don't have a direct equivalent to Java's assertNotNull.
        # However, we can check if an object is None and raise an exception if it is.
        if B64() is None:
            raise AssertionError("B64 object is None")

        # assertEquals(64, B64.B64T_ARRAY.length);
        # In Python, we don't have a direct equivalent to Java's assertEquals.
        # However, we can check if two values are equal and raise an exception if they are not.
        if len(B64.B64T_ARRAY) != 64:
            raise AssertionError("B64T_ARRAY length is not 64")
