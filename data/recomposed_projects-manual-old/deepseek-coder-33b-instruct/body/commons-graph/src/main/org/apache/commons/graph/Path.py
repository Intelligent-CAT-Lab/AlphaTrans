from __future__ import annotations
import re
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *


class Path(ABC):

    def getTarget(self) -> typing.Any:
        pass

    def getSource(self) -> typing.Any:
        pass
