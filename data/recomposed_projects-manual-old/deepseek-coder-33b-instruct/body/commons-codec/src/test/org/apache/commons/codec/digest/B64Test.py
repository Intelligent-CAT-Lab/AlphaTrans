from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.B64 import *


class B64Test(unittest.TestCase):

    def testB64from24bit(self) -> None:

        buffer = io.StringIO()
        B64.b64from24bit(8, 16, 64, 2, buffer)
        B64.b64from24bit(7, 77, 120, 4, buffer)
        self.assertEqual("./spo/", buffer.getvalue())

    def testB64T(self) -> None:

        # Check if the B64 object is not None
        self.assertIsNotNone(B64())

        # Check if the length of B64T_ARRAY is 64
        self.assertEqual(64, len(B64.B64T_ARRAY))
