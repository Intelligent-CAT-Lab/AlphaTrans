from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class HeadVertexConnector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def from_(self, head: typing.Any) -> TailVertexConnector[typing.Any, typing.Any]:
        pass

    # Class Methods End
