from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *


class CommandLineParser(ABC):

    def parse1(
        self, options: Options, arguments: typing.List[str], stopAtNonOption: bool
    ) -> CommandLine:
        return CommandLine(options, arguments, stopAtNonOption)

    def parse0(self, options: Options, arguments: typing.List[str]) -> CommandLine:
        return CommandLine(options, arguments)
