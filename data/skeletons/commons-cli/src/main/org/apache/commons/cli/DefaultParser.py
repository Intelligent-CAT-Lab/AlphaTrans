from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Util import *
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.AmbiguousOptionException import *
from src.main.org.apache.commons.cli.AlreadySelectedException import *
import configparser
import typing
from typing import *
import numbers
import io

# Imports End


class Builder:

    # Class Fields Begin
    __allowPartialMatching: bool = None
    __stripLeadingAndTrailingQuotes: bool = None
    # Class Fields End

    # Class Methods Begin
    def setStripLeadingAndTrailingQuotes(
        self, stripLeadingAndTrailingQuotes: bool
    ) -> Builder:
        pass

    def setAllowPartialMatching(self, allowPartialMatching: bool) -> Builder:
        pass

    def build(self) -> DefaultParser:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class DefaultParser(CommandLineParser):

    # Class Fields Begin
    _cmd: CommandLine = None
    _options: Options = None
    _stopAtNonOption: bool = None
    _currentToken: str = None
    _currentOption: Option = None
    _skipParsing: bool = None
    _expectedOpts: typing.List[typing.Any] = None
    __allowPartialMatching: bool = None
    __stripLeadingAndTrailingQuotes: bool = None
    # Class Fields End

    # Class Methods Begin
    def parse3(
        self,
        options: Options,
        arguments: typing.List[typing.List[str]],
        properties: typing.Union[configparser.ConfigParser, typing.Dict],
        stopAtNonOption: bool,
    ) -> CommandLine:
        pass

    def parse2(
        self,
        options: Options,
        arguments: typing.List[typing.List[str]],
        properties: typing.Union[configparser.ConfigParser, typing.Dict],
    ) -> CommandLine:
        pass

    def parse1(
        self,
        options: Options,
        arguments: typing.List[typing.List[str]],
        stopAtNonOption: bool,
    ) -> CommandLine:
        pass

    def parse0(
        self, options: Options, arguments: typing.List[typing.List[str]]
    ) -> CommandLine:
        pass

    def _handleConcatenatedOptions(self, token: str) -> None:
        pass

    def _checkRequiredOptions(self) -> None:
        pass

    def __init__(
        self,
        constructorId: int,
        allowPartialMatching: bool,
        stripLeadingAndTrailingQuotes: bool,
    ) -> None:
        pass

    @staticmethod
    def builder() -> Builder:
        pass

    def __updateRequiredOptions(self, option: Option) -> None:
        pass

    def __stripLeadingAndTrailingQuotesDefaultOn(self, token: str) -> str:
        pass

    def __stripLeadingAndTrailingQuotesDefaultOff(self, token: str) -> str:
        pass

    def __isShortOption(self, token: str) -> bool:
        pass

    def __isOption(self, token: str) -> bool:
        pass

    def __isNegativeNumber(self, token: str) -> bool:
        pass

    def __isLongOption(self, token: str) -> bool:
        pass

    def __isJavaProperty(self, token: str) -> bool:
        pass

    def __isArgument(self, token: str) -> bool:
        pass

    def __handleUnknownToken(self, token: str) -> None:
        pass

    def __handleToken(self, token: str) -> None:
        pass

    def __handleShortAndLongOption(self, token: str) -> None:
        pass

    def __handleProperties(
        self, properties: typing.Union[configparser.ConfigParser, typing.Dict]
    ) -> None:
        pass

    def __handleOption(self, option: Option) -> None:
        pass

    def __handleLongOptionWithoutEqual(self, token: str) -> None:
        pass

    def __handleLongOptionWithEqual(self, token: str) -> None:
        pass

    def __handleLongOption(self, token: str) -> None:
        pass

    def __getMatchingLongOptions(self, token: str) -> typing.List[str]:
        pass

    def __getLongPrefix(self, token: str) -> str:
        pass

    def __checkRequiredArgs(self) -> None:
        pass

    # Class Methods End
