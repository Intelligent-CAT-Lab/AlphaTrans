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

import static org.apache.commons.graph.utils.Assertions.checkNotNull;

import org.apache.commons.graph.UndirectedGraph;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

/**
 * {@link ColoringAlgorithmsSelector} implementation.
 *
 * @param <V> the Graph vertices type
 * @param <E> the Graph edges type
 * @param <C> the Color vertices type
 */
final class DefaultColoringAlgorithmsSelector<V, E, C>
        implements ColoringAlgorithmsSelector<V, E, C> {

    private final UndirectedGraph<V, E> g;

    private final Set<C> colors;

    public DefaultColoringAlgorithmsSelector(UndirectedGraph<V, E> g, Set<C> colors) {
        this.g = g;
        this.colors = colors;
    }

    /** {@inheritDoc} */
    public ColoredVertices<V, C> applyingBackTrackingAlgorithm0() {
        return applyingBackTrackingAlgorithm1(new ColoredVertices<V, C>());
    }

    /** {@inheritDoc} */
    public ColoredVertices<V, C> applyingBackTrackingAlgorithm1(
            ColoredVertices<V, C> partialColoredVertex) {
        partialColoredVertex =
                checkNotNull(partialColoredVertex, "PartialColoredVertex must be not null");

        final List<V> verticesList = new ArrayList<V>();

        for (V v : g.getVertices0()) {
            if (!partialColoredVertex.containsColoredVertex(v)) {
                verticesList.add(v);
            }
        }

        if (backtraking(-1, verticesList, partialColoredVertex)) {
            return partialColoredVertex;
        }

        throw new NotEnoughColorsException(colors);
    }

    /** {@inheritDoc} */
    public ColoredVertices<V, C> applyingGreedyAlgorithm() {
        final ColoredVertices<V, C> coloredVertices = new ColoredVertices<V, C>();

        final UncoloredOrderedVertices<V> uncoloredOrderedVertices =
                new UncoloredOrderedVertices<V>();

        for (V v : g.getVertices0()) {
            uncoloredOrderedVertices.addVertexDegree(v, g.getDegree(v));
        }

        Iterator<V> it = uncoloredOrderedVertices.iterator();
        Iterator<C> colorsIt = colors.iterator();
        while (it.hasNext()) {
            if (!colorsIt.hasNext()) {
                throw new NotEnoughColorsException(colors);
            }
            C color = colorsIt.next();

            List<V> currentColorVertices = new ArrayList<V>();
            Iterator<V> uncoloredVtxIterator = uncoloredOrderedVertices.iterator();
            while (uncoloredVtxIterator.hasNext()) {
                V uncoloredVtx = uncoloredVtxIterator.next();

                boolean foundAnAdjacentVertex = false;
                for (V currentColoredVtx : currentColorVertices) {
                    if (g.getEdge(currentColoredVtx, uncoloredVtx) != null) {
                        foundAnAdjacentVertex = true;
                        break;
                    }
                }

                if (!foundAnAdjacentVertex) {
                    uncoloredVtxIterator.remove();
                    coloredVertices.addColor(uncoloredVtx, color);
                    currentColorVertices.add(uncoloredVtx);
                }
            }

            it = uncoloredOrderedVertices.iterator();
        }

        return coloredVertices;
    }

    /**
     * This is the recursive step.
     *
     * @param result The set that will be returned
     * @param element the element
     * @return true if there is a valid coloring for the graph, false otherwise.
     */
    private boolean backtraking(
            int currentVertexIndex, List<V> verticesList, ColoredVertices<V, C> coloredVertices) {
        if (currentVertexIndex != -1
                && isThereColorConflict(verticesList.get(currentVertexIndex), coloredVertices)) {
            return false;
        }

        if (currentVertexIndex == verticesList.size() - 1) {
            return true;
        }

        int next = currentVertexIndex + 1;
        V nextVertex = verticesList.get(next);
        for (C color : colors) {
            coloredVertices.addColor(nextVertex, color);
            boolean isDone = backtraking(next, verticesList, coloredVertices);
            if (isDone) {
                return true;
            }
        }
        coloredVertices.removeColor(nextVertex);
        return false;
    }

    /**
     * Tests if there is some adjacent vertices with the same color.
     *
     * @param currentVertex
     * @return
     */
    private boolean isThereColorConflict(V currentVertex, ColoredVertices<V, C> coloredVertices) {
        if (currentVertex == null) {
            return false;
        }
        C nextVertecColor = coloredVertices.getColor(currentVertex);
        if (nextVertecColor == null) {
            return false;
        }

        for (V abj : g.getConnectedVertices(currentVertex)) {
            C adjColor = coloredVertices.getColor(abj);
            if (adjColor != null && nextVertecColor.equals(adjColor)) {
                return true;
            }
        }
        return false;
    }
}
