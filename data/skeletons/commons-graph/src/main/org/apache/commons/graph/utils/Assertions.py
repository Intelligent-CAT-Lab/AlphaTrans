from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class Assertions:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def checkState(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        pass

    @staticmethod
    def checkNotNull(
        reference: typing.Any,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> typing.Any:
        pass

    @staticmethod
    def checkArgument(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
