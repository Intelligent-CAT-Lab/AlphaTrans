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
import org.apache.commons.graph.Path;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.apache.commons.graph.model.BaseWeightedEdge;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;
import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

public final class AStarTestCase {

    /**
     * Test Graph and Dijkstra's solution can be seen on <a
     * href="http://en.wikipedia.org/wiki/A*_search_algorithm">Wikipedia</a>
     */

    @Test
    public void testFindShortestPathAndVerify_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
    }

    @Test
    public void testFindShortestPathAndVerify_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testFindShortestPathAndVerify_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testFindShortestPathAndVerify_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
    }

    @Test
    public void testFindShortestPathAndVerify_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
    }

    @Test
    public void testFindShortestPathAndVerify_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
    }

    @Test
    public void testFindShortestPathAndVerify_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
    }

    @Test
    public void testFindShortestPathAndVerify_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
    }

    @Test
    public void testFindShortestPathAndVerify_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
    }

    @Test
    public void testFindShortestPathAndVerify_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        heuristics.put(a, 4D);
        heuristics.put(b, 2D);
        heuristics.put(c, 4D);
        heuristics.put(d, 4.5D);
        heuristics.put(e, 2D);
        heuristics.put(goal, 6D);
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(
                start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
    }

    @Test
    public void testFindShortestPathAndVerify_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        heuristics.put(a, 4D);
        heuristics.put(b, 2D);
        heuristics.put(c, 4D);
        heuristics.put(d, 4.5D);
        heuristics.put(e, 2D);
        heuristics.put(goal, 6D);
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(
                start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addConnectionInTail(
                c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
    }

    @Test
    public void testFindShortestPathAndVerify_test11_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        heuristics.put(a, 4D);
        heuristics.put(b, 2D);
        heuristics.put(c, 4D);
        heuristics.put(d, 4.5D);
        heuristics.put(e, 2D);
        heuristics.put(goal, 6D);
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(
                start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addConnectionInTail(
                c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        findShortestPath(graph);
    }

    @Test
    public void testFindShortestPathAndVerify_test12_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        heuristics.put(a, 4D);
        heuristics.put(b, 2D);
        heuristics.put(c, 4D);
        heuristics.put(d, 4.5D);
        heuristics.put(e, 2D);
        heuristics.put(goal, 6D);
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(
                start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addConnectionInTail(
                c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testFindShortestPathAndVerify_test13_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        heuristics.put(a, 4D);
        heuristics.put(b, 2D);
        heuristics.put(c, 4D);
        heuristics.put(d, 4.5D);
        heuristics.put(e, 2D);
        heuristics.put(goal, 6D);
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(
                start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addConnectionInTail(
                c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start);
    }

    @Test
    public void testFindShortestPathAndVerify_test14_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        heuristics.put(a, 4D);
        heuristics.put(b, 2D);
        heuristics.put(c, 4D);
        heuristics.put(d, 4.5D);
        heuristics.put(e, 2D);
        heuristics.put(goal, 6D);
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(
                start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addConnectionInTail(
                c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start).to(goal);
    }

    @Test
    public void testFindShortestPathAndVerify_test15_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        heuristics.put(a, 4D);
        heuristics.put(b, 2D);
        heuristics.put(c, 4D);
        heuristics.put(d, 4.5D);
        heuristics.put(e, 2D);
        heuristics.put(goal, 6D);
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(
                start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addConnectionInTail(
                c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start).to(goal);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start).to(goal).applyingAStar(new DoubleWeightBaseOperations());
    }

    @Test
    public void testFindShortestPathAndVerify_test16_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        heuristics.put(a, 4D);
        heuristics.put(b, 2D);
        heuristics.put(c, 4D);
        heuristics.put(d, 4.5D);
        heuristics.put(e, 2D);
        heuristics.put(goal, 6D);
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(
                start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addConnectionInTail(
                c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start).to(goal);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start).to(goal).applyingAStar(new DoubleWeightBaseOperations());
        Path<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> actual =
                findShortestPath(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .from(start)
                        .to(goal)
                        .applyingAStar(new DoubleWeightBaseOperations())
                        .withHeuristic(heuristic);
    }

    @Test
    public void testFindShortestPathAndVerify_test17_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        graph.addVertex(start);
        graph.addVertex(a);
        graph.addVertex(b);
        graph.addVertex(c);
        graph.addVertex(d);
        graph.addVertex(e);
        graph.addVertex(goal);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        graph.addEdge(start, new BaseLabeledWeightedEdge<Double>("start <-> d", 2D), d);
        graph.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        graph.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        graph.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        graph.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 3D), e);
        graph.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> goal", 2D), goal);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        heuristics.put(a, 4D);
        heuristics.put(b, 2D);
        heuristics.put(c, 4D);
        heuristics.put(d, 4.5D);
        heuristics.put(e, 2D);
        heuristics.put(goal, 6D);
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        expected.addConnectionInTail(
                start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        expected.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        expected.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addConnectionInTail(
                c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start).to(goal);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(start).to(goal).applyingAStar(new DoubleWeightBaseOperations());
        Path<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> actual =
                findShortestPath(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .from(start)
                        .to(goal)
                        .applyingAStar(new DoubleWeightBaseOperations())
                        .withHeuristic(heuristic);
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
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
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
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
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
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
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
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b);
    }

    @Test
    public void testNotConnectGraph_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b).applyingAStar(new DoubleWeightBaseOperations());
    }

    @Test(expected = PathNotFoundException.class)
    public void testNotConnectGraph_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        graph.addVertex(a);
        graph.addVertex(b);
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic =
                new Heuristic<BaseLabeledVertex, Double>() {

                    public Double applyHeuristic(
                            BaseLabeledVertex current, BaseLabeledVertex goal) {
                        return heuristics.get(current);
                    }
                };
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b).applyingAStar(new DoubleWeightBaseOperations());
        findShortestPath(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(a)
                .to(b)
                .applyingAStar(new DoubleWeightBaseOperations())
                .withHeuristic(heuristic);
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
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null).applyingAStar(new DoubleWeightBaseOperations());
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test5_decomposed()  {
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null);
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null).applyingAStar(new DoubleWeightBaseOperations());
        findShortestPath((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(null)
                .to(null)
                .applyingAStar(new DoubleWeightBaseOperations())
                .withHeuristic(null);
    }

    @Test
    public void testNullHeuristic_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
    }

    @Test
    public void testNullHeuristic_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testNullHeuristic_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(new BaseLabeledVertex("a"));
    }

    @Test
    public void testNullHeuristic_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(new BaseLabeledVertex("a"));
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(new BaseLabeledVertex("a")).to(new BaseLabeledVertex("b"));
    }

    @Test
    public void testNullHeuristic_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(new BaseLabeledVertex("a"));
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(new BaseLabeledVertex("a")).to(new BaseLabeledVertex("b"));
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(new BaseLabeledVertex("a")).to(new BaseLabeledVertex("b")).applyingAStar(new DoubleWeightBaseOperations());
    }

    @Test(expected = NullPointerException.class)
    public void testNullHeuristic_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(new BaseLabeledVertex("a"));
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(new BaseLabeledVertex("a")).to(new BaseLabeledVertex("b"));
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(new BaseLabeledVertex("a")).to(new BaseLabeledVertex("b")).applyingAStar(new DoubleWeightBaseOperations());
        findShortestPath(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(new BaseLabeledVertex("a"))
                .to(new BaseLabeledVertex("b"))
                .applyingAStar(new DoubleWeightBaseOperations())
                .withHeuristic(null);
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
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic = null;
        try {
            graph.addVertex(a);
            graph.addVertex(b);

            heuristic =
                    new Heuristic<BaseLabeledVertex, Double>() {

                        public Double applyHeuristic(
                                BaseLabeledVertex current, BaseLabeledVertex goal) {
                            return heuristics.get(current);
                        }
                    };
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testNullMonoid_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic = null;
        try {
            graph.addVertex(a);
            graph.addVertex(b);

            heuristic =
                    new Heuristic<BaseLabeledVertex, Double>() {

                        public Double applyHeuristic(
                                BaseLabeledVertex current, BaseLabeledVertex goal) {
                            return heuristics.get(current);
                        }
                    };
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        findShortestPath(graph);
    }

    @Test
    public void testNullMonoid_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic = null;
        try {
            graph.addVertex(a);
            graph.addVertex(b);

            heuristic =
                    new Heuristic<BaseLabeledVertex, Double>() {

                        public Double applyHeuristic(
                                BaseLabeledVertex current, BaseLabeledVertex goal) {
                            return heuristics.get(current);
                        }
                    };
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testNullMonoid_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic = null;
        try {
            graph.addVertex(a);
            graph.addVertex(b);

            heuristic =
                    new Heuristic<BaseLabeledVertex, Double>() {

                        public Double applyHeuristic(
                                BaseLabeledVertex current, BaseLabeledVertex goal) {
                            return heuristics.get(current);
                        }
                    };
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
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
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic = null;
        try {
            graph.addVertex(a);
            graph.addVertex(b);

            heuristic =
                    new Heuristic<BaseLabeledVertex, Double>() {

                        public Double applyHeuristic(
                                BaseLabeledVertex current, BaseLabeledVertex goal) {
                            return heuristics.get(current);
                        }
                    };
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
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
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic = null;
        try {
            graph.addVertex(a);
            graph.addVertex(b);

            heuristic =
                    new Heuristic<BaseLabeledVertex, Double>() {

                        public Double applyHeuristic(
                                BaseLabeledVertex current, BaseLabeledVertex goal) {
                            return heuristics.get(current);
                        }
                    };
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b).applyingAStar(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullMonoid_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        final BaseLabeledVertex a = new BaseLabeledVertex("a");
        final BaseLabeledVertex b = new BaseLabeledVertex("b");
        final Map<BaseLabeledVertex, Double> heuristics = new HashMap<BaseLabeledVertex, Double>();
        Heuristic<BaseLabeledVertex, Double> heuristic = null;
        try {
            graph.addVertex(a);
            graph.addVertex(b);

            heuristic =
                    new Heuristic<BaseLabeledVertex, Double>() {

                        public Double applyHeuristic(
                                BaseLabeledVertex current, BaseLabeledVertex goal) {
                            return heuristics.get(current);
                        }
                    };
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(a).to(b).applyingAStar(null);
        findShortestPath(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(a)
                .to(b)
                .applyingAStar(null)
                .withHeuristic(heuristic);
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
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null).applyingAStar(new DoubleWeightBaseOperations());
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> graph =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        findShortestPath(graph);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null);
        findShortestPath(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).from(null).to(null).applyingAStar(new DoubleWeightBaseOperations());
        findShortestPath(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .from(null)
                .to(null)
                .applyingAStar(new DoubleWeightBaseOperations())
                .withHeuristic(null);
    }
}