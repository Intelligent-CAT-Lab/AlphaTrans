from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.Form import *

# from src.main.org.apache.commons.logging.LogFactory import *
# from src.main.org.apache.commons.logging.Log import *
import logging
import typing
from typing import *
import io

# Imports End


class FormSet:

    # Class Fields Begin
    __serialVersionUID: int = None
    __log: logging.Logger = None
    __processed: bool = None
    __language: str = None
    __country: str = None
    __variant: str = None
    __forms: typing.Dict[str, Form] = None
    __constants: typing.Dict[str, str] = None
    _GLOBAL_FORMSET: int = None
    _LANGUAGE_FORMSET: int = None
    _COUNTRY_FORMSET: int = None
    _VARIANT_FORMSET: int = None
    __merged: bool = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def displayKey(self) -> str:
        pass

    def getForms(self) -> typing.Dict[str, Form]:
        pass

    def getForm(self, formName: str) -> Form:
        pass

    def addForm(self, f: Form) -> None:
        pass

    def addConstant(self, name: str, value: str) -> None:
        pass

    def setVariant(self, variant: str) -> None:
        pass

    def getVariant(self) -> str:
        pass

    def setCountry(self, country: str) -> None:
        pass

    def getCountry(self) -> str:
        pass

    def setLanguage(self, language: str) -> None:
        pass

    def getLanguage(self) -> str:
        pass

    def isProcessed(self) -> bool:
        pass

    def _getType(self) -> int:
        pass

    def _isMerged(self) -> bool:
        pass

    def __getLog(self) -> logging.Logger:
        pass

    # Class Methods End
