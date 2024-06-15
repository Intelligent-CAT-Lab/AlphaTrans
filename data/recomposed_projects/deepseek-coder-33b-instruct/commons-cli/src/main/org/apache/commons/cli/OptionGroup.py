from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.cli.AlreadySelectedException import *
from src.main.org.apache.commons.cli.Option import *


class OptionGroup:

    __required: bool = None
    __selected: str = None

    __optionMap: Dict[str, Option] = {}

    __serialVersionUID: int = 1

    def toString(self) -> str:

        buff = io.StringIO()

        iter = self.getOptions().__iter__()

        buff.write("[")

        while iter.__next__():
            option = iter.__next__()

            if option.getOpt() != None:
                buff.write("-")
                buff.write(option.getOpt())
            else:
                buff.write("--")
                buff.write(option.getLongOpt())

            if option.getDescription() != None:
                buff.write(" ")
                buff.write(option.getDescription())

            if iter.__next__():
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
