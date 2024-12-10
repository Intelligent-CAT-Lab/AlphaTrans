from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.export.ExportSelector import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class NamedExportSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def withName(self, name: str) -> ExportSelector[typing.Any, typing.Any]:
        pass

    # Class Methods End
