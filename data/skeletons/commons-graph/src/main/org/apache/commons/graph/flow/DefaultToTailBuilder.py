from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultToTailBuilder(ToTailBuilder):

    # Class Fields Begin
    __graph: DirectedGraph[typing.Any, typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __head: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def to(
        self, tail: typing.Any
    ) -> MaxFlowAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def __init__(
        self,
        graph: DirectedGraph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        head: typing.Any,
    ) -> None:
        pass

    # Class Methods End
