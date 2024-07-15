from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.utils.Objects import *


class BaseLabeledVertex:

    __label: str = ""

    __serialVersionUID: int = -5167021719818162490

    def toString(self) -> str:
        return format("{ %s }", self.__label)

    def hashCode(self) -> int:
        return Objects.hash(1, 31, self.__label)

    def equals(self, obj: typing.Any) -> bool:
        if self == obj:
            return True

        if obj is None or type(self) != type(obj):
            return False

        other = typing.cast(BaseLabeledVertex, obj)
        return Objects.eq(self.__label, other.getLabel())

    def getLabel(self) -> str:
        return self.__label

    def __init__(self, label: str) -> None:
        self.__label = Assertions.checkNotNull(
            label, "Argument 'label' must not be null"
        )
