from __future__ import annotations
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
            errorMessage = errorMessageTemplate.format(*errorMessageArgs)
            raise IllegalStateException(errorMessage)

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
            raise ValueError(errorMessageTemplate.format(*errorMessageArgs))

    def __init__(self) -> None:

        pass  # LLM could not translate this method
