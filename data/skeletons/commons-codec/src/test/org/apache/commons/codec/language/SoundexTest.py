from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.SoundexUtils import *
from src.main.org.apache.commons.codec.language.Soundex import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import unittest
import os
import io

# Imports End


class SoundexTest(StringEncoderAbstractTest, unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testSimplifiedSoundex_test1_decomposed(self) -> None:
        pass

    def testSimplifiedSoundex_test0_decomposed(self) -> None:
        pass

    def testGenealogy_test1_decomposed(self) -> None:
        pass

    def testGenealogy_test0_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test11_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test10_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test9_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test8_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test7_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test6_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test5_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test4_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test3_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test2_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test1_decomposed(self) -> None:
        pass

    def testWikipediaAmericanSoundex_test0_decomposed(self) -> None:
        pass

    def testUsMappingOWithDiaeresis_test1_decomposed(self) -> None:
        pass

    def testUsMappingOWithDiaeresis_test0_decomposed(self) -> None:
        pass

    def testUsMappingEWithAcute_test1_decomposed(self) -> None:
        pass

    def testUsMappingEWithAcute_test0_decomposed(self) -> None:
        pass

    def testUsEnglishStatic_test0_decomposed(self) -> None:
        pass

    def testSoundexUtilsNullBehaviour_test1_decomposed(self) -> None:
        pass

    def testSoundexUtilsNullBehaviour_test0_decomposed(self) -> None:
        pass

    def testSoundexUtilsConstructable_test0_decomposed(self) -> None:
        pass

    def testNewInstance3_test0_decomposed(self) -> None:
        pass

    def testNewInstance2_test0_decomposed(self) -> None:
        pass

    def testNewInstance_test0_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test17_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test16_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test15_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test14_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test13_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test12_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test11_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test10_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test9_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test8_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test7_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test6_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test5_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test4_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test3_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test2_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test1_decomposed(self) -> None:
        pass

    def testMsSqlServer3_test0_decomposed(self) -> None:
        pass

    def testMsSqlServer2_test0_decomposed(self) -> None:
        pass

    def testMsSqlServer1_test3_decomposed(self) -> None:
        pass

    def testMsSqlServer1_test2_decomposed(self) -> None:
        pass

    def testMsSqlServer1_test1_decomposed(self) -> None:
        pass

    def testMsSqlServer1_test0_decomposed(self) -> None:
        pass

    def testHWRuleEx3_test4_decomposed(self) -> None:
        pass

    def testHWRuleEx3_test3_decomposed(self) -> None:
        pass

    def testHWRuleEx3_test2_decomposed(self) -> None:
        pass

    def testHWRuleEx3_test1_decomposed(self) -> None:
        pass

    def testHWRuleEx3_test0_decomposed(self) -> None:
        pass

    def testHWRuleEx2_test3_decomposed(self) -> None:
        pass

    def testHWRuleEx2_test2_decomposed(self) -> None:
        pass

    def testHWRuleEx2_test1_decomposed(self) -> None:
        pass

    def testHWRuleEx2_test0_decomposed(self) -> None:
        pass

    def testHWRuleEx1_test7_decomposed(self) -> None:
        pass

    def testHWRuleEx1_test6_decomposed(self) -> None:
        pass

    def testHWRuleEx1_test5_decomposed(self) -> None:
        pass

    def testHWRuleEx1_test4_decomposed(self) -> None:
        pass

    def testHWRuleEx1_test3_decomposed(self) -> None:
        pass

    def testHWRuleEx1_test2_decomposed(self) -> None:
        pass

    def testHWRuleEx1_test1_decomposed(self) -> None:
        pass

    def testHWRuleEx1_test0_decomposed(self) -> None:
        pass

    def testEncodeIgnoreTrimmable_test1_decomposed(self) -> None:
        pass

    def testEncodeIgnoreTrimmable_test0_decomposed(self) -> None:
        pass

    def testEncodeIgnoreHyphens_test0_decomposed(self) -> None:
        pass

    def testEncodeIgnoreApostrophes_test0_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test15_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test14_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test13_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test12_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test11_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test10_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test9_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test8_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test7_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test6_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test5_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test4_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test3_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test2_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test1_decomposed(self) -> None:
        pass

    def testEncodeBatch4_test0_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test13_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test12_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test11_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test10_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test9_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test8_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test7_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test6_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test5_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test4_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test3_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test2_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test1_decomposed(self) -> None:
        pass

    def testEncodeBatch3_test0_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test31_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test30_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test29_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test28_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test27_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test26_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test25_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test24_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test23_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test22_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test21_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test20_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test19_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test18_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test17_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test16_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test15_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test14_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test13_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test12_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test11_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test10_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test9_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test8_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test7_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test6_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test5_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test4_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test3_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test2_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test1_decomposed(self) -> None:
        pass

    def testEncodeBatch2_test0_decomposed(self) -> None:
        pass

    def testEncodeBasic_test19_decomposed(self) -> None:
        pass

    def testEncodeBasic_test18_decomposed(self) -> None:
        pass

    def testEncodeBasic_test17_decomposed(self) -> None:
        pass

    def testEncodeBasic_test16_decomposed(self) -> None:
        pass

    def testEncodeBasic_test15_decomposed(self) -> None:
        pass

    def testEncodeBasic_test14_decomposed(self) -> None:
        pass

    def testEncodeBasic_test13_decomposed(self) -> None:
        pass

    def testEncodeBasic_test12_decomposed(self) -> None:
        pass

    def testEncodeBasic_test11_decomposed(self) -> None:
        pass

    def testEncodeBasic_test10_decomposed(self) -> None:
        pass

    def testEncodeBasic_test9_decomposed(self) -> None:
        pass

    def testEncodeBasic_test8_decomposed(self) -> None:
        pass

    def testEncodeBasic_test7_decomposed(self) -> None:
        pass

    def testEncodeBasic_test6_decomposed(self) -> None:
        pass

    def testEncodeBasic_test5_decomposed(self) -> None:
        pass

    def testEncodeBasic_test4_decomposed(self) -> None:
        pass

    def testEncodeBasic_test3_decomposed(self) -> None:
        pass

    def testEncodeBasic_test2_decomposed(self) -> None:
        pass

    def testEncodeBasic_test1_decomposed(self) -> None:
        pass

    def testEncodeBasic_test0_decomposed(self) -> None:
        pass

    def testDifference_test23_decomposed(self) -> None:
        pass

    def testDifference_test22_decomposed(self) -> None:
        pass

    def testDifference_test21_decomposed(self) -> None:
        pass

    def testDifference_test20_decomposed(self) -> None:
        pass

    def testDifference_test19_decomposed(self) -> None:
        pass

    def testDifference_test18_decomposed(self) -> None:
        pass

    def testDifference_test17_decomposed(self) -> None:
        pass

    def testDifference_test16_decomposed(self) -> None:
        pass

    def testDifference_test15_decomposed(self) -> None:
        pass

    def testDifference_test14_decomposed(self) -> None:
        pass

    def testDifference_test13_decomposed(self) -> None:
        pass

    def testDifference_test12_decomposed(self) -> None:
        pass

    def testDifference_test11_decomposed(self) -> None:
        pass

    def testDifference_test10_decomposed(self) -> None:
        pass

    def testDifference_test9_decomposed(self) -> None:
        pass

    def testDifference_test8_decomposed(self) -> None:
        pass

    def testDifference_test7_decomposed(self) -> None:
        pass

    def testDifference_test6_decomposed(self) -> None:
        pass

    def testDifference_test5_decomposed(self) -> None:
        pass

    def testDifference_test4_decomposed(self) -> None:
        pass

    def testDifference_test3_decomposed(self) -> None:
        pass

    def testDifference_test2_decomposed(self) -> None:
        pass

    def testDifference_test1_decomposed(self) -> None:
        pass

    def testDifference_test0_decomposed(self) -> None:
        pass

    def testBadCharacters_test1_decomposed(self) -> None:
        pass

    def testBadCharacters_test0_decomposed(self) -> None:
        pass

    def testB650_test0_decomposed(self) -> None:
        pass

    def _createStringEncoder(self) -> Soundex:
        pass

    # Class Methods End
