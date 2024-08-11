from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.DaitchMokotoffSoundex import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import unittest
import os
import io

# Imports End


class DaitchMokotoffSoundexTest(StringEncoderAbstractTest, unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testSpecialRomanianCharacters_test0_decomposed(self) -> None:
        pass

    def testSoundexBasic3_test0_decomposed(self) -> None:
        pass

    def testSoundexBasic2_test0_decomposed(self) -> None:
        pass

    def testSoundexBasic_test0_decomposed(self) -> None:
        pass

    def testEncodeIgnoreTrimmable_test0_decomposed(self) -> None:
        pass

    def testEncodeIgnoreHyphens_test0_decomposed(self) -> None:
        pass

    def testEncodeIgnoreApostrophes_test0_decomposed(self) -> None:
        pass

    def testAdjacentCodes_test0_decomposed(self) -> None:
        pass

    def testAccentedCharacterFolding_test0_decomposed(self) -> None:
        pass

    def _createStringEncoder(self) -> DaitchMokotoffSoundex:
        pass

    def testEncodeBasic(self) -> None:
        pass

    def __encode(self, source: str) -> str:
        pass

    def __soundex(self, source: str) -> str:
        pass

    # Class Methods End
