# Imports Begin
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.utils.Assertions import *
import unittest
import typing
from typing import *

# Imports End


class BaseLabeledEdge(unittest.TestCase, Serializable):

    # Class Fields Begin
    __serialVersionUID: int = -4985890761880816592
    __label: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"{self.getLabel()}()"

    def hashCode(self) -> int:

        return hash(1, 31, self.__label)

    def equals(self, obj: typing.Any) -> bool:

        if self is obj:
            return True
        if obj is None or type(self) != type(obj):
            return False
        other = obj
        return self.eq(self.label, other.label)

    def getLabel(self) -> str:

        return self.__label

    def __init__(self, label: str) -> None:

        self.__label = self.checkNotNull(label, "Argument 'label' must not be null")

    # Class Methods End
