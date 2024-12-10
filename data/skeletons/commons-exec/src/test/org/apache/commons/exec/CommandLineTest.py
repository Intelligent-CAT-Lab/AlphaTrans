from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.util.StringUtils import *
from src.main.org.apache.commons.exec.CommandLine import *
import unittest
import os
import io

# Imports End


class CommandLineTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testToStringTroubleshooting_test3_decomposed(self) -> None:
        pass

    def testToStringTroubleshooting_test2_decomposed(self) -> None:
        pass

    def testToStringTroubleshooting_test1_decomposed(self) -> None:
        pass

    def testToStringTroubleshooting_test0_decomposed(self) -> None:
        pass

    def testToString_test5_decomposed(self) -> None:
        pass

    def testToString_test4_decomposed(self) -> None:
        pass

    def testToString_test3_decomposed(self) -> None:
        pass

    def testToString_test2_decomposed(self) -> None:
        pass

    def testToString_test1_decomposed(self) -> None:
        pass

    def testToString_test0_decomposed(self) -> None:
        pass

    def testParseRealLifeCommandLine_1_test2_decomposed(self) -> None:
        pass

    def testParseRealLifeCommandLine_1_test1_decomposed(self) -> None:
        pass

    def testParseRealLifeCommandLine_1_test0_decomposed(self) -> None:
        pass

    def testParseComplexCommandLine2_test3_decomposed(self) -> None:
        pass

    def testParseComplexCommandLine2_test2_decomposed(self) -> None:
        pass

    def testParseComplexCommandLine2_test1_decomposed(self) -> None:
        pass

    def testParseComplexCommandLine2_test0_decomposed(self) -> None:
        pass

    def testParseComplexCommandLine1_test1_decomposed(self) -> None:
        pass

    def testParseComplexCommandLine1_test0_decomposed(self) -> None:
        pass

    def testParseCommandLineWithUnevenQuotes_test0_decomposed(self) -> None:
        pass

    def testParseCommandLineWithQuotes_test2_decomposed(self) -> None:
        pass

    def testParseCommandLineWithQuotes_test1_decomposed(self) -> None:
        pass

    def testParseCommandLineWithQuotes_test0_decomposed(self) -> None:
        pass

    def testParseCommandLineWithOnlyWhitespace_test0_decomposed(self) -> None:
        pass

    def testParseCommandLineWithNull_test0_decomposed(self) -> None:
        pass

    def testParseCommandLine_test2_decomposed(self) -> None:
        pass

    def testParseCommandLine_test1_decomposed(self) -> None:
        pass

    def testParseCommandLine_test0_decomposed(self) -> None:
        pass

    def testNullExecutable_test0_decomposed(self) -> None:
        pass

    def testExecutableZeroLengthString_test0_decomposed(self) -> None:
        pass

    def testExecutableWhitespaceString_test0_decomposed(self) -> None:
        pass

    def testExecutable_test4_decomposed(self) -> None:
        pass

    def testExecutable_test3_decomposed(self) -> None:
        pass

    def testExecutable_test2_decomposed(self) -> None:
        pass

    def testExecutable_test1_decomposed(self) -> None:
        pass

    def testExecutable_test0_decomposed(self) -> None:
        pass

    def testCopyConstructor_test7_decomposed(self) -> None:
        pass

    def testCopyConstructor_test6_decomposed(self) -> None:
        pass

    def testCopyConstructor_test5_decomposed(self) -> None:
        pass

    def testCopyConstructor_test4_decomposed(self) -> None:
        pass

    def testCopyConstructor_test3_decomposed(self) -> None:
        pass

    def testCopyConstructor_test2_decomposed(self) -> None:
        pass

    def testCopyConstructor_test1_decomposed(self) -> None:
        pass

    def testCopyConstructor_test0_decomposed(self) -> None:
        pass

    def testComplexAddArguments2_test2_decomposed(self) -> None:
        pass

    def testComplexAddArguments2_test1_decomposed(self) -> None:
        pass

    def testComplexAddArguments2_test0_decomposed(self) -> None:
        pass

    def testComplexAddArguments1_test2_decomposed(self) -> None:
        pass

    def testComplexAddArguments1_test1_decomposed(self) -> None:
        pass

    def testComplexAddArguments1_test0_decomposed(self) -> None:
        pass

    def testComplexAddArgument_test2_decomposed(self) -> None:
        pass

    def testComplexAddArgument_test1_decomposed(self) -> None:
        pass

    def testComplexAddArgument_test0_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion3_test6_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion3_test5_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion3_test4_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion3_test3_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion3_test2_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion3_test1_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion3_test0_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test13_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test12_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test11_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test10_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test9_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test8_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test7_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test6_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test5_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test4_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test3_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test2_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test1_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion2_test0_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test13_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test12_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test11_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test10_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test9_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test8_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test7_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test6_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test5_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test4_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test3_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test2_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test1_decomposed(self) -> None:
        pass

    def testCommandLineParsingWithExpansion1_test0_decomposed(self) -> None:
        pass

    def testAddTwoArguments_test4_decomposed(self) -> None:
        pass

    def testAddTwoArguments_test3_decomposed(self) -> None:
        pass

    def testAddTwoArguments_test2_decomposed(self) -> None:
        pass

    def testAddTwoArguments_test1_decomposed(self) -> None:
        pass

    def testAddTwoArguments_test0_decomposed(self) -> None:
        pass

    def testAddNullArgument_test3_decomposed(self) -> None:
        pass

    def testAddNullArgument_test2_decomposed(self) -> None:
        pass

    def testAddNullArgument_test1_decomposed(self) -> None:
        pass

    def testAddNullArgument_test0_decomposed(self) -> None:
        pass

    def testAddArgumentWithSpace_test3_decomposed(self) -> None:
        pass

    def testAddArgumentWithSpace_test2_decomposed(self) -> None:
        pass

    def testAddArgumentWithSpace_test1_decomposed(self) -> None:
        pass

    def testAddArgumentWithSpace_test0_decomposed(self) -> None:
        pass

    def testAddArgumentWithSingleQuote_test3_decomposed(self) -> None:
        pass

    def testAddArgumentWithSingleQuote_test2_decomposed(self) -> None:
        pass

    def testAddArgumentWithSingleQuote_test1_decomposed(self) -> None:
        pass

    def testAddArgumentWithSingleQuote_test0_decomposed(self) -> None:
        pass

    def testAddArgumentWithQuotesAround_test3_decomposed(self) -> None:
        pass

    def testAddArgumentWithQuotesAround_test2_decomposed(self) -> None:
        pass

    def testAddArgumentWithQuotesAround_test1_decomposed(self) -> None:
        pass

    def testAddArgumentWithQuotesAround_test0_decomposed(self) -> None:
        pass

    def testAddArgumentWithQuote_test3_decomposed(self) -> None:
        pass

    def testAddArgumentWithQuote_test2_decomposed(self) -> None:
        pass

    def testAddArgumentWithQuote_test1_decomposed(self) -> None:
        pass

    def testAddArgumentWithQuote_test0_decomposed(self) -> None:
        pass

    def testAddArgumentWithBothQuotes_test1_decomposed(self) -> None:
        pass

    def testAddArgumentWithBothQuotes_test0_decomposed(self) -> None:
        pass

    def testAddArgumentsWithQuotesAndSpaces_test3_decomposed(self) -> None:
        pass

    def testAddArgumentsWithQuotesAndSpaces_test2_decomposed(self) -> None:
        pass

    def testAddArgumentsWithQuotesAndSpaces_test1_decomposed(self) -> None:
        pass

    def testAddArgumentsWithQuotesAndSpaces_test0_decomposed(self) -> None:
        pass

    def testAddArgumentsWithQuotes_test3_decomposed(self) -> None:
        pass

    def testAddArgumentsWithQuotes_test2_decomposed(self) -> None:
        pass

    def testAddArgumentsWithQuotes_test1_decomposed(self) -> None:
        pass

    def testAddArgumentsWithQuotes_test0_decomposed(self) -> None:
        pass

    def testAddArgumentsArrayNull_test3_decomposed(self) -> None:
        pass

    def testAddArgumentsArrayNull_test2_decomposed(self) -> None:
        pass

    def testAddArgumentsArrayNull_test1_decomposed(self) -> None:
        pass

    def testAddArgumentsArrayNull_test0_decomposed(self) -> None:
        pass

    def testAddArgumentsArray_test3_decomposed(self) -> None:
        pass

    def testAddArgumentsArray_test2_decomposed(self) -> None:
        pass

    def testAddArgumentsArray_test1_decomposed(self) -> None:
        pass

    def testAddArgumentsArray_test0_decomposed(self) -> None:
        pass

    def testAddArguments_test3_decomposed(self) -> None:
        pass

    def testAddArguments_test2_decomposed(self) -> None:
        pass

    def testAddArguments_test1_decomposed(self) -> None:
        pass

    def testAddArguments_test0_decomposed(self) -> None:
        pass

    def testAddArgument_test3_decomposed(self) -> None:
        pass

    def testAddArgument_test2_decomposed(self) -> None:
        pass

    def testAddArgument_test1_decomposed(self) -> None:
        pass

    def testAddArgument_test0_decomposed(self) -> None:
        pass

    # Class Methods End
