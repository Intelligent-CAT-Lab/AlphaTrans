from __future__ import annotations
import inspect
import re
import io
import typing
from typing import *
import logging

# from src.main.org.apache.commons.logging.Log import *
# from src.main.org.apache.commons.logging.LogFactory import *
from src.main.org.apache.commons.validator.Validator import *
from src.main.org.apache.commons.validator.ValidatorException import *


class ValidatorAction:

    __methodParameterList: typing.List[str] = []

    __dependencyList: typing.List[str] = []

    __instance: typing.Any = None
    __javascript: str = None
    __jsFunction: str = None
    __jsFunctionName: str = None
    __msg: str = None
    __depends: str = None
    __parameterClasses: typing.List[typing.Type[typing.Any]] = []
    __methodParams: str = (
        Validator.BEAN_PARAM
        + ","
        + Validator.VALIDATOR_ACTION_PARAM
        + ","
        + Validator.FIELD_PARAM
    )
    __validationMethod: typing.Union[inspect.Signature, typing.Callable] = None
    __method: str = ""
    __validationClass: typing.Type[typing.Any] = None
    __classname: str = None
    __name: str = ""
    __log: logging.Logger = None
    __serialVersionUID: int = 1339713700053204597

    @staticmethod
    def initialize_fields() -> None:
        ValidatorAction.__log: logging.Logger = logging.getLogger(
            ValidatorAction.__class__
        )

    def toString(self) -> str:
        results = StringBuilder("ValidatorAction: ")
        results.append(self.__name)
        results.append("\n")
        return results.toString()

    def getDependencyList(self) -> typing.List[str]:
        return self.__dependencyList

    def isDependency(self, validatorName: str) -> bool:
        return validatorName in self.__dependencyList

    def _loadJavascriptFunction(self) -> None:
        if self.__javascriptAlreadyLoaded():
            return
        if self.__getLog().isTraceEnabled():
            self.__getLog().trace("  Loading function begun")
        if self.__jsFunction is None:
            self.__jsFunction = self.__generateJsFunction()
        javascriptFileName = self.__formatJavascriptFileName()
        if self.__getLog().isTraceEnabled():
            self.__getLog().trace("  Loading js function '" + javascriptFileName + "'")
        self.__javascript = self.__readJavascriptFile(javascriptFileName)
        if self.__getLog().isTraceEnabled():
            self.__getLog().trace("  Loading javascript function completed")

    def _init(self) -> None:
        self._loadJavascriptFunction()

    def setJavascript(self, javascript: str) -> None:

        pass  # LLM could not translate this method

    def getJavascript(self) -> str:
        return self.__javascript

    def setJsFunction(self, jsFunction: str) -> None:

        pass  # LLM could not translate this method

    def setJsFunctionName(self, jsFunctionName: str) -> None:
        self.__jsFunctionName = jsFunctionName

    def getJsFunctionName(self) -> str:
        return self.__jsFunctionName

    def setMsg(self, msg: str) -> None:
        self.__msg = msg

    def getMsg(self) -> str:
        return self.__msg

    def setDepends(self, depends: str) -> None:
        self.__depends = depends

        self.__dependencyList.clear()

        st = StringTokenizer(depends, ",")
        while st.hasMoreTokens():
            depend = st.nextToken().trim()

            if depend != None and depend.length() > 0:
                self.__dependencyList.add(depend)

    def getDepends(self) -> str:
        return self.__depends

    def setMethodParams(self, methodParams: str) -> None:
        self.__methodParams = methodParams

        self.__methodParameterList.clear()

        st = StringTokenizer(methodParams, ",")
        while st.hasMoreTokens():
            value = st.nextToken().trim()

            if value != None and value.length() > 0:
                self.__methodParameterList.add(value)

    def getMethodParams(self) -> str:
        return self.__methodParams

    def setMethod(self, method: str) -> None:
        self.__method = method

    def getMethod(self) -> str:
        return self.__method

    def setClassname(self, classname: str) -> None:
        self.__classname = classname

    def getClassname(self) -> str:
        return self.__classname

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def __getLog(self) -> logging.Logger:
        if self.__log is None:
            self.__log = logging.getLogger(ValidatorAction.__class__)
        return self.__log

    def __onlyReturnErrors(self, params: typing.Dict[str, typing.Any]) -> bool:
        v: Validator = params.get(Validator.VALIDATOR_PARAM)
        return v.getOnlyReturnErrors()

    def __getClassLoader(self, params: typing.Dict[str, typing.Any]) -> typing.Any:
        v: Validator = params.get(Validator.VALIDATOR_PARAM)
        return v.getClassLoader()

    def __isValid(self, result: typing.Any) -> bool:
        if isinstance(result, bool):
            valid: bool = result
            return valid
        return result is not None

    def __getValidationClassInstance(self) -> typing.Any:
        if inspect.isfunction(self.__validationMethod):
            self.__instance = None
        else:
            if self.__instance is None:
                try:
                    self.__instance = self.__validationClass()
                except Exception as e:
                    msg1 = f"Couldn't create instance of {self.__classname}.  {e}"
                    raise ValidatorException(msg1)
        return self.__instance

    def __getParameterValues(
        self, params: typing.Dict[str, typing.Any]
    ) -> typing.List[typing.Any]:
        paramValue = [None] * len(self.__methodParameterList)
        for i in range(len(self.__methodParameterList)):
            paramClassName = self.__methodParameterList[i]
            paramValue[i] = params.get(paramClassName)
        return paramValue

    def __loadParameterClasses(self, loader: typing.Any) -> None:
        if self.__parameterClasses != None:
            return
        parameterClasses = [None] * len(self.__methodParameterList)
        for i in range(len(self.__methodParameterList)):
            paramClassName = self.__methodParameterList[i]
            try:
                parameterClasses[i] = loader.loadClass(paramClassName)
            except ClassNotFoundException as e:
                raise ValidatorException(e.getMessage())
        self.__parameterClasses = parameterClasses

    def __loadValidationClass(self, loader: typing.Any) -> None:
        if self.__validationClass is not None:
            return
        try:
            self.__validationClass = loader.loadClass(self.__classname)
        except ClassNotFoundException as e:
            raise ValidatorException(e.toString())

    def __loadValidationMethod(self) -> None:
        if self.__validationMethod is not None:
            return

        try:
            self.__validationMethod = self.__validationClass.getMethod(
                self.__method, self.__parameterClasses
            )
        except NoSuchMethodException as e:
            raise ValidatorException("No such validation method: " + e.getMessage())

    def __generateJsFunction(self) -> str:
        jsName = "org.apache.commons.validator.javascript"
        jsName += ".validate"
        jsName += self.__name[0].upper()
        jsName += self.__name[1:]
        return jsName

    def __javascriptAlreadyLoaded(self) -> bool:
        return self.__javascript != None

    def __formatJavascriptFileName(self) -> str:
        fname: str = self.__jsFunction[1:]

        if not self.__jsFunction.startswith("/"):
            fname = self.__jsFunction.replace(".", "/") + ".js"

        return fname

    def __readJavascriptFile(self, javascriptFileName: str) -> str:

        pass  # LLM could not translate this method


ValidatorAction.initialize_fields()
