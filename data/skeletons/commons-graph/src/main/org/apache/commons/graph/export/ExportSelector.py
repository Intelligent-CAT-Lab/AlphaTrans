from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.export.GraphExportException import *
from src.main.org.apache.commons.graph.export.DotExporter import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ExportSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def usingDotNotation(self) -> DotExporter[typing.Any, typing.Any]:
        pass

    # Class Methods End
