from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import os
import io

# Imports End


class CommandLineTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testNullhOption_test12_decomposed(self) -> None:
        pass

    def testNullhOption_test11_decomposed(self) -> None:
        pass

    def testNullhOption_test10_decomposed(self) -> None:
        pass

    def testNullhOption_test9_decomposed(self) -> None:
        pass

    def testNullhOption_test8_decomposed(self) -> None:
        pass

    def testNullhOption_test7_decomposed(self) -> None:
        pass

    def testNullhOption_test6_decomposed(self) -> None:
        pass

    def testNullhOption_test5_decomposed(self) -> None:
        pass

    def testNullhOption_test4_decomposed(self) -> None:
        pass

    def testNullhOption_test3_decomposed(self) -> None:
        pass

    def testNullhOption_test2_decomposed(self) -> None:
        pass

    def testNullhOption_test1_decomposed(self) -> None:
        pass

    def testNullhOption_test0_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test11_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test10_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test9_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test8_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test7_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test6_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test5_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test4_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test3_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test2_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test1_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithOption_test0_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test12_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test11_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test10_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test9_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test8_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test7_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test6_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test5_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test4_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test3_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test2_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test1_decomposed(self) -> None:
        pass

    def testGetParsedOptionValueWithChar_test0_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test10_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test9_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test8_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test7_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test6_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test5_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test4_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test3_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test2_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test1_decomposed(self) -> None:
        pass

    def testGetParsedOptionValue_test0_decomposed(self) -> None:
        pass

    def testGetOptions_test8_decomposed(self) -> None:
        pass

    def testGetOptions_test7_decomposed(self) -> None:
        pass

    def testGetOptions_test6_decomposed(self) -> None:
        pass

    def testGetOptions_test5_decomposed(self) -> None:
        pass

    def testGetOptions_test4_decomposed(self) -> None:
        pass

    def testGetOptions_test3_decomposed(self) -> None:
        pass

    def testGetOptions_test2_decomposed(self) -> None:
        pass

    def testGetOptions_test1_decomposed(self) -> None:
        pass

    def testGetOptions_test0_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test15_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test14_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test13_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test12_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test11_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test10_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test9_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test8_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test7_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test6_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test5_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test4_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test3_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test2_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test1_decomposed(self) -> None:
        pass

    def testGetOptionPropertiesWithOption_test0_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test16_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test15_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test14_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test13_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test12_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test11_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test10_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test9_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test8_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test7_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test6_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test5_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test4_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test3_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test2_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test1_decomposed(self) -> None:
        pass

    def testGetOptionProperties_test0_decomposed(self) -> None:
        pass

    def testBuilder_test9_decomposed(self) -> None:
        pass

    def testBuilder_test8_decomposed(self) -> None:
        pass

    def testBuilder_test7_decomposed(self) -> None:
        pass

    def testBuilder_test6_decomposed(self) -> None:
        pass

    def testBuilder_test5_decomposed(self) -> None:
        pass

    def testBuilder_test4_decomposed(self) -> None:
        pass

    def testBuilder_test3_decomposed(self) -> None:
        pass

    def testBuilder_test2_decomposed(self) -> None:
        pass

    def testBuilder_test1_decomposed(self) -> None:
        pass

    def testBuilder_test0_decomposed(self) -> None:
        pass

    # Class Methods End
