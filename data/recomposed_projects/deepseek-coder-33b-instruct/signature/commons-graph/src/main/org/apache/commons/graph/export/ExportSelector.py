from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.export.DotExporter import *
from src.main.org.apache.commons.graph.export.GraphExportException import *


class ExportSelector(ABC):

    def usingDotNotation(self) -> DotExporter[typing.Any, typing.Any]:

        try:
            return DotExporter()
        except GraphExportException as e:
            print(f"Error: {e}")
            raise
