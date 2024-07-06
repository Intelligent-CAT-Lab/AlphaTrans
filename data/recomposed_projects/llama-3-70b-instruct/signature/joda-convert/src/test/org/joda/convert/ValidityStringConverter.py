from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.test.org.joda.convert.Validity import *


class ValidityStringConverter(StringConverter):

    INSTANCE: ValidityStringConverter = None

    def convertFromString(self, cls: typing.Type[Validity], str: str) -> Validity:
        if str == "OK":
            return Validity.VALID
        return Validity.valueOf(str)

    def convertToString(self, object: Validity) -> str:
        return object.name()
