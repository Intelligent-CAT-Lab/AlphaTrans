from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.Field import *


class ResultStatus:

    __result: typing.Any = None
    __valid: bool = False
    __serialVersionUID: int = 4076665918535320007

    def isValid(self) -> bool:
        return self.__valid

    def setResult(self, result: typing.Any) -> None:
        self.__result = result

    def getResult(self) -> typing.Any:
        return self.__result

    def setValid(self, valid: bool) -> None:
        self.__valid = valid

    @staticmethod
    def ResultStatus0(
        ignored: ValidatorResult, valid: bool, result: typing.Any
    ) -> ResultStatus:
        return ResultStatus(1, result, None, valid)

    def __init__(
        self,
        constructorId: int,
        result: typing.Any,
        ignored: ValidatorResult,
        valid: bool,
    ) -> None:

        if constructorId == 1:
            self.__valid = valid
            self.__result = result
        else:
            self.__valid = valid
            self.__result = result


class ValidatorResult:

    _field: typing.Any = None
    _hAction: typing.Dict[str, ResultStatus] = {}

    __serialVersionUID: int = -3713364681647250531

    def getActionMap(self) -> typing.Dict[str, ResultStatus]:
        return typing.MappingProxyType(self._hAction)

    def getField(self) -> typing.Any:
        return self._field

    def getActions(self) -> typing.Iterator[str]:
        return iter(self._hAction.keys())

    def getResult(self, validatorName: str) -> typing.Any:
        status = self._hAction.get(validatorName)
        return None if status is None else status.getResult()

    def isValid(self, validatorName: str) -> bool:
        status = self._hAction.get(validatorName)
        return False if status is None else status.isValid()

    def containsAction(self, validatorName: str) -> bool:
        return validatorName in self._hAction

    def add1(self, validatorName: str, result: bool, value: typing.Any) -> None:
        self._hAction[validatorName] = ResultStatus(1, value, None, result)

    def add0(self, validatorName: str, result: bool) -> None:
        self.add1(validatorName, result, None)

    def __init__(self, field: typing.Any) -> None:
        self._field = field
