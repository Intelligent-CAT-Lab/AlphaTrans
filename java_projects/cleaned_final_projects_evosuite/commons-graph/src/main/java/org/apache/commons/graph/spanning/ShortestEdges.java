package org.apache.commons.graph.spanning;


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


import org.apache.commons.graph.Graph;
import org.apache.commons.graph.GraphException;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.weight.OrderedMonoid;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

/**
 * The predecessor list is a list of vertex of a {@link org.apache.commons.graph.Graph}. Each
 * vertex' entry contains the index of its predecessor in a path through the graph.
 *
 * @param <V> the Graph vertices type
 * @param <E> the Graph edges type
 * @param <W> the weight type
 */
final class ShortestEdges<V, WE, W> implements Comparator<V> {

    private static <V, WE, W> void addEdgeIgnoringExceptions(
            V vertex, MutableSpanningTree<V, WE, W> spanningTree) {
        try {
            spanningTree.addVertex(vertex);
        } catch (GraphException e) {
        }
    }

    private final Map<V, WE> predecessors = new HashMap<V, WE>();

    private final OrderedMonoid<W> weightOperations;

    private final Mapper<WE, W> weightedEdges;

    private final Graph<V, WE> graph;

    private final V source;

    public ShortestEdges(
            Graph<V, WE> graph,
            V source,
            OrderedMonoid<W> weightOperations,
            Mapper<WE, W> weightedEdges) {
        this.graph = graph;
        this.source = source;
        this.weightOperations = weightOperations;
        this.weightedEdges = weightedEdges;
    }

    /**
     * Add an edge in the predecessor list associated to the input vertex.
     *
     * @param tail the predecessor vertex
     * @param head the edge that succeeds to the input vertex
     */
    public void addPredecessor(V tail, WE head) {
        predecessors.put(tail, head);
    }

    /** {@inheritDoc} */
    public int compare(V left, V right) {
        if (!hasWeight(left) && !hasWeight(right)) {
            return 0;
        } else if (!hasWeight(left)) {
            return 1;
        } else if (!hasWeight(right)) {
            return -1;
        }
        return weightOperations.compare(getWeight(left), getWeight(right));
    }

    /**
     * Creates a spanning tree using the current data.
     *
     * @return a spanning tree using current data
     */
    public SpanningTree<V, WE, W> createSpanningTree() {
        MutableSpanningTree<V, WE, W> spanningTree =
                new MutableSpanningTree<V, WE, W>(weightOperations, weightedEdges);

        for (WE edge : this.predecessors.values()) {
            VertexPair<V> vertices = graph.getVertices1(edge);

            V head = vertices.getHead();
            V tail = vertices.getTail();

            addEdgeIgnoringExceptions(head, spanningTree);
            addEdgeIgnoringExceptions(tail, spanningTree);

            spanningTree.addEdge(head, graph.getEdge(head, tail), tail);
        }

        return spanningTree;
    }

    /**
     * Returns the distance related to input vertex, or null if it does not exist.
     *
     * <p><b>NOTE</b>: the method {@link hasWeight} should be used first to check if the input
     * vertex has an assiged weight.
     *
     * @param vertex the vertex for which the distance has to be retrieved
     * @return the distance related to input vertex, or null if it does not exist
     */
    public W getWeight(V vertex) {
        if (source.equals(vertex)) {
            return weightOperations.identity();
        }

        WE edge = predecessors.get(vertex);

        if (edge == null) {
            return null;
        }

        return weightedEdges.map(edge);
    }

    /**
     * Checks if there is a weight related to the input {@code Vertex}.
     *
     * @param vertex the input {@code Vertex}
     * @return true if there is a weight for the input {@code Vertex}, false otherwise
     */
    public boolean hasWeight(V vertex) {
        return predecessors.containsKey(vertex);
    }

    /**
     * Checks the predecessor list has no elements.
     *
     * @return true, if the predecessor list has no elements, false otherwise.
     */
    public boolean isEmpty() {
        return predecessors.isEmpty();
    }

    /** {@inheritDoc} */
    @Override
    public String toString() {
        return predecessors.toString();
    }
}
