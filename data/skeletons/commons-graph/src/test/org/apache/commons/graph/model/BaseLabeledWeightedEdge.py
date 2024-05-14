# Imports Begin
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.model.BaseLabeledEdge import *
import typing

# Imports End


class BaseLabeledWeightedEdge(BaseLabeledEdge, BaseLabeledWeightedEdge):

    # Class Fields Begin
    __serialVersionUID: int = None
    __weight: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def getWeight(self) -> typing.Any:
        pass

    def __init__(self, label: str, weight: typing.Any) -> None:
        pass

    # Class Methods End
