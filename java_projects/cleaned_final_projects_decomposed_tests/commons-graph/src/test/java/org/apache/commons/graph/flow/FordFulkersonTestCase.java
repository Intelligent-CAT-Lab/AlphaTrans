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
 * Test for Ford-Fulkerson algorithm implementation. The test graph is available on <a
 * href="http://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm#Integral_example">Wikipedia</a>.
 */
public final class FordFulkersonTestCase {

    @Test
    public void testFindMaxFlowAndVerify_test0_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testFindMaxFlowAndVerify_test1_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test
    public void testFindMaxFlowAndVerify_test2_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> C", 1000))
                                        .from(a)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 1))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> D", 1000))
                                        .from(b)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1000))
                                        .from(c)
                                        .to(d);
                            }
                        });
    }

    @Test
    public void testFindMaxFlowAndVerify_test3_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> C", 1000))
                                        .from(a)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 1))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> D", 1000))
                                        .from(b)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1000))
                                        .from(c)
                                        .to(d);
                            }
                        });
        final Integer expected = 2000;
        findMaxFlow(graph);
    }

    @Test
    public void testFindMaxFlowAndVerify_test4_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> C", 1000))
                                        .from(a)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 1))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> D", 1000))
                                        .from(b)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1000))
                                        .from(c)
                                        .to(d);
                            }
                        });
        final Integer expected = 2000;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test
    public void testFindMaxFlowAndVerify_test5_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> C", 1000))
                                        .from(a)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 1))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> D", 1000))
                                        .from(b)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1000))
                                        .from(c)
                                        .to(d);
                            }
                        });
        final Integer expected = 2000;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
    }

    @Test
    public void testFindMaxFlowAndVerify_test6_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> C", 1000))
                                        .from(a)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 1))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> D", 1000))
                                        .from(b)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1000))
                                        .from(c)
                                        .to(d);
                            }
                        });
        final Integer expected = 2000;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
    }

    @Test
    public void testFindMaxFlowAndVerify_test7_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> C", 1000))
                                        .from(a)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 1))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> D", 1000))
                                        .from(b)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1000))
                                        .from(c)
                                        .to(d);
                            }
                        });
        final Integer expected = 2000;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(d)
                        .applyingFordFulkerson(new IntegerWeightBaseOperations());
    }

    @Test
    public void testFindMaxFlowAndVerify_test8_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);

                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> C", 1000))
                                        .from(a)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> C", 1))
                                        .from(b)
                                        .to(c);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("B -> D", 1000))
                                        .from(b)
                                        .to(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("C -> D", 1000))
                                        .from(c)
                                        .to(d);
                            }
                        });
        final Integer expected = 2000;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(d)
                        .applyingFordFulkerson(new IntegerWeightBaseOperations());
        assertEquals(expected, actual);
    }

    @Test
    public void testNotConnected_test0_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testNotConnected_test1_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test
    public void testNotConnected_test2_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                            }
                        });
    }

    @Test
    public void testNotConnected_test3_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
    }

    @Test
    public void testNotConnected_test4_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test
    public void testNotConnected_test5_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
    }

    @Test
    public void testNotConnected_test6_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
    }

    @Test
    public void testNotConnected_test7_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(d)
                        .applyingFordFulkerson(new IntegerWeightBaseOperations());
    }

    @Test
    public void testNotConnected_test8_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(d)
                        .applyingFordFulkerson(new IntegerWeightBaseOperations());
        assertEquals(actual, expected);
    }

    @Test
    public void testNotConnected_2_test0_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testNotConnected_2_test1_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test
    public void testNotConnected_2_test2_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                            }
                        });
    }

    @Test
    public void testNotConnected_2_test3_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
    }

    @Test
    public void testNotConnected_2_test4_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test
    public void testNotConnected_2_test5_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
    }

    @Test
    public void testNotConnected_2_test6_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
    }

    @Test
    public void testNotConnected_2_test7_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(d)
                        .applyingFordFulkerson(new IntegerWeightBaseOperations());
    }

    @Test
    public void testNotConnected_2_test8_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>() {

                            public void connect0() {
                                addVertex(a);
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                addVertex(new BaseLabeledVertex("C"));
                                addVertex(d);
                                addEdge(new BaseLabeledWeightedEdge<Integer>("A -> B", 1000))
                                        .from(a)
                                        .to(b);
                            }
                        });
        final Integer expected = 0;
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
        Integer actual =
                findMaxFlow(graph)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                        .from(a)
                        .to(d)
                        .applyingFordFulkerson(new IntegerWeightBaseOperations());
        assertEquals(actual, expected);
    }

    @Test
    public void testNullGraph_test0_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testNullGraph_test1_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test2_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test3_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test4_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
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
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test6_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(a).to(d);
        findMaxFlow(
                        (DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                .from(a)
                .to(d)
                .applyingFordFulkerson(new IntegerWeightBaseOperations());
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraphAndVertices_test0_decomposed()  {
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraphAndVertices_test1_decomposed()  {
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraphAndVertices_test2_decomposed()  {
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraphAndVertices_test3_decomposed()  {
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null).to(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraphAndVertices_test4_decomposed()  {
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null);
        findMaxFlow((DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null).to(null);
        findMaxFlow(
                        (DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>)
                                null)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                .from(null)
                .to(null)
                .applyingFordFulkerson(new IntegerWeightBaseOperations());
    }

    @Test
    public void testNullVertices_test0_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
    }

    @Test
    public void testNullVertices_test1_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test2_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test3_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null).to(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test4_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findMaxFlow(graph);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>());
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null);
        findMaxFlow(graph).whereEdgesHaveWeights(new BaseWeightedEdge<Integer>()).from(null).to(null);
        findMaxFlow(graph)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Integer>())
                .from(null)
                .to(null)
                .applyingFordFulkerson(new IntegerWeightBaseOperations());
    }
}