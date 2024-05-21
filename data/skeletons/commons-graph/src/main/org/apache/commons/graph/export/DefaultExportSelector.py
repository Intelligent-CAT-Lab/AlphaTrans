from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.export.NamedExportSelector import *
from src.main.org.apache.commons.graph.export.ExportSelector import *
from src.main.org.apache.commons.graph.export.DotExporter import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class DefaultExportSelector(NamedExportSelector):

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def withName(self, name: str) -> ExportSelector[typing.Any, typing.Any]:
        pass

    def usingDotNotation(self) -> DotExporter[typing.Any, typing.Any]:
        pass

    def __init__(self, graph: Graph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
