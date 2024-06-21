from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.SynchronizedGraph import *
from src.main.org.apache.commons.graph.UndirectedGraph import *


class SynchronizedUndirectedGraph(UndirectedGraph, SynchronizedGraph):

    __serialVersionUID: int = 2207884889346410427

    def __init__(self, g: Graph[typing.Any, typing.Any]) -> None:

        # Call the superclass's constructor
        super().__init__(g)

        # Call the SynchronizedGraph's constructor
        SynchronizedGraph.__init__(self)
