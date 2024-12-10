from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.environment.DefaultProcessingEnvironment import *
import typing
from typing import *
import io

# Imports End


class EnvironmentUtils:

    # Class Fields Begin
    __ENVIRONMENT: DefaultProcessingEnvironment = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def toStrings(environment: typing.Dict[str, str]) -> typing.List[typing.List[str]]:
        pass

    @staticmethod
    def getProcEnvironment() -> typing.Dict[str, str]:
        pass

    @staticmethod
    def addVariableToEnvironment(
        environment: typing.Dict[str, str], keyAndValue: str
    ) -> None:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def __toString(value: str) -> str:
        pass

    @staticmethod
    def __parseEnvironmentVariable(keyAndValue: str) -> typing.List[typing.List[str]]:
        pass

    # Class Methods End
