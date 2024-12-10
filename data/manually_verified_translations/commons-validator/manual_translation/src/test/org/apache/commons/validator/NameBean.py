from __future__ import annotations
import re
import unittest
import pytest
import io


class NameBean:

    _lastName: str = ""
    _middleName: str = ""
    _firstName: str = ""

    def setLastName(self, lastName: str) -> None:
        self._lastName = lastName

    def getLastName(self) -> str:
        return self._lastName

    def setMiddleName(self, middleName: str) -> None:
        self._middleName = middleName

    def getMiddleName(self) -> str:
        return self._middleName

    def setFirstName(self, firstName: str) -> None:
        self._firstName = firstName

    def getFirstName(self) -> str:
        return self._firstName
