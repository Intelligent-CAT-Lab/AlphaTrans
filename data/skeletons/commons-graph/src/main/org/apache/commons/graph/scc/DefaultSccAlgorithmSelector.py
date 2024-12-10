from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.scc.TarjanAlgorithm import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *
from src.main.org.apache.commons.graph.scc.KosarajuSharirAlgorithm import *
from src.main.org.apache.commons.graph.scc.CheriyanMehlhornGabowAlgorithm import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import os
import typing
from typing import *
import io

# Imports End


class DefaultSccAlgorithmSelector(SccAlgorithmSelector):

    # Class Fields Begin
    __graph: DirectedGraph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def applyingTarjan(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    def applyingKosarajuSharir1(self, source: typing.Any) -> typing.Set[typing.Any]:
        pass

    def applyingKosarajuSharir0(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    def applyingCheriyanMehlhornGabow(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        pass

    def __applying(
        self, algorithm: SccAlgorithm[typing.Any]
    ) -> typing.Set[typing.Set[typing.Any]]:
        pass

    # Class Methods End
