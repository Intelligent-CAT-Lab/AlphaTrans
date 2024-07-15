from __future__ import annotations
import re
import os
from abc import ABC
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.export.GraphExportException import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class AbstractExporter(ABC):

    __writer: typing.Union[io.TextIOWrapper, io.BufferedWriter] = None

    __name: str = ""

    __edgeProperties: typing.Dict[str, Mapper[typing.Any, typing.Any]] = None

    __vertexProperties: typing.Dict[str, Mapper[typing.Any, typing.Any]] = None

    __graph: Graph[typing.Any, typing.Any] = None

    __G: str = "G"

    def to2(self, writer: typing.Union[io.TextIOWrapper, io.BufferedWriter]) -> None:

        pass  # LLM could not translate this method

    def to1(
        self, outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        self.to2(
            OutputStreamWriter(
                Assertions.checkNotNull(
                    outputStream, "Impossibe to export the graph in a null stream"
                )
            )
        )

    def to0(self, outputFile: pathlib.Path) -> None:

        pass  # LLM could not translate this method

    def _getWriter(self) -> typing.Union[io.TextIOWrapper, io.BufferedWriter]:
        return self.__writer

    def _getGraph(self) -> Graph[typing.Any, typing.Any]:
        return self.__graph

    def _addVertexProperty(
        self, propertyName: str, vertexProperty: typing.Dict[typing.Any, typing.Any]
    ) -> None:
        self.__vertexProperties.put(propertyName, vertexProperty)

    def _addEdgeProperty(
        self, propertyName: str, edgeProperty: typing.Dict[typing.Any, typing.Any]
    ) -> None:
        self.__edgeProperties.put(propertyName, edgeProperty)

    def __init__(self, graph: Graph[typing.Any, typing.Any], name: str) -> None:
        self.__graph = graph
        self.__writer = None
        self.__vertexProperties = {}
        self.__edgeProperties = {}
        self.__name = name if name is not None else self.__G

    def _vertex(
        self, vertex: typing.Any, properties: typing.Dict[str, typing.Any]
    ) -> None:
        pass

    def _startSerialization(self) -> None:
        pass

    def _startGraph(self, name: str) -> None:
        pass

    def _enlistVerticesProperty(self, name: str, type: typing.Type[typing.Any]) -> None:
        pass

    def _enlistEdgesProperty(self, name: str, type: typing.Type[typing.Any]) -> None:
        self._enlistProperty(name, type, self._edgeProperties)

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
