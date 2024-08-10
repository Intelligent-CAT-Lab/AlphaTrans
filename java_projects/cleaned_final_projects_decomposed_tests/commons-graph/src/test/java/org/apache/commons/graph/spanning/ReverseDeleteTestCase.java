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

import org.apache.commons.graph.Graph;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.apache.commons.graph.model.BaseWeightedEdge;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;
import org.junit.Test;

/** */
public class ReverseDeleteTestCase {

    

    

    

    /** Test Graph and Reverse-Delete Algorithm */
    

    /** Test Graph and Reverse-Delete Algorithm */
    

    /** Test Graph and Reverse-Delete Algorithm */
    

    /** Test Graph and Reverse-Delete Algorithm */

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

    @Test
    public void testEmptyGraph_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> tree =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testEmptyGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> tree =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(0, tree.getOrder());
    }

    @Test
    public void testEmptyGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> tree =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(0, tree.getOrder());
        assertEquals(0, tree.getSize());
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
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test(expected = NullPointerException.class)
    public void testNullMonoid_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input = null;
        minimumSpanningTree(input);
    }

    @Test(expected = NullPointerException.class)
    public void testNullMonoid_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input = null;
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullMonoid_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input = null;
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .applyingReverseDeleteAlgorithm(null);
    }

    @Test
    public void testVerifyMinimumSpanningTree_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testVerifyMinimumSpanningTree_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testVerifyMinimumSpanningTree_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
    }

    @Test
    public void testVerifyMinimumSpanningTree_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
    }

    @Test
    public void testVerifyMinimumSpanningTree_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
    }

    @Test
    public void testVerifyMinimumSpanningTree_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
    }

    @Test
    public void testVerifyMinimumSpanningTree_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
    }

    @Test
    public void testVerifyMinimumSpanningTree_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        minimumSpanningTree(input);
    }

    @Test
    public void testVerifyMinimumSpanningTree_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testVerifyMinimumSpanningTree_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyMinimumSpanningTree_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testVerifyNotConnectGraph_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testVerifyNotConnectGraph_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testVerifyNotConnectGraph_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
    }

    @Test
    public void testVerifyNotConnectGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
    }

    @Test
    public void testVerifyNotConnectGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
    }

    @Test
    public void testVerifyNotConnectGraph_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        minimumSpanningTree(input);
    }

    @Test
    public void testVerifyNotConnectGraph_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testVerifyNotConnectGraph_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyNotConnectGraph_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testVerifyNotConnectGraph2_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testVerifyNotConnectGraph2_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testVerifyNotConnectGraph2_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
    }

    @Test
    public void testVerifyNotConnectGraph2_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
    }

    @Test
    public void testVerifyNotConnectGraph2_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
    }

    @Test
    public void testVerifyNotConnectGraph2_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
    }

    @Test
    public void testVerifyNotConnectGraph2_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
    }

    @Test
    public void testVerifyNotConnectGraph2_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
    }

    @Test
    public void testVerifyNotConnectGraph2_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
    }

    @Test
    public void testVerifyNotConnectGraph2_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        minimumSpanningTree(input);
    }

    @Test
    public void testVerifyNotConnectGraph2_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testVerifyNotConnectGraph2_test11_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyNotConnectGraph2_test12_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testVerifyNotConnectGraph3_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testVerifyNotConnectGraph3_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testVerifyNotConnectGraph3_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
    }

    @Test
    public void testVerifyNotConnectGraph3_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
    }

    @Test
    public void testVerifyNotConnectGraph3_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
    }

    @Test
    public void testVerifyNotConnectGraph3_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
    }

    @Test
    public void testVerifyNotConnectGraph3_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
    }

    @Test
    public void testVerifyNotConnectGraph3_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 7D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 21D), f);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
    }

    @Test
    public void testVerifyNotConnectGraph3_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 7D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 21D), f);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
    }

    @Test
    public void testVerifyNotConnectGraph3_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 7D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 21D), f);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
    }

    @Test
    public void testVerifyNotConnectGraph3_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 7D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 21D), f);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        minimumSpanningTree(input);
    }

    @Test
    public void testVerifyNotConnectGraph3_test11_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 7D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 21D), f);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void testVerifyNotConnectGraph3_test12_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 7D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 21D), f);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyNotConnectGraph3_test13_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        input.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 7D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 21D), f);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> a", 4D), a);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> e", 4D), e);
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> d", 4D), d);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .applyingReverseDeleteAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }
}