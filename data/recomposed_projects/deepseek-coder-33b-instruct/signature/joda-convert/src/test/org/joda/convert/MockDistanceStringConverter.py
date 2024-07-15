from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.joda.convert.DistanceMethodMethod import *
from src.main.org.joda.convert.StringConverter import *


class MockDistanceStringConverter(StringConverter):

    INSTANCE: MockDistanceStringConverter = None

    def convertFromString(
        self, cls: typing.Type[DistanceMethodMethod], str: str
    ) -> DistanceMethodMethod:
        return DistanceMethodMethod.parse(str)

    def convertToString(self, object: DistanceMethodMethod) -> str:
        return object.print()
