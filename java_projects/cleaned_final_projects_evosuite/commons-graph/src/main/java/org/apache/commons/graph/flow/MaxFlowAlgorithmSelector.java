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


import org.apache.commons.graph.weight.OrderedMonoid;

/**
 * Maximum Flow algorithm selector
 *
 * @param <V> the Graph vertices type
 * @param <WE> the Graph edges type
 * @param <W> the Graph weight type
 */
public interface MaxFlowAlgorithmSelector<V, WE, W> {

    /**
     * Calculates the maximum flow using the Edmonds-Karp algorithm.
     *
     * @param <WO> the type of weight operations
     * @param weightOperations the class responsible for operations on weights
     * @return the max flow calculate with Edmonds and Karp algorithm
     */
    <WO extends OrderedMonoid<W>> W applyingEdmondsKarp(WO weightOperations);

    /**
     * Calculates the maximum flow using the Ford-Fulkerson method.
     *
     * @param <WO> the type of weight operations
     * @param weightOperations the class responsible for operations on weights
     * @return the max flow calculate with Ford and Furkenson algorithm
     */
    <WO extends OrderedMonoid<W>> W applyingFordFulkerson(WO weightOperations);
}
