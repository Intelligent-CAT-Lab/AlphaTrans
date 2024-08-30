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
import static org.apache.commons.graph.CommonsGraph.newDirectedMutableGraph;
import static org.junit.Assert.assertEquals;

import static java.lang.String.format;
import static java.lang.String.valueOf;

import org.apache.commons.graph.Graph;
import org.apache.commons.graph.GraphException;
import org.apache.commons.graph.Path;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.builder.AbstractGraphConnection;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.apache.commons.graph.model.BaseWeightedEdge;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;
import org.junit.BeforeClass;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public final class BidirDijkstraTestCase {
    private static final int TIMES = 1; // was: 10
    private static final int NODES = 50; // was: 5000
    private static final int EDGES = 1000; // was: 100000
    private static final double EPSILON = 1.0e-6;

    private static DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph;

    private static List<BaseLabeledVertex> vertices;

    private static OrderedMonoid<Double> weightOperations;

    @BeforeClass
    public static void setUp() {
        weightOperations = new DoubleWeightBaseOperations();

        graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>() {
                            Random r = new Random();

                            private boolean addEdge(BaseLabeledVertex src, BaseLabeledVertex dst) {
                                try {
                                    addEdge(
                                                    new BaseLabeledWeightedEdge<Double>(
                                                            format("%s -> %s", src, dst),
                                                            10.0 * r.nextDouble() + 1.0))
                                            .from(src)
                                            .to(dst);
                                    return true;
                                } catch (GraphException e) {
                                    return false;
                                }
                            }

                            public void connect0() {
                                vertices = new ArrayList<BaseLabeledVertex>();
                                for (int i = 0; i < NODES; i++) {
                                    BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
                                    addVertex(v);
                                    vertices.add(v);
                                }

                                for (int i = 0; i < NODES - 1; i++) {
                                    addEdge(vertices.get(i), vertices.get(i + 1));
                                }

                                addEdge(vertices.get(NODES - 1), vertices.get(0));

                                int maxEdges = Math.max(0, EDGES - NODES);
                                for (int i = 0; i < maxEdges; i++) {
                                    while (!addEdge(
                                            vertices.get(r.nextInt(NODES)),
                                            vertices.get(r.nextInt(NODES)))) {}
                                }
                            }
                        });
    }

    

    /**
     * Test Graph and Dijkstra's solution can be seen on <a
     * href="http://en.wikipedia.org/wiki/Dijkstra's_algorithm>Wikipedia</a>
     */

    @Test
    public void testCompareToUnidirectional_test0_decomposed()  {
        Random r = new Random();
        for (int ii = 0; ii < TIMES; ii++) {
            BaseLabeledVertex s = vertices.get(r.nextInt(vertices.size()));
            BaseLabeledVertex t;

            do {
                t = vertices.get(r.nextInt(vertices.size()));
            } while (s.equals(t));

            WeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> pathUni =
                    findShortestPath(graph)
                            .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                            .from(s)
                            .to(t)
                            .applyingDijkstra(weightOperations);

            WeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> pathBi =
                    findShortestPath(graph)
                            .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                            .from(s)
                            .to(t)
                            .applyingBidirectionalDijkstra(weightOperations);

            assertEquals(pathUni.getSize(), pathBi.getSize());
            assertEquals(pathUni.getWeight(), pathBi.getWeight(), EPSILON);
        }
    }

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
                        .applyingBidirectionalDijkstra(new DoubleWeightBaseOperations());
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
                        .applyingBidirectionalDijkstra(new DoubleWeightBaseOperations());
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
                .applyingBidirectionalDijkstra(new DoubleWeightBaseOperations());
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
                .applyingBidirectionalDijkstra(new DoubleWeightBaseOperations());
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
                .applyingBidirectionalDijkstra(null);
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
                .applyingBidirectionalDijkstra(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyThreeNodePath_test0_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testVerifyThreeNodePath_test1_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testVerifyThreeNodePath_test2_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
    }

    @Test
    public void testVerifyThreeNodePath_test3_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
    }

    @Test
    public void testVerifyThreeNodePath_test4_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
    }

    @Test
    public void testVerifyThreeNodePath_test5_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        a, c, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
    }

    @Test
    public void testVerifyThreeNodePath_test6_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        a, c, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
    }

    @Test
    public void testVerifyThreeNodePath_test7_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        a, c, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        findShortestPath(graph);
    }

    @Test
    public void testVerifyThreeNodePath_test8_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        a, c, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testVerifyThreeNodePath_test9_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        a, c, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
    }

    @Test
    public void testVerifyThreeNodePath_test10_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        a, c, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(c);
    }

    @Test
    public void testVerifyThreeNodePath_test11_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        a, c, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(c);
        Path<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> actual =
                findShortestPath(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .from(a)
                        .to(c)
                        .applyingBidirectionalDijkstra(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyThreeNodePath_test12_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        a, c, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a -> b", 14D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b -> c", 10D), c);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(c);
        Path<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> actual =
                findShortestPath(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .from(a)
                        .to(c)
                        .applyingBidirectionalDijkstra(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testVerifyTwoNodePath_test0_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
    }

    @Test
    public void testVerifyTwoNodePath_test1_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
    }

    @Test
    public void testVerifyTwoNodePath_test2_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        graph.addVertex(one);
        graph.addVertex(two);
    }

    @Test
    public void testVerifyTwoNodePath_test3_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
    }

    @Test
    public void testVerifyTwoNodePath_test4_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one, two, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
    }

    @Test
    public void testVerifyTwoNodePath_test5_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one, two, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        findShortestPath(graph);
    }

    @Test
    public void testVerifyTwoNodePath_test6_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one, two, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testVerifyTwoNodePath_test7_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one, two, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
    }

    @Test
    public void testVerifyTwoNodePath_test8_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one, two, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one).to(two);
    }

    @Test
    public void testVerifyTwoNodePath_test9_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one, two, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one).to(two);
        Path<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> actual =
                findShortestPath(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .from(one)
                        .to(two)
                        .applyingBidirectionalDijkstra(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyTwoNodePath_test10_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        graph.addVertex(one);
        graph.addVertex(two);
        graph.addEdge(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        one, two, new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(one, new BaseLabeledWeightedEdge<Double>("1 -> 2", 14D), two);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(one).to(two);
        Path<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> actual =
                findShortestPath(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .from(one)
                        .to(two)
                        .applyingBidirectionalDijkstra(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }
}