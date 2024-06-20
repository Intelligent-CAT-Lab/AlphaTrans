from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.Encoder import *
import unittest
import typing
from typing import *
import io
from abc import ABC

# Imports End


class StringEncoderAbstractTest(ABC, unittest.TestCase):

    # Class Fields Begin
    _stringEncoder: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def testLocaleIndependence(self) -> None:
        pass

    def testEncodeWithInvalidObject(self) -> None:
        pass

    def testEncodeNull(self) -> None:
        pass

    def testEncodeEmpty(self) -> None:
        pass

    def getStringEncoder(self) -> typing.Any:
        pass

    def _checkEncodingVariations(self, expected: str, data: typing.List[str]) -> None:
        pass

    def _checkEncodings(self, data: typing.List[typing.List[str]]) -> None:
        pass

    def checkEncoding(self, expected: str, source: str) -> None:
        pass

    def _createStringEncoder(self) -> typing.Any:
        pass

    # Class Methods End
