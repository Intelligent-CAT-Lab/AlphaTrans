from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.PatternOptionBuilder import *
from src.main.org.apache.commons.cli.ParseException import *
import urllib
import datetime
import typing
from typing import *
import numbers
import io
import pathlib

# Imports End


class TypeHandler:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def createValue0(str_: str, clazz: typing.Type[typing.Any]) -> typing.Any:
        pass

    @staticmethod
    def openFile(str_: str) -> typing.Union[io.FileIO, io.BufferedReader]:
        pass

    @staticmethod
    def createValue1(str_: str, obj: typing.Any) -> typing.Any:
        pass

    @staticmethod
    def createURL(
        str_: str,
    ) -> typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ]:
        pass

    @staticmethod
    def createObject(classname: str) -> typing.Any:
        pass

    @staticmethod
    def createNumber(str_: str) -> typing.Union[int, float, numbers.Number]:
        pass

    @staticmethod
    def createFiles(str_: str) -> typing.List[pathlib.Path]:
        pass

    @staticmethod
    def createFile(str_: str) -> pathlib.Path:
        pass

    @staticmethod
    def createDate(str_: str) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    @staticmethod
    def createClass(classname: str) -> typing.Type[typing.Any]:
        pass

    # Class Methods End
