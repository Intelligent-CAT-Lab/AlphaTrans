from __future__ import annotations
import time
import re
from abc import ABC
import io
import typing
from typing import *
import configparser
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *
from src.main.org.apache.commons.cli.Util import *


class BiDirectionalIterator:
    def __init__(self, collection):
        self.collection = collection
        self.pos = 0

    def __next__(self):
        return self.next()
    
    def next(self):
        try:
            result = self.collection[self.pos]
            self.pos += 1
        except IndexError:
            raise StopIteration
        return result

    def previous(self):
        self.pos -= 1
        if self.pos < 0:
            raise StopIteration
        return self.collection[self.pos]


class Parser(CommandLineParser, ABC):

    _cmd: CommandLine = None

    __requiredOptions: typing.List[typing.Any] = None

    __options: Options = None

    def _setOptions(self, options: Options) -> None:
        self.__options = options
        self.__requiredOptions = list(options.getRequiredOptions())

    def _processProperties(
        self, properties: typing.Union[configparser.ConfigParser, typing.Dict]
    ) -> None:

        if properties is None:
            return

        for option in properties:
            opt = self.__options.getOption(option)
            if opt is None:
                raise UnrecognizedOptionException(
                    "Default option wasn't defined", option
                )

            group = self.__options.getOptionGroup(opt)
            selected = group is not None and group.getSelected() is not None

            if not self._cmd.hasOption2(option) and not selected:
                value = properties[option]

                if opt.hasArg():
                    if opt.getValues() is None or len(opt.getValues()) == 0:
                        try:
                            opt.addValueForProcessing(value)
                        except RuntimeError:
                            pass
                elif not (
                    value.lower() == "yes" or value.lower() == "true" or value == "1"
                ):
                    continue

                self._cmd._addOption(opt)
                self.__updateRequiredOptions(opt)

    def _processOption(self, arg: str, iter_: typing.Iterator[str]) -> None:

        hasOption = self._getOptions().hasOption(arg)

        if not hasOption:
            raise UnrecognizedOptionException(
                "Unrecognized option: " + arg, arg
            )

        opt = self._getOptions().getOption(arg).clone()

        self.__updateRequiredOptions(opt)

        if opt.hasArg():
            self.processArgs(opt, iter_)

        self._cmd._addOption(opt)

    def processArgs(self, opt: Option, iter_: typing.Iterator[str]) -> None:
        while True:
            try:
                str_ = next(iter_)

                if self._getOptions().hasOption(str_) and str_.startswith("-"):
                    iter_.previous()
                    break

                try:
                    opt.addValueForProcessing(Util.stripLeadingAndTrailingQuotes(str_))
                except RuntimeError:
                    iter_.previous()
                    break
            except StopIteration:
                break

        if opt.getValues() is None and not opt.hasOptionalArg():
            raise MissingArgumentException.MissingArgumentException1(1, None, opt)

    def parse3(
        self,
        options: Options,
        arguments: typing.List[typing.List[str]],
        properties: typing.Union[configparser.ConfigParser, typing.Dict],
        stopAtNonOption: bool,
    ) -> CommandLine:

        for opt in options.helpOptions():
            opt.clearValues()

        for group in options.getOptionGroups():
            group.setSelected(None)

        self._setOptions(options)

        self._cmd = CommandLine()

        eatTheRest = False

        if arguments is None:
            arguments = []

        tokenList = self._flatten(options, arguments, stopAtNonOption)

        if tokenList is None:  # Add this line to handle the case when tokenList is None
            tokenList = []

        iterator = BiDirectionalIterator(tokenList)

        while True:
            try:
                t = next(iterator)

                if "--" == t:
                    eatTheRest = True
                elif "-" == t:
                    if stopAtNonOption:
                        eatTheRest = True
                    else:
                        self._cmd._addArg(t)
                elif t.startswith("-"):
                    if stopAtNonOption and not options.hasOption(t):
                        eatTheRest = True
                        self._cmd._addArg(t)
                    else:
                        self._processOption(t, iterator)
                else:
                    self._cmd._addArg(t)

                    if stopAtNonOption:
                        eatTheRest = True

                if eatTheRest:
                    while True:
                        try:
                            str = next(iterator)

                            if "--" != str:
                                self._cmd._addArg(str)
                        except StopIteration:
                            break
            except StopIteration:
                break

        self._processProperties(properties)
        self._checkRequiredOptions()

        return self._cmd

    def parse2(
        self,
        options: Options,
        arguments: typing.List[typing.List[str]],
        properties: typing.Union[configparser.ConfigParser, typing.Dict],
    ) -> CommandLine:

        return self.parse3(options, arguments, properties, False)

    def parse1(
        self,
        options: Options,
        arguments: typing.List[typing.List[str]],
        stopAtNonOption: bool,
    ) -> CommandLine:

        return self.parse3(options, arguments, None, stopAtNonOption)

    def parse0(
        self, options: Options, arguments: typing.List[typing.List[str]]
    ) -> CommandLine:
        return self.parse3(options, arguments, None, False)

    def _getRequiredOptions(self) -> typing.List[typing.Any]:
        return self.__requiredOptions

    def _getOptions(self) -> Options:
        return self.__options

    def _checkRequiredOptions(self) -> None:

        if len(self._getRequiredOptions()) != 0:
            raise MissingOptionException.MissingOptionException1(
                1, self._getRequiredOptions(), None
            )

    def __updateRequiredOptions(self, opt: Option) -> None:
        if opt.isRequired():
            self._getRequiredOptions().remove(opt.getKey())

        if self._getOptions().getOptionGroup(opt) is not None:
            group = self._getOptions().getOptionGroup(opt)

            if group.isRequired():
                self._getRequiredOptions().remove(group)

            group.setSelected(opt)

    def _flatten(
        self,
        opts: Options,
        arguments: typing.List[typing.List[str]],
        stopAtNonOption: bool,
    ) -> typing.List[typing.List[str]]:

        # Your implementation here
        pass
