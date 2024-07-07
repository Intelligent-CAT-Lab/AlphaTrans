from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.ValidatorResources import *


class Validator:

    _onlyReturnErrors: bool = False
    _useContextClassLoader: bool = False
    _classLoader: typing.Any = None
    _page: int = 0
    _parameters: typing.Dict[str, typing.Any] = {}

    _fieldName: str = None
    _formName: str = None
    _resources: ValidatorResources = None
    LOCALE_PARAM: str = "java.util.Locale"
    VALIDATOR_PARAM: str = None
    FIELD_PARAM: str = "org.apache.commons.validator.Field"
    FORM_PARAM: str = "org.apache.commons.validator.Form"
    VALIDATOR_RESULTS_PARAM: str = None
    VALIDATOR_ACTION_PARAM: str = None
    BEAN_PARAM: str = "java.lang.Object"
    __serialVersionUID: int = -7119418755208731611

    @staticmethod
    def initialize_fields() -> None:
        Validator.VALIDATOR_PARAM: str = "org.apache.commons.validator.Validator"

        Validator.VALIDATOR_RESULTS_PARAM: str = (
            "org.apache.commons.validator.ValidatorResults"
        )

        Validator.VALIDATOR_ACTION_PARAM: str = (
            "org.apache.commons.validator.ValidatorAction"
        )

    def setOnlyReturnErrors(self, onlyReturnErrors: bool) -> None:
        self._onlyReturnErrors = onlyReturnErrors

    def getOnlyReturnErrors(self) -> bool:
        return self._onlyReturnErrors

    def setClassLoader(self, classLoader: typing.Any) -> None:
        self._classLoader = classLoader

    def getClassLoader(self) -> typing.Any:

        if self._classLoader is not None:
            return self._classLoader

        if self._useContextClassLoader:
            contextLoader = Thread.currentThread().getContextClassLoader()
            if contextLoader is not None:
                return contextLoader

        return self.__class__.getClassLoader()

    def setUseContextClassLoader(self, use: bool) -> None:
        self._useContextClassLoader = use

    def getUseContextClassLoader(self) -> bool:
        return self._useContextClassLoader

    def clear(self) -> None:
        self._formName = None
        self._fieldName = None
        self._parameters = {}
        self._page = 0

    def setPage(self, page: int) -> None:
        self._page = page

    def getPage(self) -> int:
        return self._page

    def setFieldName(self, fieldName: str) -> None:
        self._fieldName = fieldName

    def setFormName(self, formName: str) -> None:
        self._formName = formName

    def getFormName(self) -> str:
        return self._formName

    def getParameterValue(self, parameterClassName: str) -> typing.Any:
        return self._parameters.get(parameterClassName)

    def setParameter(self, parameterClassName: str, parameterValue: typing.Any) -> None:
        self._parameters[parameterClassName] = parameterValue

    @staticmethod
    def Validator2(resources: ValidatorResources) -> Validator:
        return Validator(1, resources, None, None)

    def __init__(
        self,
        constructorId: int,
        resources: ValidatorResources,
        formName: str,
        fieldName: str,
    ) -> None:

        if constructorId == 0:
            if resources is None:
                raise ValueError("Resources cannot be null.")
            self._resources = resources
            self._formName = formName
            self._fieldName = fieldName
        else:
            if resources is None:
                raise ValueError("Resources cannot be null.")
            self._resources = resources
            self._formName = formName


Validator.initialize_fields()
