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

        for i in range(0, len(arguments)):
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
                elif opt.find("=") != -1 and options.hasOption(opt[0 : opt.find("=")]):
                    tokens.append(arg[0 : arg.find("=")])  # --foo
                    tokens.append(arg[arg.find("=") + 1 :])  # value
                elif options.hasOption(arg[0:2]):
                    tokens.append(arg[0:2])  # -D
                    tokens.append(arg[2:])  # property=value
                else:
                    eatTheRest = stopAtNonOption
                    tokens.append(arg)

            else:
                tokens.append(arg)

            if eatTheRest:
                for i in range(i + 1, len(arguments)):
                    tokens.append(arguments[i])

        return tokens
