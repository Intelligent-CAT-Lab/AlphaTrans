from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.io.Colors import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *
from src.main.org.fusesource.jansi.AnsiColors import *
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class ColorsAnsiProcessor(AnsiProcessor):

    # Class Fields Begin
    __colors: AnsiColors = None
    # Class Fields End

    # Class Methods Begin
    def _processCharsetSelect0(self, options: typing.List[typing.Any]) -> bool:
        pass

    def _processOperatingSystemCommand(self, options: typing.List[typing.Any]) -> bool:
        pass

    def _processEscapeCommand(
        self, options: typing.List[typing.Any], command: int
    ) -> bool:
        pass

    def __init__(
        self,
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        colors: AnsiColors,
    ) -> None:
        pass

    # Class Methods End
