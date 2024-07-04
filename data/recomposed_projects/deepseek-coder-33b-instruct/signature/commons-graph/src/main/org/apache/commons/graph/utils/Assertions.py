from __future__ import annotations
import re
import io
import typing
from typing import *


class Assertions:

    @staticmethod
    def checkState(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        if not expression:
            raise RuntimeError(errorMessageTemplate % errorMessageArgs)

    @staticmethod
    def checkNotNull(
        reference: typing.Any,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> typing.Any:

        if reference is None:
            raise NullPointerException(errorMessageTemplate % errorMessageArgs)
        return reference

    @staticmethod
    def checkArgument(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        if not expression:
            raise ValueError(errorMessageTemplate % errorMessageArgs)

    def __init__(self) -> None:
        pass
