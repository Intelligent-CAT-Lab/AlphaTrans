from __future__ import annotations
import re
from io import IOBase
from io import StringIO
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *


class OptionComparator:

    __serialVersionUID: int = 5305467873966684014

    def compare(self, opt1: Option, opt2: Option) -> int:
        return opt1.getKey().compareToIgnoreCase(opt2.getKey())


class HelpFormatter:

    _optionComparator: typing.Callable[[Option, Option], int] = None
    defaultNewLine: str = os.linesep
    DEFAULT_ARG_NAME: str = "arg"
    DEFAULT_LONG_OPT_SEPARATOR: str = " "
    DEFAULT_LONG_OPT_PREFIX: str = "--"
    DEFAULT_OPT_PREFIX: str = "-"
    DEFAULT_SYNTAX_PREFIX: str = "usage: "
    DEFAULT_DESC_PAD: int = 3
    DEFAULT_LEFT_PAD: int = 1
    DEFAULT_WIDTH: int = 74
    __longOptSeparator: str = DEFAULT_LONG_OPT_SEPARATOR
    defaultArgName: str = DEFAULT_ARG_NAME
    defaultLongOptPrefix: str = DEFAULT_LONG_OPT_PREFIX
    defaultOptPrefix: str = DEFAULT_OPT_PREFIX
    defaultSyntaxPrefix: str = DEFAULT_SYNTAX_PREFIX
    defaultDescPad: int = DEFAULT_DESC_PAD
    defaultLeftPad: int = DEFAULT_LEFT_PAD
    defaultWidth: int = DEFAULT_WIDTH

    @staticmethod
    def initialize_fields() -> None:
        HelpFormatter._optionComparator: typing.Callable[[Option, Option], int] = (
            OptionComparator()
        )

    def setWidth(self, width: int) -> None:
        self.defaultWidth = width

    def setSyntaxPrefix(self, prefix: str) -> None:
        self.defaultSyntaxPrefix = prefix

    def setOptPrefix(self, prefix: str) -> None:
        self.defaultOptPrefix = prefix

    def setOptionComparator(
        self, comparator: typing.Callable[[Option, Option], int]
    ) -> None:
        self._optionComparator = comparator

    def setNewLine(self, newline: str) -> None:
        self.defaultNewLine = newline

    def setLongOptSeparator(self, longOptSeparator: str) -> None:
        self.__longOptSeparator = longOptSeparator

    def setLongOptPrefix(self, prefix: str) -> None:
        self.defaultLongOptPrefix = prefix

    def setLeftPadding(self, padding: int) -> None:
        self.defaultLeftPad = padding

    def setDescPadding(self, padding: int) -> None:
        self.defaultDescPad = padding

    def setArgName(self, name: str) -> None:
        self.defaultArgName = name

    def _rtrim(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s

        pos = len(s)

        while pos > 0 and s[pos - 1].isspace():
            pos -= 1

        return s[0:pos]

    def _renderWrappedText(
        self, sb: str, width: int, nextLineTabStop: int, text: str
    ) -> str:
        pos = self._findWrapPos(text, width, 0)

        if pos == -1:
            sb.append(self._rtrim(text))

            return sb
        sb.append(self._rtrim(text[0:pos])).append(self.getNewLine())

        if nextLineTabStop >= width:
            nextLineTabStop = 1

        padding = self._createPadding(nextLineTabStop)

        while True:
            text = padding + text[pos:].strip()
            pos = self._findWrapPos(text, width, 0)

            if pos == -1:
                sb.append(text)

                return sb

            if len(text) > width and pos == nextLineTabStop - 1:
                pos = width

            sb.append(self._rtrim(text[0:pos])).append(self.getNewLine())

    def _renderOptions(
        self, sb: str, width: int, options: Options, leftPad: int, descPad: int
    ) -> str:

        pass  # LLM could not translate this method

    def printWrapped1(
        self, pw: typing.Union[io.TextIOWrapper, io.StringIO], width: int, text: str
    ) -> None:
        self.printWrapped0(pw, width, 0, text)

    def printWrapped0(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        nextLineTabStop: int,
        text: str,
    ) -> None:
        sb = StringIO(text)
        self.__renderWrappedTextBlock(sb, width, nextLineTabStop, text)
        pw.write(sb.getvalue())

    def printUsage1(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        app: str,
        options: Options,
    ) -> None:

        pass  # LLM could not translate this method

    def printUsage0(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        cmdLineSyntax: str,
    ) -> None:
        argPos = cmdLineSyntax.index(" ") + 1
        self.printWrapped0(
            pw,
            width,
            len(self.getSyntaxPrefix()) + argPos,
            self.getSyntaxPrefix() + cmdLineSyntax,
        )

    def printOptions(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        options: Options,
        leftPad: int,
        descPad: int,
    ) -> None:
        sb = ""
        self._renderOptions(sb, width, options, leftPad, descPad)
        pw.println(sb)

    def printHelp7(
        self,
        cmdLineSyntax: str,
        header: str,
        options: Options,
        footer: str,
        autoUsage: bool,
    ) -> None:
        self.printHelp1(
            self.getWidth(), cmdLineSyntax, header, options, footer, autoUsage
        )

    def printHelp6(
        self, cmdLineSyntax: str, header: str, options: Options, footer: str
    ) -> None:
        self.printHelp7(cmdLineSyntax, header, options, footer, False)

    def printHelp5(self, cmdLineSyntax: str, options: Options, autoUsage: bool) -> None:
        self.printHelp1(self.getWidth(), cmdLineSyntax, None, options, None, autoUsage)

    def printHelp4(self, cmdLineSyntax: str, options: Options) -> None:
        self.printHelp1(self.getWidth(), cmdLineSyntax, None, options, None, False)

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
        if cmdLineSyntax == None or cmdLineSyntax == "":
            raise ValueError("cmdLineSyntax not provided")

        if autoUsage:
            self.printUsage1(pw, width, cmdLineSyntax, options)
        else:
            self.printUsage0(pw, width, cmdLineSyntax)

        if header != None and header != "":
            self.printWrapped1(pw, width, header)

        self.printOptions(pw, width, options, leftPad, descPad)

        if footer != None and footer != "":
            self.printWrapped1(pw, width, footer)

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
        self.printHelp3(
            pw, width, cmdLineSyntax, header, options, leftPad, descPad, footer, False
        )

    def printHelp1(
        self,
        width: int,
        cmdLineSyntax: str,
        header: str,
        options: Options,
        footer: str,
        autoUsage: bool,
    ) -> None:
        pw: typing.Union[io.TextIOWrapper, io.StringIO] = io.StringIO()
        self.printHelp3(
            pw,
            width,
            cmdLineSyntax,
            header,
            options,
            self.getLeftPadding(),
            self.getDescPadding(),
            footer,
            autoUsage,
        )
        pw.flush()

    def printHelp0(
        self, width: int, cmdLineSyntax: str, header: str, options: Options, footer: str
    ) -> None:
        self.printHelp1(width, cmdLineSyntax, header, options, footer, False)

    def getWidth(self) -> int:
        return self.defaultWidth

    def getSyntaxPrefix(self) -> str:
        return self.defaultSyntaxPrefix

    def getOptPrefix(self) -> str:
        return self.defaultOptPrefix

    def getOptionComparator(self) -> typing.Callable[[Option, Option], int]:
        return self._optionComparator

    def getNewLine(self) -> str:
        return self.defaultNewLine

    def getLongOptSeparator(self) -> str:
        return self.__longOptSeparator

    def getLongOptPrefix(self) -> str:
        return self.defaultLongOptPrefix

    def getLeftPadding(self) -> int:
        return self.defaultLeftPad

    def getDescPadding(self) -> int:
        return self.defaultDescPad

    def getArgName(self) -> str:
        return self.defaultArgName

    def _findWrapPos(self, text: str, width: int, startPos: int) -> int:
        pos = text.find("\n", startPos)
        if pos != -1 and pos <= width:
            return pos + 1

        pos = text.find("\t", startPos)
        if pos != -1 and pos <= width:
            return pos + 1

        if startPos + width >= len(text):
            return -1

        for pos in range(startPos + width, startPos - 1, -1):
            c = text[pos]
            if c == " " or c == "\n" or c == "\r":
                break

        if pos > startPos:
            return pos

        pos = startPos + width

        return -1 if pos == len(text) else pos

    def _createPadding(self, len: int) -> str:
        padding = [" "] * len
        return "".join(padding)

    def __renderWrappedTextBlock(
        self, sb: str, width: int, nextLineTabStop: int, text: str
    ) -> typing.Union[typing.List, io.TextIOBase]:

        pass  # LLM could not translate this method

    def __appendOptionGroup(self, buff: str, group: OptionGroup) -> None:
        if not group.isRequired():
            buff.append("[")

        optList = list(group.getOptions())
        if self.getOptionComparator() is not None:
            optList.sort(key=self.getOptionComparator())

        for option in optList:
            self.__appendOption(buff, option, True)

            if option is not optList[-1]:
                buff.append(" | ")

        if not group.isRequired():
            buff.append("]")

    def __appendOption(self, buff: str, option: Option, required: bool) -> None:
        if not required:
            buff.append("[")
        if option.getOpt() is not None:
            buff.append("-").append(option.getOpt())
        else:
            buff.append("--").append(option.getLongOpt())
        if option.hasArg() and (
            option.getArgName() is None or not option.getArgName().isEmpty()
        ):
            buff.append(option.getOpt() is None and longOptSeparator or " ")
            buff.append("<")
            buff.append(
                option.getArgName() is not None
                and option.getArgName()
                or self.getArgName()
            )
            buff.append(">")
        if not required:
            buff.append("]")


HelpFormatter.initialize_fields()
