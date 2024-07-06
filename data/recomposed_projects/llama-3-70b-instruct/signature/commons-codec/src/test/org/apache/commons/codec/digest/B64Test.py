from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.B64 import *


class B64Test(unittest.TestCase):

    def testB64from24bit(self) -> None:
        buffer = ""
        B64.b64from24bit(8, 16, 64, 2, buffer)
        B64.b64from24bit(7, 77, 120, 4, buffer)
        self.assertEqual("./spo/", buffer)

    def testB64T(self) -> None:
        self.assertIsNotNone(B64())  # for the 100% code coverage :)
        self.assertEqual(64, len(B64.B64T_ARRAY))
