# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
import typing
from abc import ABC

# Imports End


class MaxFlowAlgorithmSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def applyingFordFulkerson(self, weightOperations: typing.Any) -> typing.Any:
        pass

    def applyingEdmondsKarp(self, weightOperations: typing.Any) -> typing.Any:
        pass

    # Class Methods End
