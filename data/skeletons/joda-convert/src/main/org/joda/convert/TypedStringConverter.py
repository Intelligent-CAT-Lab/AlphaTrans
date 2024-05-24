from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.TypedFromStringConverter import *
from src.main.org.joda.convert.StringConverter import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class TypedStringConverter(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    # Class Methods End
