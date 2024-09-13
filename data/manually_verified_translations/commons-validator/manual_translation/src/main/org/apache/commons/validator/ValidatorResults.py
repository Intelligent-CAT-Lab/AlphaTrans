from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.Field import *
from src.main.org.apache.commons.validator.ValidatorResult import *


class ValidatorResults:

    _hResults: typing.Dict[str, ValidatorResult] = {}

    __serialVersionUID: int = -2709911078904924839

    def getResultValueMap(self) -> typing.Dict[str, typing.Any]:
        results = {}

        for propertyKey in self._hResults.keys():
            vr = self.getValidatorResult(propertyKey)

            for actionKey in vr.getActions():
                result = vr.getResult(actionKey)

                if result is not None and not isinstance(result, bool):
                    results[propertyKey] = result

        return results

    def getPropertyNames(self) -> typing.Set[str]:
        return typing.Set(self._hResults.keys())

    def getValidatorResult(self, key: str) -> ValidatorResult:
        return self._hResults.get(key)

    def isEmpty(self) -> bool:
        return not bool(self._hResults)

    def clear(self) -> None:
        self._hResults.clear()

    def add1(
        self, field: typing.Any, validatorName: str, result: bool, value: typing.Any
    ) -> None:
        validatorResult = self.getValidatorResult(field.getKey())

        if validatorResult is None:
            validatorResult = ValidatorResult(field)
            self._hResults[field.getKey()] = validatorResult

        validatorResult.add1(validatorName, result, value)

    def add0(self, field: typing.Any, validatorName: str, result: bool) -> None:
        self.add1(field, validatorName, result, None)

    def merge(self, results: ValidatorResults) -> None:
        self._hResults.update(results._hResults)
