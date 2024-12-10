from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ToTailBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def to(
        self, tail: typing.Any
    ) -> MaxFlowAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
