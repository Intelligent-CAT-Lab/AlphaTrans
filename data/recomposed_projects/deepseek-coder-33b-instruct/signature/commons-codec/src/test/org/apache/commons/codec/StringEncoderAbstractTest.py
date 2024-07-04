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

    _stringEncoder: StringEncoder = self._createStringEncoder()

    def testLocaleIndependence(self) -> None:

        encoder = self.getStringEncoder()

        data = [
            "I",
            "i",
        ]

        orig = locale.getdefaultlocale()
        locales = [locale.ENGLISH, locale.LOCALE_CANADA, locale.getdefaultlocale()]

        try:
            for element in data:
                ref = None
                for j in range(len(locales)):
                    locale.setlocale(locale.LC_ALL, locales[j])
                    if j <= 0:
                        ref = encoder.encode(element)
                    else:
                        cur = None
                        try:
                            cur = encoder.encode(element)
                        except Exception as e:
                            self.fail(
                                locale.getdefaultlocale().__str__() + ": " + str(e)
                            )
                        self.assertEqual(
                            locale.getdefaultlocale().__str__() + ": ", ref, cur
                        )
        finally:
            locale.setlocale(locale.LC_ALL, orig)

    def testEncodeWithInvalidObject(self) -> None:

        exception_thrown = False
        try:
            encoder = self.getStringEncoder()
            encoder.encode(3.4)
        except Exception as e:
            exception_thrown = True

        self.assertTrue(
            "An exception was not thrown when we tried to encode " + "a Float object",
            exception_thrown,
        )

    def testEncodeNull(self) -> None:

        encoder = self.getStringEncoder()
        try:
            encoder.encode(None)
        except EncoderException:
            pass

    def testEncodeEmpty(self) -> None:

        encoder = self.getStringEncoder()
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

        try:
            self.assertEqual(
                "Source: " + source, expected, self.getStringEncoder().encode(source)
            )
        except EncoderException as e:
            raise pytest.fail("EncoderException: " + str(e))

    def _createStringEncoder(self) -> typing.Any:
        pass
