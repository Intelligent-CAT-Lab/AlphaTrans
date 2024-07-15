from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.export.AbstractExporter import *


class DotExporter(AbstractExporter):

    __connector: str = ""

    __printWriter: typing.Union[io.TextIOWrapper, io.StringIO] = None

    __vertexIdentifiers: typing.Dict[typing.Any, int] = None

    __LABEL: str = "label"
    __WEIGHT: str = "weight"
    __DICONNECTOR: str = "->"
    __CONNECTOR: str = "--"
    __DIGRAPH: str = "digraph"
    __GRAPH: str = "graph"

    def _vertex(
        self, vertex: typing.Any, properties: typing.Dict[str, typing.Any]
    ) -> None:
        self.__printWriter.format("  %s", self.__vertexIdentifiers.get(vertex))

        self.__printVertexOrEdgeProperties(properties)

    def _startSerialization(self) -> None:
        self.__printWriter = PrintWriter(self.getWriter())

    def _startGraph(self, name: str) -> None:
        graphDeclaration: str

        if isinstance(self.__graph, DirectedGraph):
            graphDeclaration = self.__DIGRAPH
            self.__connector = self.__DICONNECTOR
        else:
            graphDeclaration = self.__GRAPH
            self.__connector = self.__CONNECTOR

        self.__printWriter.write(f"{graphDeclaration} {name} {{\n")

    def _enlistVerticesProperty(self, name: str, type: typing.Type[typing.Any]) -> None:

        pass  # LLM could not translate this method

    def _enlistEdgesProperty(self, name: str, type: typing.Type[typing.Any]) -> None:
        self._edgeProperties[name] = Mapper(type, str)

    def _endSerialization(self) -> None:
        self.__writer.write("}")

    def _endGraph(self) -> None:
        self.__printWriter.write("}")

    def _edge(
        self,
        edge: typing.Any,
        head: typing.Any,
        tail: typing.Any,
        properties: typing.Dict[str, typing.Any],
    ) -> None:

        pass  # LLM could not translate this method

    def _comment(self, text: str) -> None:
        self.__printWriter.write(text)

    def withVertexLabels(
        self, vertexLabels: typing.Dict[typing.Any, str]
    ) -> DotExporter:
        super().addVertexProperty(self.__LABEL, vertexLabels)
        return self

    def withEdgeWeights(
        self, edgeWeights: Mapper[typing.Any, typing.Any]
    ) -> DotExporter:
        super().addEdgeProperty(self.__WEIGHT, edgeWeights)
        return self

    def withEdgeLabels(self, edgeLabels: Mapper[typing.Any, str]) -> DotExporter:
        super().addEdgeProperty(self.__LABEL, edgeLabels)
        return self

    def __printVertexOrEdgeProperties(
        self, properties: typing.Dict[str, typing.Any]
    ) -> None:
        if not properties:
            return
        count_added_properties = 0
        self.__printWriter.write(" [")
        for property in properties.items():
            formatted_string = (
                '%s="%s"'
                if count_added_properties == len(properties) - 1
                else '%s="%s" '
            )
            self.__printWriter.write(formatted_string % (property[0], property[1]))
            count_added_properties += 1
        self.__printWriter.write("];\n")

    def __generateVertexIdentifiers(
        self, graph: Graph[typing.Any, typing.Any]
    ) -> typing.Dict[typing.Any, int]:
        vertexIdentifiers = {}
        count = 1

        for vertex in graph.getVertices0():
            vertexIdentifiers[vertex] = count
            count += 1

        return vertexIdentifiers

    def __init__(self, graph: Graph[typing.Any, typing.Any], name: str) -> None:
        super().__init__(graph, name)
        self.__vertexIdentifiers = self.__generateVertexIdentifiers(graph)
