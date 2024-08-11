from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class DoubleMetaphoneTest(StringEncoderAbstractTest, unittest.TestCase):

    # Class Fields Begin
    __FIXTURE: typing.List[typing.List[str]] = None
    __MATCHES: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testSetMaxCodeLength_test5_decomposed(self) -> None:
        pass

    def testSetMaxCodeLength_test4_decomposed(self) -> None:
        pass

    def testSetMaxCodeLength_test3_decomposed(self) -> None:
        pass

    def testSetMaxCodeLength_test2_decomposed(self) -> None:
        pass

    def testSetMaxCodeLength_test1_decomposed(self) -> None:
        pass

    def testSetMaxCodeLength_test0_decomposed(self) -> None:
        pass

    def testNTilde_test1_decomposed(self) -> None:
        pass

    def testNTilde_test0_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneNotEqual_test0_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualWithMATCHES_test1_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualWithMATCHES_test0_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualExtended3_test4_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualExtended3_test3_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualExtended3_test2_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualExtended3_test1_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualExtended3_test0_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualExtended2_test0_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualBasic_test1_decomposed(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualBasic_test0_decomposed(self) -> None:
        pass

    def testEmpty_test7_decomposed(self) -> None:
        pass

    def testEmpty_test6_decomposed(self) -> None:
        pass

    def testEmpty_test5_decomposed(self) -> None:
        pass

    def testEmpty_test4_decomposed(self) -> None:
        pass

    def testEmpty_test3_decomposed(self) -> None:
        pass

    def testEmpty_test2_decomposed(self) -> None:
        pass

    def testEmpty_test1_decomposed(self) -> None:
        pass

    def testEmpty_test0_decomposed(self) -> None:
        pass

    def testDoubleMetaphone_test1_decomposed(self) -> None:
        pass

    def testDoubleMetaphone_test0_decomposed(self) -> None:
        pass

    def testCodec184_test5_decomposed(self) -> None:
        pass

    def testCodec184_test4_decomposed(self) -> None:
        pass

    def testCodec184_test3_decomposed(self) -> None:
        pass

    def testCodec184_test2_decomposed(self) -> None:
        pass

    def testCodec184_test1_decomposed(self) -> None:
        pass

    def testCodec184_test0_decomposed(self) -> None:
        pass

    def testCCedilla_test1_decomposed(self) -> None:
        pass

    def testCCedilla_test0_decomposed(self) -> None:
        pass

    def _createStringEncoder(self) -> DoubleMetaphone:
        pass

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:
        pass

    def doubleMetaphoneNotEqualTest(self, alternate: bool) -> None:
        pass

    def doubleMetaphoneEqualTest(
        self, pairs: typing.List[typing.List[str]], useAlternate: bool
    ) -> None:
        pass

    def assertDoubleMetaphoneAlt(self, expected: str, source: str) -> None:
        pass

    def __assertDoubleMetaphone(self, expected: str, source: str) -> None:
        pass

    # Class Methods End
