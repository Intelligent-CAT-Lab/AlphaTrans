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
import org.junit.Test;

public final class PrimTestCase {
    private static void internalPrimAssertion(
            UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input,
            BaseLabeledVertex source,
            MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                    expected) {

        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromSource(source)
                        .applyingPrimAlgorithm(new DoubleWeightBaseOperations());

        assertEquals(expected, actual);
    }

    

    

    

    

    

    /**
     * Test Graph and Prim's solution can be seen on these <a
     * href="http://gauguin.info.uniroma2.it/~italiano/Teaching/Algoritmi/Lezioni/cap12.pdf">slides</a>
     */
    

    /**
     * Test Graph and Prim's solution can be seen on <a
     * href="http://en.wikipedia.org/wiki/Prim%27s_algorithm">Wikipedia</a>
     */

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
                .applyingPrimAlgorithm(new DoubleWeightBaseOperations());
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
                .applyingPrimAlgorithm(new DoubleWeightBaseOperations());
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
                .applyingBoruvkaAlgorithm(null);
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
                .applyingPrimAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test5_decomposed()  {
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
    public void testVerifyMinimumSpanningTree2_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        BaseLabeledVertex g = new BaseLabeledVertex("g");
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        BaseLabeledVertex g = new BaseLabeledVertex("g");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        BaseLabeledVertex g = new BaseLabeledVertex("g");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> c", 14D), c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 30D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 10D), d);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 1D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 4D), g);
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        BaseLabeledVertex g = new BaseLabeledVertex("g");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> c", 14D), c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 30D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 10D), d);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 1D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 4D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        BaseLabeledVertex g = new BaseLabeledVertex("g");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> c", 14D), c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 30D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 10D), d);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 1D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 4D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> c", 14D), c);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 10D), d);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 1D), e);
        expected.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 6D), f);
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 4D), g);
    }

    @Test
    public void testVerifyMinimumSpanningTree2_test11_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        BaseLabeledVertex d = new BaseLabeledVertex("d");
        BaseLabeledVertex e = new BaseLabeledVertex("e");
        BaseLabeledVertex f = new BaseLabeledVertex("f");
        BaseLabeledVertex g = new BaseLabeledVertex("g");
        input.addVertex(a);
        input.addVertex(b);
        input.addVertex(c);
        input.addVertex(d);
        input.addVertex(e);
        input.addVertex(f);
        input.addVertex(g);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> c", 14D), c);
        input.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> d", 30D), d);
        input.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 21D), c);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 10D), d);
        input.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 1D), e);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 6D), f);
        input.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        input.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 4D), g);
        MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> expected =
                new MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        for (BaseLabeledVertex vertex : input.getVertices0()) {
            expected.addVertex(vertex);
        }
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 7D), b);
        expected.addEdge(a, new BaseLabeledWeightedEdge<Double>("a <-> c", 14D), c);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> d", 10D), d);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 1D), e);
        expected.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> f", 6D), f);
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("f <-> g", 4D), g);
        internalPrimAssertion(input, a, expected);
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
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
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
        expected.addEdge(b, new BaseLabeledWeightedEdge<Double>("b <-> e", 7D), e);
        expected.addEdge(c, new BaseLabeledWeightedEdge<Double>("c <-> e", 5D), e);
        expected.addEdge(d, new BaseLabeledWeightedEdge<Double>("d <-> f", 6D), f);
        expected.addEdge(e, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        internalPrimAssertion(input, d, expected);
    }
}