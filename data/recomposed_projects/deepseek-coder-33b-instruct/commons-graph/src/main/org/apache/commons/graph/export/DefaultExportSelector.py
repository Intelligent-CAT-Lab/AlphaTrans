from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.export.DotExporter import *
from src.main.org.apache.commons.graph.export.ExportSelector import *
from src.main.org.apache.commons.graph.export.NamedExportSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultExportSelector(NamedExportSelector):

    __name: str = ""
    __graph: Graph[typing.Any, typing.Any] = None

    def withName(self, name: str) -> ExportSelector[typing.Any, typing.Any]:

        # Calling the checkNotNull method from Assertions class
        self.__name = checkNotNull(name, "Graph name cannot be null.")
        return self

    def usingDotNotation(self) -> DotExporter[typing.Any, typing.Any]:

        return DotExporter(self.__graph, self.__name)

    def __init__(self, graph: Graph[typing.Any, typing.Any]) -> None:

        self.__graph = graph
