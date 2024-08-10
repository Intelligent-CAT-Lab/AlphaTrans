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

import static junit.framework.Assert.assertEquals;

import static org.apache.commons.graph.CommonsGraph.newDirectedMutableGraph;
import static org.apache.commons.graph.CommonsGraph.newUndirectedMutableGraph;
import static org.apache.commons.graph.CommonsGraph.populate;
import static org.apache.commons.graph.CommonsGraph.synchronize2;

import org.apache.commons.graph.Graph;
import org.apache.commons.graph.MutableGraph;
import org.apache.commons.graph.builder.AbstractGraphConnection;
import org.apache.commons.graph.builder.GraphConnection;
import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;
import org.junit.After;
import org.junit.Test;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

/** Provides a simple test case to test the Graph serialization. */
public class GraphSerializationTestCase {

    private static final String FILE_NAME = "target/serialiazedGraph.dat";

    private static GraphConnection<BaseLabeledVertex, BaseLabeledEdge> buildGraphConnections() {
        return new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

            @Override
            public void connect0() {
                BaseLabeledVertex a = addVertex(new BaseLabeledVertex("a"));
                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("b"));
                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("c"));
                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("d"));

                addEdge(new BaseLabeledEdge("a -> c")).from(a).to(c);
                addEdge(new BaseLabeledEdge("c -> d")).from(c).to(d);
                addEdge(new BaseLabeledEdge("d -> b")).from(d).to(b);
            }
        };
    }

    private static GraphConnection<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>
            buildWeightedGraphConnections() {
        return new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>() {

            @Override
            public void connect0() {
                BaseLabeledVertex a = addVertex(new BaseLabeledVertex("a"));
                BaseLabeledVertex b = addVertex(new BaseLabeledVertex("b"));
                BaseLabeledVertex c = addVertex(new BaseLabeledVertex("c"));
                BaseLabeledVertex d = addVertex(new BaseLabeledVertex("d"));

                addEdge(new BaseLabeledWeightedEdge<Double>("a -> c", 1D)).from(a).to(c);
                addEdge(new BaseLabeledWeightedEdge<Double>("c -> d", 1D)).from(c).to(d);
                addEdge(new BaseLabeledWeightedEdge<Double>("d -> b", 1D)).from(d).to(b);
            }
        };
    }

    /**
     * @param g
     * @throws FileNotFoundException
     * @throws IOException
     * @throws ClassNotFoundException
     */
    private static void checkSerialization(Graph<BaseLabeledVertex, ? extends Serializable> g)
            throws FileNotFoundException, IOException, ClassNotFoundException {
        FileOutputStream fout = new FileOutputStream(FILE_NAME);
        ObjectOutputStream oos = new ObjectOutputStream(fout);
        oos.writeObject(g);
        oos.close();

        FileInputStream fin = new FileInputStream(FILE_NAME);
        ObjectInputStream ois = new ObjectInputStream(fin);
        Object cloned = ois.readObject();
        ois.close();

        assertEquals(g, cloned);
    }

    @After
    public void cleanUp() {
        File f = new File(FILE_NAME);
        if (f.exists()) {
            f.delete();
        }
    }

    @Test
    public void testSerializeDirectedGraph_test0_decomposed() throws Exception {
        buildGraphConnections();
    }

    @Test
    public void testSerializeDirectedGraph_test1_decomposed() throws Exception {
        buildGraphConnections();
        MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newDirectedMutableGraph(buildGraphConnections());
    }

    @Test
    public void testSerializeDirectedGraph_test2_decomposed() throws Exception {
        buildGraphConnections();
        MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newDirectedMutableGraph(buildGraphConnections());
        checkSerialization(g);
    }

    @Test
    public void testSerializeDirectedWeightdGraph_test0_decomposed() throws Exception {
        buildWeightedGraphConnections();
    }

    @Test
    public void testSerializeDirectedWeightdGraph_test1_decomposed() throws Exception {
        buildWeightedGraphConnections();
        MutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> g =
                newDirectedMutableGraph(buildWeightedGraphConnections());
    }

    @Test
    public void testSerializeDirectedWeightdGraph_test2_decomposed() throws Exception {
        buildWeightedGraphConnections();
        MutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> g =
                newDirectedMutableGraph(buildWeightedGraphConnections());
        checkSerialization(g);
    }

    @Test
    public void testSerializePath_test0_decomposed() throws Exception {
        BaseLabeledVertex start = new BaseLabeledVertex("start");
    }

    @Test
    public void testSerializePath_test1_decomposed() throws Exception {
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
    }

    @Test
    public void testSerializePath_test2_decomposed() throws Exception {
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
    }

    @Test
    public void testSerializePath_test3_decomposed() throws Exception {
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
    }

    @Test
    public void testSerializePath_test4_decomposed() throws Exception {
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
    }

    @Test
    public void testSerializePath_test5_decomposed() throws Exception {
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> g =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        g.addConnectionInTail(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
    }

    @Test
    public void testSerializePath_test6_decomposed() throws Exception {
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> g =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        g.addConnectionInTail(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        g.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        g.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        g.addConnectionInTail(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
    }

    @Test
    public void testSerializePath_test7_decomposed() throws Exception {
        BaseLabeledVertex start = new BaseLabeledVertex("start");
        BaseLabeledVertex goal = new BaseLabeledVertex("goal");
        BaseLabeledVertex a = new BaseLabeledVertex("a");
        BaseLabeledVertex b = new BaseLabeledVertex("b");
        BaseLabeledVertex c = new BaseLabeledVertex("c");
        InMemoryWeightedPath<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> g =
                new InMemoryWeightedPath<
                        BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                        start,
                        goal,
                        new DoubleWeightBaseOperations(),
                        new BaseWeightedEdge<Double>());
        g.addConnectionInTail(start, new BaseLabeledWeightedEdge<Double>("start <-> a", 1.5D), a);
        g.addConnectionInTail(a, new BaseLabeledWeightedEdge<Double>("a <-> b", 2D), b);
        g.addConnectionInTail(b, new BaseLabeledWeightedEdge<Double>("b <-> c", 3D), c);
        g.addConnectionInTail(c, new BaseLabeledWeightedEdge<Double>("c <-> goal", 3D), goal);
        checkSerialization(g);
    }

    @Test
    public void testSerializeSpanningTree_test0_decomposed() throws Exception {
        final MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                spanningTree =
                        new MutableSpanningTree<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                                new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        populate(spanningTree);
    }

    @Test
    public void testSerializeSpanningTree_test1_decomposed() throws Exception {
        final MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                spanningTree =
                        new MutableSpanningTree<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                                new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        populate(spanningTree);
        buildWeightedGraphConnections();
    }

    @Test
    public void testSerializeSpanningTree_test2_decomposed() throws Exception {
        final MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                spanningTree =
                        new MutableSpanningTree<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                                new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        populate(spanningTree);
        buildWeightedGraphConnections();
        populate(spanningTree).withConnections(buildWeightedGraphConnections());
    }

    @Test
    public void testSerializeSpanningTree_test3_decomposed() throws Exception {
        final MutableSpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>
                spanningTree =
                        new MutableSpanningTree<
                                BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double>(
                                new DoubleWeightBaseOperations(), new BaseWeightedEdge<Double>());
        populate(spanningTree);
        buildWeightedGraphConnections();
        populate(spanningTree).withConnections(buildWeightedGraphConnections());
        checkSerialization(spanningTree);
    }

    @Test
    public void testSerializeSyncronyzedDirectedWeightdGraph_test0_decomposed() throws Exception {
        buildWeightedGraphConnections();
    }

    @Test
    public void testSerializeSyncronyzedDirectedWeightdGraph_test1_decomposed() throws Exception {
        buildWeightedGraphConnections();
        newDirectedMutableGraph(buildWeightedGraphConnections());
    }

    @Test
    public void testSerializeSyncronyzedDirectedWeightdGraph_test2_decomposed() throws Exception {
        buildWeightedGraphConnections();
        newDirectedMutableGraph(buildWeightedGraphConnections());
        Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> g =
                synchronize2(
                        (MutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>)
                                newDirectedMutableGraph(buildWeightedGraphConnections()));
    }

    @Test
    public void testSerializeSyncronyzedDirectedWeightdGraph_test3_decomposed() throws Exception {
        buildWeightedGraphConnections();
        newDirectedMutableGraph(buildWeightedGraphConnections());
        Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> g =
                synchronize2(
                        (MutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>)
                                newDirectedMutableGraph(buildWeightedGraphConnections()));
        checkSerialization(g);
    }

    @Test
    public void testSerializeUndirectedGraph_test0_decomposed() throws Exception {
        buildGraphConnections();
    }

    @Test
    public void testSerializeUndirectedGraph_test1_decomposed() throws Exception {
        buildGraphConnections();
        MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(buildGraphConnections());
    }

    @Test
    public void testSerializeUndirectedGraph_test2_decomposed() throws Exception {
        buildGraphConnections();
        MutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(buildGraphConnections());
        checkSerialization(g);
    }

    @Test
    public void testSerializeUndirectedWeightdGraph_test0_decomposed() throws Exception {
        buildWeightedGraphConnections();
    }

    @Test
    public void testSerializeUndirectedWeightdGraph_test1_decomposed() throws Exception {
        buildWeightedGraphConnections();
        MutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> g =
                newUndirectedMutableGraph(buildWeightedGraphConnections());
    }

    @Test
    public void testSerializeUndirectedWeightdGraph_test2_decomposed() throws Exception {
        buildWeightedGraphConnections();
        MutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> g =
                newUndirectedMutableGraph(buildWeightedGraphConnections());
        checkSerialization(g);
    }
}