from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.utils.Objects import *


class BaseLabeledEdge:

    __label: str = ""

    __serialVersionUID: int = -4985890761880816592

    def toString(self) -> str:
        return format("%s()", self.getLabel())

    def hashCode(self) -> int:
        return Objects.hash(1, 31, self.__label)

    def equals(self, obj: typing.Any) -> bool:
        if self == obj:
            return True

        if obj == None or type(self) != type(obj):
            return False

        other = typing.cast(BaseLabeledEdge, obj)

        return Objects.eq(self.__label, other.__label)

    def getLabel(self) -> str:
        return self.__label

    def __init__(self, label: str) -> None:
        self.__label = Assertions.checkNotNull(
            label, "Argument 'label' must not be null"
        )
