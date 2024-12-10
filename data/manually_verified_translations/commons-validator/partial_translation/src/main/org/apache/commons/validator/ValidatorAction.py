from __future__ import annotations
import time
import inspect
import re
import os
from io import StringIO
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
    __parameterClasses: typing.List[typing.Type[typing.Any]] = None

    __methodParams: str = None  # LLM could not translate this field

    __validationMethod: typing.Union[inspect.Signature, typing.Callable] = None
    __method: str = None
    __validationClass: typing.Type[typing.Any] = None
    __classname: str = None
    __name: str = ""
    __log: logging.Logger = logging.getLogger(__name__)
    __serialVersionUID: int = 1339713700053204597

    def toString(self) -> str:
        return "ValidatorAction: " + self.__name + "\n"

    def getDependencyList(self) -> typing.List[str]:
        return typing.cast(typing.List[str], self.__dependencyList)

    def isDependency(self, validatorName: str) -> bool:
        return validatorName in self.__dependencyList

    def _loadJavascriptFunction(self) -> None:

        if self.__javascriptAlreadyLoaded():
            return

        if self.__getLog().isEnabledFor(logging.TRACE):
            self.__getLog().log(logging.TRACE, "  Loading function begun")

        if self.__jsFunction is None:
            self.__jsFunction = self.__generateJsFunction()

        javascriptFileName = self.__formatJavascriptFileName()

        if self.__getLog().isEnabledFor(logging.TRACE):
            self.__getLog().log(
                logging.TRACE, "  Loading js function '" + javascriptFileName + "'"
            )

        self.__javascript = self.__readJavascriptFile(javascriptFileName)

        if self.__getLog().isEnabledFor(logging.TRACE):
            self.__getLog().log(
                logging.TRACE, "  Loading javascript function completed"
            )

    def _init(self) -> None:

        self._loadJavascriptFunction()

    def setJavascript(self, javascript: str) -> None:

        if self.__jsFunction is not None:
            raise RuntimeError(
                "Cannot call setJavascript() after calling setJsFunction()"
            )

        self.__javascript = javascript

    def getJavascript(self) -> str:
        return self.__javascript

    def setJsFunction(self, jsFunction: str) -> None:

        if self.__javascript is not None:
            raise RuntimeError(
                "Cannot call setJsFunction() after calling setJavascript()"
            )

        self.__jsFunction = jsFunction

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

        st = depends.split(",")
        for depend in st:
            depend = depend.strip()

            if depend and len(depend) > 0:
                self.__dependencyList.append(depend)

    def getDepends(self) -> str:
        return self.__depends

    def setMethodParams(self, methodParams: str) -> None:

        self.__methodParams = methodParams

        self.__methodParameterList.clear()

        st = methodParams.split(",")
        for value in st:
            value = value.strip()

            if value and len(value) > 0:
                self.__methodParameterList.append(value)

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
        return self.__log

    def __onlyReturnErrors(self, params: typing.Dict[str, typing.Any]) -> bool:
        v = params.get(Validator.VALIDATOR_PARAM)
        return v.getOnlyReturnErrors()

    def __getClassLoader(self, params: typing.Dict[str, typing.Any]) -> typing.Any:

        v = params.get(Validator.VALIDATOR_PARAM)
        if v is not None:
            return v.getClassLoader()
        else:
            return None

    def __isValid(self, result: typing.Any) -> bool:
        if isinstance(result, bool):
            return result
        return result is not None

    def __getValidationClassInstance(self) -> typing.Any:

        if self.__validationMethod and not (
            self.__validationMethod.__dict__.get("__self__") is None
        ):
            self.__instance = None

        else:
            if self.__instance is None:
                try:
                    self.__instance = self.__validationClass()
                except Exception as e:
                    msg1 = (
                        "Couldn't create instance of "
                        + self.__classname
                        + ".  "
                        + str(e)
                    )
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

        if self.__parameterClasses is not None:
            return

        parameterClasses = [None] * len(self.__methodParameterList)

        for i in range(len(self.__methodParameterList)):
            paramClassName = self.__methodParameterList[i]

            try:
                parameterClasses[i] = loader.loadClass(paramClassName)

            except Exception as e:
                raise ValidatorException(str(e))

        self.__parameterClasses = parameterClasses

    def __loadValidationClass(self, loader: typing.Any) -> None:

        if self.__validationClass is not None:
            return

        try:
            self.__validationClass = loader.loadClass(self.__classname)
        except Exception as e:
            raise ValidatorException(str(e))

    def __loadValidationMethod(self) -> None:

        if self.__validationMethod is not None:
            return

        try:
            self.__validationMethod = getattr(self.__validationClass, self.__method)

        except AttributeError as e:
            raise ValidatorException("No such validation method: " + str(e))

    def __generateJsFunction(self) -> str:

        jsName = "org.apache.commons.validator.javascript.validate"
        if self.__name:
            jsName += self.__name[0].upper() + self.__name[1:]

        return jsName

    def __javascriptAlreadyLoaded(self) -> bool:
        return self.__javascript is not None

    def __formatJavascriptFileName(self) -> str:

        fname = self.__jsFunction[1:]

        if not self.__jsFunction.startswith("/"):
            fname = self.__jsFunction.replace(".", "/") + ".js"

        return fname

    def __readJavascriptFile(self, javascriptFileName: str) -> str:

        classLoader = Thread.currentThread().getContextClassLoader()
        if classLoader is None:
            classLoader = self.__class__.getClassLoader()

        is_ = classLoader.getResourceAsStream(javascriptFileName)
        if is_ is None:
            is_ = self.__class__.getResourceAsStream(javascriptFileName)

        if is_ is None:
            self.__getLog().debug(
                "  Unable to read javascript name " + javascriptFileName
            )
            return None

        buffer = io.StringIO()
        reader = io.BufferedReader(io.InputStreamReader(is_))  # TODO encoding
        try:
            line = None
            while (line := reader.readLine()) is not None:
                buffer.write(line + "\n")

        except IOError as e:
            self.__getLog().error("Error reading javascript file.", e)

        finally:
            try:
                reader.close()
            except IOError as e:
                self.__getLog().error("Error closing stream to javascript file.", e)

        function = buffer.getvalue()
        return None if function == "" else function
