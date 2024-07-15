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
    def testWithRequiredOption(self) -> None:
        pass

    def testUnrecognizedOptionWithBursting(self) -> None:
        pass

    def testUnrecognizedOption(self) -> None:
        pass

    def testUnlimitedArgs(self) -> None:
        pass

    def testUnambiguousPartialLongOption4(self) -> None:
        pass

    def testUnambiguousPartialLongOption3(self) -> None:
        pass

    def testUnambiguousPartialLongOption2(self) -> None:
        pass

    def testUnambiguousPartialLongOption1(self) -> None:
        pass

    def testStopBursting2(self) -> None:
        pass

    def testStopBursting(self) -> None:
        pass

    def testStopAtUnexpectedArg(self) -> None:
        pass

    def testStopAtNonOptionShort(self) -> None:
        pass

    def testStopAtNonOptionLong(self) -> None:
        pass

    def testStopAtExpectedArg(self) -> None:
        pass

    def testSingleDash(self) -> None:
        pass

    def testSimpleShort(self) -> None:
        pass

    def testSimpleLong(self) -> None:
        pass

    def testShortWithUnexpectedArgument(self) -> None:
        pass

    def testShortWithoutEqual(self) -> None:
        pass

    def testShortWithEqual(self) -> None:
        pass

    def testShortOptionQuoteHandling(self) -> None:
        pass

    def testShortOptionConcatenatedQuoteHandling(self) -> None:
        pass

    def testReuseOptionsTwice(self) -> None:
        pass

    def testPropertyOverrideValues(self) -> None:
        pass

    def testPropertyOptionUnexpected(self) -> None:
        pass

    def testPropertyOptionSingularValue(self) -> None:
        pass

    def testPropertyOptionRequired(self) -> None:
        pass

    def testPropertyOptionMultipleValues(self) -> None:
        pass

    def testPropertyOptionGroup(self) -> None:
        pass

    def testPropertyOptionFlags(self) -> None:
        pass

    def testPropertiesOption2(self) -> None:
        pass

    def testPropertiesOption1(self) -> None:
        pass

    def testPartialLongOptionSingleDash(self) -> None:
        pass

    def testOptionGroupLong(self) -> None:
        pass

    def testOptionGroup(self) -> None:
        pass

    def testOptionAndRequiredOption(self) -> None:
        pass

    def testNegativeOption(self) -> None:
        pass

    def testNegativeArgument(self) -> None:
        pass

    def testMultipleWithLong(self) -> None:
        pass

    def testMultiple(self) -> None:
        pass

    def testMissingRequiredOptions(self) -> None:
        pass

    def testMissingRequiredOption(self) -> None:
        pass

    def testMissingRequiredGroup(self) -> None:
        pass

    def testMissingArgWithBursting(self) -> None:
        pass

    def testMissingArg(self) -> None:
        pass

    def testLongWithUnexpectedArgument2(self) -> None:
        pass

    def testLongWithUnexpectedArgument1(self) -> None:
        pass

    def testLongWithoutEqualSingleDash(self) -> None:
        pass

    def testLongWithoutEqualDoubleDash(self) -> None:
        pass

    def testLongWithEqualSingleDash(self) -> None:
        pass

    def testLongWithEqualDoubleDash(self) -> None:
        pass

    def testLongOptionWithEqualsQuoteHandling(self) -> None:
        pass

    def testLongOptionQuoteHandling(self) -> None:
        pass

    def testDoubleDash2(self) -> None:
        pass

    def testDoubleDash1(self) -> None:
        pass

    def testBursting(self) -> None:
        pass

    def testArgumentStartingWithHyphen(self) -> None:
        pass

    def testAmbiguousPartialLongOption4(self) -> None:
        pass

    def testAmbiguousPartialLongOption3(self) -> None:
        pass

    def testAmbiguousPartialLongOption2(self) -> None:
        pass

    def testAmbiguousPartialLongOption1(self) -> None:
        pass

    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:
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
