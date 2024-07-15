from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.ValidatorException import *
from src.main.org.apache.commons.validator.Validator import *

# from src.main.org.apache.commons.logging.LogFactory import *
# from src.main.org.apache.commons.logging.Log import *
import logging
import typing
from typing import *
import io

# Imports End


class ValidatorAction:

    # Class Fields Begin
    __jsFunction: str = None
    __javascript: str = None
    __instance: typing.Any = None
    __dependencyList: typing.List[str] = None
    __methodParameterList: typing.List[str] = None
    __serialVersionUID: int = None
    __log: logging.Logger = None
    __name: str = None
    __classname: str = None
    __validationClass: typing.Type[typing.Any] = None
    __method: str = None
    __validationMethod: typing.Union[inspect.Signature, typing.Callable] = None
    __methodParams: str = None
    __parameterClasses: typing.List[typing.Type[typing.Any]] = None
    __depends: str = None
    __msg: str = None
    __jsFunctionName: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def getDependencyList(self) -> typing.List[str]:
        pass

    def isDependency(self, validatorName: str) -> bool:
        pass

    def _loadJavascriptFunction(self) -> None:
        pass

    def _init(self) -> None:
        pass

    def setJavascript(self, javascript: str) -> None:
        pass

    def getJavascript(self) -> str:
        pass

    def setJsFunction(self, jsFunction: str) -> None:
        pass

    def setJsFunctionName(self, jsFunctionName: str) -> None:
        pass

    def getJsFunctionName(self) -> str:
        pass

    def setMsg(self, msg: str) -> None:
        pass

    def getMsg(self) -> str:
        pass

    def setDepends(self, depends: str) -> None:
        pass

    def getDepends(self) -> str:
        pass

    def setMethodParams(self, methodParams: str) -> None:
        pass

    def getMethodParams(self) -> str:
        pass

    def setMethod(self, method: str) -> None:
        pass

    def getMethod(self) -> str:
        pass

    def setClassname(self, classname: str) -> None:
        pass

    def getClassname(self) -> str:
        pass

    def setName(self, name: str) -> None:
        pass

    def getName(self) -> str:
        pass

    def __getLog(self) -> logging.Logger:
        pass

    def __onlyReturnErrors(self, params: typing.Dict[str, typing.Any]) -> bool:
        pass

    def __getClassLoader(self, params: typing.Dict[str, typing.Any]) -> typing.Any:
        pass

    def __isValid(self, result: typing.Any) -> bool:
        pass

    def __getValidationClassInstance(self) -> typing.Any:
        pass

    def __getParameterValues(
        self, params: typing.Dict[str, typing.Any]
    ) -> typing.List[typing.Any]:
        pass

    def __loadParameterClasses(self, loader: typing.Any) -> None:
        pass

    def __loadValidationClass(self, loader: typing.Any) -> None:
        pass

    def __loadValidationMethod(self) -> None:
        pass

    def __generateJsFunction(self) -> str:
        pass

    def __javascriptAlreadyLoaded(self) -> bool:
        pass

    def __formatJavascriptFileName(self) -> str:
        pass

    def __readJavascriptFile(self, javascriptFileName: str) -> str:
        pass

    # Class Methods End
