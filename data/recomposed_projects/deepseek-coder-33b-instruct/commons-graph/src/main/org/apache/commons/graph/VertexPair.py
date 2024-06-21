from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.utils.Objects import *


class VertexPair:

    __tail: typing.Any = None
    __head: typing.Any = None

    __serialVersionUID: int = 2333503391707156055

    def toString(self) -> str:

        return "[head={}, tail={}]".format(self.__head, self.__tail)

    def hashCode(self) -> int:

        prime = 31
        return hash((1, prime, self.__head, self.__tail))

    def equals(self, obj: typing.Any) -> bool:

        if self == obj:
            return True

        if obj is None or type(self) != type(obj):
            return False

        other = typing.cast(VertexPair, obj)
        return eq(self.__head, other.getHead()) and eq(self.__tail, other.getTail())

    def getTail(self) -> typing.Any:

        return self.__tail

    def getHead(self) -> typing.Any:

        return self.__head

    def __init__(self, head: typing.Any, tail: typing.Any) -> None:

        # The checkNotNull method is not available in Python, so we will use the assert statement to check if the head and tail are not None
        assert head is not None, "Impossible to construct a Vertex with a null head"
        assert tail is not None, "Impossible to construct a Vertex with a null tail"

        self.__head = head
        self.__tail = tail
