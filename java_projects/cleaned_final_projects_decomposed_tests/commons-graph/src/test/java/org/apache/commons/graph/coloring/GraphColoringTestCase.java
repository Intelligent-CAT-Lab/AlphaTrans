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

import java.util.Set;

/** */
public class GraphColoringTestCase extends AbstractColoringTest {

    private Set<Integer> colors = createColorsList(11);

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
        coloring(g).withColors(colors);
    }

    @Test
    public void testCrawnGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCrownGraph(6, g);
        coloring(g);
        coloring(g).withColors(colors);
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(colors).applyingGreedyAlgorithm();
    }

    @Test
    public void testCrawnGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildCrownGraph(6, g);
        coloring(g);
        coloring(g).withColors(colors);
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(colors).applyingGreedyAlgorithm();
        checkColoring(g, coloredVertices);
    }

    @Test
    public void testCromaticNumber_test0_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                BaseLabeledVertex two = addVertex(new BaseLabeledVertex("2"));
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
    }

    @Test
    public void testCromaticNumber_test1_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                BaseLabeledVertex two = addVertex(new BaseLabeledVertex("2"));
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        coloring(g);
    }

    @Test
    public void testCromaticNumber_test2_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                BaseLabeledVertex two = addVertex(new BaseLabeledVertex("2"));
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        coloring(g);
        coloring(g).withColors(colors);
    }

    @Test
    public void testCromaticNumber_test3_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                BaseLabeledVertex two = addVertex(new BaseLabeledVertex("2"));
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        coloring(g);
        coloring(g).withColors(colors);
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(colors).applyingGreedyAlgorithm();
    }

    @Test
    public void testCromaticNumber_test4_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                newUndirectedMutableGraph(
                        new AbstractGraphConnection<BaseLabeledVertex, BaseLabeledEdge>() {

                            public void connect0() {
                                BaseLabeledVertex one = addVertex(new BaseLabeledVertex("1"));
                                BaseLabeledVertex two = addVertex(new BaseLabeledVertex("2"));
                                BaseLabeledVertex three = addVertex(new BaseLabeledVertex("3"));

                                addEdge(new BaseLabeledEdge("1 -> 2")).from(one).to(two);
                                addEdge(new BaseLabeledEdge("2 -> 3")).from(two).to(three);
                                addEdge(new BaseLabeledEdge("3 -> 1")).from(three).to(one);
                            }
                        });
        coloring(g);
        coloring(g).withColors(colors);
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(colors).applyingGreedyAlgorithm();
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
        coloring(g1).withColors(colors);
    }

    @Test
    public void testCromaticNumberBiparted_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildBipartedGraph(100, g1);
        coloring(g1);
        coloring(g1).withColors(colors);
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(colors).applyingGreedyAlgorithm();
    }

    @Test
    public void testCromaticNumberBiparted_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildBipartedGraph(100, g1);
        coloring(g1);
        coloring(g1).withColors(colors);
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(colors).applyingGreedyAlgorithm();
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
                coloring(g1).withColors(createColorsList(100)).applyingGreedyAlgorithm();
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
                coloring(g1).withColors(createColorsList(100)).applyingGreedyAlgorithm();
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
        coloring(g1).withColors(colors);
    }

    @Test
    public void testCromaticNumberSparseGraph_test3_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
        coloring(g1);
        coloring(g1).withColors(colors);
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(colors).applyingGreedyAlgorithm();
    }

    @Test
    public void testCromaticNumberSparseGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
        coloring(g1);
        coloring(g1).withColors(colors);
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(colors).applyingGreedyAlgorithm();
        assertEquals(1, coloredVertices.getRequiredColors());
    }

    @Test
    public void testCromaticNumberSparseGraph_test5_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        for (int i = 0; i < 100; i++) {
            g1.addVertex(new BaseLabeledVertex(String.valueOf(i)));
        }
        coloring(g1);
        coloring(g1).withColors(colors);
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g1).withColors(colors).applyingGreedyAlgorithm();
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
                coloring(g).withColors(createColorsList(1)).applyingGreedyAlgorithm();
    }

    @Test
    public void testEmptyGraph_test4_decomposed()  {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        coloring(g);
        createColorsList(1);
        coloring(g).withColors(createColorsList(1));
        ColoredVertices<BaseLabeledVertex, Integer> coloredVertices =
                coloring(g).withColors(createColorsList(1)).applyingGreedyAlgorithm();
        assertNotNull(coloredVertices);
        assertEquals(0, coloredVertices.getRequiredColors());
    }

    @Test
    public void testNotEnoughtColorGreedyGraph_test0_decomposed()  {
        final BaseLabeledVertex two = new BaseLabeledVertex("2");
    }

    @Test
    public void testNotEnoughtColorGreedyGraph_test1_decomposed()  {
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
    public void testNotEnoughtColorGreedyGraph_test2_decomposed()  {
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
    public void testNotEnoughtColorGreedyGraph_test3_decomposed()  {
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
    public void testNotEnoughtColorGreedyGraph_test4_decomposed()  {
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
    public void testNotEnoughtColorGreedyGraph_test5_decomposed()  {
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
        coloring(g).withColors(createColorsList(1)).applyingGreedyAlgorithm();
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
                .applyingGreedyAlgorithm();
    }

    @Test
    public void testSudoku_test0_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildSudokuGraph(g1);
    }

    @Test
    public void testSudoku_test1_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildSudokuGraph(g1);
        Set<Integer> col = createColorsList(9);
    }

    @Test
    public void testSudoku_test2_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildSudokuGraph(g1);
        Set<Integer> col = createColorsList(9);
        coloring(g1);
    }

    @Test
    public void testSudoku_test3_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildSudokuGraph(g1);
        Set<Integer> col = createColorsList(9);
        coloring(g1);
        coloring(g1).withColors(col);
    }

    @Test
    public void testSudoku_test4_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildSudokuGraph(g1);
        Set<Integer> col = createColorsList(9);
        coloring(g1);
        coloring(g1).withColors(col);
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1).withColors(col).applyingBackTrackingAlgorithm0();
    }

    @Test
    public void testSudoku_test5_decomposed() throws Exception {
        UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g1 =
                new UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge>();
        buildSudokuGraph(g1);
        Set<Integer> col = createColorsList(9);
        coloring(g1);
        coloring(g1).withColors(col);
        ColoredVertices<BaseLabeledVertex, Integer> sudoku =
                coloring(g1).withColors(col).applyingBackTrackingAlgorithm0();
        checkColoring(g1, sudoku);
    }
}