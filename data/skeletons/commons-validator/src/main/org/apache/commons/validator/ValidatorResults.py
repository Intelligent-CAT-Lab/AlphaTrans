from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.ValidatorResult import *
from src.main.org.apache.commons.validator.Field import *
import typing
from typing import *
import io

# Imports End


class ValidatorResults:

    # Class Fields Begin
    __serialVersionUID: int = None
    _hResults: typing.Dict[str, ValidatorResult] = None
    # Class Fields End

    # Class Methods Begin
    def getResultValueMap(self) -> typing.Dict[str, typing.Any]:
        pass

    def getPropertyNames(self) -> typing.Set[str]:
        pass

    def getValidatorResult(self, key: str) -> ValidatorResult:
        pass

    def isEmpty(self) -> bool:
        pass

    def clear(self) -> None:
        pass

    def add1(
        self, field: typing.Any, validatorName: str, result: bool, value: typing.Any
    ) -> None:
        pass

    def add0(self, field: typing.Any, validatorName: str, result: bool) -> None:
        pass

    def merge(self, results: ValidatorResults) -> None:
        pass

    # Class Methods End
