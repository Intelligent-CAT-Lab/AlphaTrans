from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.language.bm.Rule import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.Lang import *
from src.main.org.apache.commons.codec.language.bm.BeiderMorseEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class BeiderMorseEncoderTest(StringEncoderAbstractTest, unittest.TestCase):

    # Class Fields Begin
    __TEST_CHARS: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def testSpeedCheck3_test1_decomposed(self) -> None:
        pass

    def testSpeedCheck3_test0_decomposed(self) -> None:
        pass

    def testSpeedCheck2_test1_decomposed(self) -> None:
        pass

    def testSpeedCheck2_test0_decomposed(self) -> None:
        pass

    def testSpeedCheck_test2_decomposed(self) -> None:
        pass

    def testSpeedCheck_test1_decomposed(self) -> None:
        pass

    def testSpeedCheck_test0_decomposed(self) -> None:
        pass

    def testSetRuleTypeToRulesIllegalArgumentException_test1_decomposed(self) -> None:
        pass

    def testSetRuleTypeToRulesIllegalArgumentException_test0_decomposed(self) -> None:
        pass

    def testSetRuleTypeExact_test2_decomposed(self) -> None:
        pass

    def testSetRuleTypeExact_test1_decomposed(self) -> None:
        pass

    def testSetRuleTypeExact_test0_decomposed(self) -> None:
        pass

    def testSetNameTypeAsh_test2_decomposed(self) -> None:
        pass

    def testSetNameTypeAsh_test1_decomposed(self) -> None:
        pass

    def testSetNameTypeAsh_test0_decomposed(self) -> None:
        pass

    def testSetConcat_test2_decomposed(self) -> None:
        pass

    def testSetConcat_test1_decomposed(self) -> None:
        pass

    def testSetConcat_test0_decomposed(self) -> None:
        pass

    def testOOM_test6_decomposed(self) -> None:
        pass

    def testOOM_test5_decomposed(self) -> None:
        pass

    def testOOM_test4_decomposed(self) -> None:
        pass

    def testOOM_test3_decomposed(self) -> None:
        pass

    def testOOM_test2_decomposed(self) -> None:
        pass

    def testOOM_test1_decomposed(self) -> None:
        pass

    def testOOM_test0_decomposed(self) -> None:
        pass

    def testNegativeIndexForRuleMatchIndexOutOfBoundsException_test1_decomposed(
        self,
    ) -> None:
        pass

    def testNegativeIndexForRuleMatchIndexOutOfBoundsException_test0_decomposed(
        self,
    ) -> None:
        pass

    def testLongestEnglishSurname_test1_decomposed(self) -> None:
        pass

    def testLongestEnglishSurname_test0_decomposed(self) -> None:
        pass

    def testInvalidLanguageIllegalArgumentException_test0_decomposed(self) -> None:
        pass

    def testInvalidLangIllegalStateException_test1_decomposed(self) -> None:
        pass

    def testInvalidLangIllegalStateException_test0_decomposed(self) -> None:
        pass

    def testInvalidLangIllegalArgumentException_test0_decomposed(self) -> None:
        pass

    def testEncodeGna_test1_decomposed(self) -> None:
        pass

    def testEncodeGna_test0_decomposed(self) -> None:
        pass

    def testEncodeAtzNotEmpty_test1_decomposed(self) -> None:
        pass

    def testEncodeAtzNotEmpty_test0_decomposed(self) -> None:
        pass

    def testAsciiEncodeNotEmpty2Letters_test1_decomposed(self) -> None:
        pass

    def testAsciiEncodeNotEmpty2Letters_test0_decomposed(self) -> None:
        pass

    def testAsciiEncodeNotEmpty1Letter_test1_decomposed(self) -> None:
        pass

    def testAsciiEncodeNotEmpty1Letter_test0_decomposed(self) -> None:
        pass

    def testAllChars_test1_decomposed(self) -> None:
        pass

    def testAllChars_test0_decomposed(self) -> None:
        pass

    def _createStringEncoder(self) -> StringEncoder:
        pass

    def __createGenericApproxEncoder(self) -> BeiderMorseEncoder:
        pass

    def __assertNotEmpty(self, bmpm: BeiderMorseEncoder, value: str) -> None:
        pass

    # Class Methods End
