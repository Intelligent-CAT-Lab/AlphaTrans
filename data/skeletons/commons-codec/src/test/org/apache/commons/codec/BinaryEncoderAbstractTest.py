from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
import unittest
import os
import io
from abc import ABC

# Imports End


class BinaryEncoderAbstractTest(ABC, unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testEncodeNull_test1_decomposed(self) -> None:
        pass

    def testEncodeNull_test0_decomposed(self) -> None:
        pass

    def testEncodeEmpty_test1_decomposed(self) -> None:
        pass

    def testEncodeEmpty_test0_decomposed(self) -> None:
        pass

    def _makeEncoder(self) -> BinaryEncoder:
        pass

    # Class Methods End
