from __future__ import annotations
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.scc.CheriyanMehlhornGabowAlgorithm import *
from src.main.org.apache.commons.graph.scc.KosarajuSharirAlgorithm import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.scc.TarjanAlgorithm import *


class DefaultSccAlgorithmSelector(SccAlgorithmSelector):

    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def applyingTarjan(self) -> typing.Set[typing.Set[typing.Any]]:

        return self.__applying(TarjanAlgorithm(self.__graph))

    def applyingKosarajuSharir1(self, source: typing.Any) -> typing.Set[typing.Any]:

        return KosarajuSharirAlgorithm(self.__graph).perform1(source)

    def applyingKosarajuSharir0(self) -> typing.Set[typing.Set[typing.Any]]:

        return self.__applying(KosarajuSharirAlgorithm(self.__graph))

    def applyingCheriyanMehlhornGabow(self) -> typing.Set[typing.Set[typing.Any]]:

        return self.__applying(CheriyanMehlhornGabowAlgorithm(self.__graph))

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:

        self.__graph = graph

    def __applying(
        self, algorithm: SccAlgorithm[typing.Any]
    ) -> typing.Set[typing.Set[typing.Any]]:

        return algorithm.perform()
