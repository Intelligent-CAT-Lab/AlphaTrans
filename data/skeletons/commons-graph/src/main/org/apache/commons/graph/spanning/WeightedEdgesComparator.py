from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.Mapper import *
import typing
from typing import *
import io

# Imports End


class WeightedEdgesComparator:

    # Class Fields Begin
    __weightComparator: typing.Callable[[typing.Any, typing.Any], int] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def compare(self, o1: typing.Any, o2: typing.Any) -> int:
        pass

    def __init__(
        self,
        weightComparator: typing.Callable[[typing.Any, typing.Any], int],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    # Class Methods End
