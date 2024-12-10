package org.apache.commons.graph.model;

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

import static org.apache.commons.graph.utils.GraphUtils.buildCompleteGraph;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.fail;

import static java.lang.String.valueOf;

import org.apache.commons.graph.CommonsGraph;
import org.apache.commons.graph.GraphException;
import org.apache.commons.graph.MutableGraph;
import org.apache.commons.graph.utils.MultiThreadedTestRunner;
import org.apache.commons.graph.utils.TestRunner;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

/** */
public class BaseMutableGraphTestCase {

    private final class GraphInsert extends TestRunner {

        private MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g;

        private int start;

        private int end;

        private GraphInsert(
                MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g, int start, int end) {
            this.g = g;
            this.start = start;
            this.end = end;
        }

        @Override
        public void runTest() {

            for (int i = start; i < end; i++) {
                BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
                g.addVertex(v);
            }
            synchronized (g) {
                for (BaseLabeledVertex v1 : g.getVertices0()) {
                    for (BaseLabeledVertex v2 : g.getVertices0()) {
                        if (!v1.equals(v2)) {
                            try {
                                BaseLabeledEdge e = new BaseLabeledEdge(v1 + " -> " + v2);
                                g.addEdge(v1, e, v2);
                            } catch (GraphException e) {
                            }
                        }
                    }
                }
            }
        }
    }

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseMutableGraph#addVertex(org.apache.commons.graph.Vertex)}.
     */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseMutableGraph#removeEdge(org.apache.commons.graph.Edge)}
     */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseMutableGraph#removeEdge(org.apache.commons.graph.Edge)}
     */
    

    /** Test Graph model in a multi-thread enviroment. */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseGraph#getConnectedVertices(org.apache.commons.graph.Vertex)}
     */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseGraph#getConnectedVertices(org.apache.commons.graph.Vertex)}
     */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseGraph#getConnectedVertices(org.apache.commons.graph.Vertex)}
     */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseGraph#getEdge(org.apache.commons.graph.Vertex,
     * org.apache.commons.graph.Vertex)}
     */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseGraph#getEdge(org.apache.commons.graph.Vertex,
     * org.apache.commons.graph.Vertex)}
     */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseGraph#getEdge(org.apache.commons.graph.Vertex,
     * org.apache.commons.graph.Vertex)}
     */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseGraph#getEdge(org.apache.commons.graph.Vertex,
     * org.apache.commons.graph.Vertex)}
     */
    

    /** Test Graph model ina multi-thread enviroment. */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseMutableGraph#removeEdge(org.apache.commons.graph.Edge)}
     */
    

    /**
     * Test method for {@link
     * org.apache.commons.graph.model.BaseMutableGraph#removeEdge(org.apache.commons.graph.Edge)}
     */

    @Test
    public void testAddVertexAndEdge_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
    }

    @Test
    public void testAddVertexAndEdge_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
    }

    @Test
    public void testAddVertexAndEdge_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
    }

    @Test
    public void testAddVertexAndEdge_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
    }

    @Test
    public void testAddVertexAndEdge_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
    }

    @Test
    public void testAddVertexAndEdge_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
    }

    @Test
    public void testAddVertexAndEdge_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
    }

    @Test
    public void testAddVertexAndEdge_test7_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
    }

    @Test
    public void testAddVertexAndEdge_test8_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
    }

    @Test
    public void testAddVertexAndEdge_test9_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
    }

    @Test
    public void testAddVertexAndEdge_test10_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        gSimple.addVertex(one);
        gSimple.addVertex(two);
    }

    @Test
    public void testAddVertexAndEdge_test11_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        gSimple.addVertex(one);
        gSimple.addVertex(two);
        gSimple.addEdge(one, new BaseLabeledEdge("1 -> 2"), two);
    }

    @Test
    public void testAddVertexAndEdge_test12_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        gSimple.addVertex(one);
        gSimple.addVertex(two);
        gSimple.addEdge(one, new BaseLabeledEdge("1 -> 2"), two);
        assertEquals(2, gSimple.getOrder());
    }

    @Test
    public void testAddVertexAndEdge_test13_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        gSimple.addVertex(one);
        gSimple.addVertex(two);
        gSimple.addEdge(one, new BaseLabeledEdge("1 -> 2"), two);
        assertEquals(2, gSimple.getOrder());
        assertEquals(1, gSimple.getSize());
    }

    @Test
    public void testAddVertexAndEdge_test14_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        gSimple.addVertex(one);
        gSimple.addVertex(two);
        gSimple.addEdge(one, new BaseLabeledEdge("1 -> 2"), two);
        assertEquals(2, gSimple.getOrder());
        assertEquals(1, gSimple.getSize());
        assertEquals(1, gSimple.getDegree(one));
        assertEquals(1, gSimple.getDegree(two));
    }

    @Test
    public void testAddVertexAndEdge_test15_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        gSimple.addVertex(one);
        gSimple.addVertex(two);
        gSimple.addEdge(one, new BaseLabeledEdge("1 -> 2"), two);
        assertEquals(2, gSimple.getOrder());
        assertEquals(1, gSimple.getSize());
        assertEquals(1, gSimple.getDegree(one));
        assertEquals(1, gSimple.getDegree(two));
        assertEquals(0, gSimple.getInDegree(one));
        assertEquals(1, gSimple.getInDegree(two));
    }

    @Test
    public void testAddVertexAndEdge_test16_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        gSimple.addVertex(one);
        gSimple.addVertex(two);
        gSimple.addEdge(one, new BaseLabeledEdge("1 -> 2"), two);
        assertEquals(2, gSimple.getOrder());
        assertEquals(1, gSimple.getSize());
        assertEquals(1, gSimple.getDegree(one));
        assertEquals(1, gSimple.getDegree(two));
        assertEquals(0, gSimple.getInDegree(one));
        assertEquals(1, gSimple.getInDegree(two));
        assertEquals(1, gSimple.getOutDegree(one));
        assertEquals(0, gSimple.getOutDegree(two));
    }

    @Test
    public void testAddVertexAndEdge_test17_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        gSimple.addVertex(one);
        gSimple.addVertex(two);
        gSimple.addEdge(one, new BaseLabeledEdge("1 -> 2"), two);
        assertEquals(2, gSimple.getOrder());
        assertEquals(1, gSimple.getSize());
        assertEquals(1, gSimple.getDegree(one));
        assertEquals(1, gSimple.getDegree(two));
        assertEquals(0, gSimple.getInDegree(one));
        assertEquals(1, gSimple.getInDegree(two));
        assertEquals(1, gSimple.getOutDegree(one));
        assertEquals(0, gSimple.getOutDegree(two));
        assertFalse(gSimple.containsEdge(new BaseLabeledEdge("Not Exist Edge")));
    }

    @Test
    public void testAddVertexAndEdge_test18_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, g);
        assertEquals(50, g.getOrder());
        assertEquals(1225, g.getSize());
        for (BaseLabeledVertex v : g.getVertices0()) {
            assertEquals(49, g.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gDirect =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(50, gDirect);
        assertEquals(50, gDirect.getOrder());
        assertEquals(2450, gDirect.getSize());
        for (BaseLabeledVertex v : gDirect.getVertices0()) {
            assertEquals(98, gDirect.getDegree(v));
        }
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> gSimple =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex one = new BaseLabeledVertex("1");
        BaseLabeledVertex two = new BaseLabeledVertex("2");
        gSimple.addVertex(one);
        gSimple.addVertex(two);
        gSimple.addEdge(one, new BaseLabeledEdge("1 -> 2"), two);
        assertEquals(2, gSimple.getOrder());
        assertEquals(1, gSimple.getSize());
        assertEquals(1, gSimple.getDegree(one));
        assertEquals(1, gSimple.getDegree(two));
        assertEquals(0, gSimple.getInDegree(one));
        assertEquals(1, gSimple.getInDegree(two));
        assertEquals(1, gSimple.getOutDegree(one));
        assertEquals(0, gSimple.getOutDegree(two));
        assertFalse(gSimple.containsEdge(new BaseLabeledEdge("Not Exist Edge")));
        assertFalse(gSimple.containsVertex(new BaseLabeledVertex("Not exist vertex")));
    }

    @Test
    public void testDirectedGraphRemoveEdge_test0_decomposed()  {
        final DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
    }

    @Test
    public void testDirectedGraphRemoveEdge_test1_decomposed()  {
        final DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
    }

    @Test
    public void testDirectedGraphRemoveEdge_test2_decomposed()  {
        final DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
    }

    @Test
    public void testDirectedGraphRemoveEdge_test3_decomposed()  {
        final DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
        BaseLabeledEdge e = g.getEdge(source, target);
    }

    @Test
    public void testDirectedGraphRemoveEdge_test4_decomposed()  {
        final DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
        BaseLabeledEdge e = g.getEdge(source, target);
        g.removeEdge(e);
    }

    @Test
    public void testDirectedGraphRemoveEdge_test5_decomposed()  {
        final DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
        BaseLabeledEdge e = g.getEdge(source, target);
        g.removeEdge(e);
        BaseLabeledEdge edge = g.getEdge(source, target);
    }

    @Test
    public void testDirectedGraphRemoveEdge_test6_decomposed()  {
        final DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
        BaseLabeledEdge e = g.getEdge(source, target);
        g.removeEdge(e);
        BaseLabeledEdge edge = g.getEdge(source, target);
        assertNull(edge);
    }

    @Test
    public void testDirectedGraphRemoveEdgeNotExists_test0_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledEdge e = null;
        try {
            g = new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            e = new BaseLabeledEdge("NOT EXIST");
        } catch (GraphException ex) {
            fail(ex.getMessage());
        }
    }

    @Test(expected = GraphException.class)
    public void testDirectedGraphRemoveEdgeNotExists_test1_decomposed()  {
        DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledEdge e = null;
        try {
            g = new DirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            e = new BaseLabeledEdge("NOT EXIST");
        } catch (GraphException ex) {
            fail(ex.getMessage());
        }
        g.removeEdge(e);
    }

    @Test
    public void testDirectedMultiTh_test0_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new DirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
    }

    @Test
    public void testDirectedMultiTh_test1_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new DirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
    }

    @Test
    public void testDirectedMultiTh_test2_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new DirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
    }

    @Test
    public void testDirectedMultiTh_test3_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new DirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
    }

    @Test
    public void testDirectedMultiTh_test4_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new DirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
        TestRunner[] trs = {tr1, tr2, tr3};
        MultiThreadedTestRunner mttr = new MultiThreadedTestRunner(trs);
    }

    @Test
    public void testDirectedMultiTh_test5_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new DirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
        TestRunner[] trs = {tr1, tr2, tr3};
        MultiThreadedTestRunner mttr = new MultiThreadedTestRunner(trs);
        mttr.runRunnables();
    }

    @Test
    public void testDirectedMultiTh_test6_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new DirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
        TestRunner[] trs = {tr1, tr2, tr3};
        MultiThreadedTestRunner mttr = new MultiThreadedTestRunner(trs);
        mttr.runRunnables();
        assertEquals(30, g.getOrder());
    }

    @Test
    public void testDirectedMultiTh_test7_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new DirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
        TestRunner[] trs = {tr1, tr2, tr3};
        MultiThreadedTestRunner mttr = new MultiThreadedTestRunner(trs);
        mttr.runRunnables();
        assertEquals(30, g.getOrder());
        assertEquals((30 * (30 - 1)), g.getSize());
    }

    @Test
    public void testGetConnectedVertices_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
    }

    @Test
    public void testGetConnectedVertices_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
        final BaseLabeledVertex testVertex = new BaseLabeledVertex(valueOf(1));
    }

    @Test
    public void testGetConnectedVertices_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
        final BaseLabeledVertex testVertex = new BaseLabeledVertex(valueOf(1));
        Iterable<BaseLabeledVertex> connectedVertices = g.getConnectedVertices(testVertex);
    }

    @Test
    public void testGetConnectedVertices_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
        final BaseLabeledVertex testVertex = new BaseLabeledVertex(valueOf(1));
        Iterable<BaseLabeledVertex> connectedVertices = g.getConnectedVertices(testVertex);
        assertNotNull(connectedVertices);
        final List<BaseLabeledVertex> v = new ArrayList<BaseLabeledVertex>();
        for (BaseLabeledVertex baseLabeledVertex : connectedVertices) {
            v.add(baseLabeledVertex);
        }
    }

    @Test
    public void testGetConnectedVertices_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
        final BaseLabeledVertex testVertex = new BaseLabeledVertex(valueOf(1));
        Iterable<BaseLabeledVertex> connectedVertices = g.getConnectedVertices(testVertex);
        assertNotNull(connectedVertices);
        final List<BaseLabeledVertex> v = new ArrayList<BaseLabeledVertex>();
        for (BaseLabeledVertex baseLabeledVertex : connectedVertices) {
            v.add(baseLabeledVertex);
        }
        assertEquals(9, v.size());
    }

    @Test
    public void testGetConnectedVertices_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
        final BaseLabeledVertex testVertex = new BaseLabeledVertex(valueOf(1));
        Iterable<BaseLabeledVertex> connectedVertices = g.getConnectedVertices(testVertex);
        assertNotNull(connectedVertices);
        final List<BaseLabeledVertex> v = new ArrayList<BaseLabeledVertex>();
        for (BaseLabeledVertex baseLabeledVertex : connectedVertices) {
            v.add(baseLabeledVertex);
        }
        assertEquals(9, v.size());
        assertFalse(v.contains(testVertex));
    }

    @Test
    public void testGetConnectedVerticesNPE_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledVertex notExistsVertex = null;
        try {
            g = new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            notExistsVertex = new BaseLabeledVertex(valueOf(1000));
        } catch (GraphException e) {
            fail(e.getMessage());
        }
    }

    @Test(expected = GraphException.class)
    public void testGetConnectedVerticesNPE_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledVertex notExistsVertex = null;
        try {
            g = new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            notExistsVertex = new BaseLabeledVertex(valueOf(1000));
        } catch (GraphException e) {
            fail(e.getMessage());
        }
        g.getConnectedVertices(notExistsVertex);
    }

    @Test
    public void testGetConnectedVerticesOnNotConnectedGraph_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
    }

    @Test
    public void testGetConnectedVerticesOnNotConnectedGraph_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
        final BaseLabeledVertex testVertex = new BaseLabeledVertex(valueOf(1));
    }

    @Test
    public void testGetConnectedVerticesOnNotConnectedGraph_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
        final BaseLabeledVertex testVertex = new BaseLabeledVertex(valueOf(1));
        Iterable<BaseLabeledVertex> connectedVertices = g.getConnectedVertices(testVertex);
    }

    @Test
    public void testGetConnectedVerticesOnNotConnectedGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
        final BaseLabeledVertex testVertex = new BaseLabeledVertex(valueOf(1));
        Iterable<BaseLabeledVertex> connectedVertices = g.getConnectedVertices(testVertex);
        assertNotNull(connectedVertices);
        final List<BaseLabeledVertex> v = new ArrayList<BaseLabeledVertex>();
        for (BaseLabeledVertex baseLabeledVertex : connectedVertices) {
            v.add(baseLabeledVertex);
        }
    }

    @Test
    public void testGetConnectedVerticesOnNotConnectedGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
        final BaseLabeledVertex testVertex = new BaseLabeledVertex(valueOf(1));
        Iterable<BaseLabeledVertex> connectedVertices = g.getConnectedVertices(testVertex);
        assertNotNull(connectedVertices);
        final List<BaseLabeledVertex> v = new ArrayList<BaseLabeledVertex>();
        for (BaseLabeledVertex baseLabeledVertex : connectedVertices) {
            v.add(baseLabeledVertex);
        }
        assertEquals(0, v.size());
    }

    @Test
    public void testGetEdge_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
    }

    @Test
    public void testGetEdge_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
    }

    @Test
    public void testGetEdge_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
    }

    @Test
    public void testGetEdge_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        BaseLabeledEdge edge = g.getEdge(source, target);
    }

    @Test
    public void testGetEdge_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(10, g);
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        BaseLabeledEdge edge = g.getEdge(source, target);
        assertNotNull(edge);
    }

    @Test
    public void testGetEgdeNotExistsVertex_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledVertex source = null;
        BaseLabeledVertex target = null;
        try {
            g = new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            source = new BaseLabeledVertex(valueOf(100));
            target = new BaseLabeledVertex(valueOf(2));
        } catch (GraphException e) {
            fail(e.getMessage());
        }
    }

    @Test(expected = GraphException.class)
    public void testGetEgdeNotExistsVertex_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledVertex source = null;
        BaseLabeledVertex target = null;
        try {
            g = new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            source = new BaseLabeledVertex(valueOf(100));
            target = new BaseLabeledVertex(valueOf(2));
        } catch (GraphException e) {
            fail(e.getMessage());
        }
        g.getEdge(source, target);
    }

    @Test
    public void testGetEgdeNotExistsVertex_2_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledVertex source = null;
        BaseLabeledVertex target = null;
        try {
            g = new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            source = new BaseLabeledVertex(valueOf(1));
            target = new BaseLabeledVertex(valueOf(200));
        } catch (GraphException e) {
            fail(e.getMessage());
        }
    }

    @Test(expected = GraphException.class)
    public void testGetEgdeNotExistsVertex_2_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledVertex source = null;
        BaseLabeledVertex target = null;
        try {
            g = new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            source = new BaseLabeledVertex(valueOf(1));
            target = new BaseLabeledVertex(valueOf(200));
        } catch (GraphException e) {
            fail(e.getMessage());
        }
        g.getEdge(source, target);
    }

    @Test
    public void testGetNotExistsEdge_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
    }

    @Test
    public void testGetNotExistsEdge_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
    }

    @Test
    public void testGetNotExistsEdge_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
    }

    @Test
    public void testGetNotExistsEdge_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        BaseLabeledEdge edge = g.getEdge(source, target);
    }

    @Test
    public void testGetNotExistsEdge_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 4; i++) {
            BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
            g.addVertex(v);
        }
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        BaseLabeledEdge edge = g.getEdge(source, target);
        assertNull(edge);
    }

    @Test
    public void testMultiThreadUndirectGraph_test0_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new UndirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
    }

    @Test
    public void testMultiThreadUndirectGraph_test1_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new UndirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
    }

    @Test
    public void testMultiThreadUndirectGraph_test2_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new UndirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
    }

    @Test
    public void testMultiThreadUndirectGraph_test3_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new UndirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
    }

    @Test
    public void testMultiThreadUndirectGraph_test4_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new UndirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
        TestRunner[] trs = {tr1, tr2, tr3};
        MultiThreadedTestRunner mttr = new MultiThreadedTestRunner(trs);
    }

    @Test
    public void testMultiThreadUndirectGraph_test5_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new UndirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
        TestRunner[] trs = {tr1, tr2, tr3};
        MultiThreadedTestRunner mttr = new MultiThreadedTestRunner(trs);
        mttr.runRunnables();
    }

    @Test
    public void testMultiThreadUndirectGraph_test6_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new UndirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
        TestRunner[] trs = {tr1, tr2, tr3};
        MultiThreadedTestRunner mttr = new MultiThreadedTestRunner(trs);
        mttr.runRunnables();
        assertEquals(30, g.getOrder());
    }

    @Test
    public void testMultiThreadUndirectGraph_test7_decomposed() throws Throwable {
        final MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                        CommonsGraph.synchronize2(
                                (MutableGraph<BaseLabeledVertex, BaseLabeledEdge>)
                                        new UndirectedMutableGraph<
                                                BaseLabeledVertex, BaseLabeledEdge>());
        TestRunner tr1, tr2, tr3;
        tr1 = new GraphInsert(g, 0, 10);
        tr2 = new GraphInsert(g, 10, 20);
        tr3 = new GraphInsert(g, 20, 30);
        TestRunner[] trs = {tr1, tr2, tr3};
        MultiThreadedTestRunner mttr = new MultiThreadedTestRunner(trs);
        mttr.runRunnables();
        assertEquals(30, g.getOrder());
        assertEquals((30 * (30 - 1) / 2), g.getSize());
    }

    @Test
    public void testUndirectedGraphRemoveEdge_test0_decomposed()  {
        final UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
    }

    @Test
    public void testUndirectedGraphRemoveEdge_test1_decomposed()  {
        final UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
    }

    @Test
    public void testUndirectedGraphRemoveEdge_test2_decomposed()  {
        final UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
    }

    @Test
    public void testUndirectedGraphRemoveEdge_test3_decomposed()  {
        final UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
        BaseLabeledEdge e = g.getEdge(source, target);
    }

    @Test
    public void testUndirectedGraphRemoveEdge_test4_decomposed()  {
        final UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
        BaseLabeledEdge e = g.getEdge(source, target);
        g.removeEdge(e);
    }

    @Test
    public void testUndirectedGraphRemoveEdge_test5_decomposed()  {
        final UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
        BaseLabeledEdge e = g.getEdge(source, target);
        g.removeEdge(e);
        BaseLabeledEdge edge = g.getEdge(source, target);
    }

    @Test
    public void testUndirectedGraphRemoveEdge_test6_decomposed()  {
        final UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        final BaseLabeledVertex source = new BaseLabeledVertex(valueOf(1));
        final BaseLabeledVertex target = new BaseLabeledVertex(valueOf(2));
        buildCompleteGraph(10, g);
        BaseLabeledEdge e = g.getEdge(source, target);
        g.removeEdge(e);
        BaseLabeledEdge edge = g.getEdge(source, target);
        assertNull(edge);
    }

    @Test
    public void testUndirectedGraphRemoveEdgeNotExists_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledEdge e = null;
        try {
            g = new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            e = new BaseLabeledEdge("NOT EXIST");
        } catch (GraphException ex) {
            fail(ex.getMessage());
        }
    }

    @Test(expected = GraphException.class)
    public void testUndirectedGraphRemoveEdgeNotExists_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g = null;
        BaseLabeledEdge e = null;
        try {
            g = new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
            buildCompleteGraph(10, g);

            e = new BaseLabeledEdge("NOT EXIST");
        } catch (GraphException ex) {
            fail(ex.getMessage());
        }
        g.removeEdge(e);
    }
}