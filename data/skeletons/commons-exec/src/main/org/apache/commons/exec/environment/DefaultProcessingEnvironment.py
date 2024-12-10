from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.OS import *
from src.main.org.apache.commons.exec.CommandLine import *
import typing
from typing import *
import io

# Imports End


class DefaultProcessingEnvironment:

    # Class Fields Begin
    _procEnvironment: typing.Dict[str, str] = None
    # Class Fields End

    # Class Methods Begin
    def _runProcEnvCommand(self) -> io.BufferedReader:
        pass

    def _getProcEnvCommand(self) -> CommandLine:
        pass

    def getProcEnvironment(self) -> typing.Dict[str, str]:
        pass

    def _createProcEnvironment(self) -> typing.Dict[str, str]:
        pass

    def __createEnvironmentMap(self) -> typing.Dict[str, str]:
        pass

    # Class Methods End
