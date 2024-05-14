# Imports Begin
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.utils.Assertions import *
import typing

# Imports End


class VertexPair(Serializable, VertexPair):

    # Class Fields Begin
    __serialVersionUID: int = None
    __head: typing.Any = None
    __tail: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def getTail(self) -> typing.Any:
        pass

    def getHead(self) -> typing.Any:
        pass

    def __init__(self, head: typing.Any, tail: typing.Any) -> None:
        pass

    # Class Methods End
