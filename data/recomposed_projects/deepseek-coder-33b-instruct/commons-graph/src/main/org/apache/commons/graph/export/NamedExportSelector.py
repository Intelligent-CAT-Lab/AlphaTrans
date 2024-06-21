from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.export.ExportSelector import *


class NamedExportSelector(ABC):

    def withName(self, name: str) -> ExportSelector[typing.Any, typing.Any]:

        pass
