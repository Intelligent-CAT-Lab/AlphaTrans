# Imports Begin
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *
import typing
from abc import ABC

# Imports End


class FromHeadBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def from_(
        self, head: typing.Any
    ) -> ToTailBuilder[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
