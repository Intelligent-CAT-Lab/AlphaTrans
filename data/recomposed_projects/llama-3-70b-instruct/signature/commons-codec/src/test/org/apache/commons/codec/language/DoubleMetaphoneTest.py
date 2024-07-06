from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *


class DoubleMetaphoneTest(StringEncoderAbstractTest, unittest.TestCase):

    __FIXTURE: typing.List[typing.List[str]] = (
        None  # LLM could not translate this field
    )

    def testSetMaxCodeLength(self) -> None:
        value = "jumped"

        doubleMetaphone = DoubleMetaphone()

        self.assertEqual("Default Max Code Length", 4, doubleMetaphone.getMaxCodeLen())
        self.assertEqual(
            "Default Primary", "JMPT", doubleMetaphone.doubleMetaphone1(value, False)
        )
        self.assertEqual(
            "Default Alternate", "AMPT", doubleMetaphone.doubleMetaphone1(value, True)
        )

        doubleMetaphone.setMaxCodeLen(3)
        self.assertEqual("Set Max Code Length", 3, doubleMetaphone.getMaxCodeLen())
        self.assertEqual(
            "Max=3 Primary", "JMP", doubleMetaphone.doubleMetaphone1(value, False)
        )
        self.assertEqual(
            "Max=3 Alternate", "AMP", doubleMetaphone.doubleMetaphone1(value, True)
        )

    def testNTilde(self) -> None:
        self.assertTrue(
            self.getStringEncoder().isDoubleMetaphoneEqual0("\u00f1", "N")
        )  # n-tilde

    def testIsDoubleMetaphoneNotEqual(self) -> None:
        self.doubleMetaphoneNotEqualTest(False)
        self.doubleMetaphoneNotEqualTest(True)

    def testIsDoubleMetaphoneEqualWithMATCHES(self) -> None:
        self.validateFixture(self.__MATCHES)
        for i in range(len(self.__MATCHES)):
            name0: str = self.__MATCHES[i][0]
            name1: str = self.__MATCHES[i][1]
            match1: bool = self._stringEncoder.isDoubleMetaphoneEqual1(
                name0, name1, False
            )
            match2: bool = self._stringEncoder.isDoubleMetaphoneEqual1(
                name0, name1, True
            )
            if not match1 and not match2:
                self.fail("Expected match [" + str(i) + "] " + name0 + " and " + name1)

    def testIsDoubleMetaphoneEqualExtended3(self) -> None:

        pass  # LLM could not translate this method

    def testIsDoubleMetaphoneEqualExtended2(self) -> None:
        testFixture = [["Jablonski", "Yablonsky"]]
        self.doubleMetaphoneEqualTest(testFixture, True)

    def testIsDoubleMetaphoneEqualExtended1(self) -> None:

        pass  # LLM could not translate this method

    def testIsDoubleMetaphoneEqualBasic(self) -> None:

        pass  # LLM could not translate this method

    def testEmpty(self) -> None:
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(None))
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(""))
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(" "))
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0("\t\n\r "))

    def testDoubleMetaphone(self) -> None:
        self.__assertDoubleMetaphone("TSTN", "testing")
        self.__assertDoubleMetaphone("0", "The")
        self.__assertDoubleMetaphone("KK", "quick")
        self.__assertDoubleMetaphone("PRN", "brown")
        self.__assertDoubleMetaphone("FKS", "fox")
        self.__assertDoubleMetaphone("JMPT", "jumped")
        self.__assertDoubleMetaphone("AFR", "over")
        self.__assertDoubleMetaphone("0", "the")
        self.__assertDoubleMetaphone("LS", "lazy")
        self.__assertDoubleMetaphone("TKS", "dogs")
        self.__assertDoubleMetaphone("MKFR", "MacCafferey")
        self.__assertDoubleMetaphone("STFN", "Stephan")
        self.__assertDoubleMetaphone("KSSK", "Kuczewski")
        self.__assertDoubleMetaphone("MKLL", "McClelland")
        self.__assertDoubleMetaphone("SNHS", "san jose")
        self.__assertDoubleMetaphone("SNFP", "xenophobia")

        self.assertDoubleMetaphoneAlt("TSTN", "testing")
        self.assertDoubleMetaphoneAlt("T", "The")
        self.assertDoubleMetaphoneAlt("KK", "quick")
        self.assertDoubleMetaphoneAlt("PRN", "brown")
        self.assertDoubleMetaphoneAlt("FKS", "fox")
        self.assertDoubleMetaphoneAlt("AMPT", "jumped")
        self.assertDoubleMetaphoneAlt("AFR", "over")
        self.assertDoubleMetaphoneAlt("T", "the")
        self.assertDoubleMetaphoneAlt("LS", "lazy")
        self.assertDoubleMetaphoneAlt("TKS", "dogs")
        self.assertDoubleMetaphoneAlt("MKFR", "MacCafferey")
        self.assertDoubleMetaphoneAlt("STFN", "Stephan")
        self.assertDoubleMetaphoneAlt("KXFS", "Kutchefski")
        self.assertDoubleMetaphoneAlt("MKLL", "McClelland")
        self.assertDoubleMetaphoneAlt("SNHS", "san jose")
        self.assertDoubleMetaphoneAlt("SNFP", "xenophobia")
        self.assertDoubleMetaphoneAlt("FKR", "Fokker")
        self.assertDoubleMetaphoneAlt("AK", "Joqqi")
        self.assertDoubleMetaphoneAlt("HF", "Hovvi")
        self.assertDoubleMetaphoneAlt("XRN", "Czerny")

    def testCodec184(self) -> None:
        self.assertTrue(self._stringEncoder.isDoubleMetaphoneEqual1("", "", False))
        self.assertTrue(self._stringEncoder.isDoubleMetaphoneEqual1("", "", True))
        self.assertFalse(self._stringEncoder.isDoubleMetaphoneEqual1("aa", "", False))
        self.assertFalse(self._stringEncoder.isDoubleMetaphoneEqual1("aa", "", True))
        self.assertFalse(self._stringEncoder.isDoubleMetaphoneEqual1("", "aa", False))
        self.assertFalse(self._stringEncoder.isDoubleMetaphoneEqual1("", "aa", True))

    def testCCedilla(self) -> None:
        self.assertTrue(
            self.getStringEncoder().isDoubleMetaphoneEqual0("\u00e7", "S")
        )  # c-cedilla

    def _createStringEncoder(self) -> DoubleMetaphone:
        return DoubleMetaphone()

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:
        if len(pairs) == 0:
            self.fail("Test fixture is empty")
        for i in range(len(pairs)):
            if len(pairs[i]) != 2:
                self.fail("Error in test fixture in the data array at index " + str(i))

    def doubleMetaphoneNotEqualTest(self, alternate: bool) -> None:
        self.assertFalse(
            self._stringEncoder.isDoubleMetaphoneEqual1("Brain", "Band", alternate)
        )
        self.assertFalse(
            self._stringEncoder.isDoubleMetaphoneEqual1("Band", "Brain", alternate)
        )

        if not alternate:
            self.assertFalse(
                self._stringEncoder.isDoubleMetaphoneEqual0("Brain", "Band")
            )
            self.assertFalse(
                self._stringEncoder.isDoubleMetaphoneEqual0("Band", "Brain")
            )

    def doubleMetaphoneEqualTest(
        self, pairs: typing.List[typing.List[str]], useAlternate: bool
    ) -> None:
        self.validateFixture(pairs)
        for pair in pairs:
            name0 = pair[0]
            name1 = pair[1]
            failMsg = (
                "Expected match between "
                + name0
                + " and "
                + name1
                + " (use alternate: "
                + str(useAlternate)
                + ")"
            )
            self.assertTrue(
                failMsg,
                self.getStringEncoder().isDoubleMetaphoneEqual1(
                    name0, name1, useAlternate
                ),
            )
            self.assertTrue(
                failMsg,
                self.getStringEncoder().isDoubleMetaphoneEqual1(
                    name1, name0, useAlternate
                ),
            )
            if not useAlternate:
                self.assertTrue(
                    failMsg,
                    self.getStringEncoder().isDoubleMetaphoneEqual0(name0, name1),
                )
                self.assertTrue(
                    failMsg,
                    self.getStringEncoder().isDoubleMetaphoneEqual0(name1, name0),
                )

    def assertDoubleMetaphoneAlt(self, expected: str, source: str) -> None:
        self.assertEqual(expected, self._stringEncoder.doubleMetaphone1(source, True))

    def __assertDoubleMetaphone(self, expected: str, source: str) -> None:
        self.assertEqual(expected, self._stringEncoder.encode1(source))
        try:
            self.assertEqual(expected, self._stringEncoder.encode0(source))
        except EncoderException as e:
            self.fail("Unexpected expection: " + str(e))
        self.assertEqual(expected, self._stringEncoder.doubleMetaphone0(source))
        self.assertEqual(expected, self._stringEncoder.doubleMetaphone1(source, False))
