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

    @Test(expected = IllegalStateException.class)
    public void testEmptyGraph() {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromArbitrarySource()
                .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test(expected = IllegalStateException.class)
    public void testNotExistVertex() {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromSource(new BaseLabeledVertex("NOT EXIST"));
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph() {
        minimumSpanningTree((Graph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromArbitrarySource()
                .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
    }

    @Test(expected = NullPointerException.class)
    public void testNullMonoid() {
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

        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromSource(a)
                .applyingBoruvkaAlgorithm(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullVertex() {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();
        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromSource(null)
                .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
    }

    /** Test Graph and boruvka's solution can be seen on */
    @Test
    public void testVerifyWikipediaMinimumSpanningTree() {
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

        SpanningTree<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>, Double> actual =
                minimumSpanningTree(input)
                        .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                        .fromArbitrarySource()
                        .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());

        assertEquals(expected, actual);
    }

    /** Test Boruvka's solution on a not-connected graph. */
    @Test(expected = IllegalStateException.class)
    public void verifySparseGraphMinimumSpanningTree() {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>> input =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>();

        input.addVertex(new BaseLabeledVertex("A"));
        input.addVertex(new BaseLabeledVertex("B"));
        input.addVertex(new BaseLabeledVertex("C"));
        input.addVertex(new BaseLabeledVertex("D"));
        input.addVertex(new BaseLabeledVertex("E"));
        input.addVertex(new BaseLabeledVertex("F"));
        input.addVertex(new BaseLabeledVertex("G"));

        minimumSpanningTree(input)
                .whereEdgesHaveWeights(new BaseWeightedEdge<Double>())
                .fromArbitrarySource()
                .applyingBoruvkaAlgorithm(new DoubleWeightBaseOperations());
    }
}
