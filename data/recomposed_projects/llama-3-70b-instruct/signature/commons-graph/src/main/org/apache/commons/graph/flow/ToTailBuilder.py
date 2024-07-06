from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *


class ToTailBuilder(ABC):

    def to(
        self, tail: typing.Any
    ) -> MaxFlowAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        return MaxFlowAlgorithmSelector(tail)
