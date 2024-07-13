from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Util import *
from src.main.org.apache.commons.cli.TypeHandler import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Option import *
import configparser
import typing
from typing import *
import io

# Imports End


class Builder:

    # Class Fields Begin
    __commandLine: CommandLine = None
    # Class Fields End

    # Class Methods Begin
    def build(self) -> CommandLine:
        pass

    def addOption(self, opt: Option) -> Builder:
        pass

    def addArg(self, arg: str) -> Builder:
        pass

    # Class Methods End


class CommandLine:

    # Class Fields Begin
    __serialVersionUID: int = None
    __args: typing.List[str] = None
    __options: typing.List[Option] = None
    # Class Fields End

    # Class Methods Begin
    def getOptionObject1(self, opt: str) -> typing.Any:
        pass

    def getOptionObject0(self, opt: str) -> typing.Any:
        pass

    def iterator(self) -> typing.Iterator[Option]:
        pass

    def hasOption2(self, opt: str) -> bool:
        pass

    def hasOption1(self, opt: Option) -> bool:
        pass

    def hasOption0(self, opt: str) -> bool:
        pass

    def getParsedOptionValue2(self, opt: str) -> typing.Any:
        pass

    def getParsedOptionValue1(self, option: Option) -> typing.Any:
        pass

    def getParsedOptionValue0(self, opt: str) -> typing.Any:
        pass

    def getOptionValues2(self, opt: str) -> typing.List[typing.List[str]]:
        pass

    def getOptionValues1(self, option: Option) -> typing.List[typing.List[str]]:
        pass

    def getOptionValues0(self, opt: str) -> typing.List[typing.List[str]]:
        pass

    def getOptionValue5(self, opt: str, defaultValue: str) -> str:
        pass

    def getOptionValue4(self, opt: str) -> str:
        pass

    def getOptionValue3(self, option: Option, defaultValue: str) -> str:
        pass

    def getOptionValue2(self, option: Option) -> str:
        pass

    def getOptionValue1(self, opt: str, defaultValue: str) -> str:
        pass

    def getOptionValue0(self, opt: str) -> str:
        pass

    def getOptions(self) -> typing.List[Option]:
        pass

    def getOptionProperties1(
        self, opt: str
    ) -> typing.Union[configparser.ConfigParser, typing.Dict]:
        pass

    def getOptionProperties0(
        self, option: Option
    ) -> typing.Union[configparser.ConfigParser, typing.Dict]:
        pass

    def getArgs(self) -> typing.List[typing.List[str]]:
        pass

    def getArgList(self) -> typing.List[str]:
        pass

    def _addOption(self, opt: Option) -> None:
        pass

    def _addArg(self, arg: str) -> None:
        pass

    def __init__(self) -> None:
        pass

    def __resolveOption(self, opt: str) -> Option:
        pass

    # Class Methods End
