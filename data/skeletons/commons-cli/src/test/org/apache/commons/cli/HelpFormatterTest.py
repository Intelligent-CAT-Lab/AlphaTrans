from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.HelpFormatter import *
import unittest
import os
import io

# Imports End


class HelpFormatterTest(unittest.TestCase):

    # Class Fields Begin
    __EOL: str = None
    # Class Fields End

    # Class Methods Begin
    def testUsageWithLongOptSeparator_test18_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test17_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test16_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test15_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test14_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test13_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test12_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test11_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test10_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test9_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test8_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test7_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test6_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test5_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test4_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test3_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test2_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test1_decomposed(self) -> None:
        pass

    def testUsageWithLongOptSeparator_test0_decomposed(self) -> None:
        pass

    def testRtrim_test1_decomposed(self) -> None:
        pass

    def testRtrim_test0_decomposed(self) -> None:
        pass

    def testRenderWrappedTextWordCut_test1_decomposed(self) -> None:
        pass

    def testRenderWrappedTextWordCut_test0_decomposed(self) -> None:
        pass

    def testRenderWrappedTextSingleLinePadded2_test1_decomposed(self) -> None:
        pass

    def testRenderWrappedTextSingleLinePadded2_test0_decomposed(self) -> None:
        pass

    def testRenderWrappedTextSingleLinePadded_test1_decomposed(self) -> None:
        pass

    def testRenderWrappedTextSingleLinePadded_test0_decomposed(self) -> None:
        pass

    def testRenderWrappedTextSingleLine_test1_decomposed(self) -> None:
        pass

    def testRenderWrappedTextSingleLine_test0_decomposed(self) -> None:
        pass

    def testRenderWrappedTextMultiLinePadded_test1_decomposed(self) -> None:
        pass

    def testRenderWrappedTextMultiLinePadded_test0_decomposed(self) -> None:
        pass

    def testRenderWrappedTextMultiLine_test1_decomposed(self) -> None:
        pass

    def testRenderWrappedTextMultiLine_test0_decomposed(self) -> None:
        pass

    def testPrintUsage_test5_decomposed(self) -> None:
        pass

    def testPrintUsage_test4_decomposed(self) -> None:
        pass

    def testPrintUsage_test3_decomposed(self) -> None:
        pass

    def testPrintUsage_test2_decomposed(self) -> None:
        pass

    def testPrintUsage_test1_decomposed(self) -> None:
        pass

    def testPrintUsage_test0_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test10_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test9_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test8_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test7_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test6_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test5_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test4_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test3_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test2_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test1_decomposed(self) -> None:
        pass

    def testPrintSortedUsageWithNullComparator_test0_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test10_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test9_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test8_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test7_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test6_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test5_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test4_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test3_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test2_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test1_decomposed(self) -> None:
        pass

    def testPrintSortedUsage_test0_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test15_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test14_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test13_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test12_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test11_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test10_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test9_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test8_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test7_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test6_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test5_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test4_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test3_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test2_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test1_decomposed(self) -> None:
        pass

    def testPrintRequiredOptionGroupUsage_test0_decomposed(self) -> None:
        pass

    def testPrintOptionWithEmptyArgNameUsage_test7_decomposed(self) -> None:
        pass

    def testPrintOptionWithEmptyArgNameUsage_test6_decomposed(self) -> None:
        pass

    def testPrintOptionWithEmptyArgNameUsage_test5_decomposed(self) -> None:
        pass

    def testPrintOptionWithEmptyArgNameUsage_test4_decomposed(self) -> None:
        pass

    def testPrintOptionWithEmptyArgNameUsage_test3_decomposed(self) -> None:
        pass

    def testPrintOptionWithEmptyArgNameUsage_test2_decomposed(self) -> None:
        pass

    def testPrintOptionWithEmptyArgNameUsage_test1_decomposed(self) -> None:
        pass

    def testPrintOptionWithEmptyArgNameUsage_test0_decomposed(self) -> None:
        pass

    def testPrintOptions_test19_decomposed(self) -> None:
        pass

    def testPrintOptions_test18_decomposed(self) -> None:
        pass

    def testPrintOptions_test17_decomposed(self) -> None:
        pass

    def testPrintOptions_test16_decomposed(self) -> None:
        pass

    def testPrintOptions_test15_decomposed(self) -> None:
        pass

    def testPrintOptions_test14_decomposed(self) -> None:
        pass

    def testPrintOptions_test13_decomposed(self) -> None:
        pass

    def testPrintOptions_test12_decomposed(self) -> None:
        pass

    def testPrintOptions_test11_decomposed(self) -> None:
        pass

    def testPrintOptions_test10_decomposed(self) -> None:
        pass

    def testPrintOptions_test9_decomposed(self) -> None:
        pass

    def testPrintOptions_test8_decomposed(self) -> None:
        pass

    def testPrintOptions_test7_decomposed(self) -> None:
        pass

    def testPrintOptions_test6_decomposed(self) -> None:
        pass

    def testPrintOptions_test5_decomposed(self) -> None:
        pass

    def testPrintOptions_test4_decomposed(self) -> None:
        pass

    def testPrintOptions_test3_decomposed(self) -> None:
        pass

    def testPrintOptions_test2_decomposed(self) -> None:
        pass

    def testPrintOptions_test1_decomposed(self) -> None:
        pass

    def testPrintOptions_test0_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test14_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test13_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test12_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test11_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test10_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test9_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test8_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test7_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test6_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test5_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test4_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test3_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test2_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test1_decomposed(self) -> None:
        pass

    def testPrintOptionGroupUsage_test0_decomposed(self) -> None:
        pass

    def testPrintHelpWithEmptySyntax_test2_decomposed(self) -> None:
        pass

    def testPrintHelpWithEmptySyntax_test1_decomposed(self) -> None:
        pass

    def testPrintHelpWithEmptySyntax_test0_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineHeader_test4_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineHeader_test3_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineHeader_test2_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineHeader_test1_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineHeader_test0_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineFooter_test4_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineFooter_test3_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineFooter_test2_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineFooter_test1_decomposed(self) -> None:
        pass

    def testPrintHelpNewlineFooter_test0_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test38_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test37_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test36_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test35_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test34_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test33_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test32_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test31_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test30_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test29_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test28_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test27_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test26_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test25_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test24_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test23_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test22_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test21_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test20_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test19_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test18_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test17_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test16_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test15_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test14_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test13_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test12_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test11_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test10_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test9_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test8_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test7_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test6_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test5_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test4_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test3_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test2_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test1_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat2_test0_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat_test6_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat_test5_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat_test4_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat_test3_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat_test2_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat_test1_decomposed(self) -> None:
        pass

    def testOptionWithoutShortFormat_test0_decomposed(self) -> None:
        pass

    def testIndentedHeaderAndFooter_test3_decomposed(self) -> None:
        pass

    def testIndentedHeaderAndFooter_test2_decomposed(self) -> None:
        pass

    def testIndentedHeaderAndFooter_test1_decomposed(self) -> None:
        pass

    def testIndentedHeaderAndFooter_test0_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test20_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test19_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test18_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test17_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test16_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test15_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test14_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test13_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test12_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test11_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test10_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test9_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test8_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test7_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test6_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test5_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test4_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test3_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test2_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test1_decomposed(self) -> None:
        pass

    def testHelpWithLongOptSeparator_test0_decomposed(self) -> None:
        pass

    def testHeaderStartingWithLineSeparator_test3_decomposed(self) -> None:
        pass

    def testHeaderStartingWithLineSeparator_test2_decomposed(self) -> None:
        pass

    def testHeaderStartingWithLineSeparator_test1_decomposed(self) -> None:
        pass

    def testHeaderStartingWithLineSeparator_test0_decomposed(self) -> None:
        pass

    def testFindWrapPos_test7_decomposed(self) -> None:
        pass

    def testFindWrapPos_test6_decomposed(self) -> None:
        pass

    def testFindWrapPos_test5_decomposed(self) -> None:
        pass

    def testFindWrapPos_test4_decomposed(self) -> None:
        pass

    def testFindWrapPos_test3_decomposed(self) -> None:
        pass

    def testFindWrapPos_test2_decomposed(self) -> None:
        pass

    def testFindWrapPos_test1_decomposed(self) -> None:
        pass

    def testFindWrapPos_test0_decomposed(self) -> None:
        pass

    def testDefaultArgName_test9_decomposed(self) -> None:
        pass

    def testDefaultArgName_test8_decomposed(self) -> None:
        pass

    def testDefaultArgName_test7_decomposed(self) -> None:
        pass

    def testDefaultArgName_test6_decomposed(self) -> None:
        pass

    def testDefaultArgName_test5_decomposed(self) -> None:
        pass

    def testDefaultArgName_test4_decomposed(self) -> None:
        pass

    def testDefaultArgName_test3_decomposed(self) -> None:
        pass

    def testDefaultArgName_test2_decomposed(self) -> None:
        pass

    def testDefaultArgName_test1_decomposed(self) -> None:
        pass

    def testDefaultArgName_test0_decomposed(self) -> None:
        pass

    def testAutomaticUsage_test8_decomposed(self) -> None:
        pass

    def testAutomaticUsage_test7_decomposed(self) -> None:
        pass

    def testAutomaticUsage_test6_decomposed(self) -> None:
        pass

    def testAutomaticUsage_test5_decomposed(self) -> None:
        pass

    def testAutomaticUsage_test4_decomposed(self) -> None:
        pass

    def testAutomaticUsage_test3_decomposed(self) -> None:
        pass

    def testAutomaticUsage_test2_decomposed(self) -> None:
        pass

    def testAutomaticUsage_test1_decomposed(self) -> None:
        pass

    def testAutomaticUsage_test0_decomposed(self) -> None:
        pass

    def testAccessors_test16_decomposed(self) -> None:
        pass

    def testAccessors_test15_decomposed(self) -> None:
        pass

    def testAccessors_test14_decomposed(self) -> None:
        pass

    def testAccessors_test13_decomposed(self) -> None:
        pass

    def testAccessors_test12_decomposed(self) -> None:
        pass

    def testAccessors_test11_decomposed(self) -> None:
        pass

    def testAccessors_test10_decomposed(self) -> None:
        pass

    def testAccessors_test9_decomposed(self) -> None:
        pass

    def testAccessors_test8_decomposed(self) -> None:
        pass

    def testAccessors_test7_decomposed(self) -> None:
        pass

    def testAccessors_test6_decomposed(self) -> None:
        pass

    def testAccessors_test5_decomposed(self) -> None:
        pass

    def testAccessors_test4_decomposed(self) -> None:
        pass

    def testAccessors_test3_decomposed(self) -> None:
        pass

    def testAccessors_test2_decomposed(self) -> None:
        pass

    def testAccessors_test1_decomposed(self) -> None:
        pass

    def testAccessors_test0_decomposed(self) -> None:
        pass

    # Class Methods End
