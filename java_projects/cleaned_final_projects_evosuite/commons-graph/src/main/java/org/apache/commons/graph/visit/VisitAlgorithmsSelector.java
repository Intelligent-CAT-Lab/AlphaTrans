package org.apache.commons.graph.visit;


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

/**
 * Applies different implementations of Graph visitor algorithms.
 *
 * @param <V> the Graph vertices type
 * @param <E> the Graph edges type
 * @param <G> the Graph type
 */
public interface VisitAlgorithmsSelector<V, E, G extends Graph<V, E>> {

    /**
     * Breadth-first search algorithm implementation.
     *
     * @return the breadth first search tree
     */
    Graph<V, E> applyingBreadthFirstSearch0();

    /**
     * Breadth-first search algorithm implementation.
     *
     * @param handler the handler intercepts visit actions
     */
    <O> O applyingBreadthFirstSearch1(GraphVisitHandler<V, E, G, O> handler);

    /**
     * Depth-first search algorithm implementation.
     *
     * @return the depth first search tree
     */
    Graph<V, E> applyingDepthFirstSearch0();

    /**
     * Depth-first search algorithm implementation.
     *
     * @param handler the handler intercepts visit actions
     */
    <O> O applyingDepthFirstSearch1(GraphVisitHandler<V, E, G, O> handler);
}
