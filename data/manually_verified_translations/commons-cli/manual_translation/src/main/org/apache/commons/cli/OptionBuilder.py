from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.cli.Option import *


class OptionBuilder:

    __INSTANCE: OptionBuilder = None
    __valueSeparator: str = "\u0000"

    __optionalArg: bool = False

    __type: typing.Type[typing.Any] = None

    __argCount: int = Option.UNINITIALIZED
    __required: bool = False

    __argName: str = ""

    __description: str = ""

    __longOption: str = ""

    @staticmethod
    def run_static_init():
        OptionBuilder.__reset()

    @staticmethod
    def initialize_fields() -> None:
        OptionBuilder.__INSTANCE: OptionBuilder = OptionBuilder()

    @staticmethod
    def withType1(newType: typing.Any) -> OptionBuilder:
        return OptionBuilder.withType0(type(newType))

    @staticmethod
    def withValueSeparator1(sep: str) -> OptionBuilder:
        OptionBuilder.__valueSeparator = sep
        return OptionBuilder.__INSTANCE

    @staticmethod
    def withValueSeparator0() -> OptionBuilder:
        OptionBuilder.__valueSeparator = "="
        return OptionBuilder.__INSTANCE

    @staticmethod
    def withType0(newType: typing.Type[typing.Any]) -> OptionBuilder:
        OptionBuilder.__type = newType
        return OptionBuilder.__INSTANCE

    @staticmethod
    def withLongOpt(newLongopt: str) -> OptionBuilder:
        OptionBuilder.__longOption = newLongopt
        return OptionBuilder.__INSTANCE

    @staticmethod
    def withDescription(newDescription: str) -> OptionBuilder:
        OptionBuilder.__description = newDescription
        return OptionBuilder.__INSTANCE

    @staticmethod
    def withArgName(name: str) -> OptionBuilder:
        OptionBuilder.__argName = name
        return OptionBuilder.__INSTANCE

    @staticmethod
    def isRequired1(newRequired: bool) -> OptionBuilder:
        OptionBuilder.__required = newRequired
        return OptionBuilder.__INSTANCE

    @staticmethod
    def isRequired0() -> OptionBuilder:
        OptionBuilder.__required = True
        return OptionBuilder.__INSTANCE

    @staticmethod
    def hasOptionalArgs1(numArgs: int) -> OptionBuilder:

        OptionBuilder.__argCount = numArgs
        OptionBuilder.__optionalArg = True

        return OptionBuilder.__INSTANCE

    @staticmethod
    def hasOptionalArgs0() -> OptionBuilder:

        OptionBuilder.__argCount = Option.UNLIMITED_VALUES
        OptionBuilder.__optionalArg = True

        return OptionBuilder.__INSTANCE

    @staticmethod
    def hasOptionalArg() -> OptionBuilder:

        OptionBuilder.__argCount = 1
        OptionBuilder.__optionalArg = True

        return OptionBuilder.__INSTANCE

    @staticmethod
    def hasArgs1(num: int) -> OptionBuilder:
        OptionBuilder.__argCount = num
        return OptionBuilder.__INSTANCE

    @staticmethod
    def hasArgs0() -> OptionBuilder:
        OptionBuilder.__argCount = Option.UNLIMITED_VALUES
        return OptionBuilder.__INSTANCE

    @staticmethod
    def hasArg1(hasArg: bool) -> OptionBuilder:
        OptionBuilder.__argCount = 1 if hasArg else Option.UNINITIALIZED
        return OptionBuilder.__INSTANCE

    @staticmethod
    def hasArg0() -> OptionBuilder:
        OptionBuilder.__argCount = 1
        return OptionBuilder.__INSTANCE

    @staticmethod
    def create2(opt: str) -> Option:
        option = None
        try:
            option = Option.Option1(opt, OptionBuilder.__description)

            option.setLongOpt(OptionBuilder.__longOption)
            option.setRequired(OptionBuilder.__required)
            option.setOptionalArg(OptionBuilder.__optionalArg)
            option.setArgs(OptionBuilder.__argCount)
            option.setType0(OptionBuilder.__type)
            option.setValueSeparator(OptionBuilder.__valueSeparator)
            option.setArgName(OptionBuilder.__argName)
        finally:
            OptionBuilder.__reset()

        return option

    @staticmethod
    def create1(opt: str) -> Option:
        return OptionBuilder.create2(opt)

    @staticmethod
    def create0() -> Option:

        if OptionBuilder.__longOption is None:
            OptionBuilder.__reset()
            raise ValueError("must specify longopt")

        return OptionBuilder.create2(None)

    def __init__(self) -> None:
        pass

    @staticmethod
    def __reset() -> None:

        OptionBuilder.__description = None
        OptionBuilder.__argName = None
        OptionBuilder.__longOption = None
        OptionBuilder.__type = str
        OptionBuilder.__required = False
        OptionBuilder.__argCount = Option.UNINITIALIZED
        OptionBuilder.__optionalArg = False
        OptionBuilder.__valueSeparator = "\u0000"


OptionBuilder.run_static_init()

OptionBuilder.initialize_fields()
