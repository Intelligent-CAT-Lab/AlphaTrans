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

import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Path;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.apache.commons.graph.model.BaseWeightedEdge;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;
import org.junit.Test;

public final class DijkstraTestCase {

    /**
     * Test Graph and Dijkstra's solution can be seen on <a
     * href="http://en.wikipedia.org/wiki/Dijkstra's_algorithm>Wikipedia</a>
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 6", 14D), six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 7D), two);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 10D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 15D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 4", 11D), four);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 6D), five);
        graph.addEdge(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 6", 14D), six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 7D), two);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 10D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 15D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 4", 11D), four);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 6D), five);
        graph.addEdge(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        five,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 6", 14D), six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 7D), two);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 10D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 15D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 4", 11D), four);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 6D), five);
        graph.addEdge(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        five,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        expected.addConnectionInTail(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        expected.addConnectionInTail(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 6", 14D), six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 7D), two);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 10D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 15D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 4", 11D), four);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 6D), five);
        graph.addEdge(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        five,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        expected.addConnectionInTail(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        expected.addConnectionInTail(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        findShortestPath(graph);
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 6", 14D), six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 7D), two);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 10D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 15D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 4", 11D), four);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 6D), five);
        graph.addEdge(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        five,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        expected.addConnectionInTail(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        expected.addConnectionInTail(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 6", 14D), six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 7D), two);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 10D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 15D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 4", 11D), four);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 6D), five);
        graph.addEdge(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        five,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        expected.addConnectionInTail(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        expected.addConnectionInTail(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 6", 14D), six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 7D), two);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 10D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 15D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 4", 11D), four);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 6D), five);
        graph.addEdge(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        five,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        expected.addConnectionInTail(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        expected.addConnectionInTail(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one).to(five);
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
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 6", 14D), six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 7D), two);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 10D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 15D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 4", 11D), four);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 6D), five);
        graph.addEdge(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        five,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        expected.addConnectionInTail(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        expected.addConnectionInTail(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one).to(five);
        Path<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> actual =
                findShortestPath(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .from(one)
                        .to(five)
                        .applyingDijkstra(new DoubleWeightBaseOperations());
    }

    @Test
    public void testFindShortestPathAndVerify_test15_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        BaseLabeledVertex three = new BaseLabeledVertex("3");
        BaseLabeledVertex four = new BaseLabeledVertex("4");
        BaseLabeledVertex five = new BaseLabeledVertex("5");
        BaseLabeledVertex six = new BaseLabeledVertex("6");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addVertex(three);
        graph.addVertex(four);
        graph.addVertex(five);
        graph.addVertex(six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 6", 14D), six);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 7D), two);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 3", 10D), three);
        graph.addEdge(two, new BaseLabeledWeightedEdge<Double>("2 -> 4", 15D), four);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        graph.addEdge(three, new BaseLabeledWeightedEdge<Double>("3 -> 4", 11D), four);
        graph.addEdge(four, new BaseLabeledWeightedEdge<Double>("4 -> 5", 6D), five);
        graph.addEdge(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one,
                        five,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 3", 9D), three);
        expected.addConnectionInTail(three, new BaseLabeledWeightedEdge<Double>("3 -> 6", 2D), six);
        expected.addConnectionInTail(six, new BaseLabeledWeightedEdge<Double>("6 -> 5", 9D), five);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one).to(five);
        Path<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> actual =
                findShortestPath(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .from(one)
                        .to(five)
                        .applyingDijkstra(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testNotConnectGraph_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testNotConnectGraph_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testNotConnectGraph_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
    }

    @Test
    public void testNotConnectGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
    }

    @Test
    public void testNotConnectGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testNotConnectGraph_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
    }

    @Test
    public void testNotConnectGraph_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b);
    }

    @Test(expected = PathNotFoundException.class)
    public void testNotConnectGraph_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b);
        findShortestPath(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(a)
                .to(b)
                .applyingDijkstra(new DoubleWeightBaseOperations());
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
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test4_decomposed()  {
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(null)
                .to(null)
                .applyingDijkstra(new DoubleWeightBaseOperations());
    }

    @Test
    public void testNullMonoid_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testNullMonoid_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testNullMonoid_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
    }

    @Test
    public void testNullMonoid_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
    }

    @Test
    public void testNullMonoid_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testNullMonoid_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
    }

    @Test
    public void testNullMonoid_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b);
    }

    @Test(expected = NullPointerException.class)
    public void testNullMonoid_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b);
        findShortestPath(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(a)
                .to(b)
                .applyingDijkstra(null);
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
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null);
        findShortestPath(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(null)
                .to(null)
                .applyingDijkstra(new DoubleWeightBaseOperations());
    }
}