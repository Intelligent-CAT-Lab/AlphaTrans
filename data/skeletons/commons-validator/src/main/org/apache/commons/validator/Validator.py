from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.ValidatorResources import *
import typing
from typing import *
import io

# Imports End


class Validator:

    # Class Fields Begin
    _classLoader: typing.Any = None
    _useContextClassLoader: bool = None
    _onlyReturnErrors: bool = None
    __serialVersionUID: int = None
    BEAN_PARAM: str = None
    VALIDATOR_ACTION_PARAM: str = None
    VALIDATOR_RESULTS_PARAM: str = None
    FORM_PARAM: str = None
    FIELD_PARAM: str = None
    VALIDATOR_PARAM: str = None
    LOCALE_PARAM: str = None
    _resources: ValidatorResources = None
    _formName: str = None
    _fieldName: str = None
    _parameters: typing.Dict[str, typing.Any] = None
    _page: int = None
    # Class Fields End

    # Class Methods Begin
    def setOnlyReturnErrors(self, onlyReturnErrors: bool) -> None:
        pass

    def getOnlyReturnErrors(self) -> bool:
        pass

    def setClassLoader(self, classLoader: typing.Any) -> None:
        pass

    def getClassLoader(self) -> typing.Any:
        pass

    def setUseContextClassLoader(self, use: bool) -> None:
        pass

    def getUseContextClassLoader(self) -> bool:
        pass

    def clear(self) -> None:
        pass

    def setPage(self, page: int) -> None:
        pass

    def getPage(self) -> int:
        pass

    def setFieldName(self, fieldName: str) -> None:
        pass

    def setFormName(self, formName: str) -> None:
        pass

    def getFormName(self) -> str:
        pass

    def getParameterValue(self, parameterClassName: str) -> typing.Any:
        pass

    def setParameter(self, parameterClassName: str, parameterValue: typing.Any) -> None:
        pass

    @staticmethod
    def Validator2(resources: ValidatorResources) -> Validator:
        pass

    def __init__(
        self,
        constructorId: int,
        resources: ValidatorResources,
        formName: str,
        fieldName: str,
    ) -> None:
        pass

    # Class Methods End
