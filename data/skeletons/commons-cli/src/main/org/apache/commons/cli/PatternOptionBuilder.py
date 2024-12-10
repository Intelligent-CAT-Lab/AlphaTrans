from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
import urllib
import datetime
import typing
from typing import *
import numbers
import io
import pathlib

# Imports End


class PatternOptionBuilder:

    # Class Fields Begin
    STRING_VALUE: typing.Type[str] = None
    OBJECT_VALUE: typing.Type[typing.Any] = None
    NUMBER_VALUE: typing.Type[typing.Union[int, float, numbers.Number]] = None
    DATE_VALUE: typing.Type[typing.Union[datetime.date, datetime.datetime]] = None
    CLASS_VALUE: typing.Type[typing.Any] = None
    EXISTING_FILE_VALUE: typing.Type[
        typing.Union[io.FileIO, io.BufferedReader, io.TextIOWrapper]
    ] = None
    FILE_VALUE: typing.Type[pathlib.Path] = None
    FILES_VALUE: typing.Type[typing.List[pathlib.Path]] = None
    URL_VALUE: typing.Type[
        typing.Union[
            urllib.parse.ParseResult,
            urllib.parse.SplitResult,
            urllib.parse.DefragResult,
            str,
        ]
    ] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def parsePattern(pattern: str) -> Options:
        pass

    @staticmethod
    def isValueCode(ch: str) -> bool:
        pass

    @staticmethod
    def getValueClass(ch: str) -> typing.Any:
        pass

    # Class Methods End
