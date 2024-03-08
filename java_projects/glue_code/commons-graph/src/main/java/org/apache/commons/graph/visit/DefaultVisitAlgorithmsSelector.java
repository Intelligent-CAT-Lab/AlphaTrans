package org.apache.commons.graph.visit;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import java.util.Iterator;
import java.util.Set;
import java.util.HashSet;
import java.util.LinkedList;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.VertexPair;
import static org.apache.commons.graph.visit.VisitState.CONTINUE;
import static org.apache.commons.graph.visit.VisitState.ABORT;
import static org.apache.commons.graph.utils.Assertions.checkNotNull;
final class DefaultVisitAlgorithmsSelector<V, E, G extends Graph<V, E>>
    private static Value clz = ContextInitializer.getPythonClass("/visit/DefaultVisitAlgorithmsSelector.py", "DefaultVisitAlgorithmsSelector");
    private Value obj;
    public DefaultVisitAlgorithmsSelector(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public <O> O applyingDepthFirstSearch1(GraphVisitHandler<V, E, G, O> handler) {
// 
// return applyingSearch(handler, false);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingDepthFirstSearch1", handler).as(O.class);
}
    public Graph<V, E> applyingDepthFirstSearch0() {
// 
// return applyingDepthFirstSearch1(new VisitGraphBuilder<V, E, G>());
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingDepthFirstSearch0").as(Graph.class);
}
    public <O> O applyingBreadthFirstSearch1(GraphVisitHandler<V, E, G, O> handler) {
// 
// return applyingSearch(handler, true);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingBreadthFirstSearch1", handler).as(O.class);
}
    public Graph<V, E> applyingBreadthFirstSearch0() {
// 
// return applyingBreadthFirstSearch1(new VisitGraphBuilder<V, E, G>());
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingBreadthFirstSearch0").as(Graph.class);
}
    public DefaultVisitAlgorithmsSelector(final G graph, final V source) {
// 
// this.graph = graph;
// this.source = source;
// 

this.obj = clz.invokeMember("__init__", graph, source);
}
    private <O> O applyingSearch(GraphVisitHandler<V, E, G, O> handler, boolean enqueue) {
// 
// handler = checkNotNull(handler, "Graph visitor handler can not be null.");
// 
// handler.discoverGraph(graph);
// 
// final LinkedList<VertexPair<V>> vertexList = new LinkedList<VertexPair<V>>();
// 
// vertexList.addLast(new VertexPair<V>(source, source));
// 
// final Set<V> visitedVertices = new HashSet<V>();
// visitedVertices.add(source);
// 
// boolean visitingGraph = true;
// 
// while (visitingGraph && !vertexList.isEmpty()) {
// final VertexPair<V> pair = enqueue ? vertexList.removeFirst() : vertexList.removeLast();
// final V v = pair.getHead();
// final V prevHead = pair.getTail();
// final E e = prevHead.equals(v) ? null : graph.getEdge(prevHead, v);
// 
// boolean skipVertex = false;
// 
// if (e != null) {
// if (visitedVertices.contains(v)) {
// skipVertex = true;
// } else {
// VisitState stateAfterEdgeDiscovery = handler.discoverEdge(prevHead, e, v);
// if (CONTINUE != stateAfterEdgeDiscovery) {
// skipVertex = true;
// if (ABORT == stateAfterEdgeDiscovery) {
// visitingGraph = false;
// }
// }
// 
// if (ABORT == handler.finishEdge(prevHead, e, v)) {
// skipVertex = true;
// visitingGraph = false;
// }
// }
// }
// 
// boolean vertexWasDiscovered = false;
// if (!skipVertex) {
// visitedVertices.add(v);
// VisitState stateAfterVertexDiscovery = handler.discoverVertex(v);
// vertexWasDiscovered = true;
// if (CONTINUE != stateAfterVertexDiscovery) {
// skipVertex = true;
// if (ABORT == stateAfterVertexDiscovery) {
// visitingGraph = false;
// }
// }
// }
// 
// if (!skipVertex) {
// Iterator<V> connected =
// (graph instanceof DirectedGraph)
// ? ((DirectedGraph<V, E>) graph).getOutbound(v).iterator()
// : graph.getConnectedVertices(v).iterator();
// 
// while (connected.hasNext()) {
// V w = connected.next();
// if (!visitedVertices.contains(w)) {
// vertexList.addLast(new VertexPair<V>(w, v));
// }
// }
// }
// 
// if (vertexWasDiscovered && ABORT == handler.finishVertex(v)) {
// visitingGraph = false;
// }
// }
// 
// handler.finishGraph(graph);
// 
// return handler.onCompleted();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingSearch", handler, enqueue).as(O.class);
}
}
