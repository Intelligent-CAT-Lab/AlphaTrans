from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.AmbiguousOptionException import *
import configparser
import unittest
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ParserTestCase(ABC, unittest.TestCase):

    # Class Fields Begin
    _parser: CommandLineParser = None
    _options: Options = None
    # Class Fields End

    # Class Methods Begin
    def testWithRequiredOption_test10_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test9_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test8_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test7_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test6_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test5_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test4_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test3_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test2_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test1_decomposed(self) -> None:
        pass

    def testWithRequiredOption_test0_decomposed(self) -> None:
        pass

    def testUnrecognizedOptionWithBursting_test0_decomposed(self) -> None:
        pass

    def testUnrecognizedOption_test0_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test11_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test10_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test9_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test8_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test7_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test6_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test5_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test4_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test3_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test2_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test1_decomposed(self) -> None:
        pass

    def testUnlimitedArgs_test0_decomposed(self) -> None:
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

    def testStopAtUnexpectedArg_test2_decomposed(self) -> None:
        pass

    def testStopAtUnexpectedArg_test1_decomposed(self) -> None:
        pass

    def testStopAtUnexpectedArg_test0_decomposed(self) -> None:
        pass

    def testStopAtNonOptionShort_test2_decomposed(self) -> None:
        pass

    def testStopAtNonOptionShort_test1_decomposed(self) -> None:
        pass

    def testStopAtNonOptionShort_test0_decomposed(self) -> None:
        pass

    def testStopAtNonOptionLong_test2_decomposed(self) -> None:
        pass

    def testStopAtNonOptionLong_test1_decomposed(self) -> None:
        pass

    def testStopAtNonOptionLong_test0_decomposed(self) -> None:
        pass

    def testStopAtExpectedArg_test3_decomposed(self) -> None:
        pass

    def testStopAtExpectedArg_test2_decomposed(self) -> None:
        pass

    def testStopAtExpectedArg_test1_decomposed(self) -> None:
        pass

    def testStopAtExpectedArg_test0_decomposed(self) -> None:
        pass

    def testSingleDash_test3_decomposed(self) -> None:
        pass

    def testSingleDash_test2_decomposed(self) -> None:
        pass

    def testSingleDash_test1_decomposed(self) -> None:
        pass

    def testSingleDash_test0_decomposed(self) -> None:
        pass

    def testSimpleShort_test3_decomposed(self) -> None:
        pass

    def testSimpleShort_test2_decomposed(self) -> None:
        pass

    def testSimpleShort_test1_decomposed(self) -> None:
        pass

    def testSimpleShort_test0_decomposed(self) -> None:
        pass

    def testSimpleLong_test3_decomposed(self) -> None:
        pass

    def testSimpleLong_test2_decomposed(self) -> None:
        pass

    def testSimpleLong_test1_decomposed(self) -> None:
        pass

    def testSimpleLong_test0_decomposed(self) -> None:
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

    def testShortWithoutEqual_test6_decomposed(self) -> None:
        pass

    def testShortWithoutEqual_test5_decomposed(self) -> None:
        pass

    def testShortWithoutEqual_test4_decomposed(self) -> None:
        pass

    def testShortWithoutEqual_test3_decomposed(self) -> None:
        pass

    def testShortWithoutEqual_test2_decomposed(self) -> None:
        pass

    def testShortWithoutEqual_test1_decomposed(self) -> None:
        pass

    def testShortWithoutEqual_test0_decomposed(self) -> None:
        pass

    def testShortWithEqual_test6_decomposed(self) -> None:
        pass

    def testShortWithEqual_test5_decomposed(self) -> None:
        pass

    def testShortWithEqual_test4_decomposed(self) -> None:
        pass

    def testShortWithEqual_test3_decomposed(self) -> None:
        pass

    def testShortWithEqual_test2_decomposed(self) -> None:
        pass

    def testShortWithEqual_test1_decomposed(self) -> None:
        pass

    def testShortWithEqual_test0_decomposed(self) -> None:
        pass

    def testShortOptionQuoteHandling_test1_decomposed(self) -> None:
        pass

    def testShortOptionQuoteHandling_test0_decomposed(self) -> None:
        pass

    def testShortOptionConcatenatedQuoteHandling_test1_decomposed(self) -> None:
        pass

    def testShortOptionConcatenatedQuoteHandling_test0_decomposed(self) -> None:
        pass

    def testReuseOptionsTwice_test4_decomposed(self) -> None:
        pass

    def testReuseOptionsTwice_test3_decomposed(self) -> None:
        pass

    def testReuseOptionsTwice_test2_decomposed(self) -> None:
        pass

    def testReuseOptionsTwice_test1_decomposed(self) -> None:
        pass

    def testReuseOptionsTwice_test0_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test12_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test11_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test10_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test9_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test8_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test7_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test6_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test5_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test4_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test3_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test2_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test1_decomposed(self) -> None:
        pass

    def testPropertyOverrideValues_test0_decomposed(self) -> None:
        pass

    def testPropertyOptionUnexpected_test1_decomposed(self) -> None:
        pass

    def testPropertyOptionUnexpected_test0_decomposed(self) -> None:
        pass

    def testPropertyOptionSingularValue_test8_decomposed(self) -> None:
        pass

    def testPropertyOptionSingularValue_test7_decomposed(self) -> None:
        pass

    def testPropertyOptionSingularValue_test6_decomposed(self) -> None:
        pass

    def testPropertyOptionSingularValue_test5_decomposed(self) -> None:
        pass

    def testPropertyOptionSingularValue_test4_decomposed(self) -> None:
        pass

    def testPropertyOptionSingularValue_test3_decomposed(self) -> None:
        pass

    def testPropertyOptionSingularValue_test2_decomposed(self) -> None:
        pass

    def testPropertyOptionSingularValue_test1_decomposed(self) -> None:
        pass

    def testPropertyOptionSingularValue_test0_decomposed(self) -> None:
        pass

    def testPropertyOptionRequired_test5_decomposed(self) -> None:
        pass

    def testPropertyOptionRequired_test4_decomposed(self) -> None:
        pass

    def testPropertyOptionRequired_test3_decomposed(self) -> None:
        pass

    def testPropertyOptionRequired_test2_decomposed(self) -> None:
        pass

    def testPropertyOptionRequired_test1_decomposed(self) -> None:
        pass

    def testPropertyOptionRequired_test0_decomposed(self) -> None:
        pass

    def testPropertyOptionMultipleValues_test7_decomposed(self) -> None:
        pass

    def testPropertyOptionMultipleValues_test6_decomposed(self) -> None:
        pass

    def testPropertyOptionMultipleValues_test5_decomposed(self) -> None:
        pass

    def testPropertyOptionMultipleValues_test4_decomposed(self) -> None:
        pass

    def testPropertyOptionMultipleValues_test3_decomposed(self) -> None:
        pass

    def testPropertyOptionMultipleValues_test2_decomposed(self) -> None:
        pass

    def testPropertyOptionMultipleValues_test1_decomposed(self) -> None:
        pass

    def testPropertyOptionMultipleValues_test0_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test14_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test13_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test12_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test11_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test10_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test9_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test8_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test7_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test6_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test5_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test4_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test3_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test2_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test1_decomposed(self) -> None:
        pass

    def testPropertyOptionGroup_test0_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test15_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test14_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test13_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test12_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test11_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test10_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test9_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test8_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test7_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test6_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test5_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test4_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test3_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test2_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test1_decomposed(self) -> None:
        pass

    def testPropertyOptionFlags_test0_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test10_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test9_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test8_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test7_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test6_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test5_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test4_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test3_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test2_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test1_decomposed(self) -> None:
        pass

    def testPropertiesOption2_test0_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test11_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test10_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test9_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test8_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test7_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test6_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test5_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test4_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test3_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test2_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test1_decomposed(self) -> None:
        pass

    def testPropertiesOption1_test0_decomposed(self) -> None:
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

    def testOptionGroupLong_test11_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test10_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test9_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test8_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test7_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test6_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test5_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test4_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test3_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test2_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test1_decomposed(self) -> None:
        pass

    def testOptionGroupLong_test0_decomposed(self) -> None:
        pass

    def testOptionGroup_test8_decomposed(self) -> None:
        pass

    def testOptionGroup_test7_decomposed(self) -> None:
        pass

    def testOptionGroup_test6_decomposed(self) -> None:
        pass

    def testOptionGroup_test5_decomposed(self) -> None:
        pass

    def testOptionGroup_test4_decomposed(self) -> None:
        pass

    def testOptionGroup_test3_decomposed(self) -> None:
        pass

    def testOptionGroup_test2_decomposed(self) -> None:
        pass

    def testOptionGroup_test1_decomposed(self) -> None:
        pass

    def testOptionGroup_test0_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test10_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test9_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test8_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test7_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test6_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test5_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test4_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test3_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test2_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test1_decomposed(self) -> None:
        pass

    def testOptionAndRequiredOption_test0_decomposed(self) -> None:
        pass

    def testNegativeOption_test2_decomposed(self) -> None:
        pass

    def testNegativeOption_test1_decomposed(self) -> None:
        pass

    def testNegativeOption_test0_decomposed(self) -> None:
        pass

    def testNegativeArgument_test1_decomposed(self) -> None:
        pass

    def testNegativeArgument_test0_decomposed(self) -> None:
        pass

    def testMultipleWithLong_test7_decomposed(self) -> None:
        pass

    def testMultipleWithLong_test6_decomposed(self) -> None:
        pass

    def testMultipleWithLong_test5_decomposed(self) -> None:
        pass

    def testMultipleWithLong_test4_decomposed(self) -> None:
        pass

    def testMultipleWithLong_test3_decomposed(self) -> None:
        pass

    def testMultipleWithLong_test2_decomposed(self) -> None:
        pass

    def testMultipleWithLong_test1_decomposed(self) -> None:
        pass

    def testMultipleWithLong_test0_decomposed(self) -> None:
        pass

    def testMultiple_test7_decomposed(self) -> None:
        pass

    def testMultiple_test6_decomposed(self) -> None:
        pass

    def testMultiple_test5_decomposed(self) -> None:
        pass

    def testMultiple_test4_decomposed(self) -> None:
        pass

    def testMultiple_test3_decomposed(self) -> None:
        pass

    def testMultiple_test2_decomposed(self) -> None:
        pass

    def testMultiple_test1_decomposed(self) -> None:
        pass

    def testMultiple_test0_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test12_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test11_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test10_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test9_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test8_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test7_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test6_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test5_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test4_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test3_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test2_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test1_decomposed(self) -> None:
        pass

    def testMissingRequiredOptions_test0_decomposed(self) -> None:
        pass

    def testMissingRequiredOption_test7_decomposed(self) -> None:
        pass

    def testMissingRequiredOption_test6_decomposed(self) -> None:
        pass

    def testMissingRequiredOption_test5_decomposed(self) -> None:
        pass

    def testMissingRequiredOption_test4_decomposed(self) -> None:
        pass

    def testMissingRequiredOption_test3_decomposed(self) -> None:
        pass

    def testMissingRequiredOption_test2_decomposed(self) -> None:
        pass

    def testMissingRequiredOption_test1_decomposed(self) -> None:
        pass

    def testMissingRequiredOption_test0_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test11_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test10_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test9_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test8_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test7_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test6_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test5_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test4_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test3_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test2_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test1_decomposed(self) -> None:
        pass

    def testMissingRequiredGroup_test0_decomposed(self) -> None:
        pass

    def testMissingArgWithBursting_test1_decomposed(self) -> None:
        pass

    def testMissingArgWithBursting_test0_decomposed(self) -> None:
        pass

    def testMissingArg_test1_decomposed(self) -> None:
        pass

    def testMissingArg_test0_decomposed(self) -> None:
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

    def testLongWithoutEqualDoubleDash_test6_decomposed(self) -> None:
        pass

    def testLongWithoutEqualDoubleDash_test5_decomposed(self) -> None:
        pass

    def testLongWithoutEqualDoubleDash_test4_decomposed(self) -> None:
        pass

    def testLongWithoutEqualDoubleDash_test3_decomposed(self) -> None:
        pass

    def testLongWithoutEqualDoubleDash_test2_decomposed(self) -> None:
        pass

    def testLongWithoutEqualDoubleDash_test1_decomposed(self) -> None:
        pass

    def testLongWithoutEqualDoubleDash_test0_decomposed(self) -> None:
        pass

    def testLongWithEqualSingleDash_test6_decomposed(self) -> None:
        pass

    def testLongWithEqualSingleDash_test5_decomposed(self) -> None:
        pass

    def testLongWithEqualSingleDash_test4_decomposed(self) -> None:
        pass

    def testLongWithEqualSingleDash_test3_decomposed(self) -> None:
        pass

    def testLongWithEqualSingleDash_test2_decomposed(self) -> None:
        pass

    def testLongWithEqualSingleDash_test1_decomposed(self) -> None:
        pass

    def testLongWithEqualSingleDash_test0_decomposed(self) -> None:
        pass

    def testLongWithEqualDoubleDash_test6_decomposed(self) -> None:
        pass

    def testLongWithEqualDoubleDash_test5_decomposed(self) -> None:
        pass

    def testLongWithEqualDoubleDash_test4_decomposed(self) -> None:
        pass

    def testLongWithEqualDoubleDash_test3_decomposed(self) -> None:
        pass

    def testLongWithEqualDoubleDash_test2_decomposed(self) -> None:
        pass

    def testLongWithEqualDoubleDash_test1_decomposed(self) -> None:
        pass

    def testLongWithEqualDoubleDash_test0_decomposed(self) -> None:
        pass

    def testLongOptionWithEqualsQuoteHandling_test1_decomposed(self) -> None:
        pass

    def testLongOptionWithEqualsQuoteHandling_test0_decomposed(self) -> None:
        pass

    def testLongOptionQuoteHandling_test1_decomposed(self) -> None:
        pass

    def testLongOptionQuoteHandling_test0_decomposed(self) -> None:
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

    def testDoubleDash1_test2_decomposed(self) -> None:
        pass

    def testDoubleDash1_test1_decomposed(self) -> None:
        pass

    def testDoubleDash1_test0_decomposed(self) -> None:
        pass

    def testBursting_test3_decomposed(self) -> None:
        pass

    def testBursting_test2_decomposed(self) -> None:
        pass

    def testBursting_test1_decomposed(self) -> None:
        pass

    def testBursting_test0_decomposed(self) -> None:
        pass

    def testArgumentStartingWithHyphen_test1_decomposed(self) -> None:
        pass

    def testArgumentStartingWithHyphen_test0_decomposed(self) -> None:
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

    def __parse(
        self,
        parser: CommandLineParser,
        opts: Options,
        args: typing.List[typing.List[str]],
        properties: typing.Union[configparser.ConfigParser, typing.Dict],
    ) -> CommandLine:
        pass

    # Class Methods End
