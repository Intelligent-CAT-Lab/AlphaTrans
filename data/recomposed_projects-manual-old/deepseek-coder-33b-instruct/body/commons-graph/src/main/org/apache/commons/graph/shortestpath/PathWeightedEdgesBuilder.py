from __future__ import annotations
import re
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *


class PathWeightedEdgesBuilder(ABC):

    def whereEdgesHaveWeights(
        self, weightedEdges: typing.Any
    ) -> PathSourceSelector[typing.Any, typing.Any, typing.Any]:
        pass
