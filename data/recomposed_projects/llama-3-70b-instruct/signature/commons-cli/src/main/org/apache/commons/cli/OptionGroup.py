from __future__ import annotations
import re
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
        buff = StringBuilder()

        iter = getOptions().iterator()

        buff.append("[")

        while iter.hasNext():
            option = iter.next()

            if option.getOpt() != None:
                buff.append("-")
                buff.append(option.getOpt())
            else:
                buff.append("--")
                buff.append(option.getLongOpt())

            if option.getDescription() != None:
                buff.append(" ")
                buff.append(option.getDescription())

            if iter.hasNext():
                buff.append(", ")

        buff.append("]")

        return buff.toString()

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
