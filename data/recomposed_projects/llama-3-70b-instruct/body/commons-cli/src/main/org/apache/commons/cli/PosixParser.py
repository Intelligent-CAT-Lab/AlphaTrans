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
        self, options: Options, arguments: typing.List[str], stopAtNonOption: bool
    ) -> typing.List[str]:

        pass  # LLM could not translate this method

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
                self.__tokens.append(token[i + 1])

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

    def __gobble(self, iter: typing.Iterator[str]) -> None:
        if self.__eatTheRest:
            while iter.hasNext():
                self.__tokens.append(iter.next())
