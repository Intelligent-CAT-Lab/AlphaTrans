from __future__ import annotations
import locale
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.Encoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class StringEncoderAbstractTest(ABC, unittest.TestCase):

    _stringEncoder: typing.Any = self._createStringEncoder()

    def testLocaleIndependence(self) -> None:
        encoder: StringEncoder = self.getStringEncoder()

        data: List[str] = ["I", "i"]

        orig: Locale = Locale.getDefault()
        locales: List[Locale] = [Locale.ENGLISH, Locale("tr"), Locale.getDefault()]

        try:
            for element in data:
                ref: str = None
                for j in range(len(locales)):
                    Locale.setDefault(locales[j])
                    if j <= 0:
                        ref = encoder.encode(element)
                    else:
                        cur: str = None
                        try:
                            cur = encoder.encode(element)
                        except Exception as e:
                            self.fail(
                                Locale.getDefault().toString() + ": " + e.getMessage()
                            )
                        self.assertEqual(
                            Locale.getDefault().toString() + ": ", ref, cur
                        )
        finally:
            Locale.setDefault(orig)

    def testEncodeWithInvalidObject(self) -> None:
        exceptionThrown = False
        try:
            encoder = self.getStringEncoder()
            encoder.encode(3.4)
        except Exception as e:
            exceptionThrown = True
        self.assertTrue(
            exceptionThrown,
            "An exception was not thrown when we tried to encode a Float object",
        )

    def testEncodeNull(self) -> None:
        encoder: StringEncoder = self.getStringEncoder()
        try:
            encoder.encode(None)
        except EncoderException as ee:
            pass

    def testEncodeEmpty(self) -> None:
        encoder: Encoder = self.getStringEncoder()
        encoder.encode("")
        encoder.encode(" ")
        encoder.encode("\t")

    def getStringEncoder(self) -> typing.Any:
        return self._stringEncoder

    def _checkEncodingVariations(self, expected: str, data: typing.List[str]) -> None:
        for element in data:
            self.checkEncoding(expected, element)

    def _checkEncodings(self, data: typing.List[typing.List[str]]) -> None:
        for element in data:
            self.checkEncoding(element[1], element[0])

    def checkEncoding(self, expected: str, source: str) -> None:
        assert expected == self.getStringEncoder().encode(source), f"Source: {source}"

    def _createStringEncoder(self) -> typing.Any:
        return self.createStringEncoder()
