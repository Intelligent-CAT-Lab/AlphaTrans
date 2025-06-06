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


import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.VertexPair;

import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;

/**
 * A memory-based implementation of a mutable directed Graph.
 *
 * <p>This class is NOT thread safe!
 *
 * @param <V> the Graph vertices type
 * @param <E> the Graph edges type
 */
public class DirectedMutableGraph<V, E> extends BaseMutableGraph<V, E>
        implements DirectedGraph<V, E> {

    private static final long serialVersionUID = 630111985439492792L;

    private final Map<V, Set<V>> inbound = new HashMap<V, Set<V>>();

    private final Map<V, Set<V>> outbound = new HashMap<V, Set<V>>();

    /** {@inheritDoc} */
    @Override
    protected void decorateAddEdge(V head, E e, V tail) {
        inbound.get(tail).add(head);
        outbound.get(head).add(tail);
    }

    /** {@inheritDoc} */
    @Override
    protected void decorateAddVertex(V v) {
        inbound.put(v, new LinkedHashSet<V>());
        outbound.put(v, new LinkedHashSet<V>());
    }

    /** {@inheritDoc} */
    @Override
    protected void decorateRemoveEdge(E e) {
        final VertexPair<V> vertices = getVertices1(e);
        inbound.get(vertices.getTail()).remove(vertices.getHead());
        outbound.get(vertices.getHead()).remove(vertices.getTail());
    }

    /** {@inheritDoc} */
    @Override
    protected void decorateRemoveVertex(V v) {
        inbound.remove(v);
        outbound.remove(v);
    }

    /** {@inheritDoc} */
    public final int getDegree(V v) {
        return getInDegree(v) + getOutDegree(v);
    }

    /** {@inheritDoc} */
    public final Iterable<V> getInbound(V v) {
        return inbound.get(v);
    }

    /** {@inheritDoc} */
    public final int getInDegree(V v) {
        return inbound.get(v).size();
    }

    /** {@inheritDoc} */
    public final Iterable<V> getOutbound(V v) {
        return outbound.get(v);
    }

    /** {@inheritDoc} */
    public final int getOutDegree(V v) {
        return outbound.get(v).size();
    }
}
