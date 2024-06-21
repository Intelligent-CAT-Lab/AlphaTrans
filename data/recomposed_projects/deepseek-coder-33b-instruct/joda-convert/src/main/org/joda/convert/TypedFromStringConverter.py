from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.FromStringConverter import *


class TypedFromStringConverter(ABC):

    def getEffectiveType(self) -> typing.Type[typing.Any]:

        pass  # LLM could not translate this method
