from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class VisitAlgorithmsSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def applyingDepthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:
        pass

    def applyingDepthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:
        pass

    def applyingBreadthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:
        pass

    def applyingBreadthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:
        pass

    # Class Methods End
