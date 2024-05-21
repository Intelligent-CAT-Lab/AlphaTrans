from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.SynchronizedGraph import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class SynchronizedUndirectedGraph(UndirectedGraph, SynchronizedGraph):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, g: Graph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
