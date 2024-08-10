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

public final class BoruvkaTestCase {

    

    

    

    

    

    /** Test Graph and boruvka's solution can be seen on */
    

    /** Test Boruvka's solution on a not-connected graph. */

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
                .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
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
                .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
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
                .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
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
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
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
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
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
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
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
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
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
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
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
        expected.addEdge(f, new BaseLabeledWeightedEdge<Double>("e <-> g", 9D), g);
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
        input.addVertex(new BaseLabeledVertex("D"));
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
        input.addVertex(new BaseLabeledVertex("D"));
        input.addVertex(new BaseLabeledVertex("E"));
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
        input.addVertex(new BaseLabeledVertex("D"));
        input.addVertex(new BaseLabeledVertex("E"));
        input.addVertex(new BaseLabeledVertex("F"));
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
        input.addVertex(new BaseLabeledVertex("D"));
        input.addVertex(new BaseLabeledVertex("E"));
        input.addVertex(new BaseLabeledVertex("F"));
        input.addVertex(new BaseLabeledVertex("G"));
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
        input.addVertex(new BaseLabeledVertex("D"));
        input.addVertex(new BaseLabeledVertex("E"));
        input.addVertex(new BaseLabeledVertex("F"));
        input.addVertex(new BaseLabeledVertex("G"));
        minimumSpanningTree(input);
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
        input.addVertex(new BaseLabeledVertex("D"));
        input.addVertex(new BaseLabeledVertex("E"));
        input.addVertex(new BaseLabeledVertex("F"));
        input.addVertex(new BaseLabeledVertex("G"));
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
    }

    @Test
    public void verifySparseGraphMinimumSpanningTree_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
        input.addVertex(new BaseLabeledVertex("D"));
        input.addVertex(new BaseLabeledVertex("E"));
        input.addVertex(new BaseLabeledVertex("F"));
        input.addVertex(new BaseLabeledVertex("G"));
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
    }

    @Test(expected = IllegalStateException.class)
    public void verifySparseGraphMinimumSpanningTree_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
        input.addVertex(new BaseLabeledVertex("D"));
        input.addVertex(new BaseLabeledVertex("E"));
        input.addVertex(new BaseLabeledVertex("F"));
        input.addVertex(new BaseLabeledVertex("G"));
        minimumSpanningTree(input);
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>());
        minimumSpanningTree(input).whereEdgesHaveWeights(new BaseWeightedEdge<Double>()).fromArbitrarySource();
        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromArbitrarySource()
                .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
    }
}