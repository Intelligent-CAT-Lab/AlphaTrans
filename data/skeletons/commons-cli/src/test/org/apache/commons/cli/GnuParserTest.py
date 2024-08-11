from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.cli.ParserTestCase import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
import unittest
import os
import io

# Imports End


class GnuParserTest(ParserTestCase, unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testUnrecognizedOptionWithBursting_test0_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test10_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test9_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test8_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test7_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test6_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test5_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test4_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test3_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test2_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test1_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption4_test0_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test10_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test9_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test8_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test7_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test6_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test5_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test4_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test3_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test2_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test1_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption3_test0_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption2_test8_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption2_test7_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption2_test6_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption2_test5_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption2_test4_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption2_test3_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption2_test2_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption2_test1_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption2_test0_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption1_test8_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption1_test7_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption1_test6_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption1_test5_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption1_test4_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption1_test3_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption1_test2_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption1_test1_decomposed(self) -> None:
        pass

    def testUnambiguousPartialLongOption1_test0_decomposed(self) -> None:
        pass

    def testStopBursting2_test7_decomposed(self) -> None:
        pass

    def testStopBursting2_test6_decomposed(self) -> None:
        pass

    def testStopBursting2_test5_decomposed(self) -> None:
        pass

    def testStopBursting2_test4_decomposed(self) -> None:
        pass

    def testStopBursting2_test3_decomposed(self) -> None:
        pass

    def testStopBursting2_test2_decomposed(self) -> None:
        pass

    def testStopBursting2_test1_decomposed(self) -> None:
        pass

    def testStopBursting2_test0_decomposed(self) -> None:
        pass

    def testStopBursting_test2_decomposed(self) -> None:
        pass

    def testStopBursting_test1_decomposed(self) -> None:
        pass

    def testStopBursting_test0_decomposed(self) -> None:
        pass

    def testShortWithUnexpectedArgument_test5_decomposed(self) -> None:
        pass

    def testShortWithUnexpectedArgument_test4_decomposed(self) -> None:
        pass

    def testShortWithUnexpectedArgument_test3_decomposed(self) -> None:
        pass

    def testShortWithUnexpectedArgument_test2_decomposed(self) -> None:
        pass

    def testShortWithUnexpectedArgument_test1_decomposed(self) -> None:
        pass

    def testShortWithUnexpectedArgument_test0_decomposed(self) -> None:
        pass

    def testPartialLongOptionSingleDash_test8_decomposed(self) -> None:
        pass

    def testPartialLongOptionSingleDash_test7_decomposed(self) -> None:
        pass

    def testPartialLongOptionSingleDash_test6_decomposed(self) -> None:
        pass

    def testPartialLongOptionSingleDash_test5_decomposed(self) -> None:
        pass

    def testPartialLongOptionSingleDash_test4_decomposed(self) -> None:
        pass

    def testPartialLongOptionSingleDash_test3_decomposed(self) -> None:
        pass

    def testPartialLongOptionSingleDash_test2_decomposed(self) -> None:
        pass

    def testPartialLongOptionSingleDash_test1_decomposed(self) -> None:
        pass

    def testPartialLongOptionSingleDash_test0_decomposed(self) -> None:
        pass

    def testNegativeOption_test2_decomposed(self) -> None:
        pass

    def testNegativeOption_test1_decomposed(self) -> None:
        pass

    def testNegativeOption_test0_decomposed(self) -> None:
        pass

    def testMissingArgWithBursting_test1_decomposed(self) -> None:
        pass

    def testMissingArgWithBursting_test0_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument2_test5_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument2_test4_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument2_test3_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument2_test2_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument2_test1_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument2_test0_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument1_test5_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument1_test4_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument1_test3_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument1_test2_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument1_test1_decomposed(self) -> None:
        pass

    def testLongWithUnexpectedArgument1_test0_decomposed(self) -> None:
        pass

    def testLongWithoutEqualSingleDash_test6_decomposed(self) -> None:
        pass

    def testLongWithoutEqualSingleDash_test5_decomposed(self) -> None:
        pass

    def testLongWithoutEqualSingleDash_test4_decomposed(self) -> None:
        pass

    def testLongWithoutEqualSingleDash_test3_decomposed(self) -> None:
        pass

    def testLongWithoutEqualSingleDash_test2_decomposed(self) -> None:
        pass

    def testLongWithoutEqualSingleDash_test1_decomposed(self) -> None:
        pass

    def testLongWithoutEqualSingleDash_test0_decomposed(self) -> None:
        pass

    def testDoubleDash2_test6_decomposed(self) -> None:
        pass

    def testDoubleDash2_test5_decomposed(self) -> None:
        pass

    def testDoubleDash2_test4_decomposed(self) -> None:
        pass

    def testDoubleDash2_test3_decomposed(self) -> None:
        pass

    def testDoubleDash2_test2_decomposed(self) -> None:
        pass

    def testDoubleDash2_test1_decomposed(self) -> None:
        pass

    def testDoubleDash2_test0_decomposed(self) -> None:
        pass

    def testBursting_test3_decomposed(self) -> None:
        pass

    def testBursting_test2_decomposed(self) -> None:
        pass

    def testBursting_test1_decomposed(self) -> None:
        pass

    def testBursting_test0_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test9_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test8_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test7_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test6_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test5_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test4_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test3_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test2_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test1_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption4_test0_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test9_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test8_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test7_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test6_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test5_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test4_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test3_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test2_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test1_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption3_test0_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption2_test8_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption2_test7_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption2_test6_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption2_test5_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption2_test4_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption2_test3_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption2_test2_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption2_test1_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption2_test0_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption1_test8_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption1_test7_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption1_test6_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption1_test5_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption1_test4_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption1_test3_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption1_test2_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption1_test1_decomposed(self) -> None:
        pass

    def testAmbiguousPartialLongOption1_test0_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test11_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test10_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test9_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test8_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test7_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test6_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test5_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test4_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test3_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test2_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test1_decomposed(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash_test0_decomposed(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    # Class Methods End
