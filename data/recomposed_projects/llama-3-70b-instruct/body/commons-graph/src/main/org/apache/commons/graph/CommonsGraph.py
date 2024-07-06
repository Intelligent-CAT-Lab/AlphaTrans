from __future__ import annotations
import re
import os
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.SynchronizedDirectedGraph import *
from src.main.org.apache.commons.graph.SynchronizedGraph import *
from src.main.org.apache.commons.graph.SynchronizedMutableGraph import *
from src.main.org.apache.commons.graph.SynchronizedUndirectedGraph import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.builder.DefaultLinkedConnectionBuilder import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.builder.LinkedConnectionBuilder import *
from src.main.org.apache.commons.graph.coloring.ColorsBuilder import *
from src.main.org.apache.commons.graph.coloring.DefaultColorsBuilder import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityBuilder import *
from src.main.org.apache.commons.graph.connectivity.DefaultConnectivityBuilder import *
from src.main.org.apache.commons.graph.elo.DefaultRankingSelector import *
from src.main.org.apache.commons.graph.elo.GameResult import *
from src.main.org.apache.commons.graph.elo.RankingSelector import *
from src.main.org.apache.commons.graph.export.DefaultExportSelector import *
from src.main.org.apache.commons.graph.export.NamedExportSelector import *
from src.main.org.apache.commons.graph.flow.DefaultFlowWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.flow.FlowWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.scc.DefaultSccAlgorithmSelector import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.DefaultWeightedEdgesSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.spanning.DefaultSpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.visit.DefaultVisitSourceSelector import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *


class CommonsGraph:

    @staticmethod
    def visit(
        graph: typing.Any,
    ) -> VisitSourceSelector[typing.Any, typing.Any, typing.Any]:
        graph = Assertions.checkNotNull(
            graph, "No algorithm can be applied on null graph!"
        )
        return DefaultVisitSourceSelector(graph)

    @staticmethod
    def synchronize3(
        graph: UndirectedGraph[typing.Any, typing.Any]
    ) -> Graph[typing.Any, typing.Any]:
        return SynchronizedUndirectedGraph(graph)

    @staticmethod
    def synchronize2(
        graph: MutableGraph[typing.Any, typing.Any]
    ) -> Graph[typing.Any, typing.Any]:
        return SynchronizedMutableGraph(graph)

    @staticmethod
    def synchronize1(
        graph: Graph[typing.Any, typing.Any]
    ) -> Graph[typing.Any, typing.Any]:
        return SynchronizedGraph(graph)

    @staticmethod
    def synchronize0(
        graph: DirectedGraph[typing.Any, typing.Any]
    ) -> Graph[typing.Any, typing.Any]:
        return SynchronizedDirectedGraph[typing.Any, typing.Any](graph)

    @staticmethod
    def populate(
        graph: typing.Any,
    ) -> LinkedConnectionBuilder[typing.Any, typing.Any, typing.Any]:
        return DefaultLinkedConnectionBuilder[typing.Any, typing.Any, typing.Any](
            Assertions.checkNotNull(graph, "Impossible to configure null graph!")
        )

    @staticmethod
    def newUndirectedMutableGraph(
        graphConnection: GraphConnection[typing.Any, typing.Any]
    ) -> UndirectedMutableGraph[typing.Any, typing.Any]:
        return CommonsGraph.populate(
            UndirectedMutableGraph[typing.Any, typing.Any]()
        ).withConnections(graphConnection)

    @staticmethod
    def newDirectedMutableGraph(
        graphConnection: GraphConnection[typing.Any, typing.Any]
    ) -> DirectedMutableGraph[typing.Any, typing.Any]:
        return CommonsGraph.populate(
            DirectedMutableGraph[typing.Any, typing.Any]()
        ).withConnections(graphConnection)

    @staticmethod
    def minimumSpanningTree(
        graph: typing.Any,
    ) -> SpanningWeightedEdgeMapperBuilder[typing.Any, typing.Any]:
        graph = Assertions.checkNotNull(
            graph, "Minimum spanning tree can not be calculated on null graph"
        )
        return DefaultSpanningWeightedEdgeMapperBuilder(graph)

    @staticmethod
    def findStronglyConnectedComponent(
        graph: typing.Any,
    ) -> SccAlgorithmSelector[typing.Any, typing.Any]:
        graph = Assertions.checkNotNull(
            graph, "Strongly Connected Component cannot be calculated from a null graph"
        )
        return DefaultSccAlgorithmSelector(graph)

    @staticmethod
    def findShortestPath(
        graph: typing.Any,
    ) -> PathWeightedEdgesBuilder[typing.Any, typing.Any]:
        graph = Assertions.checkNotNull(
            graph, "Shortest path can not be calculated on null graph"
        )
        return DefaultWeightedEdgesSelector(graph)

    @staticmethod
    def findMaxFlow(
        graph: typing.Any,
    ) -> FlowWeightedEdgesBuilder[typing.Any, typing.Any]:
        graph = Assertions.checkNotNull(
            graph, "Max flow can not be calculated on null graph"
        )
        return DefaultFlowWeightedEdgesBuilder(graph)

    @staticmethod
    def findConnectedComponent(
        graph: typing.Any,
    ) -> ConnectivityBuilder[typing.Any, typing.Any]:
        graph = Assertions.checkNotNull(
            graph, "Connected Component cannot be calculated from a null graph"
        )
        return DefaultConnectivityBuilder(graph)

    @staticmethod
    def export(graph: typing.Any) -> NamedExportSelector[typing.Any, typing.Any]:
        graph = Assertions.checkNotNull(graph, "Null graph can not be exported")
        return DefaultExportSelector(graph)

    @staticmethod
    def eloRate(tournamentGraph: typing.Any) -> RankingSelector[typing.Any]:
        tournamentGraph = Assertions.checkNotNull(
            tournamentGraph, "ELO ranking can not be applied on null graph!"
        )
        return DefaultRankingSelector(tournamentGraph)

    @staticmethod
    def coloring(graph: typing.Any) -> ColorsBuilder[typing.Any, typing.Any]:
        graph = Assertions.checkNotNull(
            graph, "Coloring can not be calculated on null graph"
        )
        return DefaultColorsBuilder[typing.Any, typing.Any](graph)

    def __init__(self) -> None:
        pass
