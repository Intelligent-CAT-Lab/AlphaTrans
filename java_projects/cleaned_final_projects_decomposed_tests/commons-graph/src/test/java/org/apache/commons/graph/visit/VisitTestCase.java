package org.apache.commons.graph.visit;

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

import static org.apache.commons.graph.CommonsGraph.newUndirectedMutableGraph;
import static org.apache.commons.graph.CommonsGraph.visit;
import static org.junit.Assert.assertEquals;

import org.apache.commons.graph.Graph;
import org.apache.commons.graph.builder.AbstractGraphConnection;
import org.apache.commons.graph.model.BaseLabeledEdge;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public final class VisitTestCase {

    

    /**
     * Graph picture can be see <a
     * href="http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/GraphAlgor/breadthSearch.htm">here</a>
     */
    

    /**
     * Graph picture can be see <a
     * href="http://aiukswkelasgkelompok7.wordpress.com/metode-pencarian-dan-pelacakan/">here</a>
     */

    @Test
    public void testNotExistVertex_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {}
                        });
    }

    @Test
    public void testNotExistVertex_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {}
                        });
        visit(input);
    }

    @Test(expected = IllegalStateException.class)
    public void testNotExistVertex_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {}
                        });
        visit(input);
        visit(input).from(new BaseLabeledVertex("NOT EXIST"));
    }

    @Test
    public void testVerifyBreadthFirstSearch_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);
                                addEdge(new BaseLabeledEdge("t <-> x")).from(t).to(x);

                                addEdge(new BaseLabeledEdge("y <-> u")).from(y).to(u);
                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> expected =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);

                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
    }

    @Test
    public void testVerifyBreadthFirstSearch_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);
                                addEdge(new BaseLabeledEdge("t <-> x")).from(t).to(x);

                                addEdge(new BaseLabeledEdge("y <-> u")).from(y).to(u);
                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> expected =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);

                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
        visit(input);
    }

    @Test
    public void testVerifyBreadthFirstSearch_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);
                                addEdge(new BaseLabeledEdge("t <-> x")).from(t).to(x);

                                addEdge(new BaseLabeledEdge("y <-> u")).from(y).to(u);
                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> expected =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);

                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
        visit(input);
        visit(input).from(new BaseLabeledVertex("s"));
    }

    @Test
    public void testVerifyBreadthFirstSearch_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);
                                addEdge(new BaseLabeledEdge("t <-> x")).from(t).to(x);

                                addEdge(new BaseLabeledEdge("y <-> u")).from(y).to(u);
                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> expected =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);

                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
        visit(input);
        visit(input).from(new BaseLabeledVertex("s"));
        Graph<BaseLabeledVertex, BaseLabeledEdge> actual =
                visit(input).from(new BaseLabeledVertex("s")).applyingBreadthFirstSearch0();
    }

    @Test
    public void testVerifyBreadthFirstSearch_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);
                                addEdge(new BaseLabeledEdge("t <-> x")).from(t).to(x);

                                addEdge(new BaseLabeledEdge("y <-> u")).from(y).to(u);
                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> expected =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex r = addVertex(new BaseLabeledVertex("r"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("s"));
                                BaseLabeledVertex t = addVertex(new BaseLabeledVertex("t"));
                                BaseLabeledVertex u = addVertex(new BaseLabeledVertex("u"));
                                BaseLabeledVertex v = addVertex(new BaseLabeledVertex("v"));
                                BaseLabeledVertex w = addVertex(new BaseLabeledVertex("w"));
                                BaseLabeledVertex x = addVertex(new BaseLabeledVertex("x"));
                                BaseLabeledVertex y = addVertex(new BaseLabeledVertex("y"));

                                addEdge(new BaseLabeledEdge("s <-> r")).from(s).to(r);
                                addEdge(new BaseLabeledEdge("s <-> w")).from(s).to(w);

                                addEdge(new BaseLabeledEdge("r <-> v")).from(r).to(v);

                                addEdge(new BaseLabeledEdge("w <-> t")).from(w).to(t);
                                addEdge(new BaseLabeledEdge("w <-> x")).from(w).to(x);

                                addEdge(new BaseLabeledEdge("t <-> u")).from(t).to(u);

                                addEdge(new BaseLabeledEdge("x <-> y")).from(x).to(y);
                            }
                        });
        visit(input);
        visit(input).from(new BaseLabeledVertex("s"));
        Graph<BaseLabeledVertex, BaseLabeledEdge> actual =
                visit(input).from(new BaseLabeledVertex("s")).applyingBreadthFirstSearch0();
        assertEquals(expected, actual);
    }

    @Test
    public void testVerifyDepthFirstSearch_test0_decomposed()  {
        final List<BaseLabeledVertex> expected = new ArrayList<BaseLabeledVertex>();
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex a = addVertex(new BaseLabeledVertex("A"));
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                BaseLabeledVertex g = addVertex(new BaseLabeledVertex("G"));
                                BaseLabeledVertex h = addVertex(new BaseLabeledVertex("H"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("S"));

                                addEdge(new BaseLabeledEdge("S <-> A")).from(s).to(a);
                                addEdge(new BaseLabeledEdge("S <-> B")).from(s).to(b);

                                addEdge(new BaseLabeledEdge("A <-> C")).from(a).to(c);
                                addEdge(new BaseLabeledEdge("A <-> D")).from(a).to(d);

                                addEdge(new BaseLabeledEdge("B <-> E")).from(b).to(e);
                                addEdge(new BaseLabeledEdge("B <-> F")).from(b).to(f);

                                addEdge(new BaseLabeledEdge("E <-> H")).from(e).to(h);
                                addEdge(new BaseLabeledEdge("E <-> G")).from(e).to(g);

                                expected.add(s);
                                expected.add(b);
                                expected.add(f);
                                expected.add(e);
                                expected.add(g);
                                expected.add(h);
                                expected.add(a);
                                expected.add(d);
                                expected.add(c);
                            }
                        });
    }

    @Test
    public void testVerifyDepthFirstSearch_test1_decomposed()  {
        final List<BaseLabeledVertex> expected = new ArrayList<BaseLabeledVertex>();
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex a = addVertex(new BaseLabeledVertex("A"));
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                BaseLabeledVertex g = addVertex(new BaseLabeledVertex("G"));
                                BaseLabeledVertex h = addVertex(new BaseLabeledVertex("H"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("S"));

                                addEdge(new BaseLabeledEdge("S <-> A")).from(s).to(a);
                                addEdge(new BaseLabeledEdge("S <-> B")).from(s).to(b);

                                addEdge(new BaseLabeledEdge("A <-> C")).from(a).to(c);
                                addEdge(new BaseLabeledEdge("A <-> D")).from(a).to(d);

                                addEdge(new BaseLabeledEdge("B <-> E")).from(b).to(e);
                                addEdge(new BaseLabeledEdge("B <-> F")).from(b).to(f);

                                addEdge(new BaseLabeledEdge("E <-> H")).from(e).to(h);
                                addEdge(new BaseLabeledEdge("E <-> G")).from(e).to(g);

                                expected.add(s);
                                expected.add(b);
                                expected.add(f);
                                expected.add(e);
                                expected.add(g);
                                expected.add(h);
                                expected.add(a);
                                expected.add(d);
                                expected.add(c);
                            }
                        });
        visit(input);
    }

    @Test
    public void testVerifyDepthFirstSearch_test2_decomposed()  {
        final List<BaseLabeledVertex> expected = new ArrayList<BaseLabeledVertex>();
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex a = addVertex(new BaseLabeledVertex("A"));
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                BaseLabeledVertex g = addVertex(new BaseLabeledVertex("G"));
                                BaseLabeledVertex h = addVertex(new BaseLabeledVertex("H"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("S"));

                                addEdge(new BaseLabeledEdge("S <-> A")).from(s).to(a);
                                addEdge(new BaseLabeledEdge("S <-> B")).from(s).to(b);

                                addEdge(new BaseLabeledEdge("A <-> C")).from(a).to(c);
                                addEdge(new BaseLabeledEdge("A <-> D")).from(a).to(d);

                                addEdge(new BaseLabeledEdge("B <-> E")).from(b).to(e);
                                addEdge(new BaseLabeledEdge("B <-> F")).from(b).to(f);

                                addEdge(new BaseLabeledEdge("E <-> H")).from(e).to(h);
                                addEdge(new BaseLabeledEdge("E <-> G")).from(e).to(g);

                                expected.add(s);
                                expected.add(b);
                                expected.add(f);
                                expected.add(e);
                                expected.add(g);
                                expected.add(h);
                                expected.add(a);
                                expected.add(d);
                                expected.add(c);
                            }
                        });
        visit(input);
        visit(input).from(new BaseLabeledVertex("S"));
    }

    @Test
    public void testVerifyDepthFirstSearch_test3_decomposed()  {
        final List<BaseLabeledVertex> expected = new ArrayList<BaseLabeledVertex>();
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex a = addVertex(new BaseLabeledVertex("A"));
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                BaseLabeledVertex g = addVertex(new BaseLabeledVertex("G"));
                                BaseLabeledVertex h = addVertex(new BaseLabeledVertex("H"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("S"));

                                addEdge(new BaseLabeledEdge("S <-> A")).from(s).to(a);
                                addEdge(new BaseLabeledEdge("S <-> B")).from(s).to(b);

                                addEdge(new BaseLabeledEdge("A <-> C")).from(a).to(c);
                                addEdge(new BaseLabeledEdge("A <-> D")).from(a).to(d);

                                addEdge(new BaseLabeledEdge("B <-> E")).from(b).to(e);
                                addEdge(new BaseLabeledEdge("B <-> F")).from(b).to(f);

                                addEdge(new BaseLabeledEdge("E <-> H")).from(e).to(h);
                                addEdge(new BaseLabeledEdge("E <-> G")).from(e).to(g);

                                expected.add(s);
                                expected.add(b);
                                expected.add(f);
                                expected.add(e);
                                expected.add(g);
                                expected.add(h);
                                expected.add(a);
                                expected.add(d);
                                expected.add(c);
                            }
                        });
        visit(input);
        visit(input).from(new BaseLabeledVertex("S"));
        final List<BaseLabeledVertex> actual =
                visit(input)
                        .from(new BaseLabeledVertex("S"))
                        .applyingDepthFirstSearch1(new NodeSequenceVisitor());
    }

    @Test
    public void testVerifyDepthFirstSearch_test4_decomposed()  {
        final List<BaseLabeledVertex> expected = new ArrayList<BaseLabeledVertex>();
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> input =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex a = addVertex(new BaseLabeledVertex("A"));
                                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("B"));
                                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("C"));
                                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("D"));
                                BaseLabeledVertex e = addVertex(new BaseLabeledVertex("E"));
                                BaseLabeledVertex f = addVertex(new BaseLabeledVertex("F"));
                                BaseLabeledVertex g = addVertex(new BaseLabeledVertex("G"));
                                BaseLabeledVertex h = addVertex(new BaseLabeledVertex("H"));
                                BaseLabeledVertex s = addVertex(new BaseLabeledVertex("S"));

                                addEdge(new BaseLabeledEdge("S <-> A")).from(s).to(a);
                                addEdge(new BaseLabeledEdge("S <-> B")).from(s).to(b);

                                addEdge(new BaseLabeledEdge("A <-> C")).from(a).to(c);
                                addEdge(new BaseLabeledEdge("A <-> D")).from(a).to(d);

                                addEdge(new BaseLabeledEdge("B <-> E")).from(b).to(e);
                                addEdge(new BaseLabeledEdge("B <-> F")).from(b).to(f);

                                addEdge(new BaseLabeledEdge("E <-> H")).from(e).to(h);
                                addEdge(new BaseLabeledEdge("E <-> G")).from(e).to(g);

                                expected.add(s);
                                expected.add(b);
                                expected.add(f);
                                expected.add(e);
                                expected.add(g);
                                expected.add(h);
                                expected.add(a);
                                expected.add(d);
                                expected.add(c);
                            }
                        });
        visit(input);
        visit(input).from(new BaseLabeledVertex("S"));
        final List<BaseLabeledVertex> actual =
                visit(input)
                        .from(new BaseLabeledVertex("S"))
                        .applyingDepthFirstSearch1(new NodeSequenceVisitor());
        assertEquals(expected, actual);
    }
}