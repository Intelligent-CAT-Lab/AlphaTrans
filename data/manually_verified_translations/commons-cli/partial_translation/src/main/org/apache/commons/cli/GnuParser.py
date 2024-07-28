from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Util import *


class GnuParser(Parser):

    def _flatten(
        self,
        options: Options,
        arguments: typing.List[typing.List[str]],
        stopAtNonOption: bool,
    ) -> typing.List[typing.List[str]]:

        tokens: List[str] = []

        eatTheRest: bool = False

        for i in range(len(arguments)):
            arg: str = arguments[i]

            if arg == "--":
                eatTheRest = True
                tokens.append("--")
            elif arg == "-":
                tokens.append("-")
            elif arg.startswith("-"):
                opt: str = Util.stripLeadingHyphens(arg)

                if options.hasOption(opt):
                    tokens.append(arg)
                elif "=" in opt and options.hasOption(opt.split("=")[0]):
                    tokens.append(opt.split("=")[0])
                    tokens.append(opt.split("=")[1])
                elif len(arg) > 2 and options.hasOption(arg[:2]):
                    tokens.append(arg[:2])
                    tokens.append(arg[2:])
                else:
                    eatTheRest = stopAtNonOption
                    tokens.append(arg)
            else:
                tokens.append(arg)

            if eatTheRest:
                for j in range(i + 1, len(arguments)):
                    tokens.append(arguments[j])

        return tokens
