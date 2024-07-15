from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *


class MockIntegerStringConverter(StringConverter):

    INSTANCE: MockIntegerStringConverter = None

    def convertFromString(self, cls: typing.Type[int], str: str) -> int:
        return int(str)

    def convertToString(self, object: int) -> str:
        return str(object)
