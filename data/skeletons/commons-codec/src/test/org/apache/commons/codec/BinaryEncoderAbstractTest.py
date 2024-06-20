from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
import unittest
import io
from abc import ABC

# Imports End


class BinaryEncoderAbstractTest(ABC, unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testEncodeNull(self) -> None:
        pass

    def testEncodeEmpty(self) -> None:
        pass

    def _makeEncoder(self) -> BinaryEncoder:
        pass

    # Class Methods End
