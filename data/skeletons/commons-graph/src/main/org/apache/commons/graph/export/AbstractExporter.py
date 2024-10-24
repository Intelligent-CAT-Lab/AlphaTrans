from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.export.GraphExportException import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
from io import IOBase
import pathlib
from abc import ABC

# Imports End


class AbstractExporter(ABC):

    # Class Fields Begin
    __G: str = None
    __graph: Graph[typing.Any, typing.Any] = None
    __vertexProperties: typing.Dict[str, Mapper[typing.Any, typing.Any]] = None
    __edgeProperties: typing.Dict[str, Mapper[typing.Any, typing.Any]] = None
    __name: str = None
    __writer: typing.Union[io.TextIOWrapper, io.BufferedWriter, io.TextIOBase] = None
    # Class Fields End

    # Class Methods Begin
    def to2(
        self, writer: typing.Union[io.TextIOWrapper, io.BufferedWriter, io.TextIOBase]
    ) -> None:
        pass

    def to1(
        self, outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        pass

    def to0(self, outputFile: pathlib.Path) -> None:
        pass

    def _getWriter(
        self,
    ) -> typing.Union[io.TextIOWrapper, io.BufferedWriter, io.TextIOBase]:
        pass

    def _getGraph(self) -> Graph[typing.Any, typing.Any]:
        pass

    def _addVertexProperty(
        self, propertyName: str, vertexProperty: typing.Dict[typing.Any, typing.Any]
    ) -> None:
        pass

    def _addEdgeProperty(
        self, propertyName: str, edgeProperty: typing.Dict[typing.Any, typing.Any]
    ) -> None:
        pass

    def __init__(self, graph: Graph[typing.Any, typing.Any], name: str) -> None:
        pass

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

    # Class Methods End
