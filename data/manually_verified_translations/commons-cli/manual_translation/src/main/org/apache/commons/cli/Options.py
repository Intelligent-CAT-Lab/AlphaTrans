from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Util import *


class Options:

    __serialVersionUID: int = 1
    
    def __init__(self):
        self.__optionGroups: typing.Dict[str, OptionGroup] = {}
        self.__requiredOpts: typing.List[typing.Any] = []
        self.__longOpts: typing.Dict[str, Option] = {}
        self.__shortOpts: typing.Dict[str, Option] = {}

    def __str__(self) -> str:
        return self.toString()

    def toString(self) -> str:

        buf = io.StringIO()

        buf.write("[ Options: [ short ")
        buf.write(str(self.__shortOpts))
        buf.write(" ] [ long ")
        buf.write(str(self.__longOpts))
        buf.write(" ]")

        return buf.getvalue()

    def hasShortOption(self, opt: str) -> bool:

        opt = Util.stripLeadingHyphens(opt)

        return opt in self.__shortOpts.keys()

    def hasOption(self, opt: str) -> bool:

        opt = Util.stripLeadingHyphens(opt)

        return opt in self.__shortOpts or opt in self.__longOpts

    def hasLongOption(self, opt: str) -> bool:

        opt = Util.stripLeadingHyphens(opt)

        return opt in self.__longOpts

    def getRequiredOptions(self) -> typing.List[typing.Any]:
        return self.__requiredOpts

    def getOptions(self) -> typing.Collection[Option]:
        return self.helpOptions()

    def getOptionGroup(self, opt: Option) -> OptionGroup:
        return self.__optionGroups.get(opt.getKey())

    def getOption(self, opt: str) -> Option:

        opt = Util.stripLeadingHyphens(opt)

        if opt in self.__shortOpts:
            return self.__shortOpts[opt]

        if opt in self.__longOpts:
            return self.__longOpts[opt]

        return None

    def getMatchingOptions(self, opt: str) -> typing.List[str]:

        opt = Util.stripLeadingHyphens(opt)

        matchingOpts: List[str] = []

        if opt in self.__longOpts:
            return [opt]

        for longOpt in self.__longOpts.keys():
            if longOpt.startswith(opt):
                matchingOpts.append(longOpt)

        return matchingOpts

    def addRequiredOption(
        self, opt: str, longOpt: str, hasArg: bool, description: str
    ) -> Options:

        option = Option(0, opt, longOpt, description, hasArg, None)
        option.setRequired(True)
        self.addOption0(option)

        return self

    def addOptionGroup(self, group: OptionGroup) -> Options:

        if group.isRequired():
            self.__requiredOpts.append(group)

        for option in group.getOptions():
            option.setRequired(False)
            self.addOption0(option)

            self.__optionGroups[option.getKey()] = group

        return self

    def addOption3(
        self, opt: str, longOpt: str, hasArg: bool, description: str
    ) -> Options:

        self.addOption0(Option(0, opt, longOpt, description, hasArg, None))
        return self

    def addOption2(self, opt: str, description: str) -> Options:

        self.addOption3(opt, None, False, description)
        return self

    def addOption1(self, opt: str, hasArg: bool, description: str) -> Options:

        self.addOption3(opt, None, hasArg, description)
        return self

    def addOption0(self, opt: Option) -> Options:

        key = opt.getKey()

        if opt.hasLongOpt():
            self.__longOpts[opt.getLongOpt()] = opt

        if opt.isRequired():
            if key in self.__requiredOpts:
                self.__requiredOpts.remove(key)
            self.__requiredOpts.append(key)

        self.__shortOpts[key] = opt

        return self

    def helpOptions(self) -> typing.List[Option]:
        return list(self.__shortOpts.values())

    def getOptionGroups(self) -> typing.Collection[OptionGroup]:
        return set(self.__optionGroups.values())
