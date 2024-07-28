from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.cli.AlreadySelectedException import *
from src.main.org.apache.commons.cli.Option import *


class OptionGroup:

    __required: bool = False

    __selected: str = ""

    __optionMap: typing.Dict[str, Option] = {}

    __serialVersionUID: int = 1

    def toString(self) -> str:

        buff = io.StringIO()

        iter = iter(self.getOptions())

        buff.write("[")

        while True:
            try:
                option = next(iter)
            except StopIteration:
                break

            if option.getOpt() is not None:
                buff.write("-")
                buff.write(option.getOpt())
            else:
                buff.write("--")
                buff.write(option.getLongOpt())

            if option.getDescription() is not None:
                buff.write(" ")
                buff.write(option.getDescription())

            try:
                next(iter)
            except StopIteration:
                break
            else:
                buff.write(", ")

        buff.write("]")

        return buff.getvalue()

    def setSelected(self, option: Option) -> None:
        if option is None:
            self.__selected = None
            return

        if self.__selected is not None and self.__selected != option.getKey():
            raise AlreadySelectedException.AlreadySelectedException1(self, option)
        self.__selected = option.getKey()

    def setRequired(self, required: bool) -> None:
        self.__required = required

    def isRequired(self) -> bool:
        return self.__required

    def getSelected(self) -> str:
        return self.__selected

    def getOptions(self) -> typing.Collection[Option]:
        return self.__optionMap.values()

    def getNames(self) -> typing.Collection[str]:
        return self.__optionMap.keys()

    def addOption(self, option: Option) -> OptionGroup:
        self.__optionMap[option.getKey()] = option
        return self
