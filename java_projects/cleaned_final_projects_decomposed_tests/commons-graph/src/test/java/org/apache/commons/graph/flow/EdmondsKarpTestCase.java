package org.apache.commons.graph.flow;

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

import static org.apache.commons.graph.CommonsGraph.findMaxFlow;
import static org.apache.commons.graph.CommonsGraph.newDirectedMutableGraph;
import static org.junit.Assert.assertEquals;

import org.apache.commons.graph.builder.AbstractGraphConnection;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.apache.commons.graph.model.BaseWeightedEdge;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.junit.Test;

/**
 * Test for Edmonds-Karp algorithm implementation. The test graph is available on <a
 * href="http://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm#Example">Wikipedia</a>.
 */
public class EdmondsKarpTestCase {

    @Test
    public void testFindMaxFlowAndVerify_test0_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testFindMaxFlowAndVerify_test1_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
    }

    @Test
    public void testFindMaxFlowAndVerify_test2_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> D", 3))
                                        .from(a)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> A", 3))
                                        .from(c)
                                        .to(a);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1))
                                        .from(c)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> E", 2))
                                        .from(c)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> E", 2))
                                        .from(d)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> F", 6))
                                        .from(d)
                                        .to(f);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> B", 1))
                                        .from(e)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> G", 1))
                                        .from(e)
                                        .to(g);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("F -> G", 9))
                                        .from(f)
                                        .to(g);
                            }
                        });
    }

    @Test
    public void testFindMaxFlowAndVerify_test3_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> D", 3))
                                        .from(a)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> A", 3))
                                        .from(c)
                                        .to(a);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1))
                                        .from(c)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> E", 2))
                                        .from(c)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> E", 2))
                                        .from(d)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> F", 6))
                                        .from(d)
                                        .to(f);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> B", 1))
                                        .from(e)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> G", 1))
                                        .from(e)
                                        .to(g);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("F -> G", 9))
                                        .from(f)
                                        .to(g);
                            }
                        });
        final Integer expected = 5;
        findMaxFlow(graph);
    }

    @Test
    public void testFindMaxFlowAndVerify_test4_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> D", 3))
                                        .from(a)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> A", 3))
                                        .from(c)
                                        .to(a);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1))
                                        .from(c)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> E", 2))
                                        .from(c)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> E", 2))
                                        .from(d)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> F", 6))
                                        .from(d)
                                        .to(f);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> B", 1))
                                        .from(e)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> G", 1))
                                        .from(e)
                                        .to(g);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("F -> G", 9))
                                        .from(f)
                                        .to(g);
                            }
                        });
        final Integer expected = 5;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test
    public void testFindMaxFlowAndVerify_test5_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> D", 3))
                                        .from(a)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> A", 3))
                                        .from(c)
                                        .to(a);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1))
                                        .from(c)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> E", 2))
                                        .from(c)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> E", 2))
                                        .from(d)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> F", 6))
                                        .from(d)
                                        .to(f);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> B", 1))
                                        .from(e)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> G", 1))
                                        .from(e)
                                        .to(g);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("F -> G", 9))
                                        .from(f)
                                        .to(g);
                            }
                        });
        final Integer expected = 5;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
    }

    @Test
    public void testFindMaxFlowAndVerify_test6_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> D", 3))
                                        .from(a)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> A", 3))
                                        .from(c)
                                        .to(a);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1))
                                        .from(c)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> E", 2))
                                        .from(c)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> E", 2))
                                        .from(d)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> F", 6))
                                        .from(d)
                                        .to(f);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> B", 1))
                                        .from(e)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> G", 1))
                                        .from(e)
                                        .to(g);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("F -> G", 9))
                                        .from(f)
                                        .to(g);
                            }
                        });
        final Integer expected = 5;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
    }

    @Test
    public void testFindMaxFlowAndVerify_test7_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> D", 3))
                                        .from(a)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> A", 3))
                                        .from(c)
                                        .to(a);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1))
                                        .from(c)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> E", 2))
                                        .from(c)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> E", 2))
                                        .from(d)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> F", 6))
                                        .from(d)
                                        .to(f);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> B", 1))
                                        .from(e)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> G", 1))
                                        .from(e)
                                        .to(g);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("F -> G", 9))
                                        .from(f)
                                        .to(g);
                            }
                        });
        final Integer expected = 5;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(g)
                        .applyingEdmondsKarp(new IntegerWeightBaseOperations());
    }

    @Test
    public void testFindMaxFlowAndVerify_test8_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> D", 3))
                                        .from(a)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> A", 3))
                                        .from(c)
                                        .to(a);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1))
                                        .from(c)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> E", 2))
                                        .from(c)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> E", 2))
                                        .from(d)
                                        .to(e);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("D -> F", 6))
                                        .from(d)
                                        .to(f);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> B", 1))
                                        .from(e)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("E -> G", 1))
                                        .from(e)
                                        .to(g);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("F -> G", 9))
                                        .from(f)
                                        .to(g);
                            }
                        });
        final Integer expected = 5;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(g)
                        .applyingEdmondsKarp(new IntegerWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testNullGraph_test0_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testNullGraph_test1_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test2_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test3_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test4_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test5_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test6_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
        findMaxFlow(
                        (DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                .from(a)
                .to(g)
                .applyingEdmondsKarp(new IntegerWeightBaseOperations());
    }

    @Test
    public void testNullVertices_test0_decomposed()  {
        final BaseLabeledVertex a = null;
        final BaseLabeledVertex g = null;
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
    }

    @Test
    public void testNullVertices_test1_decomposed()  {
        final BaseLabeledVertex a = null;
        final BaseLabeledVertex g = null;
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test2_decomposed()  {
        final BaseLabeledVertex a = null;
        final BaseLabeledVertex g = null;
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test3_decomposed()  {
        final BaseLabeledVertex a = null;
        final BaseLabeledVertex g = null;
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test4_decomposed()  {
        final BaseLabeledVertex a = null;
        final BaseLabeledVertex g = null;
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
        findMaxFlow(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                .from(a)
                .to(g)
                .applyingEdmondsKarp(new IntegerWeightBaseOperations());
    }

    @Test
    public void testSparse_test0_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testSparse_test1_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
    }

    @Test
    public void testSparse_test2_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(new BaseLabeledVertex("D"));
                                addVertex(new BaseLabeledVertex("E"));
                                addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                            }
                        });
    }

    @Test
    public void testSparse_test3_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(new BaseLabeledVertex("D"));
                                addVertex(new BaseLabeledVertex("E"));
                                addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
    }

    @Test
    public void testSparse_test4_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(new BaseLabeledVertex("D"));
                                addVertex(new BaseLabeledVertex("E"));
                                addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test
    public void testSparse_test5_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(new BaseLabeledVertex("D"));
                                addVertex(new BaseLabeledVertex("E"));
                                addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
    }

    @Test
    public void testSparse_test6_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(new BaseLabeledVertex("D"));
                                addVertex(new BaseLabeledVertex("E"));
                                addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
    }

    @Test
    public void testSparse_test7_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(new BaseLabeledVertex("D"));
                                addVertex(new BaseLabeledVertex("E"));
                                addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(g)
                        .applyingEdmondsKarp(new IntegerWeightBaseOperations());
    }

    @Test
    public void testSparse_test8_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(new BaseLabeledVertex("D"));
                                addVertex(new BaseLabeledVertex("E"));
                                addVertex(new BaseLabeledVertex("F"));
                                addVertex(g);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 3))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 4))
                                        .from(b)
                                        .to(c);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(g);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(g)
                        .applyingEdmondsKarp(new IntegerWeightBaseOperations());
        assertEquals(actual, expected);
    }
}