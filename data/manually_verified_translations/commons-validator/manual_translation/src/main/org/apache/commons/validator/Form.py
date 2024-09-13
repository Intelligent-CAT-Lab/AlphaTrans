from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.Field import *


class Form:

    _inherit: str = None
    _lFields: typing.List[Field] = []

    _name: str = ""
    __processed: bool = False
    __serialVersionUID: int = 6445211789563796371

    def toString(self) -> str:

        results = io.StringIO()

        results.write("Form: ")
        results.write(self._name)
        results.write("\n")

        for field in self._lFields:
            results.write("\tField: \n")
            results.write(str(field))
            results.write("\n")

        return results.getvalue()

    def isExtending(self) -> bool:
        return self._inherit is not None

    def setExtends(self, inherit: str) -> None:
        self._inherit = inherit

    def getExtends(self) -> str:
        return self._inherit

    def isProcessed(self) -> bool:
        return self.__processed

    def getFields(self) -> typing.List[Field]:
        return typing.cast(typing.List[Field], self._lFields)

    def setName(self, name: str) -> None:
        self._name = name

    def getName(self) -> str:
        return self._name
