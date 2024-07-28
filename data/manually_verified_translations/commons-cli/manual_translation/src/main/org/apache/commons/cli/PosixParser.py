from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.cli.AmbiguousOptionException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Util import *


class PosixParser(Parser):

    __options: Options = None

    __currentOption: Option = None

    __eatTheRest: bool = False

    __tokens: typing.List[str] = []

    def _flatten(
        self,
        options: Options,
        arguments: typing.List[typing.List[str]],
        stopAtNonOption: bool,
    ) -> typing.List[typing.List[str]]:

        self.__init()
        self.__options = options

        iter_ = iter(arguments)

        while True:
            try:
                token = next(iter_)
            except StopIteration:
                break

            if token == "-" or token == "--":
                self.__tokens.append(token)
            elif token.startswith("--"):
                pos = token.find("=")
                opt = token if pos == -1 else token[:pos]

                matchingOpts = options.getMatchingOptions(opt)

                if not matchingOpts:
                    self.__processNonOptionToken(token, stopAtNonOption)
                elif len(matchingOpts) > 1:
                    raise AmbiguousOptionException(opt, matchingOpts)
                else:
                    self.__currentOption = options.getOption(matchingOpts[0])

                    self.__tokens.append("--" + self.__currentOption.getLongOpt())
                    if pos != -1:
                        self.__tokens.append(token[pos + 1 :])
            elif token.startswith("-"):
                if len(token) == 2 or options.hasOption(token):
                    self.__processOptionToken(token, stopAtNonOption)
                elif options.getMatchingOptions(token):
                    matchingOpts = options.getMatchingOptions(token)
                    if len(matchingOpts) > 1:
                        raise AmbiguousOptionException(token, matchingOpts)
                    opt = options.getOption(matchingOpts[0])
                    self.__processOptionToken("-" + opt.getLongOpt(), stopAtNonOption)
                else:
                    self._burstToken(token, stopAtNonOption)
            else:
                self.__processNonOptionToken(token, stopAtNonOption)

            self.__gobble(iter_)

        return self.__tokens

    def _burstToken(self, token: str, stopAtNonOption: bool) -> None:

        for i in range(1, len(token)):
            ch = token[i]

            if not self.__options.hasOption(ch):
                if stopAtNonOption:
                    self.__processNonOptionToken(token[i:], True)
                else:
                    self.__tokens.append(token)
                break
            self.__tokens.append("-" + ch)
            self.__currentOption = self.__options.getOption(ch)

            if self.__currentOption.hasArg() and len(token) != i + 1:
                self.__tokens.append(token[i + 1 :])

                break

    def __processOptionToken(self, token: str, stopAtNonOption: bool) -> None:

        if stopAtNonOption and not self.__options.hasOption(token):
            self.__eatTheRest = True

        if self.__options.hasOption(token):
            self.__currentOption = self.__options.getOption(token)

        self.__tokens.append(token)

    def __processNonOptionToken(self, value: str, stopAtNonOption: bool) -> None:

        if stopAtNonOption and (
            self.__currentOption is None or not self.__currentOption.hasArg()
        ):
            self.__eatTheRest = True
            self.__tokens.append("--")

        self.__tokens.append(value)

    def __init(self) -> None:
        self.__eatTheRest = False
        self.__tokens.clear()

    def __gobble(self, iter_: typing.Iterator[str]) -> None:
        if self.__eatTheRest:
            while True:
                try:
                    self.__tokens.append(next(iter_))
                except StopIteration:
                    break
