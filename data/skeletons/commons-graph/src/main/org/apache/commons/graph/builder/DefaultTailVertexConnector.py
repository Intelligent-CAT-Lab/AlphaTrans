from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.MutableGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultTailVertexConnector(TailVertexConnector):

    # Class Fields Begin
    __graph: MutableGraph[typing.Any, typing.Any] = None
    __edge: typing.Any = None
    __head: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def to(self, tail: typing.Any) -> None:
        pass

    def __init__(
        self,
        graph: MutableGraph[typing.Any, typing.Any],
        edge: typing.Any,
        head: typing.Any,
    ) -> None:
        pass

    # Class Methods End
