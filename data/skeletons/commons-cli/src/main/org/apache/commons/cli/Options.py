from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Util import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Option import *
import typing
from typing import *
import io

# Imports End


class Options:

    # Class Fields Begin
    __serialVersionUID: int = None
    __shortOpts: typing.Dict[str, Option] = None
    __longOpts: typing.Dict[str, Option] = None
    __requiredOpts: typing.List[typing.Any] = None
    __optionGroups: typing.Dict[str, OptionGroup] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hasShortOption(self, opt: str) -> bool:
        pass

    def hasOption(self, opt: str) -> bool:
        pass

    def hasLongOption(self, opt: str) -> bool:
        pass

    def getRequiredOptions(self) -> typing.List[typing.Any]:
        pass

    def getOptions(self) -> typing.Collection[Option]:
        pass

    def getOptionGroup(self, opt: Option) -> OptionGroup:
        pass

    def getOption(self, opt: str) -> Option:
        pass

    def getMatchingOptions(self, opt: str) -> typing.List[str]:
        pass

    def addRequiredOption(
        self, opt: str, longOpt: str, hasArg: bool, description: str
    ) -> Options:
        pass

    def addOptionGroup(self, group: OptionGroup) -> Options:
        pass

    def addOption3(
        self, opt: str, longOpt: str, hasArg: bool, description: str
    ) -> Options:
        pass

    def addOption2(self, opt: str, description: str) -> Options:
        pass

    def addOption1(self, opt: str, hasArg: bool, description: str) -> Options:
        pass

    def addOption0(self, opt: Option) -> Options:
        pass

    def helpOptions(self) -> typing.List[Option]:
        pass

    def getOptionGroups(self) -> typing.Collection[OptionGroup]:
        pass

    # Class Methods End
