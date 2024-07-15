from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.NotEnoughColorsException import *
from src.main.org.apache.commons.graph.coloring.UncoloredOrderedVertices import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultColoringAlgorithmsSelector:

    __colors: typing.Set[typing.Any] = None

    __g: UndirectedGraph[typing.Any, typing.Any] = None

    def applyingGreedyAlgorithm(self) -> ColoredVertices[typing.Any, typing.Any]:

        colored_vertices = ColoredVertices()
        uncolored_ordered_vertices = UncoloredOrderedVertices()

        for v in self.__g.getVertices0():
            uncolored_ordered_vertices.addVertexDegree(v, self.__g.getDegree(v))

        it = iter(uncolored_ordered_vertices.getVertices())
        colors_it = iter(self.__colors)

        while True:
            try:
                v = next(it)
            except StopIteration:
                break

            try:
                color = next(colors_it)
            except StopIteration:
                raise NotEnoughColorsException(self.__colors)

            current_color_vertices = []
            uncolored_vtx_iterator = iter(uncolored_ordered_vertices.getVertices())

            while True:
                try:
                    uncolored_vtx = next(uncolored_vtx_iterator)
                except StopIteration:
                    break

                found_an_adjacent_vertex = any(
                    self.__g.getEdge(current_colored_vtx, uncolored_vtx) is not None
                    for current_colored_vtx in current_color_vertices
                )

                if not found_an_adjacent_vertex:
                    uncolored_ordered_vertices.removeVertex(uncolored_vtx)
                    colored_vertices.addColor(uncolored_vtx, color)
                    current_color_vertices.append(uncolored_vtx)

        return colored_vertices

    def applyingBackTrackingAlgorithm1(
        self, partialColoredVertex: ColoredVertices[typing.Any, typing.Any]
    ) -> ColoredVertices[typing.Any, typing.Any]:

        partialColoredVertex = Assertions.checkNotNull(
            partialColoredVertex, "PartialColoredVertex must be not null"
        )

        verticesList = []

        for v in self.__g.getVertices0():
            if not partialColoredVertex.containsColoredVertex(v):
                verticesList.append(v)

        if self.__backtraking(-1, verticesList, partialColoredVertex):
            return partialColoredVertex

        raise NotEnoughColorsException(self.__colors)

    def applyingBackTrackingAlgorithm0(self) -> ColoredVertices[typing.Any, typing.Any]:
        return self.applyingBackTrackingAlgorithm1(ColoredVertices())

    def __init__(
        self, g: UndirectedGraph[typing.Any, typing.Any], colors: typing.Set[typing.Any]
    ) -> None:
        self.__g = g
        self.__colors = colors

    def __isThereColorConflict(
        self,
        currentVertex: typing.Any,
        coloredVertices: ColoredVertices[typing.Any, typing.Any],
    ) -> bool:

        if currentVertex is None:
            return False

        nextVertexColor = coloredVertices.getColor(currentVertex)

        if nextVertexColor is None:
            return False

        for adj in self.__g.getConnectedVertices(currentVertex):
            adjColor = coloredVertices.getColor(adj)
            if adjColor is not None and nextVertexColor == adjColor:
                return True

        return False

    def __backtraking(
        self,
        currentVertexIndex: int,
        verticesList: typing.List[typing.Any],
        coloredVertices: ColoredVertices[typing.Any, typing.Any],
    ) -> bool:

        if currentVertexIndex != -1 and self.__isThereColorConflict(
            verticesList[currentVertexIndex], coloredVertices
        ):
            return False

        if currentVertexIndex == len(verticesList) - 1:
            return True

        next = currentVertexIndex + 1
        nextVertex = verticesList[next]
        for color in self.__colors:
            coloredVertices.addColor(nextVertex, color)
            isDone = self.__backtraking(next, verticesList, coloredVertices)
            if isDone:
                return True

        coloredVertices.removeColor(nextVertex)
        return False
