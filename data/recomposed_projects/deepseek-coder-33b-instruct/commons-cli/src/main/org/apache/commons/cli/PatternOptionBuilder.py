from __future__ import annotations
import urllib
import pathlib
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *


class PatternOptionBuilder:

    URL_VALUE: typing.Type[
        typing.Union[
            urllib.parse.ParseResult,
            urllib.parse.SplitResult,
            urllib.parse.DefragResult,
            str,
        ]
    ] = urllib.parse.ParseResult

    FILES_VALUE: typing.Type[typing.List[pathlib.Path]] = list

    FILE_VALUE: typing.Type[pathlib.Path] = pathlib.Path

    EXISTING_FILE_VALUE: typing.Type[typing.Union[io.FileIO, io.BufferedReader]] = (
        io.FileIO
    )

    CLASS_VALUE: typing.Type[typing.Any] = type(None)

    DATE_VALUE: typing.Type[typing.Union[datetime.date, datetime.datetime]] = (
        datetime.date
    )

    NUMBER_VALUE: typing.Type[typing.Union[int, float, numbers.Number]] = numbers.Number

    OBJECT_VALUE: typing.Type[typing.Any] = object

    STRING_VALUE: typing.Type[str] = str

    @staticmethod
    def parsePattern(pattern: str) -> Options:

        opt = " "
        required = False
        type = None

        options = Options()

        for i in range(len(pattern)):
            ch = pattern[i]

            if not PatternOptionBuilder.isValueCode(ch):
                if opt != " ":
                    option = (
                        Option.builder1(str(opt))
                        .hasArg1(type is not None)
                        .required1(required)
                        .type(type)
                        .build()
                    )

                    options.addOption0(option)
                    required = False
                    type = None
                    opt = " "

                opt = ch
            elif ch == "1":
                required = True
            else:
                type = PatternOptionBuilder.getValueClass(ch)

        if opt != " ":
            option = (
                Option.builder1(str(opt))
                .hasArg1(type is not None)
                .required1(required)
                .type(type)
                .build()
            )

            options.addOption0(option)

        return options

    @staticmethod
    def isValueCode(ch: str) -> bool:

        return (
            ch == "@"
            or ch == ":"
            or ch == "%"
            or ch == "+"
            or ch == "#"
            or ch == "<"
            or ch == ">"
            or ch == "*"
            or ch == "/"
            or ch == "!"
        )

    @staticmethod
    def getValueClass(ch: str) -> typing.Any:

        if ch == "@":
            return PatternOptionBuilder.OBJECT_VALUE
        elif ch == ":":
            return PatternOptionBuilder.STRING_VALUE
        elif ch == "%":
            return PatternOptionBuilder.NUMBER_VALUE
        elif ch == "+":
            return PatternOptionBuilder.CLASS_VALUE
        elif ch == "#":
            return PatternOptionBuilder.DATE_VALUE
        elif ch == "<":
            return PatternOptionBuilder.EXISTING_FILE_VALUE
        elif ch == ">":
            return PatternOptionBuilder.FILE_VALUE
        elif ch == "*":
            return PatternOptionBuilder.FILES_VALUE
        elif ch == "/":
            return PatternOptionBuilder.URL_VALUE

        return None
