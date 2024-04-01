# Imports Begin
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.utils.Assertions import *
import unittest
import typing
from typing import *

# Imports End


class BaseLabeledVertex(unittest.TestCase, Serializable):

    # Class Fields Begin
    __serialVersionUID: int = -5167021719818162490
    __label: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"{{ {self.__label} }}"

    def hashCode(self) -> int:

        return hash(1, 31, self.__label)

    def equals(self, obj: typing.Any) -> bool:

        if self is obj:
            return True
        if obj is None or type(obj) != type(self):
            return False
        other = obj
        return self.eq(self.__label, other.getLabel())

    def getLabel(self) -> str:

        return self.__label

    def __init__(self, label: str) -> None:

        self.__label = self.checkNotNull(label, "Argument 'label' must not be null")

    # Class Methods End
