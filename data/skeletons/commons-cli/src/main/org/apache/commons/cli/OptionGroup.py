from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.AlreadySelectedException import *
import typing
from typing import *
import io

# Imports End


class OptionGroup:

    # Class Fields Begin
    __serialVersionUID: int = None
    __optionMap: typing.Dict[str, Option] = None
    __selected: str = None
    __required: bool = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def setSelected(self, option: Option) -> None:
        pass

    def setRequired(self, required: bool) -> None:
        pass

    def isRequired(self) -> bool:
        pass

    def getSelected(self) -> str:
        pass

    def getOptions(self) -> typing.Collection[Option]:
        pass

    def getNames(self) -> typing.Collection[str]:
        pass

    def addOption(self, option: Option) -> OptionGroup:
        pass

    # Class Methods End
