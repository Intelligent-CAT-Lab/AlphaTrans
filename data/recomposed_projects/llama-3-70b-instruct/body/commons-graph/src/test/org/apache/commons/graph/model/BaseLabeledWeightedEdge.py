from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.utils.Objects import *


class BaseLabeledWeightedEdge(BaseLabeledEdge):

    __weight: typing.Any = None

    __serialVersionUID: int = 5935967858178091436

    def toString(self) -> str:
        return format("%s( %s )", self.getLabel(), self.__weight)

    def hashCode(self) -> int:
        return Objects.hash(super().hashCode(), 31, self.__weight)

    def equals(self, obj: typing.Any) -> bool:
        if self == obj:
            return True

        if obj == None or type(self) != type(obj):
            return False

        other = typing.cast(BaseLabeledWeightedEdge, obj)

        return Objects.eq(self.__label, other.__label) and Objects.eq(
            self.__weight, other.getWeight()
        )

    def getWeight(self) -> typing.Any:
        return self.__weight

    def __init__(self, label: str, weight: typing.Any) -> None:
        super().__init__(label)
        self.__weight = Assertions.checkNotNull(
            weight, "Argument 'weight' must not be null"
        )
