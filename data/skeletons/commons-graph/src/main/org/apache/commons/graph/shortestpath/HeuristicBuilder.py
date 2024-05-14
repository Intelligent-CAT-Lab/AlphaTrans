# Imports Begin
from src.main.org.apache.commons.graph.shortestpath.Heuristic import *
from src.main.org.apache.commons.graph.WeightedPath import *
import typing
import pathlib
from abc import ABC

# Imports End


class HeuristicBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def withHeuristic(
        self, heuristic: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
