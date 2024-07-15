from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class MaxFlowAlgorithmSelector(ABC):

    def applyingFordFulkerson(self, weightOperations: typing.Any) -> typing.Any:
        return weightOperations

    def applyingEdmondsKarp(self, weightOperations: typing.Any) -> typing.Any:
        return EdmondsKarp(weightOperations).apply(self)
