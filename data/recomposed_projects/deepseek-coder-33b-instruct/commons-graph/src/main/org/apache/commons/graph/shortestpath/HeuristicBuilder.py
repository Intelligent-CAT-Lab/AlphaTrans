from __future__ import annotations
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.Heuristic import *


class HeuristicBuilder(ABC):

    def withHeuristic(
        self, heuristic: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:

        # Your implementation here
        pass
