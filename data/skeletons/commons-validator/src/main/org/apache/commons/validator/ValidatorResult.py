from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.Field import *
import typing
from typing import *
import io

# Imports End


class ResultStatus:

    # Class Fields Begin
    __serialVersionUID: int = None
    __valid: bool = None
    __result: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def isValid(self) -> bool:
        pass

    def setResult(self, result: typing.Any) -> None:
        pass

    def getResult(self) -> typing.Any:
        pass

    def setValid(self, valid: bool) -> None:
        pass

    @staticmethod
    def ResultStatus0(
        ignored: ValidatorResult, valid: bool, result: typing.Any
    ) -> ResultStatus:
        pass

    def __init__(
        self,
        constructorId: int,
        result: typing.Any,
        ignored: ValidatorResult,
        valid: bool,
    ) -> None:
        pass

    # Class Methods End


class ValidatorResult:

    # Class Fields Begin
    __serialVersionUID: int = None
    _hAction: typing.Dict[str, ResultStatus] = None
    _field: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def getActionMap(self) -> typing.Dict[str, ResultStatus]:
        pass

    def getField(self) -> typing.Any:
        pass

    def getActions(self) -> typing.Iterator[str]:
        pass

    def getResult(self, validatorName: str) -> typing.Any:
        pass

    def isValid(self, validatorName: str) -> bool:
        pass

    def containsAction(self, validatorName: str) -> bool:
        pass

    def add1(self, validatorName: str, result: bool, value: typing.Any) -> None:
        pass

    def add0(self, validatorName: str, result: bool) -> None:
        pass

    def __init__(self, field: typing.Any) -> None:
        pass

    # Class Methods End
