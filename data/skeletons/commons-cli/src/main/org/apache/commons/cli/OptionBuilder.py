from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Option import *
import typing
from typing import *
import io

# Imports End


class OptionBuilder:

    # Class Fields Begin
    __longOption: str = None
    __description: str = None
    __argName: str = None
    __required: bool = None
    __argCount: int = None
    __type: typing.Type[typing.Any] = None
    __optionalArg: bool = None
    __valueSeparator: str = None
    __INSTANCE: OptionBuilder = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def withType1(newType: typing.Any) -> OptionBuilder:
        pass

    @staticmethod
    def withValueSeparator1(sep: str) -> OptionBuilder:
        pass

    @staticmethod
    def withValueSeparator0() -> OptionBuilder:
        pass

    @staticmethod
    def withType0(newType: typing.Type[typing.Any]) -> OptionBuilder:
        pass

    @staticmethod
    def withLongOpt(newLongopt: str) -> OptionBuilder:
        pass

    @staticmethod
    def withDescription(newDescription: str) -> OptionBuilder:
        pass

    @staticmethod
    def withArgName(name: str) -> OptionBuilder:
        pass

    @staticmethod
    def isRequired1(newRequired: bool) -> OptionBuilder:
        pass

    @staticmethod
    def isRequired0() -> OptionBuilder:
        pass

    @staticmethod
    def hasOptionalArgs1(numArgs: int) -> OptionBuilder:
        pass

    @staticmethod
    def hasOptionalArgs0() -> OptionBuilder:
        pass

    @staticmethod
    def hasOptionalArg() -> OptionBuilder:
        pass

    @staticmethod
    def hasArgs1(num: int) -> OptionBuilder:
        pass

    @staticmethod
    def hasArgs0() -> OptionBuilder:
        pass

    @staticmethod
    def hasArg1(hasArg: bool) -> OptionBuilder:
        pass

    @staticmethod
    def hasArg0() -> OptionBuilder:
        pass

    @staticmethod
    def create2(opt: str) -> Option:
        pass

    @staticmethod
    def create1(opt: str) -> Option:
        pass

    @staticmethod
    def create0() -> Option:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def __reset() -> None:
        pass

    # Class Methods End
