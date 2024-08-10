package org.apache.commons.graph.shortestpath;

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

import static org.apache.commons.graph.CommonsGraph.findShortestPath;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import org.apache.commons.graph.Graph;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.apache.commons.graph.model.BaseWeightedEdge;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;
import org.junit.Test;

public final class BellmannFordTestCase {

    /**
     * Test Graph and Dijkstra's solution can be seen on <a
     * href="http://compprog.wordpress.com/2007/11/29/one-source-shortest-path-the-bellman-ford-algorithm/">Wikipedia</a>
     */

    @Test
    public void testFindShortestPathAndVerify_test0_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
    }

    @Test
    public void testFindShortestPathAndVerify_test1_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
    }

    @Test
    public void testFindShortestPathAndVerify_test2_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
    }

    @Test
    public void testFindShortestPathAndVerify_test3_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
    }

    @Test
    public void testFindShortestPathAndVerify_test4_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
    }

    @Test
    public void testFindShortestPathAndVerify_test5_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
    }

    @Test
    public void testFindShortestPathAndVerify_test6_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 6D), two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 5D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 5", -4D), five);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 8D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 2", -2D), two);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 9D), five);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 3", 7D), three);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 1", 2D), one);
    }

    @Test
    public void testFindShortestPathAndVerify_test7_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 6D), two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 5D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 5", -4D), five);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 8D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 2", -2D), two);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 9D), five);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 3", 7D), three);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 1", 2D), one);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        three,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
    }

    @Test
    public void testFindShortestPathAndVerify_test8_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 6D), two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 5D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 5", -4D), five);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 8D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 2", -2D), two);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 9D), five);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 3", 7D), three);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 1", 2D), one);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        three,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        expected.addConnectionInTail(
                four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
    }

    @Test
    public void testFindShortestPathAndVerify_test9_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 6D), two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 5D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 5", -4D), five);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 8D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 2", -2D), two);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 9D), five);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 3", 7D), three);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 1", 2D), one);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        three,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        expected.addConnectionInTail(
                four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        findShortestPath(graph);
    }

    @Test
    public void testFindShortestPathAndVerify_test10_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 6D), two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 5D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 5", -4D), five);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 8D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 2", -2D), two);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 9D), five);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 3", 7D), three);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 1", 2D), one);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        three,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        expected.addConnectionInTail(
                four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testFindShortestPathAndVerify_test11_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 6D), two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 5D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 5", -4D), five);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 8D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 2", -2D), two);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 9D), five);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 3", 7D), three);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 1", 2D), one);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        three,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        expected.addConnectionInTail(
                four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
    }

    @Test
    public void testFindShortestPathAndVerify_test12_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 6D), two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 5D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 5", -4D), five);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 8D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 2", -2D), two);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 9D), five);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 3", 7D), three);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 1", 2D), one);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        three,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        expected.addConnectionInTail(
                four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
        AllVertexPairsShortestPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                allVertexPairsShortestPath =
                        findShortestPath(graph)
                                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                                .from(one)
                                .applyingBelmannFord(new DoubleWeightBaseOperations());
    }

    @Test
    public void testFindShortestPathAndVerify_test13_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 6D), two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 5D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 5", -4D), five);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 8D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 2", -2D), two);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 9D), five);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 3", 7D), three);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 1", 2D), one);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        three,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        expected.addConnectionInTail(
                four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
        AllVertexPairsShortestPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                allVertexPairsShortestPath =
                        findShortestPath(graph)
                                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                                .from(one)
                                .applyingBelmannFord(new DoubleWeightBaseOperations());
        WeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                allVertexPairsShortestPath.findShortestPath(one, three);
    }

    @Test
    public void testFindShortestPathAndVerify_test14_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 6D), two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 5D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 5", -4D), five);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 8D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 2", -2D), two);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 9D), five);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 3", 7D), three);
        graph.addEdge(five, new BaseLabeledWeightedEdge<Double>("5 -> 1", 2D), one);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        three,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 4", 7D), four);
        expected.addConnectionInTail(
                four, new BaseLabeledWeightedEdge<Double>("4 -> 3", -3D), three);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
        AllVertexPairsShortestPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                allVertexPairsShortestPath =
                        findShortestPath(graph)
                                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                                .from(one)
                                .applyingBelmannFord(new DoubleWeightBaseOperations());
        WeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                allVertexPairsShortestPath.findShortestPath(one, three);
        assertEquals(expected, actual);
    }

    @Test
    public void testNotConnectGraph_test0_decomposed()  {
        BaseLabeledVertex a = null;
        BaseLabeledVertex b = null;
        AllVertexPairsShortestPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                allVertexPairsShortestPath = null;
        try {
            UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

            a = new BaseLabeledVertex("a");
            b = new BaseLabeledVertex("b");
            graph.addVertex(a);
            graph.addVertex(b);

            allVertexPairsShortestPath =
                    findShortestPath(graph)
                            .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                            .from(a)
                            .applyingBelmannFord(new DoubleWeightBaseOperations());
        } catch (PathNotFoundException e) {
            fail(e.getMessage());
        }
    }

    @Test(expected = PathNotFoundException.class)
    public void testNotConnectGraph_test1_decomposed()  {
        BaseLabeledVertex a = null;
        BaseLabeledVertex b = null;
        AllVertexPairsShortestPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                allVertexPairsShortestPath = null;
        try {
            UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

            a = new BaseLabeledVertex("a");
            b = new BaseLabeledVertex("b");
            graph.addVertex(a);
            graph.addVertex(b);

            allVertexPairsShortestPath =
                    findShortestPath(graph)
                            .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                            .from(a)
                            .applyingBelmannFord(new DoubleWeightBaseOperations());
        } catch (PathNotFoundException e) {
            fail(e.getMessage());
        }
        allVertexPairsShortestPath.findShortestPath(a, b);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test0_decomposed()  {
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test1_decomposed()  {
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test2_decomposed()  {
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test3_decomposed()  {
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(null)
                .applyingBelmannFord(new DoubleWeightBaseOperations());
    }

    @Test
    public void testNullMonoid_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph = null;
        BaseLabeledVertex a = null;
        try {
            graph =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

            a = new BaseLabeledVertex("a");
            final BaseLabeledVertex b = new BaseLabeledVertex("b");
            graph.addVertex(a);
            graph.addVertex(b);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testNullMonoid_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph = null;
        BaseLabeledVertex a = null;
        try {
            graph =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

            a = new BaseLabeledVertex("a");
            final BaseLabeledVertex b = new BaseLabeledVertex("b");
            graph.addVertex(a);
            graph.addVertex(b);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        findShortestPath(graph);
    }

    @Test
    public void testNullMonoid_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph = null;
        BaseLabeledVertex a = null;
        try {
            graph =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

            a = new BaseLabeledVertex("a");
            final BaseLabeledVertex b = new BaseLabeledVertex("b");
            graph.addVertex(a);
            graph.addVertex(b);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testNullMonoid_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph = null;
        BaseLabeledVertex a = null;
        try {
            graph =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

            a = new BaseLabeledVertex("a");
            final BaseLabeledVertex b = new BaseLabeledVertex("b");
            graph.addVertex(a);
            graph.addVertex(b);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
    }

    @Test(expected = NullPointerException.class)
    public void testNullMonoid_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph = null;
        BaseLabeledVertex a = null;
        try {
            graph =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

            a = new BaseLabeledVertex("a");
            final BaseLabeledVertex b = new BaseLabeledVertex("b");
            graph.addVertex(a);
            graph.addVertex(b);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(a)
                .applyingBelmannFord(null);
    }

    @Test
    public void testNullVertices_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
    }

    @Test
    public void testNullVertices_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null);
        findShortestPath(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(null)
                .applyingBelmannFord(new DoubleWeightBaseOperations());
    }
}