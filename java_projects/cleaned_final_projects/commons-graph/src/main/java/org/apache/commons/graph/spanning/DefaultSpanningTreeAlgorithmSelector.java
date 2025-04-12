package org.apache.commons.graph.spanning;

/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import static org.apache.commons.graph.utils.Assertions.checkNotNull;
import static org.apache.commons.graph.utils.Assertions.checkState;

import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.collections.DisjointSet;
import org.apache.commons.graph.collections.FibonacciHeap;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.weight.OrderedMonoid;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

/**
 * {@link SpanningTreeAlgorithmSelector} implementation.
 *
 * @param <V> the Graph vertices type
 * @param <W> the weight type
 * @param <WE> the Graph weighted edges type
 */
final class DefaultSpanningTreeAlgorithmSelector<V, W, WE>
        implements SpanningTreeAlgorithmSelector<V, W, WE> {
    /** The graph. */
    private final Graph<V, WE> graph;

    private final Mapper<WE, W> weightedEdges;

    /** The start vertex. */
    private final V source;

    /**
     * Creates a default {@link SpanningTreeAlgorithmSelector} for the given {@link Graph} and start
     * vertex.
     *
     * @param graph the {@link Graph} to be used.
     * @param source the start vertex.
     */
    public DefaultSpanningTreeAlgorithmSelector(
            final Graph<V, WE> graph, Mapper<WE, W> weightedEdges, final V source) {
        this.graph = graph;
        this.weightedEdges = weightedEdges;
        this.source = source;
    }

    /** {@inheritDoc} */
    public <WO extends OrderedMonoid<W>> SpanningTree<V, WE, W> applyingBoruvkaAlgorithm(
            WO weightOperations) {
        /*
         * <pre>
         * procedure Boruvka MST(G(V; E)):
         *     T <= V
         *     while |T| < n do
         *         for all connected component C in T do
         *             e <= the smallest-weight edge from C to another component in T
         *             if e not exists in T then
         *                 T <= T u {e}
         *             end if
         *         end for
         *     end while
         * <pre>
         */

        checkNotNull(
                weightOperations,
                "The Boruvka algorithm cannot be calculated with null weight operations");

        final MutableSpanningTree<V, WE, W> spanningTree =
                new MutableSpanningTree<V, WE, W>(weightOperations, weightedEdges);

        final Set<SuperVertex<V, W, WE>> components =
                new HashSet<SuperVertex<V, W, WE>>(graph.getOrder());

        final Map<V, SuperVertex<V, W, WE>> mapping =
                new HashMap<V, SuperVertex<V, W, WE>>(graph.getOrder());

        for (V v : graph.getVertices0()) {
            final SuperVertex<V, W, WE> sv =
                    new SuperVertex<V, W, WE>(
                            v,
                            graph,
                            new WeightedEdgesComparator<W, WE>(weightOperations, weightedEdges));

            components.add(sv);

            mapping.put(v, sv);

            spanningTree.addVertex(v);
        }

        while (components.size() > 1) {
            final List<WE> edges = new LinkedList<WE>();
            for (SuperVertex<V, W, WE> sv : components) {
                final WE edge = sv.getMinimumWeightEdge();
                if (edge != null) {
                    edges.add(edge);
                }
            }

            checkState(!edges.isEmpty() || components.size() == 1, "unconnected graph");

            for (final WE edge : edges) {
                final VertexPair<V> pair = graph.getVertices1(edge);
                final V head = pair.getHead();
                final V tail = pair.getTail();

                final SuperVertex<V, W, WE> headSv = mapping.get(head);
                final SuperVertex<V, W, WE> tailSv = mapping.get(tail);

                if (headSv != tailSv) {
                    headSv.merge(tailSv);

                    for (final V v : tailSv) {
                        mapping.put(v, headSv);
                    }

                    components.remove(tailSv);

                    if (spanningTree.getVertices1(edge) == null) {
                        spanningTree.addEdge(head, edge, tail);
                    }
                }
            }
        }

        return spanningTree;
    }

    /** {@inheritDoc} */
    public <WO extends OrderedMonoid<W>> SpanningTree<V, WE, W> applyingKruskalAlgorithm(
            WO weightOperations) {
        checkNotNull(
                weightOperations,
                "The Kruskal algorithm cannot be calculated with null weight operations");
        final Set<V> settledNodes = new HashSet<V>();

        final Queue<WE> orderedEdges =
                new FibonacciHeap<WE>(
                        new WeightedEdgesComparator<W, WE>(weightOperations, weightedEdges));

        for (WE edge : graph.getEdges()) {
            orderedEdges.add(edge);
        }

        final DisjointSet<V> disjointSet = new DisjointSet<V>();

        final MutableSpanningTree<V, WE, W> spanningTree =
                new MutableSpanningTree<V, WE, W>(weightOperations, weightedEdges);

        for (V v : graph.getVertices0()) {
            spanningTree.addVertex(v);
        }

        while (!orderedEdges.isEmpty() && settledNodes.size() < graph.getOrder()) {
            WE edge = orderedEdges.remove();

            VertexPair<V> vertices = graph.getVertices1(edge);
            V head = vertices.getHead();
            V tail = vertices.getTail();
            settledNodes.add(head);
            settledNodes.add(tail);

            if (!disjointSet.find1(head).equals(disjointSet.find1(tail))) {
                disjointSet.union(head, tail);
                spanningTree.addEdge(head, edge, tail);
            }
        }

        return spanningTree;
    }

    /** {@inheritDoc} */
    public <WO extends OrderedMonoid<W>> SpanningTree<V, WE, W> applyingPrimAlgorithm(
            WO weightOperations) {
        checkNotNull(
                weightOperations,
                "The Prim algorithm cannot be calculated with null weight operations");

        final ShortestEdges<V, WE, W> shortestEdges =
                new ShortestEdges<V, WE, W>(graph, source, weightOperations, weightedEdges);

        final Queue<V> unsettledNodes = new FibonacciHeap<V>(shortestEdges);
        unsettledNodes.add(source);

        final Set<WE> settledEdges = new HashSet<WE>();

        while (!unsettledNodes.isEmpty()) {
            V vertex = unsettledNodes.remove();

            for (V v : graph.getConnectedVertices(vertex)) {
                WE edge = graph.getEdge(vertex, v);
                boolean weightLessThanCurrent =
                        !shortestEdges.hasWeight(v)
                                || weightOperations.compare(
                                                weightedEdges.map(edge), shortestEdges.getWeight(v))
                                        < 0;
                if (settledEdges.add(edge) && weightLessThanCurrent) {
                    if (!unsettledNodes.contains(v)) {
                        unsettledNodes.add(v);
                    }

                    shortestEdges.addPredecessor(v, edge);
                }
            }
        }

        return shortestEdges.createSpanningTree();
    }
}
