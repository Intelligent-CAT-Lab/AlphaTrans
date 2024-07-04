from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Mapper import *


class WeightedEdgesComparator:

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __weightComparator: typing.Callable[[typing.Any, typing.Any], int] = None

    def compare(self, o1: typing.Any, o2: typing.Any) -> int:
        return self.__weightComparator(
            self.__weightedEdges.map(o1), self.__weightedEdges.map(o2)
        )

    def __init__(
        self,
        weightComparator: typing.Callable[[typing.Any, typing.Any], int],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        self.__weightComparator = weightComparator
        self.__weightedEdges = weightedEdges
