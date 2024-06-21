from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *


class BinaryEncoderAbstractTest(ABC, unittest.TestCase):

    def testEncodeNull(self) -> None:

        encoder = self._makeEncoder()
        try:
            encoder.encode(None)
            self.fail("EncoderException expected")
        except EncoderException:
            pass

    def testEncodeEmpty(self) -> None:

        encoder = self._makeEncoder()
        encoder.encode(bytearray())

    def _makeEncoder(self) -> BinaryEncoder:

        pass
