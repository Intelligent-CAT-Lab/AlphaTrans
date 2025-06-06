package org.apache.commons.graph.scc;


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

import java.util.Set;

/**
 * {@link SccAlgorithmSelector} implementation
 *
 * @param <V> the Graph vertices type.
 * @param <E> the Graph edges type.
 */
public final class DefaultSccAlgorithmSelector<V, E> implements SccAlgorithmSelector<V, E> {
    /** The graph. */
    private final DirectedGraph<V, E> graph;

    /**
     * Create a default {@link SccAlgorithmSelector} for the given {@link
     * org.apache.commons.graph.Graph}.
     *
     * @param graph the {@link org.apache.commons.graph.Graph}.
     */
    public DefaultSccAlgorithmSelector(final DirectedGraph<V, E> graph) {
        this.graph = graph;
    }

    /**
     * Just calculates the SCC depending on the selected algorithm.
     *
     * @param algorithm
     * @return
     */
    private Set<Set<V>> applying(SccAlgorithm<V> algorithm) {
        return algorithm.perform();
    }

    /** {@inheritDoc} */
    public Set<Set<V>> applyingCheriyanMehlhornGabow() {
        return applying(new CheriyanMehlhornGabowAlgorithm<V, E>(graph));
    }

    /** {@inheritDoc} */
    public Set<Set<V>> applyingKosarajuSharir0() {
        return applying(new KosarajuSharirAlgorithm<V, E>(graph));
    }

    /** {@inheritDoc} */
    public Set<V> applyingKosarajuSharir1(final V source) {
        return new KosarajuSharirAlgorithm<V, E>(graph).perform1(source);
    }

    /** {@inheritDoc} */
    public Set<Set<V>> applyingTarjan() {
        return applying(new TarjanAlgorithm<V, E>(graph));
    }
}
