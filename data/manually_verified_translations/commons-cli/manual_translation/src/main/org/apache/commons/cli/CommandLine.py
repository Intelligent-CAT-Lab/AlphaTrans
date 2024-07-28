from __future__ import annotations
import re
import io
import typing
from typing import *
import configparser
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.TypeHandler import *
from src.main.org.apache.commons.cli.Util import *


class Builder:

    __commandLine: CommandLine = None

    @staticmethod
    def initialize_fields() -> None:
        Builder.__commandLine: CommandLine = CommandLine()

    def build(self) -> CommandLine:
        return self.__commandLine

    def addOption(self, opt: Option) -> Builder:
        self.__commandLine._addOption(opt)
        return self

    def addArg(self, arg: str) -> Builder:
        self.__commandLine._addArg(arg)
        return self


class CommandLine:

    __serialVersionUID: int = 1

    def getOptionObject1(self, opt: str) -> typing.Any:
        try:
            return self.getParsedOptionValue2(opt)
        except ParseException as pe:
            print(
                f"Exception found converting {opt} to desired type: {pe.getMessage()}"
            )
            return None

    def getOptionObject0(self, opt: str) -> typing.Any:
        return self.getOptionObject1(opt)

    def iterator(self) -> typing.Iterator[Option]:
        return iter(self.__options)

    def hasOption2(self, opt: str) -> bool:
        return self.hasOption1(self.__resolveOption(opt))

    def hasOption1(self, opt: Option) -> bool:
        return opt in self.__options

    def hasOption0(self, opt: str) -> bool:
        return self.hasOption2(opt)

    def getParsedOptionValue2(self, opt: str) -> typing.Any:
        try:
            return self.getParsedOptionValue1(self.__resolveOption(opt))
        except ParseException as e:
            print(f"Error parsing option: {e}")

    def getParsedOptionValue1(self, option: Option) -> typing.Any:
        if option is None:
            return None
        res = self.getOptionValue2(option)
        if res is None:
            return None
        return TypeHandler.createValue1(res, option.getType())

    def getParsedOptionValue0(self, opt: str) -> typing.Any:
        try:
            return self.getParsedOptionValue2(opt)
        except ParseException as e:
            print(f"Error parsing option: {e}")

    def getOptionValues2(self, opt: str) -> typing.List[typing.List[str]]:
        return self.getOptionValues1(self.__resolveOption(opt))

    def getOptionValues1(self, option: Option) -> typing.List[typing.List[str]]:
        values = []

        for processedOption in self.__options:
            if processedOption.equals(option):
                values.extend(processedOption.getValuesList())

        return values if values else None

    def getOptionValues0(self, opt: str) -> typing.List[typing.List[str]]:
        return self.getOptionValues2(opt)

    def getOptionValue5(self, opt: str, defaultValue: str) -> str:
        return self.getOptionValue3(self.__resolveOption(opt), defaultValue)

    def getOptionValue4(self, opt: str) -> str:
        return self.getOptionValue2(self.__resolveOption(opt))

    def getOptionValue3(self, option: Option, defaultValue: str) -> str:
        answer = self.getOptionValue2(option)
        return answer if answer is not None else defaultValue

    def getOptionValue2(self, option: Option) -> str:
        if option is None:
            return None
        values = self.getOptionValues1(option)

        return values[0] if values is not None else None

    def getOptionValue1(self, opt: str, defaultValue: str) -> str:
        return self.getOptionValue5(opt, defaultValue)

    def getOptionValue0(self, opt: str) -> str:
        return self.getOptionValue4(opt)

    def getOptions(self) -> typing.List[Option]:
        return self.__options

    def getOptionProperties1(
        self, opt: str
    ) -> typing.Dict:

        props = dict()

        for option in self.__options:
            if opt == option.getOpt() or opt == option.getLongOpt():
                values = option.getValuesList()
                if len(values) >= 2:
                    props[values[0]] = values[1]
                elif len(values) == 1:
                    props[values[0]] = "true"

        return props

    def getOptionProperties0(
        self, option: Option
    ) -> typing.Dict:
        props = dict()

        for processedOption in self.__options:
            if processedOption.equals(option):
                values = processedOption.getValuesList()
                if len(values) >= 2:
                    props[values[0]] = values[1]
                elif len(values) == 1:
                    props[values[0]] = "true"

        return props

    def getArgs(self) -> typing.List[typing.List[str]]:
        return self.__args

    def getArgList(self) -> typing.List[str]:
        return self.__args

    def _addOption(self, opt: Option) -> None:
        self.__options.append(opt)

    def _addArg(self, arg: str) -> None:
        self.__args.append(arg)

    def __init__(self) -> None:
        self.__options: typing.List[Option] = []
        self.__args: typing.List[str] = []

    def __resolveOption(self, opt: str) -> Option:

        opt = Util.stripLeadingHyphens(opt)
        for option in self.__options:
            if opt == option.getOpt() or opt == option.getLongOpt():
                return option
        return None


Builder.initialize_fields()
