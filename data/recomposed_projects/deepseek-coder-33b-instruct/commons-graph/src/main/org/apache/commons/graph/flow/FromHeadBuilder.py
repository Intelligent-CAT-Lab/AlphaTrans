from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *


class FromHeadBuilder(ABC):

    def from_(
        self, head: typing.Any
    ) -> ToTailBuilder[typing.Any, typing.Any, typing.Any]:

        pass
