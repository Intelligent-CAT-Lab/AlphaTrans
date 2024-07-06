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

    __MATCHES: typing.List[typing.List[str]] = (
        None  # LLM could not translate this field
    )

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

        double_metaphone = DoubleMetaphone()
        assert double_metaphone.isDoubleMetaphoneEqual0("\u00f1", "N")

    def testIsDoubleMetaphoneNotEqual(self) -> None:

        self.doubleMetaphoneNotEqualTest(False)
        self.doubleMetaphoneNotEqualTest(True)

    def testIsDoubleMetaphoneEqualWithMATCHES(self) -> None:

        self.validateFixture(self.__MATCHES)

        for i in range(len(self.__MATCHES)):
            name0 = self.__MATCHES[i][0]
            name1 = self.__MATCHES[i][1]
            match1 = self.getStringEncoder().isDoubleMetaphoneEqual1(
                name0, name1, False
            )
            match2 = self.getStringEncoder().isDoubleMetaphoneEqual1(name0, name1, True)

            if not match1 and not match2:
                self.fail(f"Expected match [{i}] {name0} and {name1}")

    def testIsDoubleMetaphoneEqualExtended3(self) -> None:

        self.validateFixture(self.__FIXTURE)
        failures = []
        matches = []
        cr = "\n"
        matches.append("__MATCHES = [" + cr)
        failCount = 0
        for i in range(len(self.__FIXTURE)):
            name0 = self.__FIXTURE[i][0]
            name1 = self.__FIXTURE[i][1]
            match1 = self.getStringEncoder().isDoubleMetaphoneEqual1(
                name0, name1, False
            )
            match2 = self.getStringEncoder().isDoubleMetaphoneEqual1(name0, name1, True)
            if not match1 and not match2:
                failMsg = "[" + str(i) + "] " + name0 + " and " + name1 + cr
                failures.append(failMsg)
                failCount += 1
            else:
                matches.append('["' + name0 + '", "' + name1 + '"],' + cr)
        matches.append("];")
        if failCount > 0:
            self.fail(
                "Test failed with " + str(failCount) + " failures: " + "".join(failures)
            )

    def testIsDoubleMetaphoneEqualExtended2(self) -> None:

        testFixture = [["Jablonski", "Yablonsky"]]
        self.doubleMetaphoneEqualTest(testFixture, True)

    def testIsDoubleMetaphoneEqualExtended1(self) -> None:

        double_metaphone: DoubleMetaphone = DoubleMetaphone()

        for pair in self.__MATCHES:
            self.assertEqual(
                double_metaphone.isDoubleMetaphoneEqual(pair[0], pair[1]), True
            )

        for pair in self.__FIXTURE:
            self.assertEqual(
                double_metaphone.isDoubleMetaphoneEqual(pair[0], pair[1]), False
            )

    def testIsDoubleMetaphoneEqualBasic(self) -> None:

        testFixture = [
            ["", ""],
            ["Case", "case"],
            ["CASE", "Case"],
            ["caSe", "cAsE"],
            ["cookie", "quick"],
            ["quick", "cookie"],
            ["Brian", "Bryan"],
            ["Auto", "Otto"],
            ["Steven", "Stefan"],
            ["Philipowitz", "Filipowicz"],
        ]

        self.doubleMetaphoneEqualTest(testFixture, False)
        self.doubleMetaphoneEqualTest(testFixture, True)

    def testEmpty(self) -> None:

        assert self.getStringEncoder().doubleMetaphone0(None) is None
        assert self.getStringEncoder().doubleMetaphone0("") is None
        assert self.getStringEncoder().doubleMetaphone0(" ") is None
        assert self.getStringEncoder().doubleMetaphone0("\t\n\r ") is None

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

        dm = DoubleMetaphone()

        assert dm.isDoubleMetaphoneEqual1("", "", False)
        assert dm.isDoubleMetaphoneEqual1("", "", True)
        assert not dm.isDoubleMetaphoneEqual1("aa", "", False)
        assert not dm.isDoubleMetaphoneEqual1("aa", "", True)
        assert not dm.isDoubleMetaphoneEqual1("", "aa", False)
        assert not dm.isDoubleMetaphoneEqual1("", "aa", True)

    def testCCedilla(self) -> None:

        double_metaphone = DoubleMetaphone()
        assert double_metaphone.isDoubleMetaphoneEqual0("\u00e7", "S")

    def _createStringEncoder(self) -> DoubleMetaphone:

        return DoubleMetaphone()

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:

        if len(pairs) == 0:
            self.fail("Test fixture is empty")

        for i in range(len(pairs)):
            if len(pairs[i]) != 2:
                self.fail(f"Error in test fixture in the data array at index {i}")

    def doubleMetaphoneNotEqualTest(self, alternate: bool) -> None:

        assert not self.getStringEncoder().isDoubleMetaphoneEqual1(
            "Brain", "Band", alternate
        )
        assert not self.getStringEncoder().isDoubleMetaphoneEqual1(
            "Band", "Brain", alternate
        )

        if not alternate:
            assert not self.getStringEncoder().isDoubleMetaphoneEqual0("Brain", "Band")
            assert not self.getStringEncoder().isDoubleMetaphoneEqual0("Band", "Brain")

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

            assert self.getStringEncoder().isDoubleMetaphoneEqual1(
                name0, name1, useAlternate
            ), failMsg
            assert self.getStringEncoder().isDoubleMetaphoneEqual1(
                name1, name0, useAlternate
            ), failMsg

            if not useAlternate:
                assert self.getStringEncoder().isDoubleMetaphoneEqual0(
                    name0, name1
                ), failMsg
                assert self.getStringEncoder().isDoubleMetaphoneEqual0(
                    name1, name0
                ), failMsg

    def assertDoubleMetaphoneAlt(self, expected: str, source: str) -> None:

        encoder = DoubleMetaphone()
        result = encoder.doubleMetaphone1(source, True)
        assert result == expected, f"Expected {expected}, but got {result}"

    def __assertDoubleMetaphone(self, expected: str, source: str) -> None:

        assert expected == self.getStringEncoder().encode1(source)
        try:
            assert expected == self.getStringEncoder().encode0(source)
        except EncoderException as e:
            pytest.fail("Unexpected expection: " + str(e))
        assert expected == self.getStringEncoder().doubleMetaphone0(source)
        assert expected == self.getStringEncoder().doubleMetaphone1(source, False)
