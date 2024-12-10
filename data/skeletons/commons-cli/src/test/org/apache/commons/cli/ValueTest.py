from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import os
import io

# Imports End


class ValueTest(unittest.TestCase):

    # Class Fields Begin
    __cl: CommandLine = None
    __opts: Options = None
    # Class Fields End

    # Class Methods Begin
    def testShortWithArgWithOption_test5_decomposed(self) -> None:
        pass

    def testShortWithArgWithOption_test4_decomposed(self) -> None:
        pass

    def testShortWithArgWithOption_test3_decomposed(self) -> None:
        pass

    def testShortWithArgWithOption_test2_decomposed(self) -> None:
        pass

    def testShortWithArgWithOption_test1_decomposed(self) -> None:
        pass

    def testShortWithArgWithOption_test0_decomposed(self) -> None:
        pass

    def testShortWithArg_test1_decomposed(self) -> None:
        pass

    def testShortWithArg_test0_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test9_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test8_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test7_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test6_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test5_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test4_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test3_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test2_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test1_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValuesWithOption_test0_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValues_test5_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValues_test4_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValues_test3_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValues_test2_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValues_test1_decomposed(self) -> None:
        pass

    def testShortOptionalNArgValues_test0_decomposed(self) -> None:
        pass

    def testShortOptionalArgValueWithOption_test5_decomposed(self) -> None:
        pass

    def testShortOptionalArgValueWithOption_test4_decomposed(self) -> None:
        pass

    def testShortOptionalArgValueWithOption_test3_decomposed(self) -> None:
        pass

    def testShortOptionalArgValueWithOption_test2_decomposed(self) -> None:
        pass

    def testShortOptionalArgValueWithOption_test1_decomposed(self) -> None:
        pass

    def testShortOptionalArgValueWithOption_test0_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test10_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test9_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test8_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test7_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test6_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test5_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test4_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test3_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test2_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test1_decomposed(self) -> None:
        pass

    def testShortOptionalArgValuesWithOption_test0_decomposed(self) -> None:
        pass

    def testShortOptionalArgValues_test5_decomposed(self) -> None:
        pass

    def testShortOptionalArgValues_test4_decomposed(self) -> None:
        pass

    def testShortOptionalArgValues_test3_decomposed(self) -> None:
        pass

    def testShortOptionalArgValues_test2_decomposed(self) -> None:
        pass

    def testShortOptionalArgValues_test1_decomposed(self) -> None:
        pass

    def testShortOptionalArgValues_test0_decomposed(self) -> None:
        pass

    def testShortOptionalArgValue_test3_decomposed(self) -> None:
        pass

    def testShortOptionalArgValue_test2_decomposed(self) -> None:
        pass

    def testShortOptionalArgValue_test1_decomposed(self) -> None:
        pass

    def testShortOptionalArgValue_test0_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValueWithOption_test5_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValueWithOption_test4_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValueWithOption_test3_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValueWithOption_test2_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValueWithOption_test1_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValueWithOption_test0_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValue_test3_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValue_test2_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValue_test1_decomposed(self) -> None:
        pass

    def testShortOptionalArgNoValue_test0_decomposed(self) -> None:
        pass

    def testShortNoArgWithOption_test3_decomposed(self) -> None:
        pass

    def testShortNoArgWithOption_test2_decomposed(self) -> None:
        pass

    def testShortNoArgWithOption_test1_decomposed(self) -> None:
        pass

    def testShortNoArgWithOption_test0_decomposed(self) -> None:
        pass

    def testShortNoArg_test1_decomposed(self) -> None:
        pass

    def testShortNoArg_test0_decomposed(self) -> None:
        pass

    def testLongWithArgWithOption_test5_decomposed(self) -> None:
        pass

    def testLongWithArgWithOption_test4_decomposed(self) -> None:
        pass

    def testLongWithArgWithOption_test3_decomposed(self) -> None:
        pass

    def testLongWithArgWithOption_test2_decomposed(self) -> None:
        pass

    def testLongWithArgWithOption_test1_decomposed(self) -> None:
        pass

    def testLongWithArgWithOption_test0_decomposed(self) -> None:
        pass

    def testLongWithArg_test1_decomposed(self) -> None:
        pass

    def testLongWithArg_test0_decomposed(self) -> None:
        pass

    def testLongOptionalNoValueWithOption_test5_decomposed(self) -> None:
        pass

    def testLongOptionalNoValueWithOption_test4_decomposed(self) -> None:
        pass

    def testLongOptionalNoValueWithOption_test3_decomposed(self) -> None:
        pass

    def testLongOptionalNoValueWithOption_test2_decomposed(self) -> None:
        pass

    def testLongOptionalNoValueWithOption_test1_decomposed(self) -> None:
        pass

    def testLongOptionalNoValueWithOption_test0_decomposed(self) -> None:
        pass

    def testLongOptionalNoValue_test3_decomposed(self) -> None:
        pass

    def testLongOptionalNoValue_test2_decomposed(self) -> None:
        pass

    def testLongOptionalNoValue_test1_decomposed(self) -> None:
        pass

    def testLongOptionalNoValue_test0_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test10_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test9_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test8_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test7_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test6_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test5_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test4_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test3_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test2_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test1_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValuesWithOption_test0_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValues_test5_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValues_test4_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValues_test3_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValues_test2_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValues_test1_decomposed(self) -> None:
        pass

    def testLongOptionalNArgValues_test0_decomposed(self) -> None:
        pass

    def testLongOptionalArgValueWithOption_test5_decomposed(self) -> None:
        pass

    def testLongOptionalArgValueWithOption_test4_decomposed(self) -> None:
        pass

    def testLongOptionalArgValueWithOption_test3_decomposed(self) -> None:
        pass

    def testLongOptionalArgValueWithOption_test2_decomposed(self) -> None:
        pass

    def testLongOptionalArgValueWithOption_test1_decomposed(self) -> None:
        pass

    def testLongOptionalArgValueWithOption_test0_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test10_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test9_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test8_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test7_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test6_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test5_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test4_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test3_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test2_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test1_decomposed(self) -> None:
        pass

    def testLongOptionalArgValuesWithOption_test0_decomposed(self) -> None:
        pass

    def testLongOptionalArgValues_test5_decomposed(self) -> None:
        pass

    def testLongOptionalArgValues_test4_decomposed(self) -> None:
        pass

    def testLongOptionalArgValues_test3_decomposed(self) -> None:
        pass

    def testLongOptionalArgValues_test2_decomposed(self) -> None:
        pass

    def testLongOptionalArgValues_test1_decomposed(self) -> None:
        pass

    def testLongOptionalArgValues_test0_decomposed(self) -> None:
        pass

    def testLongOptionalArgValue_test3_decomposed(self) -> None:
        pass

    def testLongOptionalArgValue_test2_decomposed(self) -> None:
        pass

    def testLongOptionalArgValue_test1_decomposed(self) -> None:
        pass

    def testLongOptionalArgValue_test0_decomposed(self) -> None:
        pass

    def testLongNoArgWithOption_test3_decomposed(self) -> None:
        pass

    def testLongNoArgWithOption_test2_decomposed(self) -> None:
        pass

    def testLongNoArgWithOption_test1_decomposed(self) -> None:
        pass

    def testLongNoArgWithOption_test0_decomposed(self) -> None:
        pass

    def testLongNoArg_test1_decomposed(self) -> None:
        pass

    def testLongNoArg_test0_decomposed(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    # Class Methods End
