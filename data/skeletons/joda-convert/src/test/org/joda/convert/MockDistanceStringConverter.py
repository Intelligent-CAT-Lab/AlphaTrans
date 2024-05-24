from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.StringConverter import *
from src.test.org.joda.convert.DistanceMethodMethod import *
import typing
from typing import *
import io

# Imports End


class MockDistanceStringConverter(StringConverter):

    # Class Fields Begin
    INSTANCE: MockDistanceStringConverter = None
    # Class Fields End

    # Class Methods Begin
    def convertFromString(
        self, cls: typing.Type[DistanceMethodMethod], str: str
    ) -> DistanceMethodMethod:
        pass

    def convertToString(self, object: DistanceMethodMethod) -> str:
        pass

    # Class Methods End
