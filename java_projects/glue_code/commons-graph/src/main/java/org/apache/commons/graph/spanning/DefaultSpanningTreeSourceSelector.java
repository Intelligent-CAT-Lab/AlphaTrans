package org.apache.commons.graph.spanning;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import java.util.List;
import java.util.Queue;
import java.util.ArrayList;
import java.util.PriorityQueue;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.shortestpath.PathNotFoundException;
import static java.util.Collections.reverseOrder;
import static org.apache.commons.graph.CommonsGraph.findShortestPath;
import static org.apache.commons.graph.utils.Assertions.checkNotNull;
import static org.apache.commons.graph.utils.Assertions.checkState;
final class DefaultSpanningTreeSourceSelector<V, W, WE>
    private static Value clz = ContextInitializer.getPythonClass("/spanning/DefaultSpanningTreeSourceSelector.py", "DefaultSpanningTreeSourceSelector");
    private Value obj;
    public DefaultSpanningTreeSourceSelector(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public <S extends V> SpanningTreeAlgorithmSelector<V, W, WE> fromSource(S source) {
// 
// source =
// checkNotNull(
// source,
// "Spanning tree cannot be calculated without expressing the source vertex");
// checkState(graph.containsVertex(source), "Vertex %s does not exist in the Graph", source);
// return new DefaultSpanningTreeAlgorithmSelector<V, W, WE>(graph, weightedEdges, source);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("fromSource", source).as(SpanningTreeAlgorithmSelector.class);
}
    public SpanningTreeAlgorithmSelector<V, W, WE> fromArbitrarySource() {
// 
// checkState(graph.getOrder() > 0, "Spanning tree cannot be calculated on an empty graph");
// return fromSource(graph.getVertices0().iterator().next());
// 


// TODO: Check the type mapping below!
return obj.invokeMember("fromArbitrarySource").as(SpanningTreeAlgorithmSelector.class);
}
    public <WO extends OrderedMonoid<W>> SpanningTree<V, WE, W> applyingReverseDeleteAlgorithm(
            WO weightOperations) {
// 
// 
// checkNotNull(
// weightOperations,
// "The Reverse-Delete algorithm cannot be calulated with null weight operations");
// 
// final Queue<WE> sortedEdge =
// new PriorityQueue<WE>(
// 11,
// reverseOrder(
// new WeightedEdgesComparator<W, WE>(
// weightOperations, weightedEdges)));
// final List<WE> visitedEdge = new ArrayList<WE>();
// 
// Iterable<WE> edges = graph.getEdges();
// for (WE we : edges) {
// sortedEdge.offer(we);
// }
// 
// Graph<V, WE> tmpGraph = new ReverseDeleteGraph<V, WE>(graph, sortedEdge, visitedEdge);
// 
// while (!sortedEdge.isEmpty()) {
// WE we = sortedEdge.poll();
// 
// VertexPair<V> vertices = graph.getVertices1(we);
// 
// try {
// findShortestPath(tmpGraph)
// .whereEdgesHaveWeights(weightedEdges)
// .from(vertices.getHead())
// .to(vertices.getTail())
// .applyingDijkstra(weightOperations);
// } catch (PathNotFoundException ex) {
// visitedEdge.add(we);
// }
// }
// 
// final MutableSpanningTree<V, WE, W> res =
// new MutableSpanningTree<V, WE, W>(weightOperations, weightedEdges);
// for (V v : graph.getVertices0()) {
// res.addVertex(v);
// }
// 
// for (WE we : edges) {
// VertexPair<V> pair = tmpGraph.getVertices1(we);
// if (pair != null) {
// res.addEdge(pair.getHead(), we, pair.getTail());
// }
// }
// 
// return res;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingReverseDeleteAlgorithm", weightOperations).as(SpanningTree.class);
}
    public DefaultSpanningTreeSourceSelector(Graph<V, WE> graph, Mapper<WE, W> weightedEdges) {
// 
// this.graph = graph;
// this.weightedEdges = weightedEdges;
// 

this.obj = clz.invokeMember("__init__", graph, weightedEdges);
}
}
