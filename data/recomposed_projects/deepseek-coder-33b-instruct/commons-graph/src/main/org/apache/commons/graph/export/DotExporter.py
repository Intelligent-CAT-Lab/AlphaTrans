from __future__ import annotations
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.export.AbstractExporter import *


class DotExporter(AbstractExporter):

    __connector: str = None
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

        self.__printWriter.write("  {}".format(self.__vertexIdentifiers.get(vertex)))

        self.__printVertexOrEdgeProperties(properties)

    def _startSerialization(self) -> None:

        self.__printWriter = io.StringIO()

    def _startGraph(self, name: str) -> None:

        if isinstance(self.getGraph(), DirectedGraph):
            graphDeclaration = self._DIGRAPH
            self._connector = self._DICONNECTOR
        else:
            graphDeclaration = self._GRAPH
            self._connector = self._CONNECTOR

        self._printWriter.write(f"{graphDeclaration} {name} {{\n")

    def _enlistVerticesProperty(self, name: str, type: typing.Type[typing.Any]) -> None:

        pass

    def _enlistEdgesProperty(self, name: str, type: typing.Type[typing.Any]) -> None:

        pass

    def _endSerialization(self) -> None:

        pass

    def _endGraph(self) -> None:

        self.__printWriter.write("}")

    def _edge(
        self,
        edge: typing.Any,
        head: typing.Any,
        tail: typing.Any,
        properties: typing.Dict[str, typing.Any],
    ) -> None:

        self.__printWriter.write(
            "  {} {} {}".format(
                self.__vertexIdentifiers.get(head),
                self.__connector,
                self.__vertexIdentifiers.get(tail),
            )
        )

        self.__printVertexOrEdgeProperties(properties)

    def _comment(self, text: str) -> None:

        if self.__printWriter is None:
            self.__printWriter = io.StringIO()

        self.__printWriter.write(text)

    def withVertexLabels(
        self, vertexLabels: typing.Dict[typing.Any, str]
    ) -> DotExporter:

        # Assuming that the addVertexProperty method is a method in the AbstractExporter class
        # and it takes two arguments: the property name and the property value
        super().addVertexProperty(self.__LABEL, vertexLabels)
        return self

    def withEdgeWeights(
        self, edgeWeights: Mapper[typing.Any, typing.Any]
    ) -> DotExporter:

        self.addEdgeProperty(self.__WEIGHT, edgeWeights)
        return self

    def withEdgeLabels(self, edgeLabels: Mapper[typing.Any, str]) -> DotExporter:

        self.addEdgeProperty(self.__LABEL, edgeLabels)
        return self

    def __printVertexOrEdgeProperties(
        self, properties: typing.Dict[str, typing.Any]
    ) -> None:

        if properties:
            countAddedProperties = 0
            self.__printWriter.write(" [")

            for property in properties.items():
                formattedString = (
                    '="%s"' % property[1]
                    if countAddedProperties == len(properties) - 1
                    else '="%s" ' % property[1]
                )
                self.__printWriter.write(property[0] + formattedString)
                countAddedProperties += 1

            self.__printWriter.write("];\n")

    def __generateVertexIdentifiers(
        self, graph: Graph[typing.Any, typing.Any]
    ) -> typing.Dict[typing.Any, int]:

        vertexIdentifiers: typing.Dict[typing.Any, int] = {}
        count = 1

        for vertex in graph.getVertices0():
            vertexIdentifiers[vertex] = count
            count += 1

        return vertexIdentifiers

    def __init__(self, graph: Graph[typing.Any, typing.Any], name: str) -> None:

        super().__init__(graph, name)
        self.__vertexIdentifiers = self.__generateVertexIdentifiers(graph)

    def __generateVertexIdentifiers(
        self, graph: Graph[typing.Any, typing.Any]
    ) -> typing.Dict[typing.Any, int]:
        pass
