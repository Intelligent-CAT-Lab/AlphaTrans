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
        try:
            encoder.encode(None)
            self.fail("EncoderException exptected")
        except EncoderException as ee:
            pass

    def testEncodeEmpty(self) -> None:
        encoder: BinaryEncoder = self._makeEncoder()
        encoder.encode([])

    def _makeEncoder(self) -> BinaryEncoder:
        return self.makeEncoder()
