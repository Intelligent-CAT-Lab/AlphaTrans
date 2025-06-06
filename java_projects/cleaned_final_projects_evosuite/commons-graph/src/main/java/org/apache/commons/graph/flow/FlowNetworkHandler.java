package org.apache.commons.graph.flow;


/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


import static org.apache.commons.graph.visit.VisitState.ABORT;
import static org.apache.commons.graph.visit.VisitState.CONTINUE;
import static org.apache.commons.graph.visit.VisitState.SKIP;

import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.shortestpath.PredecessorsList;
import org.apache.commons.graph.visit.BaseGraphVisitHandler;
import org.apache.commons.graph.visit.VisitState;
import org.apache.commons.graph.weight.OrderedMonoid;

import java.util.HashMap;
import java.util.Map;

/**
 * Provides standard operations for max-flow algorithms, like Ford-Fulkerson or Edmonds-Karp.
 *
 * @param <V> the vertex type
 * @param <W> the weight type
 */
final class FlowNetworkHandler<V, E, W>
        extends BaseGraphVisitHandler<V, E, DirectedGraph<V, E>, W> {

    private final DirectedGraph<V, E> flowNetwork;

    private final V source;

    private final V target;

    private final OrderedMonoid<W> weightOperations;

    private final Mapper<E, W> weightedEdges;

    private W maxFlow;

    private final Map<E, W> residualEdgeCapacities = new HashMap<E, W>();

    private PredecessorsList<V, E, W> predecessors;

    private boolean foundAugmentingPath;

    FlowNetworkHandler(
            DirectedGraph<V, E> flowNetwork,
            V source,
            V target,
            OrderedMonoid<W> weightOperations,
            Mapper<E, W> weightedEdges) {
        this.flowNetwork = flowNetwork;
        this.source = source;
        this.target = target;
        this.weightOperations = weightOperations;
        this.weightedEdges = weightedEdges;

        maxFlow = weightOperations.identity();

        for (E edge : flowNetwork.getEdges()) {
            residualEdgeCapacities.put(edge, weightedEdges.map(edge));
        }

        predecessors = null;
    }

    /** {@inheritDoc} */
    @Override
    public VisitState discoverEdge(V head, E edge, V tail) {
        W residualEdgeCapacity = residualEdgeCapacities.get(edge);
        if (weightOperations.compare(residualEdgeCapacity, weightOperations.identity()) <= 0) {
            return SKIP;
        }
        predecessors.addPredecessor(tail, head);
        return CONTINUE;
    }

    /** {@inheritDoc} */
    @Override
    public void discoverGraph(DirectedGraph<V, E> graph) {
        predecessors = new PredecessorsList<V, E, W>(graph, weightOperations, weightedEdges);
        foundAugmentingPath = false;
    }

    /** {@inheritDoc} */
    public VisitState discoverVertex(V vertex) {
        return finishVertex(vertex);
    }

    /** {@inheritDoc} */
    public VisitState finishVertex(V vertex) {
        if (vertex.equals(target)) {
            foundAugmentingPath = true;
            return ABORT;
        }
        return CONTINUE;
    }

    /**
     * Checks whether there is an augmenting path in the flow network, given the current residual
     * capacities.
     *
     * @return true if there is an augmenting path, false otherwise
     */
    boolean hasAugmentingPath() {
        return foundAugmentingPath;
    }

    @Override
    public W onCompleted() {
        return maxFlow;
    }

    /**
     * Updates the residual capacities in the flow network, based on the most recent augmenting
     * path.
     */
    void updateResidualNetworkWithCurrentAugmentingPath() {
        WeightedPath<V, E, W> augmentingPath = predecessors.buildPath0(source, target);

        W flowIncrement = null;
        for (E edge : augmentingPath.getEdges()) {
            W edgeCapacity = residualEdgeCapacities.get(edge);
            if (flowIncrement == null
                    || weightOperations.compare(edgeCapacity, flowIncrement) < 0) {
                flowIncrement = edgeCapacity;
            }
        }

        maxFlow = weightOperations.append(maxFlow, flowIncrement);
        for (E edge : augmentingPath.getEdges()) {
            W directCapacity = residualEdgeCapacities.get(edge);
            residualEdgeCapacities.put(
                    edge,
                    weightOperations.append(
                            directCapacity, weightOperations.inverse(flowIncrement)));

            VertexPair<V> vertexPair = flowNetwork.getVertices1(edge);
            E inverseEdge = flowNetwork.getEdge(vertexPair.getTail(), vertexPair.getHead());
            W inverseCapacity = residualEdgeCapacities.get(inverseEdge);
            residualEdgeCapacities.put(
                    inverseEdge, weightOperations.append(inverseCapacity, flowIncrement));
        }
    }
}
