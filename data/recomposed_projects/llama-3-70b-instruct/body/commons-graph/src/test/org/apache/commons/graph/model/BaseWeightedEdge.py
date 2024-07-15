from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Mapper import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *


class BaseWeightedEdge:

    __serialVersionUID: int = -2024378704087762740

    def map(self, edge: BaseLabeledWeightedEdge[typing.Any]) -> typing.Any:
        return edge.getWeight()

    def __init__(self) -> None:
        pass
