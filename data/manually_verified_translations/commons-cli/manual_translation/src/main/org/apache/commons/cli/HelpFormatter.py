from __future__ import annotations
import re
import enum
from io import IOBase
from io import StringIO
import io
import typing
from typing import *
import os
import inspect
import sys
from functools import cmp_to_key
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *


class OptionComparator:
    __serialVersionUID: int = 5305467873966684014
    
    def __call__(self, opt1: Option, opt2: Option) -> int:
        return self.compare(opt1, opt2)

    def compare(self, opt1: Option, opt2: Option) -> int:
        if opt1.getKey().casefold() < opt2.getKey().casefold():
            return -1
        if opt1.getKey().casefold() > opt2.getKey().casefold():
            return 1
        return 0


class HelpFormatter:

    _optionComparator: typing.Callable[[Option, Option], int] = None
    DEFAULT_ARG_NAME: str = "arg"
    DEFAULT_DESC_PAD: int = 3
    DEFAULT_WIDTH: int = 74
    DEFAULT_LONG_OPT_SEPARATOR: str = " "
    DEFAULT_LONG_OPT_PREFIX: str = "--"
    DEFAULT_OPT_PREFIX: str = "-"
    DEFAULT_SYNTAX_PREFIX: str = "usage: "
    DEFAULT_LEFT_PAD: int = 1
    __longOptSeparator: str = DEFAULT_LONG_OPT_SEPARATOR
    defaultWidth: int = DEFAULT_WIDTH
    defaultLeftPad: int = DEFAULT_LEFT_PAD
    defaultDescPad: int = DEFAULT_DESC_PAD
    defaultLongOptPrefix: str = DEFAULT_LONG_OPT_PREFIX
    defaultOptPrefix: str = DEFAULT_OPT_PREFIX
    defaultNewLine: str = os.linesep
    defaultSyntaxPrefix: str = DEFAULT_SYNTAX_PREFIX
    defaultArgName: str = DEFAULT_ARG_NAME

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

        return s[:pos]

    def _renderWrappedText(
        self, sb: StringIO, width: int, nextLineTabStop: int, text: str
    ) -> str:

        pos = self._findWrapPos(text, width, 0)

        if pos == -1:
            sb.write(self._rtrim(text))

            return sb

        sb.write(self._rtrim(text[:pos]) + self.getNewLine())

        if nextLineTabStop >= width:
            nextLineTabStop = 1

        padding = self._createPadding(nextLineTabStop)

        while True:
            text = padding + text[pos:].strip()
            pos = self._findWrapPos(text, width, 0)

            if pos == -1:
                sb.write(text)

                return sb

            if len(text) > width and pos == nextLineTabStop - 1:
                pos = width

            sb.write(self._rtrim(text[:pos]) + self.getNewLine())

    def _renderOptions(
        self, sb: StringIO, width: int, options: Options, leftPad: int, descPad: int
    ) -> str:

        lpad = self._createPadding(leftPad)
        dpad = self._createPadding(descPad)

        max_ = 0
        prefixList = []

        optList = options.helpOptions()

        if self.getOptionComparator() is not None:
            optList.sort(key=cmp_to_key(self.getOptionComparator()))

        for option in optList:
            optBuf = StringIO()

            if option.getOpt() is None:
                optBuf.write(lpad)
                optBuf.write("   ")
                optBuf.write(self.getLongOptPrefix())
                optBuf.write(option.getLongOpt())
            else:
                optBuf.write(lpad)
                optBuf.write(self.getOptPrefix())
                optBuf.write(option.getOpt())

                if option.hasLongOpt():
                    optBuf.write(",")
                    optBuf.write(self.getLongOptPrefix())
                    optBuf.write(option.getLongOpt())

            if option.hasArg():
                argName = option.getArgName()
                if argName is not None and argName == "":
                    optBuf.write(" ")
                else:
                    optBuf.write(self.__longOptSeparator if option.hasLongOpt() else " ")
                    optBuf.write("<")
                    optBuf.write(argName if argName is not None else self.getArgName())
                    optBuf.write(">")

            prefixList.append(optBuf)
            max_ = max(optBuf.tell(), max_)

        x = 0

        for option in optList:
            optBuf = StringIO()
            optBuf.write(prefixList[x].getvalue())
            x += 1

            if optBuf.tell() < max_:
                optBuf.write(self._createPadding(max_ - optBuf.tell()))

            optBuf.write(dpad)

            nextLineTabStop = max_ + descPad

            if option.getDescription() is not None:
                optBuf.write(option.getDescription())

            self._renderWrappedText(sb, width, nextLineTabStop, optBuf.getvalue())

            if x < len(optList):
                sb.write(self.getNewLine())

        return sb

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
        sb = StringIO()

        self.__renderWrappedTextBlock(sb, width, nextLineTabStop, text)
        pw.write(sb.getvalue() + os.linesep)

    def printUsage1(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        app: str,
        options: Options,
    ) -> None:

        buff = StringIO()
        buff.write(self.getSyntaxPrefix() + app + " ")

        processedGroups = []

        optList = list(options.getOptions())
        if self.getOptionComparator() != None:
            optList.sort(key=cmp_to_key(self.getOptionComparator()))
        for i, option in enumerate(optList):
            group = options.getOptionGroup(option)

            if group != None:
                if group not in processedGroups:
                    processedGroups.append(group)

                    self.__appendOptionGroup(buff, group)

            else:
                self.__appendOption(buff, option, option.isRequired())

            if i < len(optList) - 1:
                buff.write(" ")

        self.printWrapped0(pw, width, buff.getvalue().index(" ") + 1, buff.getvalue())

    def printUsage0(
        self,
        pw: typing.Union[io.TextIOWrapper, io.StringIO],
        width: int,
        cmdLineSyntax: str,
    ) -> None:

        argPos = cmdLineSyntax.find(" ") + 1

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

        sb = StringIO()

        self._renderOptions(sb, width, options, leftPad, descPad)
        pw.write(sb.getvalue() + os.linesep)

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

        pw = sys.stdout

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

        return pos if pos != len(text) else -1

    def _createPadding(self, len_: int) -> str:
        padding = [" "] * len_
        return "".join(padding)

    def __renderWrappedTextBlock(
        self, sb: StringIO, width: int, nextLineTabStop: int, text: str
    ) -> typing.Union[typing.List, io.TextIOBase]:

        in_stream = io.StringIO(text)
        line = in_stream.readline()
        firstLine = True

        while line:
            line = line.rstrip(os.linesep)
            if not firstLine: 
                sb.write(self.getNewLine())
            else:
                firstLine = False

            self._renderWrappedText(sb, width, nextLineTabStop, line)
            line = in_stream.readline()

        return sb

    def __appendOptionGroup(self, buff: StringIO, group: OptionGroup) -> None:

        if not group.isRequired():
            buff.write("[")

        optList = list(group.getOptions())
        if self.getOptionComparator() != None:
            optList.sort(key=cmp_to_key(self.getOptionComparator()))
        for i, option in enumerate(optList):
            self.__appendOption(buff, option, True)

            if i < len(optList) - 1:
                buff.write(" | ")

        if not group.isRequired():
            buff.write("]")

    def __appendOption(self, buff: StringIO, option: Option, required: bool) -> None:

        if not required:
            buff.write("[")

        if option.getOpt() != None:
            buff.write("-" + option.getOpt())
        else:
            buff.write("--" + option.getLongOpt())

        if option.hasArg() and (
            option.getArgName() == None or option.getArgName() != ""
        ):
            buff.write(self.__longOptSeparator if option.getOpt() == None else " ")
            buff.write(
                "<"
                + (
                    option.getArgName()
                    if option.getArgName() != None
                    else self.getArgName()
                )
                + ">"
            )

        if not required:
            buff.write("]")


HelpFormatter.initialize_fields()
