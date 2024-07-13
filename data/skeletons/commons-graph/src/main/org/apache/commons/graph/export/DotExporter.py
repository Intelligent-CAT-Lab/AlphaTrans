from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.export.AbstractExporter import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io
from io import StringIO

# Imports End


class DotExporter(AbstractExporter):

    # Class Fields Begin
    __GRAPH: str = None
    __DIGRAPH: str = None
    __CONNECTOR: str = None
    __DICONNECTOR: str = None
    __WEIGHT: str = None
    __LABEL: str = None
    __vertexIdentifiers: typing.Dict[typing.Any, int] = None
    __printWriter: typing.Union[io.TextIOWrapper, io.StringIO] = None
    __connector: str = None
    # Class Fields End

    # Class Methods Begin
    def _vertex(
        self, vertex: typing.Any, properties: typing.Dict[str, typing.Any]
    ) -> None:
        pass

    def _startSerialization(self) -> None:
        pass

    def _startGraph(self, name: str) -> None:
        pass

    def _enlistVerticesProperty(
        self, name: str, type_: typing.Type[typing.Any]
    ) -> None:
        pass

    def _enlistEdgesProperty(self, name: str, type_: typing.Type[typing.Any]) -> None:
        pass

    def _endSerialization(self) -> None:
        pass

    def _endGraph(self) -> None:
        pass

    def _edge(
        self,
        edge: typing.Any,
        head: typing.Any,
        tail: typing.Any,
        properties: typing.Dict[str, typing.Any],
    ) -> None:
        pass

    def _comment(self, text: str) -> None:
        pass

    def withVertexLabels(
        self, vertexLabels: typing.Dict[typing.Any, str]
    ) -> DotExporter:
        pass

    def withEdgeWeights(
        self, edgeWeights: Mapper[typing.Any, typing.Any]
    ) -> DotExporter:
        pass

    def withEdgeLabels(self, edgeLabels: Mapper[typing.Any, str]) -> DotExporter:
        pass

    def __printVertexOrEdgeProperties(
        self, properties: typing.Dict[str, typing.Any]
    ) -> None:
        pass

    def __generateVertexIdentifiers(
        self, graph: Graph[typing.Any, typing.Any]
    ) -> typing.Dict[typing.Any, int]:
        pass

    def __init__(self, graph: Graph[typing.Any, typing.Any], name: str) -> None:
        pass

    # Class Methods End
