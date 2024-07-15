from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import unittest
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *


class BinaryEncoderAbstractTest(ABC, unittest.TestCase):

    def testEncodeNull(self) -> None:

        encoder = self._makeEncoder()
        with pytest.raises(EncoderException):
            encoder.encode(None)

    def testEncodeEmpty(self) -> None:

        # Create an instance of BinaryEncoder
        encoder = self._makeEncoder()

        # Call the encode method with an empty byte array
        encoder.encode([])

    def _makeEncoder(self) -> BinaryEncoder:
        pass
