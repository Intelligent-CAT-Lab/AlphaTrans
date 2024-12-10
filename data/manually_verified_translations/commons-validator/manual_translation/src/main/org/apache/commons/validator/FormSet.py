from __future__ import annotations
import time
import re
from io import StringIO
import io
import typing
from typing import *
import logging

# from src.main.org.apache.commons.logging.Log import *
# from src.main.org.apache.commons.logging.LogFactory import *
from src.main.org.apache.commons.validator.Form import *


class FormSet:

    _VARIANT_FORMSET: int = 4
    _COUNTRY_FORMSET: int = 3
    _LANGUAGE_FORMSET: int = 2
    _GLOBAL_FORMSET: int = 1
    __merged: bool = False

    __constants: typing.Dict[str, str] = {}

    __forms: typing.Dict[str, Form] = {}

    __variant: str = None
    __country: str = None
    __language: str = ""
    __processed: bool = False
    __log: logging.Logger = logging.getLogger(__name__)
    __serialVersionUID: int = -8936513232763306055

    def toString(self) -> str:

        results = io.StringIO()

        results.write("FormSet: language=")
        results.write(self.__language)
        results.write("  country=")
        results.write(self.__country)
        results.write("  variant=")
        results.write(self.__variant)
        results.write("\n")

        for form in self.getForms().values():
            results.write("   ")
            results.write(str(form))
            results.write("\n")

        return results.getvalue()

    def displayKey(self) -> str:

        results = []

        if self.__language and len(self.__language) > 0:
            results.append(f"language={self.__language}")
        if self.__country and len(self.__country) > 0:
            if len(results) > 0:
                results.append(", ")
            results.append(f"country={self.__country}")
        if self.__variant and len(self.__variant) > 0:
            if len(results) > 0:
                results.append(", ")
            results.append(f"variant={self.__variant}")
        if len(results) == 0:
            results.append("default")

        return "".join(results)

    def getForms(self) -> typing.Dict[str, Form]:
        return typing.MappingProxyType(self.__forms)

    def getForm(self, formName: str) -> Form:
        return self.__forms.get(formName)

    def addForm(self, f: Form) -> None:

        formName = f.getName()
        if formName in self.__forms:
            self.__getLog().error(
                "Form '"
                + formName
                + "' already exists in FormSet["
                + self.displayKey()
                + "] - ignoring."
            )

        else:
            self.__forms[formName] = f

    def addConstant(self, name: str, value: str) -> None:

        if name in self.__constants:
            self.__getLog().error(
                "Constant '"
                + name
                + "' already exists in FormSet["
                + self.displayKey()
                + "] - ignoring."
            )

        else:
            self.__constants[name] = value

    def setVariant(self, variant: str) -> None:
        self.__variant = variant

    def getVariant(self) -> str:
        return self.__variant

    def setCountry(self, country: str) -> None:
        self.__country = country

    def getCountry(self) -> str:
        return self.__country

    def setLanguage(self, language: str) -> None:
        self.__language = language

    def getLanguage(self) -> str:
        return self.__language

    def isProcessed(self) -> bool:
        return self.__processed

    def _getType(self) -> int:
        if self.getVariant() is not None:
            if self.getLanguage() is None or self.getCountry() is None:
                raise RuntimeError(
                    "When variant is specified, country and language must be specified."
                )
            return self._VARIANT_FORMSET
        elif self.getCountry() is not None:
            if self.getLanguage() is None:
                raise RuntimeError(
                    "When country is specified, language must be specified."
                )
            return self._COUNTRY_FORMSET
        elif self.getLanguage() is not None:
            return self._LANGUAGE_FORMSET
        else:
            return self._GLOBAL_FORMSET

    def _isMerged(self) -> bool:
        return self.__merged

    def __getLog(self) -> logging.Logger:
        return self.__log
