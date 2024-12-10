from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Option import *
import os
import typing
from typing import *
import io
from io import StringIO
from io import IOBase

# Imports End


class OptionComparator:

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def compare(self, opt1: Option, opt2: Option) -> int:
        pass

    # Class Methods End


class HelpFormatter:

    # Class Fields Begin
    DEFAULT_LONG_OPT_PREFIX: str = None
    DEFAULT_LONG_OPT_SEPARATOR: str = None
    DEFAULT_ARG_NAME: str = None
    defaultWidth: int = None
    defaultLeftPad: int = None
    defaultDescPad: int = None
    defaultSyntaxPrefix: str = None
    defaultNewLine: str = None
    defaultOptPrefix: str = None
    defaultLongOptPrefix: str = None
    defaultArgName: str = None
    _optionComparator: typing.Callable[[Option, Option], int] = None
    __longOptSeparator: str = None
    DEFAULT_WIDTH: int = None
    DEFAULT_LEFT_PAD: int = None
    DEFAULT_DESC_PAD: int = None
    DEFAULT_SYNTAX_PREFIX: str = None
    DEFAULT_OPT_PREFIX: str = None
    # Class Fields End

    # Class Methods Begin
    def setWidth(self, width: int) -> None:
        pass

    def setSyntaxPrefix(self, prefix: str) -> None:
        pass

    def setOptPrefix(self, prefix: str) -> None:
        pass

    def setOptionComparator(
        self, comparator: typing.Callable[[Option, Option], int]
    ) -> None:
        pass

    def setNewLine(self, newline: str) -> None:
        pass

    def setLongOptSeparator(self, longOptSeparator: str) -> None:
        pass

    def setLongOptPrefix(self, prefix: str) -> None:
        pass

    def setLeftPadding(self, padding: int) -> None:
        pass

    def setDescPadding(self, padding: int) -> None:
        pass

    def setArgName(self, name: str) -> None:
        pass

    def _rtrim(self, s: str) -> str:
        pass

    def _renderWrappedText(
        self, sb: io.StringIO, width: int, nextLineTabStop: int, text: str
    ) -> io.StringIO:
        pass

    def _renderOptions(
        self, sb: io.StringIO, width: int, options: Options, leftPad: int, descPad: int
    ) -> io.StringIO:
        pass

    def printWrapped1(
        self, pw: typing.Union[io.TextIOWrapper, io.StringIO], width: int, text: str
    ) -> None:
        pass

    def printWrapped0(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        nextLineTabStop: int,
        text: str,
    ) -> None:
        pass

    def printUsage1(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        app: str,
        options: Options,
    ) -> None:
        pass

    def printUsage0(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        cmdLineSyntax: str,
    ) -> None:
        pass

    def printOptions(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        options: Options,
        leftPad: int,
        descPad: int,
    ) -> None:
        pass

    def printHelp7(
        self,
        cmdLineSyntax: str,
        header: str,
        options: Options,
        footer: str,
        autoUsage: bool,
    ) -> None:
        pass

    def printHelp6(
        self, cmdLineSyntax: str, header: str, options: Options, footer: str
    ) -> None:
        pass

    def printHelp5(self, cmdLineSyntax: str, options: Options, autoUsage: bool) -> None:
        pass

    def printHelp4(self, cmdLineSyntax: str, options: Options) -> None:
        pass

    def printHelp3(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        cmdLineSyntax: str,
        header: str,
        options: Options,
        leftPad: int,
        descPad: int,
        footer: str,
        autoUsage: bool,
    ) -> None:
        pass

    def printHelp2(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        cmdLineSyntax: str,
        header: str,
        options: Options,
        leftPad: int,
        descPad: int,
        footer: str,
    ) -> None:
        pass

    def printHelp1(
        self,
        width: int,
        cmdLineSyntax: str,
        header: str,
        options: Options,
        footer: str,
        autoUsage: bool,
    ) -> None:
        pass

    def printHelp0(
        self, width: int, cmdLineSyntax: str, header: str, options: Options, footer: str
    ) -> None:
        pass

    def getWidth(self) -> int:
        pass

    def getSyntaxPrefix(self) -> str:
        pass

    def getOptPrefix(self) -> str:
        pass

    def getOptionComparator(self) -> typing.Callable[[Option, Option], int]:
        pass

    def getNewLine(self) -> str:
        pass

    def getLongOptSeparator(self) -> str:
        pass

    def getLongOptPrefix(self) -> str:
        pass

    def getLeftPadding(self) -> int:
        pass

    def getDescPadding(self) -> int:
        pass

    def getArgName(self) -> str:
        pass

    def _findWrapPos(self, text: str, width: int, startPos: int) -> int:
        pass

    def _createPadding(self, len_: int) -> str:
        pass

    def __renderWrappedTextBlock(
        self, sb: io.StringIO, width: int, nextLineTabStop: int, text: str
    ) -> typing.Union[typing.List, io.TextIOBase]:
        pass

    def __appendOptionGroup(self, buff: io.StringIO, group: OptionGroup) -> None:
        pass

    def __appendOption(self, buff: io.StringIO, option: Option, required: bool) -> None:
        pass

    # Class Methods End
