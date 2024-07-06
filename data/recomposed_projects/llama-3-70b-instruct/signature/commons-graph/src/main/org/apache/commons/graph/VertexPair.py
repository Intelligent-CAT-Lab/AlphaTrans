from __future__ import annotations
import re
import os
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
        return format("[head=%s, tail=%s]", self.__head, self.__tail)

    def hashCode(self) -> int:
        return Objects.hash(1, 31, self.__head, self.__tail)

    def equals(self, obj: typing.Any) -> bool:
        if self == obj:
            return True

        if obj is None or type(self) != type(obj):
            return False

        other: VertexPair = obj
        return Objects.eq(self.__head, other.getHead()) and Objects.eq(
            self.__tail, other.getTail()
        )

    def getTail(self) -> typing.Any:
        return self.__tail

    def getHead(self) -> typing.Any:
        return self.__head

    def __init__(self, head: typing.Any, tail: typing.Any) -> None:
        self.__head = Assertions.checkNotNull(
            head, "Impossible to construct a Vertex with a null head"
        )
        self.__tail = Assertions.checkNotNull(
            tail, "Impossible to construct a Vertex with a null tail"
        )
