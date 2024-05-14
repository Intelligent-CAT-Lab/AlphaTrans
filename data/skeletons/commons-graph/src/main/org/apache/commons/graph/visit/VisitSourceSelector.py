# Imports Begin
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
import typing
from abc import ABC

# Imports End


class VisitSourceSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def from_(
        self, source: typing.Any
    ) -> VisitAlgorithmsSelector[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
