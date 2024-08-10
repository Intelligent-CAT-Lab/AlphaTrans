package org.apache.commons.graph.scc;

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

import static org.apache.commons.graph.CommonsGraph.findStronglyConnectedComponent;
import static org.apache.commons.graph.CommonsGraph.newDirectedMutableGraph;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;

import org.apache.commons.graph.builder.AbstractGraphConnection;
import org.apache.commons.graph.model.BaseLabeledEdge;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.junit.Test;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

/**
 * Test for Kosaraju's algorithm implementation, see the <a
 * href="http://scienceblogs.com/goodmath/2007/10/computing_strongly_connected_c.php">online</a>
 * test.
 */
public final class KosarajuSharirTestCase {

    @Test
    public void testNotExistVertex_test0_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findStronglyConnectedComponent(graph);
    }

    @Test(expected = IllegalStateException.class)
    public void testNotExistVertex_test1_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findStronglyConnectedComponent(graph);
        findStronglyConnectedComponent(graph)
                .applyingKosarajuSharir1(new BaseLabeledVertex("NOT EXISTS"));
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test0_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph = null;
        findStronglyConnectedComponent(graph);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test1_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph = null;
        findStronglyConnectedComponent(graph);
        findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
    }

    @Test
    public void testNullVertices_test0_decomposed()  {
        final BaseLabeledVertex a = null;
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findStronglyConnectedComponent(graph);
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertices_test1_decomposed()  {
        final BaseLabeledVertex a = null;
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>> graph =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Integer>>();
        findStronglyConnectedComponent(graph);
        findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
    }

    @Test
    public void testUnconnectedGraph_test0_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testUnconnectedGraph_test1_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
    }

    @Test
    public void testUnconnectedGraph_test2_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
    }

    @Test
    public void testUnconnectedGraph_test3_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test
    public void testUnconnectedGraph_test4_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
    }

    @Test
    public void testUnconnectedGraph_test5_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
    }

    @Test
    public void testUnconnectedGraph_test6_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
    }

    @Test
    public void testUnconnectedGraph_test7_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
    }

    @Test
    public void testUnconnectedGraph_test8_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
    }

    @Test
    public void testUnconnectedGraph_test9_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
    }

    @Test
    public void testUnconnectedGraph_test10_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
    }

    @Test
    public void testUnconnectedGraph_test11_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
    }

    @Test
    public void testUnconnectedGraph_test12_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
    }

    @Test
    public void testUnconnectedGraph_test13_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
    }

    @Test
    public void testUnconnectedGraph_test14_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
    }

    @Test
    public void testUnconnectedGraph_test15_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
    }

    @Test
    public void testUnconnectedGraph_test16_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
    }

    @Test
    public void testUnconnectedGraph_test17_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
    }

    @Test
    public void testUnconnectedGraph_test18_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
    }

    @Test
    public void testUnconnectedGraph_test19_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
    }

    @Test
    public void testUnconnectedGraph_test20_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
    }

    @Test
    public void testUnconnectedGraph_test21_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
    }

    @Test
    public void testUnconnectedGraph_test22_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
    }

    @Test
    public void testUnconnectedGraph_test23_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
    }

    @Test
    public void testUnconnectedGraph_test24_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
        assertEquals(scc2, actualE);
        findStronglyConnectedComponent(graph);
    }

    @Test
    public void testUnconnectedGraph_test25_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
        assertEquals(scc2, actualE);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualG =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(g);
    }

    @Test
    public void testUnconnectedGraph_test26_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
        assertEquals(scc2, actualE);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualG =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(g);
        assertFalse(actualG.isEmpty());
    }

    @Test
    public void testUnconnectedGraph_test27_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
        assertEquals(scc2, actualE);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualG =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(g);
        assertFalse(actualG.isEmpty());
        assertEquals(scc3, actualG);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test0_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test1_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test2_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test3_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test4_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test5_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test6_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test7_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test8_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test9_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test10_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test11_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test12_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test13_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test14_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test15_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test16_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test17_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test18_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test19_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test20_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test21_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test22_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test23_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test24_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
        assertEquals(scc2, actualE);
        findStronglyConnectedComponent(graph);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test25_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
        assertEquals(scc2, actualE);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualG =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(g);
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test26_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
        assertEquals(scc2, actualE);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualG =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(g);
        assertFalse(actualG.isEmpty());
    }

    @Test
    public void testVerifyHasStronglyConnectedComponents_test27_decomposed()  {
        final BaseLabeledVertex a = new BaseLabeledVertex("A");
        final BaseLabeledVertex b = new BaseLabeledVertex("B");
        final BaseLabeledVertex c = new BaseLabeledVertex("C");
        final BaseLabeledVertex d = new BaseLabeledVertex("D");
        final BaseLabeledVertex e = new BaseLabeledVertex("E");
        final BaseLabeledVertex f = new BaseLabeledVertex("F");
        final BaseLabeledVertex g = new BaseLabeledVertex("G");
        final BaseLabeledVertex h = new BaseLabeledVertex("H");
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> graph =
                newDirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                addVertex(a);
                                addVertex(b);
                                addVertex(c);
                                addVertex(d);
                                addVertex(e);
                                addVertex(f);
                                addVertex(g);
                                addVertex(h);

                                addEdge(new BaseLabeledEdge("A -> F")).from(a).to(f);
                                addEdge(new BaseLabeledEdge("A -> B")).from(a).to(b);
                                addEdge(new BaseLabeledEdge("B -> D")).from(b).to(d);
                                addEdge(new BaseLabeledEdge("C -> G")).from(c).to(g);
                                addEdge(new BaseLabeledEdge("D -> A")).from(d).to(a);
                                addEdge(new BaseLabeledEdge("D -> G")).from(d).to(g);
                                addEdge(new BaseLabeledEdge("E -> C")).from(e).to(c);
                                addEdge(new BaseLabeledEdge("E -> F")).from(e).to(f);
                                addEdge(new BaseLabeledEdge("F -> E")).from(f).to(e);
                                addEdge(new BaseLabeledEdge("G -> H")).from(g).to(h);
                                addEdge(new BaseLabeledEdge("H -> C")).from(h).to(c);
                            }
                        });
        Set<Set<BaseLabeledVertex>> expected = new HashSet<Set<BaseLabeledVertex>>();
        Set<BaseLabeledVertex> scc1 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc1, a, b, d);
        expected.add(scc1);
        Set<BaseLabeledVertex> scc2 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc2, e, f);
        expected.add(scc2);
        Set<BaseLabeledVertex> scc3 = new HashSet<BaseLabeledVertex>();
        Collections.addAll(scc3, g, h, c);
        expected.add(scc3);
        findStronglyConnectedComponent(graph);
        Set<Set<BaseLabeledVertex>> actual =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir0();
        assertFalse(actual.isEmpty());
        assertEquals(expected, actual);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualA =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a);
        assertFalse(actualA.isEmpty());
        assertEquals(scc1, actualA);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualE =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e);
        assertFalse(actualE.isEmpty());
        assertEquals(scc2, actualE);
        findStronglyConnectedComponent(graph);
        Set<BaseLabeledVertex> actualG =
                findStronglyConnectedComponent(graph).applyingKosarajuSharir1(g);
        assertFalse(actualG.isEmpty());
        assertEquals(scc3, actualG);
    }
}