from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.cli.Option import *


class OptionGroup:

    __required: bool = False

    __selected: str = ""

    __serialVersionUID: int = 1
    
    def __init__(self):
        self.__optionMap: typing.Dict[str, Option] = {}

    def __str__(self) -> str:
        return self.toString()

    def toString(self) -> str:

        buff = io.StringIO()

        iter_ = iter(self.getOptions())

        buff.write("[")

        while True:
            try:
                option = next(iter_)

                if option.getOpt() is not None:
                    buff.write("-")
                    buff.write(option.getOpt())
                else:
                    buff.write("--")
                    buff.write(option.getLongOpt())

                if option.getDescription() is not None:
                    buff.write(" ")
                    buff.write(option.getDescription())

                buff.write(", ")
            except StopIteration:
                buff.seek(buff.tell() - 2)
                buff.truncate()
                break

        buff.write("]")

        return buff.getvalue()

    def setSelected(self, option: Option) -> None:
        from src.main.org.apache.commons.cli.AlreadySelectedException import AlreadySelectedException
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
