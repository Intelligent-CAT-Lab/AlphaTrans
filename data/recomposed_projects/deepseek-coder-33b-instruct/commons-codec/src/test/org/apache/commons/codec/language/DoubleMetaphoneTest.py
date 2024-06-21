from __future__ import annotations
import re
from dataclasses import field
import sys
import unittest
import pytest
import io
import typing
from typing import *
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

        # Create an instance of DoubleMetaphone
        double_metaphone = DoubleMetaphone()

        # Call the isDoubleMetaphoneEqual0 method
        result = double_metaphone.isDoubleMetaphoneEqual0("\u00f1", "N")

        # Assert that the result is True
        assert result == True

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
                self.fail("Expected match [" + str(i) + "] " + name0 + " and " + name1)

    def testIsDoubleMetaphoneEqualExtended3(self) -> None:

        self.validateFixture(self.__FIXTURE)
        failures = io.StringIO()
        matches = io.StringIO()
        cr = "\n"
        matches.write("private static final String[][] MATCHES = {" + cr)
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
                failures.write(failMsg)
                failCount += 1
            else:
                matches.write('{"' + name0 + '", "' + name1 + '"},' + cr)
        matches.write("};")
        if failCount > 0:
            pass

    def testIsDoubleMetaphoneEqualExtended2(self) -> None:

        testFixture = [["Jablonski", "Yablonsky"]]
        self.doubleMetaphoneEqualTest(testFixture, True)

    def testIsDoubleMetaphoneEqualExtended1(self) -> None:

        # Create an instance of DoubleMetaphone
        double_metaphone = DoubleMetaphone()

        # Define the test cases
        test_cases = [
            ("algorithm", ("ALTRNT", "")),
            ("program", ("PRKRM", "")),
            ("software", ("SRF", "")),
            ("language", ("LNKNT", "")),
            ("computer", ("KMPTR", "")),
            ("technology", ("TNKLT", "")),
            ("information", ("NFXN", "")),
            ("system", ("SMT", "")),
            ("data", ("T", "")),
            ("science", ("SNS", "")),
        ]

        # Iterate over the test cases
        for word, expected in test_cases:
            # Encode the word using DoubleMetaphone
            encoded = double_metaphone.doubleMetaphone(word)

            # Check if the encoded word matches the expected result
            self.assertEqual(encoded, expected)

    def testIsDoubleMetaphoneEqualBasic(self) -> None:

        test_fixture = [
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

        self.doubleMetaphoneEqualTest(test_fixture, False)
        self.doubleMetaphoneEqualTest(test_fixture, True)

    def testEmpty(self) -> None:

        assert self.getStringEncoder().doubleMetaphone0(None) is None
        assert self.getStringEncoder().doubleMetaphone0("") is None
        assert self.getStringEncoder().doubleMetaphone0(" ") is None
        assert self.getStringEncoder().doubleMetaphone0("\t\n\r ") is None

    def testDoubleMetaphone(self) -> None:

        def assertDoubleMetaphone(expected: str, source: str) -> None:
            doubleMetaphone = DoubleMetaphone()
            self.assertEqual(expected, doubleMetaphone.doubleMetaphone(source))

        assertDoubleMetaphone("TSTN", "testing")
        assertDoubleMetaphone("0", "The")
        assertDoubleMetaphone("KK", "quick")
        assertDoubleMetaphone("PRN", "brown")
        assertDoubleMetaphone("FKS", "fox")
        assertDoubleMetaphone("JMPT", "jumped")
        assertDoubleMetaphone("AFR", "over")
        assertDoubleMetaphone("0", "the")
        assertDoubleMetaphone("LS", "lazy")
        assertDoubleMetaphone("TKS", "dogs")
        assertDoubleMetaphone("MKFR", "MacCafferey")
        assertDoubleMetaphone("STFN", "Stephan")
        assertDoubleMetaphone("KSSK", "Kuczewski")
        assertDoubleMetaphone("MKLL", "McClelland")
        assertDoubleMetaphone("SNHS", "san jose")
        assertDoubleMetaphone("SNFP", "xenophobia")

        def assertDoubleMetaphoneAlt(expected: str, source: str) -> None:
            doubleMetaphone = DoubleMetaphone()
            self.assertEqual(expected, doubleMetaphone.doubleMetaphoneAlt(source))

        assertDoubleMetaphoneAlt("TSTN", "testing")
        assertDoubleMetaphoneAlt("T", "The")
        assertDoubleMetaphoneAlt("KK", "quick")
        assertDoubleMetaphoneAlt("PRN", "brown")
        assertDoubleMetaphoneAlt("FKS", "fox")
        assertDoubleMetaphoneAlt("AMPT", "jumped")
        assertDoubleMetaphoneAlt("AFR", "over")
        assertDoubleMetaphoneAlt("T", "the")
        assertDoubleMetaphoneAlt("LS", "lazy")
        assertDoubleMetaphoneAlt("TKS", "dogs")
        assertDoubleMetaphoneAlt("MKFR", "MacCafferey")
        assertDoubleMetaphoneAlt("STFN", "Stephan")
        assertDoubleMetaphoneAlt("KXFS", "Kutchefski")
        assertDoubleMetaphoneAlt("MKLL", "McClelland")
        assertDoubleMetaphoneAlt("SNHS", "san jose")
        assertDoubleMetaphoneAlt("SNFP", "xenophobia")
        assertDoubleMetaphoneAlt("FKR", "Fokker")
        assertDoubleMetaphoneAlt("AK", "Joqqi")
        assertDoubleMetaphoneAlt("HF", "Hovvi")
        assertDoubleMetaphoneAlt("XRN", "Czerny")

    def testCodec184(self) -> None:

        assert DoubleMetaphone().isDoubleMetaphoneEqual1("", "", False)
        assert DoubleMetaphone().isDoubleMetaphoneEqual1("", "", True)
        assert not DoubleMetaphone().isDoubleMetaphoneEqual1("aa", "", False)
        assert not DoubleMetaphone().isDoubleMetaphoneEqual1("aa", "", True)
        assert not DoubleMetaphone().isDoubleMetaphoneEqual1("", "aa", False)
        assert not DoubleMetaphone().isDoubleMetaphoneEqual1("", "aa", True)

    def testCCedilla(self) -> None:

        # Create an instance of DoubleMetaphone
        double_metaphone = DoubleMetaphone()

        # Call the isDoubleMetaphoneEqual0 method
        result = double_metaphone.isDoubleMetaphoneEqual0("\u00e7", "S")

        # Assert that the result is True
        assert result, "c-cedilla"

    def _createStringEncoder(self) -> DoubleMetaphone:

        return DoubleMetaphone()

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:

        if len(pairs) == 0:
            self.fail("Test fixture is empty")
        for i in range(len(pairs)):
            if len(pairs[i]) != 2:
                self.fail("Error in test fixture in the data array at index " + str(i))

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

        from src.main.org.apache.commons.codec.language.DoubleMetaphone import (
            DoubleMetaphone,
        )

        double_metaphone = DoubleMetaphone()
        result = double_metaphone.doubleMetaphone1(source, True)

        assert expected == result, f"Expected {expected}, but got {result}"

    def __assertDoubleMetaphone(self, expected: str, source: str) -> None:

        # Calling encode1 method from DoubleMetaphone class
        try:
            assert expected == self.getStringEncoder().encode1(source)
        except AssertionError:
            self.fail("Unexpected exception: " + str(AssertionError))

        # Calling encode0 method from DoubleMetaphone class
        try:
            assert expected == self.getStringEncoder().encode0(source)
        except EncoderException as e:
            self.fail("Unexpected exception: " + str(e))
        except AssertionError:
            self.fail("Unexpected exception: " + str(AssertionError))

        # Calling doubleMetaphone0 method from DoubleMetaphone class
        try:
            assert expected == self.getStringEncoder().doubleMetaphone0(source)
        except AssertionError:
            self.fail("Unexpected exception: " + str(AssertionError))

        # Calling doubleMetaphone1 method from DoubleMetaphone class
        try:
            assert expected == self.getStringEncoder().doubleMetaphone1(source, False)
        except AssertionError:
            self.fail("Unexpected exception: " + str(AssertionError))
