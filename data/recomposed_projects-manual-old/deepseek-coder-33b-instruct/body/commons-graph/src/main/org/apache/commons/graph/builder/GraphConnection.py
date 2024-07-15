from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.builder.GraphConnector import *


class GraphConnection(ABC):

    def connect(self, grapher: GraphConnector[typing.Any, typing.Any]) -> None:
        pass
