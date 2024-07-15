from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.launcher.CommandLauncherImpl import *
from src.main.org.apache.commons.exec.launcher.CommandLauncher import *
from src.main.org.apache.commons.exec.CommandLine import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class CommandLauncherProxy(CommandLauncherImpl, ABC):

    # Class Fields Begin
    __launcher: CommandLauncher = None
    # Class Fields End

    # Class Methods Begin
    def exec0(self, cmd: CommandLine, env: typing.Dict[str, str]) -> subprocess.Popen:
        pass

    def __init__(self, launcher: CommandLauncher) -> None:
        pass

    # Class Methods End
