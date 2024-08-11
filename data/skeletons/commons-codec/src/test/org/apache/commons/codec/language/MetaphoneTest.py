from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.Metaphone import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class MetaphoneTest(StringEncoderAbstractTest, unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testSetMaxLengthWithTruncation_test3_decomposed(self) -> None:
        pass

    def testSetMaxLengthWithTruncation_test2_decomposed(self) -> None:
        pass

    def testSetMaxLengthWithTruncation_test1_decomposed(self) -> None:
        pass

    def testSetMaxLengthWithTruncation_test0_decomposed(self) -> None:
        pass

    def testExceedLength_test1_decomposed(self) -> None:
        pass

    def testExceedLength_test0_decomposed(self) -> None:
        pass

    def testTCH_test3_decomposed(self) -> None:
        pass

    def testTCH_test2_decomposed(self) -> None:
        pass

    def testTCH_test1_decomposed(self) -> None:
        pass

    def testTCH_test0_decomposed(self) -> None:
        pass

    def testTIOAndTIAToX_test3_decomposed(self) -> None:
        pass

    def testTIOAndTIAToX_test2_decomposed(self) -> None:
        pass

    def testTIOAndTIAToX_test1_decomposed(self) -> None:
        pass

    def testTIOAndTIAToX_test0_decomposed(self) -> None:
        pass

    def testSHAndSIOAndSIAToX_test5_decomposed(self) -> None:
        pass

    def testSHAndSIOAndSIAToX_test4_decomposed(self) -> None:
        pass

    def testSHAndSIOAndSIAToX_test3_decomposed(self) -> None:
        pass

    def testSHAndSIOAndSIAToX_test2_decomposed(self) -> None:
        pass

    def testSHAndSIOAndSIAToX_test1_decomposed(self) -> None:
        pass

    def testSHAndSIOAndSIAToX_test0_decomposed(self) -> None:
        pass

    def testPHTOF_test1_decomposed(self) -> None:
        pass

    def testPHTOF_test0_decomposed(self) -> None:
        pass

    def testDiscardOfSilentGN_test3_decomposed(self) -> None:
        pass

    def testDiscardOfSilentGN_test2_decomposed(self) -> None:
        pass

    def testDiscardOfSilentGN_test1_decomposed(self) -> None:
        pass

    def testDiscardOfSilentGN_test0_decomposed(self) -> None:
        pass

    def testDiscardOfSilentHAfterG_test3_decomposed(self) -> None:
        pass

    def testDiscardOfSilentHAfterG_test2_decomposed(self) -> None:
        pass

    def testDiscardOfSilentHAfterG_test1_decomposed(self) -> None:
        pass

    def testDiscardOfSilentHAfterG_test0_decomposed(self) -> None:
        pass

    def testTranslateToJOfDGEOrDGIOrDGY_test5_decomposed(self) -> None:
        pass

    def testTranslateToJOfDGEOrDGIOrDGY_test4_decomposed(self) -> None:
        pass

    def testTranslateToJOfDGEOrDGIOrDGY_test3_decomposed(self) -> None:
        pass

    def testTranslateToJOfDGEOrDGIOrDGY_test2_decomposed(self) -> None:
        pass

    def testTranslateToJOfDGEOrDGIOrDGY_test1_decomposed(self) -> None:
        pass

    def testTranslateToJOfDGEOrDGIOrDGY_test0_decomposed(self) -> None:
        pass

    def testTranslateOfSCHAndCH_test7_decomposed(self) -> None:
        pass

    def testTranslateOfSCHAndCH_test6_decomposed(self) -> None:
        pass

    def testTranslateOfSCHAndCH_test5_decomposed(self) -> None:
        pass

    def testTranslateOfSCHAndCH_test4_decomposed(self) -> None:
        pass

    def testTranslateOfSCHAndCH_test3_decomposed(self) -> None:
        pass

    def testTranslateOfSCHAndCH_test2_decomposed(self) -> None:
        pass

    def testTranslateOfSCHAndCH_test1_decomposed(self) -> None:
        pass

    def testTranslateOfSCHAndCH_test0_decomposed(self) -> None:
        pass

    def testWordsWithCIA_test1_decomposed(self) -> None:
        pass

    def testWordsWithCIA_test0_decomposed(self) -> None:
        pass

    def testWhy_test1_decomposed(self) -> None:
        pass

    def testWhy_test0_decomposed(self) -> None:
        pass

    def testDiscardOfSCEOrSCIOrSCY_test5_decomposed(self) -> None:
        pass

    def testDiscardOfSCEOrSCIOrSCY_test4_decomposed(self) -> None:
        pass

    def testDiscardOfSCEOrSCIOrSCY_test3_decomposed(self) -> None:
        pass

    def testDiscardOfSCEOrSCIOrSCY_test2_decomposed(self) -> None:
        pass

    def testDiscardOfSCEOrSCIOrSCY_test1_decomposed(self) -> None:
        pass

    def testDiscardOfSCEOrSCIOrSCY_test0_decomposed(self) -> None:
        pass

    def testWordEndingInMB_test5_decomposed(self) -> None:
        pass

    def testWordEndingInMB_test4_decomposed(self) -> None:
        pass

    def testWordEndingInMB_test3_decomposed(self) -> None:
        pass

    def testWordEndingInMB_test2_decomposed(self) -> None:
        pass

    def testWordEndingInMB_test1_decomposed(self) -> None:
        pass

    def testWordEndingInMB_test0_decomposed(self) -> None:
        pass

    def testMetaphone_test21_decomposed(self) -> None:
        pass

    def testMetaphone_test20_decomposed(self) -> None:
        pass

    def testMetaphone_test19_decomposed(self) -> None:
        pass

    def testMetaphone_test18_decomposed(self) -> None:
        pass

    def testMetaphone_test17_decomposed(self) -> None:
        pass

    def testMetaphone_test16_decomposed(self) -> None:
        pass

    def testMetaphone_test15_decomposed(self) -> None:
        pass

    def testMetaphone_test14_decomposed(self) -> None:
        pass

    def testMetaphone_test13_decomposed(self) -> None:
        pass

    def testMetaphone_test12_decomposed(self) -> None:
        pass

    def testMetaphone_test11_decomposed(self) -> None:
        pass

    def testMetaphone_test10_decomposed(self) -> None:
        pass

    def testMetaphone_test9_decomposed(self) -> None:
        pass

    def testMetaphone_test8_decomposed(self) -> None:
        pass

    def testMetaphone_test7_decomposed(self) -> None:
        pass

    def testMetaphone_test6_decomposed(self) -> None:
        pass

    def testMetaphone_test5_decomposed(self) -> None:
        pass

    def testMetaphone_test4_decomposed(self) -> None:
        pass

    def testMetaphone_test3_decomposed(self) -> None:
        pass

    def testMetaphone_test2_decomposed(self) -> None:
        pass

    def testMetaphone_test1_decomposed(self) -> None:
        pass

    def testMetaphone_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualXalan_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualWright_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualSusan_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualRay_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualPeter_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualParis_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualMary_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualKnight_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualJohn_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualGary_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualAlbert_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualWhite_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqualAero_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqual2_test0_decomposed(self) -> None:
        pass

    def testIsMetaphoneEqual1_test0_decomposed(self) -> None:
        pass

    def _createStringEncoder(self) -> Metaphone:
        pass

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:
        pass

    def assertMetaphoneEqual(self, pairs: typing.List[typing.List[str]]) -> None:
        pass

    def assertIsMetaphoneEqual(
        self, source: str, matches: typing.List[typing.List[str]]
    ) -> None:
        pass

    # Class Methods End
