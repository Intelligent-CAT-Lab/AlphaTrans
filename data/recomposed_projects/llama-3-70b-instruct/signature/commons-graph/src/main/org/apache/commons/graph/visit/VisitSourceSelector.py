from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *


class VisitSourceSelector(ABC):

    def from_(
        self, source: typing.Any
    ) -> VisitAlgorithmsSelector[typing.Any, typing.Any, typing.Any]:
        return VisitAlgorithmsSelector(source)
