package org.apache.commons.graph.spanning;

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

import static org.apache.commons.graph.CommonsGraph.minimumSpanningTree;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import org.apache.commons.graph.Graph;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.apache.commons.graph.model.BaseWeightedEdge;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;
import org.junit.Ignore;
import org.junit.Test;

public final class KruskalTestCase {

    /**
     * Test the algorithm with a disconnected graph on 4 vertices. In this case, we expect the
     * Minimum spanning "tree" to actually be a minimum spanning forest with 2 components.
     */
    

    

    

    

    

    

    /** Test the minimum spanning tree on a path graph with 4 vertices and non-uniform weights. */
    

    /** Test the minimum spanning tree on a path graph with 4 vertices and unit weights. */
    

    /**
     * Test Graph and Prim's solution can be seen on <a
     * href="http://en.wikipedia.org/wiki/Prim%27s_algorithm">Wikipedia</a>
     */
    

    /**
     * Test Graph and Prim's solution can be seen on <a
     * href="http://en.wikipedia.org/wiki/Prim%27s_algorithm">Wikipedia</a>
     */

    @Test
    public void testDisconnectedMinimumSpanningTree_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test11_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testDisconnectedMinimumSpanningTree_test12_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testEmptyGraph_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
    }

    @Test
    public void testEmptyGraph_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test(expected = IllegalStateException.class)
    public void testEmptyGraph_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
    }

    @Test(expected = IllegalStateException.class)
    public void testEmptyGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromArbitrarySource()
                .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testNotExistVertex_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
    }

    @Test
    public void testNotExistVertex_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test(expected = IllegalStateException.class)
    public void testNotExistVertex_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromSource(new BaseLabeledVertex("NOT EXIST"));
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test0_decomposed()  {
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test1_decomposed()  {
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test2_decomposed()  {
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test3_decomposed()  {
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromArbitrarySource()
                .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testNullMonoid_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input = null;
        BaseLabeledVertex a = null;
        try {
            input =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
            a = new BaseLabeledVertex("A");
            input.addVertex(a);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testNullMonoid_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input = null;
        BaseLabeledVertex a = null;
        try {
            input =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
            a = new BaseLabeledVertex("A");
            input.addVertex(a);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        minimumSpanningTree(input);
    }

    @Test
    public void testNullMonoid_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input = null;
        BaseLabeledVertex a = null;
        try {
            input =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
            a = new BaseLabeledVertex("A");
            input.addVertex(a);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testNullMonoid_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input = null;
        BaseLabeledVertex a = null;
        try {
            input =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
            a = new BaseLabeledVertex("A");
            input.addVertex(a);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromSource(a);
    }

    @Test(expected = NullPointerException.class)
    public void testNullMonoid_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input = null;
        BaseLabeledVertex a = null;
        try {
            input =
                    new UndirectedMutableGraph<
                            BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
            a = new BaseLabeledVertex("A");
            input.addVertex(a);
        } catch (NullPointerException e) {
            fail(e.getMessage());
        }
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromSource(a);
        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromSource(a)
                .applyingKruskalAlgorithm(null);
    }

    @Test
    public void testNullVertex_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
    }

    @Test
    public void testNullVertex_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertex_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromSource(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertex_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromSource(null);
        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromSource(null)
                .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test11_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testP4NonUniformWeightsMinimumSpanningTree_test12_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 4D), b);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 2D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Ignore
    @Test
    public void testP4UniformWeightsMinimumSpanningTree_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 1D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 1D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 1D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 1D), b);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 1D), c);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 1D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        minimumSpanningTree(input);
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test11_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyNotConnectedMinimumSpanningTree_test12_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 8D), c);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> d", 9D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 15D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 8D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 11D), g);
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 8D), c);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> d", 9D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 15D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 8D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 11D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 8D), c);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> d", 9D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 15D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 8D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 11D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 9D), e);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        expected.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test11_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 8D), c);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> d", 9D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 15D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 8D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 11D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 9D), e);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        expected.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        minimumSpanningTree(input);
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test12_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 8D), c);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> d", 9D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 15D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 8D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 11D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 9D), e);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        expected.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test13_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 8D), c);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> d", 9D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 15D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 8D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 11D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 9D), e);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        expected.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test14_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 8D), c);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> d", 9D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 15D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 8D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 11D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 9D), e);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        expected.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyWikipediaMinimumSpanningTree_test15_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("A");
        BaseLabeledVertex b = new BaseLabeledVertex("B");
        BaseLabeledVertex c = new BaseLabeledVertex("C");
        BaseLabeledVertex d = new BaseLabeledVertex("D");
        BaseLabeledVertex e = new BaseLabeledVertex("E");
        BaseLabeledVertex f = new BaseLabeledVertex("F");
        BaseLabeledVertex g = new BaseLabeledVertex("G");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 8D), c);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> d", 9D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 15D), e);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 8D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 11D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 5D), d);
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 9D), e);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        expected.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingKruskalAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }
}