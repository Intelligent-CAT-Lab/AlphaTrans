package org.apache.commons.graph.coloring;

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

import static org.apache.commons.graph.CommonsGraph.coloring;
import static org.apache.commons.graph.CommonsGraph.newUndirectedMutableGraph;
import static org.apache.commons.graph.utils.GraphUtils.buildBipartedGraph;
import static org.apache.commons.graph.utils.GraphUtils.buildCompleteGraph;
import static org.apache.commons.graph.utils.GraphUtils.buildCrownGraph;
import static org.apache.commons.graph.utils.GraphUtils.buildSudokuGraph;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import org.apache.commons.graph.UndirectedGraph;
import org.apache.commons.graph.builder.AbstractGraphConnection;
import org.apache.commons.graph.model.BaseLabeledEdge;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.junit.Test;

import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.logging.Logger;

/** */
public class GraphColoringBackTrackingTestCase extends AbstractColoringTest {

    /** see <a href="http://en.wikipedia.org/wiki/Crown_graph">wiki</a> for more details */

    @Test
    public void testCrawnGraph_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCrownGraph(6, g);
    }

    @Test
    public void testCrawnGraph_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCrownGraph(6, g);
        coloring(g);
    }

    @Test
    public void testCrawnGraph_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCrownGraph(6, g);
        coloring(g);
        createColorsList(2);
    }

    @Test
    public void testCrawnGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCrownGraph(6, g);
        coloring(g);
        createColorsList(2);
        coloring(g).withColors(createColorsList(2));
    }

    @Test
    public void testCrawnGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCrownGraph(6, g);
        coloring(g);
        createColorsList(2);
        coloring(g).withColors(createColorsList(2));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(createColorsList(2)).applyingBackTrackingAlgorithm0();
    }

    @Test
    public void testCrawnGraph_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCrownGraph(6, g);
        coloring(g);
        createColorsList(2);
        coloring(g).withColors(createColorsList(2));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(createColorsList(2)).applyingBackTrackingAlgorithm0();
        assertNotNull(coloredVertices);
        assertEquals(2, coloredVertices.getRequiredColors());
    }

    @Test
    public void testCrawnGraph_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCrownGraph(6, g);
        coloring(g);
        createColorsList(2);
        coloring(g).withColors(createColorsList(2));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(createColorsList(2)).applyingBackTrackingAlgorithm0();
        assertNotNull(coloredVertices);
        assertEquals(2, coloredVertices.getRequiredColors());
        checkColoring(g, coloredVertices);
    }

    @Test
    public void testCromaticNumber_test0_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
    }

    @Test
    public void testCromaticNumber_test1_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
    }

    @Test
    public void testCromaticNumber_test2_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertex =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        coloredVertex.addColor(two, 2);
    }

    @Test
    public void testCromaticNumber_test3_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertex =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        coloredVertex.addColor(two, 2);
        coloring(g);
    }

    @Test
    public void testCromaticNumber_test4_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertex =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        coloredVertex.addColor(two, 2);
        coloring(g);
        createColorsList(3);
    }

    @Test
    public void testCromaticNumber_test5_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertex =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        coloredVertex.addColor(two, 2);
        coloring(g);
        createColorsList(3);
        coloring(g).withColors(createColorsList(3));
    }

    @Test
    public void testCromaticNumber_test6_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertex =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        coloredVertex.addColor(two, 2);
        coloring(g);
        createColorsList(3);
        coloring(g).withColors(createColorsList(3));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g)
                        .withColors(createColorsList(3))
                        .applyingBackTrackingAlgorithm1(coloredVertex);
    }

    @Test
    public void testCromaticNumber_test7_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertex =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        coloredVertex.addColor(two, 2);
        coloring(g);
        createColorsList(3);
        coloring(g).withColors(createColorsList(3));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g)
                        .withColors(createColorsList(3))
                        .applyingBackTrackingAlgorithm1(coloredVertex);
        assertNotNull(coloredVertices);
        assertEquals(3, coloredVertices.getRequiredColors());
    }

    @Test
    public void testCromaticNumber_test8_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertex =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        coloredVertex.addColor(two, 2);
        coloring(g);
        createColorsList(3);
        coloring(g).withColors(createColorsList(3));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g)
                        .withColors(createColorsList(3))
                        .applyingBackTrackingAlgorithm1(coloredVertex);
        assertNotNull(coloredVertices);
        assertEquals(3, coloredVertices.getRequiredColors());
        assertEquals(new Integer(2), coloredVertices.getColor(two));
    }

    @Test
    public void testCromaticNumber_test9_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertex =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        coloredVertex.addColor(two, 2);
        coloring(g);
        createColorsList(3);
        coloring(g).withColors(createColorsList(3));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g)
                        .withColors(createColorsList(3))
                        .applyingBackTrackingAlgorithm1(coloredVertex);
        assertNotNull(coloredVertices);
        assertEquals(3, coloredVertices.getRequiredColors());
        assertEquals(new Integer(2), coloredVertices.getColor(two));
        checkColoring(g, coloredVertices);
    }

    @Test
    public void testCromaticNumberBiparted_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildBipartedGraph(100, g1);
    }

    @Test
    public void testCromaticNumberBiparted_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildBipartedGraph(100, g1);
        coloring(g1);
    }

    @Test
    public void testCromaticNumberBiparted_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildBipartedGraph(100, g1);
        coloring(g1);
        createColorsList(2);
    }

    @Test
    public void testCromaticNumberBiparted_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildBipartedGraph(100, g1);
        coloring(g1);
        createColorsList(2);
        coloring(g1).withColors(createColorsList(2));
    }

    @Test
    public void testCromaticNumberBiparted_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildBipartedGraph(100, g1);
        coloring(g1);
        createColorsList(2);
        coloring(g1).withColors(createColorsList(2));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(createColorsList(2)).applyingBackTrackingAlgorithm0();
    }

    @Test
    public void testCromaticNumberBiparted_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildBipartedGraph(100, g1);
        coloring(g1);
        createColorsList(2);
        coloring(g1).withColors(createColorsList(2));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(createColorsList(2)).applyingBackTrackingAlgorithm0();
        assertNotNull(coloredVertices);
        assertEquals(2, coloredVertices.getRequiredColors());
    }

    @Test
    public void testCromaticNumberBiparted_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildBipartedGraph(100, g1);
        coloring(g1);
        createColorsList(2);
        coloring(g1).withColors(createColorsList(2));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(createColorsList(2)).applyingBackTrackingAlgorithm0();
        assertNotNull(coloredVertices);
        assertEquals(2, coloredVertices.getRequiredColors());
        checkColoring(g1, coloredVertices);
    }

    @Test
    public void testCromaticNumberComplete_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(100, g1);
    }

    @Test
    public void testCromaticNumberComplete_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(100, g1);
        coloring(g1);
    }

    @Test
    public void testCromaticNumberComplete_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(100, g1);
        coloring(g1);
        createColorsList(100);
    }

    @Test
    public void testCromaticNumberComplete_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(100, g1);
        coloring(g1);
        createColorsList(100);
        coloring(g1).withColors(createColorsList(100));
    }

    @Test
    public void testCromaticNumberComplete_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(100, g1);
        coloring(g1);
        createColorsList(100);
        coloring(g1).withColors(createColorsList(100));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(createColorsList(100)).applyingBackTrackingAlgorithm0();
    }

    @Test
    public void testCromaticNumberComplete_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(100, g1);
        coloring(g1);
        createColorsList(100);
        coloring(g1).withColors(createColorsList(100));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(createColorsList(100)).applyingBackTrackingAlgorithm0();
        assertNotNull(coloredVertices);
        assertEquals(100, coloredVertices.getRequiredColors());
    }

    @Test
    public void testCromaticNumberComplete_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCompleteGraph(100, g1);
        coloring(g1);
        createColorsList(100);
        coloring(g1).withColors(createColorsList(100));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(createColorsList(100)).applyingBackTrackingAlgorithm0();
        assertNotNull(coloredVertices);
        assertEquals(100, coloredVertices.getRequiredColors());
        checkColoring(g1, coloredVertices);
    }

    @Test
    public void testCromaticNumberSparseGraph_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
    }

    @Test
    public void testCromaticNumberSparseGraph_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
        coloring(g1);
    }

    @Test
    public void testCromaticNumberSparseGraph_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
        coloring(g1);
        createColorsList(1);
    }

    @Test
    public void testCromaticNumberSparseGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
        coloring(g1);
        createColorsList(1);
        coloring(g1).withColors(createColorsList(1));
    }

    @Test
    public void testCromaticNumberSparseGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
        coloring(g1);
        createColorsList(1);
        coloring(g1).withColors(createColorsList(1));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(createColorsList(1)).applyingBackTrackingAlgorithm0();
    }

    @Test
    public void testCromaticNumberSparseGraph_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
        coloring(g1);
        createColorsList(1);
        coloring(g1).withColors(createColorsList(1));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(createColorsList(1)).applyingBackTrackingAlgorithm0();
        assertNotNull(coloredVertices);
        assertEquals(1, coloredVertices.getRequiredColors());
    }

    @Test
    public void testCromaticNumberSparseGraph_test6_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
        coloring(g1);
        createColorsList(1);
        coloring(g1).withColors(createColorsList(1));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(createColorsList(1)).applyingBackTrackingAlgorithm0();
        assertNotNull(coloredVertices);
        assertEquals(1, coloredVertices.getRequiredColors());
        checkColoring(g1, coloredVertices);
    }

    @Test
    public void testEmptyGraph_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        coloring(g);
    }

    @Test
    public void testEmptyGraph_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        coloring(g);
        createColorsList(1);
    }

    @Test
    public void testEmptyGraph_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        coloring(g);
        createColorsList(1);
        coloring(g).withColors(createColorsList(1));
    }

    @Test
    public void testEmptyGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        coloring(g);
        createColorsList(1);
        coloring(g).withColors(createColorsList(1));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(createColorsList(1)).applyingBackTrackingAlgorithm0();
    }

    @Test
    public void testEmptyGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        coloring(g);
        createColorsList(1);
        coloring(g).withColors(createColorsList(1));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(createColorsList(1)).applyingBackTrackingAlgorithm0();
        assertNotNull(coloredVertices);
        assertEquals(0, coloredVertices.getRequiredColors());
    }

    @Test
    public void testNotEnoughtColorGraph_test0_decomposed() throws NotEnoughColorsException {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
    }

    @Test
    public void testNotEnoughtColorGraph_test1_decomposed() throws NotEnoughColorsException {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
    }

    @Test
    public void testNotEnoughtColorGraph_test2_decomposed() throws NotEnoughColorsException {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        coloring(g);
    }

    @Test
    public void testNotEnoughtColorGraph_test3_decomposed() throws NotEnoughColorsException {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        coloring(g);
        createColorsList(1);
    }

    @Test
    public void testNotEnoughtColorGraph_test4_decomposed() throws NotEnoughColorsException {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        coloring(g);
        createColorsList(1);
        coloring(g).withColors(createColorsList(1));
    }

    @Test(expected = NotEnoughColorsException.class)
    public void testNotEnoughtColorGraph_test5_decomposed() throws NotEnoughColorsException {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                addVertex(two);
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        coloring(g);
        createColorsList(1);
        coloring(g).withColors(createColorsList(1));
        coloring(g).withColors(createColorsList(1)).applyingBackTrackingAlgorithm0();
    }

    @Test
    public void testNullColorGraph_test0_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        coloring(g);
    }

    @Test(expected = NullPointerException.class)
    public void testNullColorGraph_test1_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        coloring(g);
        coloring(g).withColors(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullColorGraph_test2_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        coloring(g);
        coloring(g).withColors(null);
        coloring(g).withColors(null).applyingBackTrackingAlgorithm0();
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test0_decomposed()  {
        coloring((UndirectedGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test1_decomposed()  {
        coloring((UndirectedGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        coloring((UndirectedGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).withColors(null);
    }

    @Test(expected = NullPointerException.class)
    public void testNullGraph_test2_decomposed()  {
        coloring((UndirectedGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null);
        coloring((UndirectedGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null).withColors(null);
        coloring((UndirectedGraph<BaseLabeledVertex, BaseLabeledWeightedEdge<Double>>) null)
                .withColors(null)
                .applyingBackTrackingAlgorithm0();
    }

    @Test
    public void testSudoku_test0_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
    }

    @Test
    public void testSudoku_test1_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        coloring(g1);
    }

    @Test
    public void testSudoku_test2_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        coloring(g1);
        createColorsList(9);
    }

    @Test
    public void testSudoku_test3_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
    }

    @Test
    public void testSudoku_test4_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1).withColors(createColorsList(9)).applyingBackTrackingAlgorithm0();
    }

    @Test
    public void testSudoku_test5_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1).withColors(createColorsList(9)).applyingBackTrackingAlgorithm0();
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
    }

    @Test
    public void testSudoku_test6_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1).withColors(createColorsList(9)).applyingBackTrackingAlgorithm0();
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
        assertEquals(9, sudoku.getRequiredColors());
    }

    @Test
    public void testSudoku_test7_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1).withColors(createColorsList(9)).applyingBackTrackingAlgorithm0();
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
        assertEquals(9, sudoku.getRequiredColors());
        StringBuilder sb = new StringBuilder();
        NumberFormat nf = new DecimalFormat("00");
        sb.append("\n");
    }

    @Test
    public void testSudoku_test8_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1).withColors(createColorsList(9)).applyingBackTrackingAlgorithm0();
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
        assertEquals(9, sudoku.getRequiredColors());
        StringBuilder sb = new StringBuilder();
        NumberFormat nf = new DecimalFormat("00");
        sb.append("\n");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append("| " + nf.format(sudoku.getColor(grid[i][j])) + " | ");
            }
            sb.append("\n");
        }
    }

    @Test
    public void testSudoku_test9_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1).withColors(createColorsList(9)).applyingBackTrackingAlgorithm0();
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
        assertEquals(9, sudoku.getRequiredColors());
        StringBuilder sb = new StringBuilder();
        NumberFormat nf = new DecimalFormat("00");
        sb.append("\n");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append("| " + nf.format(sudoku.getColor(grid[i][j])) + " | ");
            }
            sb.append("\n");
        }
        Logger.getAnonymousLogger().fine(sb.toString());
    }

    @Test
    public void testSudokuWithConstraints_test0_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
    }

    @Test
    public void testSudokuWithConstraints_test1_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
    }

    @Test
    public void testSudokuWithConstraints_test2_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
    }

    @Test
    public void testSudokuWithConstraints_test3_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
    }

    @Test
    public void testSudokuWithConstraints_test4_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
        createColorsList(9);
    }

    @Test
    public void testSudokuWithConstraints_test5_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
    }

    @Test
    public void testSudokuWithConstraints_test6_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1)
                        .withColors(createColorsList(9))
                        .applyingBackTrackingAlgorithm1(predefinedColor);
    }

    @Test
    public void testSudokuWithConstraints_test7_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1)
                        .withColors(createColorsList(9))
                        .applyingBackTrackingAlgorithm1(predefinedColor);
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
    }

    @Test
    public void testSudokuWithConstraints_test8_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1)
                        .withColors(createColorsList(9))
                        .applyingBackTrackingAlgorithm1(predefinedColor);
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
        assertEquals(9, sudoku.getRequiredColors());
    }

    @Test
    public void testSudokuWithConstraints_test9_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1)
                        .withColors(createColorsList(9))
                        .applyingBackTrackingAlgorithm1(predefinedColor);
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
        assertEquals(9, sudoku.getRequiredColors());
        assertEquals(new Integer(1), sudoku.getColor(grid[0][0]));
        assertEquals(new Integer(8), sudoku.getColor(grid[5][5]));
        assertEquals(new Integer(5), sudoku.getColor(grid[1][2]));
    }

    @Test
    public void testSudokuWithConstraints_test10_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1)
                        .withColors(createColorsList(9))
                        .applyingBackTrackingAlgorithm1(predefinedColor);
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
        assertEquals(9, sudoku.getRequiredColors());
        assertEquals(new Integer(1), sudoku.getColor(grid[0][0]));
        assertEquals(new Integer(8), sudoku.getColor(grid[5][5]));
        assertEquals(new Integer(5), sudoku.getColor(grid[1][2]));
        StringBuilder sb = new StringBuilder();
        NumberFormat nf = new DecimalFormat("00");
        sb.append("\n");
    }

    @Test
    public void testSudokuWithConstraints_test11_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1)
                        .withColors(createColorsList(9))
                        .applyingBackTrackingAlgorithm1(predefinedColor);
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
        assertEquals(9, sudoku.getRequiredColors());
        assertEquals(new Integer(1), sudoku.getColor(grid[0][0]));
        assertEquals(new Integer(8), sudoku.getColor(grid[5][5]));
        assertEquals(new Integer(5), sudoku.getColor(grid[1][2]));
        StringBuilder sb = new StringBuilder();
        NumberFormat nf = new DecimalFormat("00");
        sb.append("\n");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append("| ");
                sb.append(nf.format(sudoku.getColor(grid[i][j])));
                sb.append(" | ");
            }
            sb.append("\n");
        }
    }

    @Test
    public void testSudokuWithConstraints_test12_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        BaseLabeledVertex[][] grid = buildSudokuGraph(g1);
        ColoredVertices<BaseLabeledVertex, Integer> predefinedColor =
                new ColoredVertices<BaseLabeledVertex, Integer>();
        predefinedColor.addColor(grid[0][0], 1);
        predefinedColor.addColor(grid[5][5], 8);
        predefinedColor.addColor(grid[1][2], 5);
        coloring(g1);
        createColorsList(9);
        coloring(g1).withColors(createColorsList(9));
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1)
                        .withColors(createColorsList(9))
                        .applyingBackTrackingAlgorithm1(predefinedColor);
        assertNotNull(sudoku);
        checkColoring(g1, sudoku);
        assertEquals(9, sudoku.getRequiredColors());
        assertEquals(new Integer(1), sudoku.getColor(grid[0][0]));
        assertEquals(new Integer(8), sudoku.getColor(grid[5][5]));
        assertEquals(new Integer(5), sudoku.getColor(grid[1][2]));
        StringBuilder sb = new StringBuilder();
        NumberFormat nf = new DecimalFormat("00");
        sb.append("\n");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append("| ");
                sb.append(nf.format(sudoku.getColor(grid[i][j])));
                sb.append(" | ");
            }
            sb.append("\n");
        }
        Logger.getAnonymousLogger().fine(sb.toString());
    }
}