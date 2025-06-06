package org.apache.commons.graph.builder;


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


/**
 * TODO Fillme!!
 *
 * @param <V> the Graph vertices type
 * @param <E> the Graph edges type
 */
public interface GraphConnector<V, E> {

    /**
     * Adds a new edge to graph.
     *
     * @param <A> the Graph edges type
     * @param arc the edge to add.
     * @return the {@link HeadVertexConnector}
     */
    <A extends E> HeadVertexConnector<V, E> addEdge(A arc);

    /**
     * Adds a new vertex to graph.
     *
     * @param <N> the Graph vertices type
     * @param node the vertex to add
     * @return the vertex added
     */
    <N extends V> N addVertex(N node);
}
