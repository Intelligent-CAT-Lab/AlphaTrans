from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class ShortestDistances:

    __weightOperations: OrderedMonoid[typing.Any] = None

    __distances: typing.Dict[typing.Any, typing.Any] = {}

    def setWeight(self, vertex: typing.Any, distance: typing.Any) -> None:
        self.__distances[vertex] = distance

    def getWeight(self, vertex: typing.Any) -> typing.Any:
        return self.__distances.get(vertex)

    def compare(self, left: typing.Any, right: typing.Any) -> int:
        if not self.alreadyVisited(left) and not self.alreadyVisited(right):
            return 0
        elif not self.alreadyVisited(left):
            return 1
        elif not self.alreadyVisited(right):
            return -1
        return self.__weightOperations.compare(
            self.getWeight(left), self.getWeight(right)
        )

    def alreadyVisited(self, vertex: typing.Any) -> bool:
        return vertex in self.__distances

    def __init__(self, weightOperations: OrderedMonoid[typing.Any]) -> None:
        self.__weightOperations = weightOperations
