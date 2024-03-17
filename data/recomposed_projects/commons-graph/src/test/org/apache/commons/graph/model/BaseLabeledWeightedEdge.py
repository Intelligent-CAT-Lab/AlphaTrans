# Imports Begin
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.model.BaseLabeledEdge import *
import unittest
import typing
from typing import *
# Imports End

class BaseLabeledWeightedEdge(unittest.TestCase, BaseLabeledEdge, BaseLabeledWeightedEdge<>):

    # Class Fields Begin
    __serialVersionUID: int = 5935967858178091436
    __weight: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

            return f"{self.getLabel()} ({self.__weight})"

    def hashCode(self) -> int:

            return hash(super().hashCode(), 31, self.__weight)

    def equals(self, obj: typing.Any) -> bool:

            if self is obj:
                return True
            if not super().equals(obj):
                return False
            if type(self) != type(obj):
                return False
            other = obj
            return self.eq(self.__weight, other.getWeight())

    def getWeight(self) -> typing.Any:

            return self.__weight

    def __init__(self, label: str, weight: typing.Any) -> None:

            super().__init__(label)
            self.__weight = self.checkNotNull(weight, "Argument 'weight' must not be null")

    # Class Methods End


