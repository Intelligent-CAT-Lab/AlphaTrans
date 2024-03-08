package org.apache.commons.graph.coloring;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.ArrayList;
import org.apache.commons.graph.UndirectedGraph;
import static org.apache.commons.graph.utils.Assertions.checkNotNull;
final class DefaultColoringAlgorithmsSelector<V, E, C>
    private static Value clz = ContextInitializer.getPythonClass("/coloring/DefaultColoringAlgorithmsSelector.py", "DefaultColoringAlgorithmsSelector");
    private Value obj;
    public DefaultColoringAlgorithmsSelector(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public ColoredVertices<V, C> applyingGreedyAlgorithm() {
// 
// final ColoredVertices<V, C> coloredVertices = new ColoredVertices<V, C>();
// 
// final UncoloredOrderedVertices<V> uncoloredOrderedVertices =
// new UncoloredOrderedVertices<V>();
// 
// for (V v : g.getVertices0()) {
// uncoloredOrderedVertices.addVertexDegree(v, g.getDegree(v));
// }
// 
// Iterator<V> it = uncoloredOrderedVertices.iterator();
// Iterator<C> colorsIt = colors.iterator();
// while (it.hasNext()) {
// if (!colorsIt.hasNext()) {
// throw new NotEnoughColorsException(colors);
// }
// C color = colorsIt.next();
// 
// List<V> currentColorVertices = new ArrayList<V>();
// Iterator<V> uncoloredVtxIterator = uncoloredOrderedVertices.iterator();
// while (uncoloredVtxIterator.hasNext()) {
// V uncoloredVtx = uncoloredVtxIterator.next();
// 
// boolean foundAnAdjacentVertex = false;
// for (V currentColoredVtx : currentColorVertices) {
// if (g.getEdge(currentColoredVtx, uncoloredVtx) != null) {
// foundAnAdjacentVertex = true;
// break;
// }
// }
// 
// if (!foundAnAdjacentVertex) {
// uncoloredVtxIterator.remove();
// coloredVertices.addColor(uncoloredVtx, color);
// currentColorVertices.add(uncoloredVtx);
// }
// }
// 
// it = uncoloredOrderedVertices.iterator();
// }
// 
// return coloredVertices;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingGreedyAlgorithm").as(ColoredVertices.class);
}
    public ColoredVertices<V, C> applyingBackTrackingAlgorithm1(
            ColoredVertices<V, C> partialColoredVertex) {
// 
// partialColoredVertex =
// checkNotNull(partialColoredVertex, "PartialColoredVertex must be not null");
// 
// final List<V> verticesList = new ArrayList<V>();
// 
// for (V v : g.getVertices0()) {
// if (!partialColoredVertex.containsColoredVertex(v)) {
// verticesList.add(v);
// }
// }
// 
// if (backtraking(-1, verticesList, partialColoredVertex)) {
// return partialColoredVertex;
// }
// 
// throw new NotEnoughColorsException(colors);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingBackTrackingAlgorithm1", partialColoredVertex).as(ColoredVertices.class);
}
    public ColoredVertices<V, C> applyingBackTrackingAlgorithm0() {
// 
// return applyingBackTrackingAlgorithm1(new ColoredVertices<V, C>());
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingBackTrackingAlgorithm0").as(ColoredVertices.class);
}
    public DefaultColoringAlgorithmsSelector(UndirectedGraph<V, E> g, Set<C> colors) {
// 
// this.g = g;
// this.colors = colors;
// 

this.obj = clz.invokeMember("__init__", g, colors);
}
    private boolean isThereColorConflict(V currentVertex, ColoredVertices<V, C> coloredVertices) {
// 
// if (currentVertex == null) {
// return false;
// }
// C nextVertecColor = coloredVertices.getColor(currentVertex);
// if (nextVertecColor == null) {
// return false;
// }
// 
// for (V abj : g.getConnectedVertices(currentVertex)) {
// C adjColor = coloredVertices.getColor(abj);
// if (adjColor != null && nextVertecColor.equals(adjColor)) {
// return true;
// }
// }
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isThereColorConflict", currentVertex, coloredVertices).as(boolean.class);
}
    private boolean backtraking(
            int currentVertexIndex, List<V> verticesList, ColoredVertices<V, C> coloredVertices) {
// 
// if (currentVertexIndex != -1
// && isThereColorConflict(verticesList.get(currentVertexIndex), coloredVertices)) {
// return false;
// }
// 
// if (currentVertexIndex == verticesList.size() - 1) {
// return true;
// }
// 
// int next = currentVertexIndex + 1;
// V nextVertex = verticesList.get(next);
// for (C color : colors) {
// coloredVertices.addColor(nextVertex, color);
// boolean isDone = backtraking(next, verticesList, coloredVertices);
// if (isDone) {
// return true;
// }
// }
// coloredVertices.removeColor(nextVertex);
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("backtraking", currentVertexIndex, verticesList, coloredVertices).as(boolean.class);
}
}
