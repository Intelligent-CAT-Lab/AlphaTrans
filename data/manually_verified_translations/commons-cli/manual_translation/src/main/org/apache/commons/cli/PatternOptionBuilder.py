from __future__ import annotations
import time
import re
import pathlib
import io
import numbers
import typing
from typing import *
from datetime import datetime, date
import urllib
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *


class PatternOptionBuilder:

    URL_VALUE: typing.Type[urllib.parse.ParseResult] = urllib.parse.ParseResult
    FILES_VALUE: typing.Type[typing.List[pathlib.Path]] = list
    FILE_VALUE: typing.Type[pathlib.Path] = pathlib.Path
    EXISTING_FILE_VALUE: io.TextIOWrapper = io.TextIOWrapper
    CLASS_VALUE: typing.Type[typing.Any] = type
    DATE_VALUE: typing.Type[typing.Union[date, datetime]] = (
        datetime
    )
    NUMBER_VALUE: typing.Type[typing.Union[int, float, numbers.Number]] = numbers.Number
    OBJECT_VALUE: typing.Type[typing.Any] = object
    STRING_VALUE: typing.Type[str] = str

    @staticmethod
    def parsePattern(pattern: str) -> Options:

        opt = " "
        required = False
        type_ = None

        options = Options()

        for i in range(len(pattern)):
            ch = pattern[i]

            if not PatternOptionBuilder.isValueCode(ch):
                if opt != " ":
                    option = (
                        Option.builder1(str(opt))
                        .hasArg1(type_ is not None)
                        .required1(required)
                        .type_(type_)
                        .build()
                    )

                    options.addOption0(option)
                    required = False
                    type_ = None
                    opt = " "

                opt = ch
            elif ch == "!":
                required = True
            else:
                type_ = PatternOptionBuilder.getValueClass(ch)

        if opt != " ":
            option = (
                Option.builder1(str(opt))
                .hasArg1(type_ is not None)
                .required1(required)
                .type_(type_)
                .build()
            )
            options.addOption0(option)

        return options

    @staticmethod
    def isValueCode(ch: str) -> bool:
        return ch in ["@", ":", "%", "+", "#", "<", ">", "*", "/", "!"]

    @staticmethod
    def getValueClass(ch: str) -> typing.Any:

        match ch:
            case "@":
                return PatternOptionBuilder.OBJECT_VALUE
            case ":":
                return PatternOptionBuilder.STRING_VALUE
            case "%":
                return PatternOptionBuilder.NUMBER_VALUE
            case "+":
                return PatternOptionBuilder.CLASS_VALUE
            case "#":
                return PatternOptionBuilder.DATE_VALUE
            case "<":
                return PatternOptionBuilder.EXISTING_FILE_VALUE
            case ">":
                return PatternOptionBuilder.FILE_VALUE
            case "*":
                return PatternOptionBuilder.FILES_VALUE
            case "/":
                return PatternOptionBuilder.URL_VALUE
        return None
