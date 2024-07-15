from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class ConnectivityAlgorithmsSelector(ABC):

    def applyingMinimumSpanningTreeAlgorithm(
        self,
    ) -> typing.Collection[typing.List[typing.Any]]:
        return self.minimumSpanningTreeAlgorithm.apply(self.graph)
