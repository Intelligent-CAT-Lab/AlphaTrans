from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *


class LinkedConnectionBuilder(ABC):

    def withConnections(
        self, graphConnection: GraphConnection[typing.Any, typing.Any]
    ) -> typing.Any:
        return graphConnection
