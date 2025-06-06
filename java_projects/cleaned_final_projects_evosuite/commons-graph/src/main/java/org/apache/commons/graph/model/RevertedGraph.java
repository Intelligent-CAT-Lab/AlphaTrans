package org.apache.commons.graph.model;


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


import static org.apache.commons.graph.utils.Assertions.checkNotNull;

import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.VertexPair;

/**
 * An adapted class that mirrors {@link DirectedGraph} instances, inverting vertices relationships.
 *
 * <p>It is useful for algorithms such as Kosaraju-Sharir for strongly connected components search.
 *
 * @param <V> the Graph vertices type
 * @param <E> the Graph edges type
 */
public final class RevertedGraph<V, E> implements DirectedGraph<V, E> {

    private static final long serialVersionUID = 5867643705350331891L;

    /** The DirectedGraph has to be adapted. */
    private final DirectedGraph<V, E> directedGraph;

    /**
     * Build a new DirectedGraph mirror.
     *
     * @param directedGraph the DirectedGraph has to be adapted
     */
    public RevertedGraph(DirectedGraph<V, E> directedGraph) {
        directedGraph = checkNotNull(directedGraph, "Adapted DirectedGraph must be not null");
        this.directedGraph = directedGraph;
    }

    /** {@inheritDoc} */
    public boolean containsEdge(E e) {
        return directedGraph.containsEdge(e);
    }

    /** {@inheritDoc} */
    public boolean containsVertex(V v) {
        return directedGraph.containsVertex(v);
    }

    /** {@inheritDoc} */
    public Iterable<V> getConnectedVertices(V v) {
        return directedGraph.getConnectedVertices(v);
    }

    /** {@inheritDoc} */
    public int getDegree(V v) {
        return directedGraph.getDegree(v);
    }

    /** {@inheritDoc} */
    public E getEdge(V source, V target) {
        return directedGraph.getEdge(target, source);
    }

    /** {@inheritDoc} */
    public Iterable<E> getEdges() {
        return directedGraph.getEdges();
    }

    /** {@inheritDoc} */
    public Iterable<V> getInbound(V v) {
        return directedGraph.getOutbound(v);
    }

    /** {@inheritDoc} */
    public int getInDegree(V v) {
        return directedGraph.getOutDegree(v);
    }

    /** {@inheritDoc} */
    public int getOrder() {
        return directedGraph.getOrder();
    }

    /** {@inheritDoc} */
    public Iterable<V> getOutbound(V v) {
        return directedGraph.getInbound(v);
    }

    /** {@inheritDoc} */
    public int getOutDegree(V v) {
        return directedGraph.getOutDegree(v);
    }

    /** {@inheritDoc} */
    public int getSize() {
        return directedGraph.getSize();
    }

    /** {@inheritDoc} */
    public Iterable<V> getVertices0() {
        return directedGraph.getVertices0();
    }

    /** {@inheritDoc} */
    public VertexPair<V> getVertices1(E e) {
        VertexPair<V> directedVertexPair = directedGraph.getVertices1(e);
        return new VertexPair<V>(directedVertexPair.getTail(), directedVertexPair.getHead());
    }
}
