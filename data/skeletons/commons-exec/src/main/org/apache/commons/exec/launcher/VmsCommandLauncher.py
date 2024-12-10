from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.util.StringUtils import *
from src.main.org.apache.commons.exec.launcher.Java13CommandLauncher import *
from src.main.org.apache.commons.exec.CommandLine import *
import typing
from typing import *
import io
import pathlib

# Imports End


class VmsCommandLauncher(Java13CommandLauncher):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def isFailure(self, exitValue: int) -> bool:
        pass

    def exec1(
        self, cmd: CommandLine, env: typing.Dict[str, str], workingDir: pathlib.Path
    ) -> subprocess.Popen:
        pass

    def exec0(self, cmd: CommandLine, env: typing.Dict[str, str]) -> subprocess.Popen:
        pass

    def __createCommandFile(
        self, cmd: CommandLine, env: typing.Dict[str, str]
    ) -> pathlib.Path:
        pass

    # Class Methods End
