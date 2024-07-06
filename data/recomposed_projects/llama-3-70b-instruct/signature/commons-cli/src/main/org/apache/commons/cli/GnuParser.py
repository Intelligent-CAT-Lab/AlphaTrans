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
        self, options: Options, arguments: typing.List[str], stopAtNonOption: bool
    ) -> typing.List[str]:
        tokens: typing.List[str] = []
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
                elif opt.find("=") != -1 and options.hasOption(opt[: opt.find("=")]):
                    tokens.append(arg[: arg.find("=")])
                    tokens.append(arg[arg.find("=") + 1 :])
                elif options.hasOption(arg[:2]):
                    tokens.append(arg[:2])
                    tokens.append(arg[2:])
                else:
                    eatTheRest = stopAtNonOption
                    tokens.append(arg)
            else:
                tokens.append(arg)
            if eatTheRest:
                for i in range(i + 1, len(arguments)):
                    tokens.append(arguments[i])
        return tokens
