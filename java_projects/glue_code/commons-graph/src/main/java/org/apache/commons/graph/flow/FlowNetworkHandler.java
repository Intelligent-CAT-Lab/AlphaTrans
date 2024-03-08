package org.apache.commons.graph.flow;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import java.util.Map;
import java.util.HashMap;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.visit.BaseGraphVisitHandler;
import org.apache.commons.graph.visit.VisitState;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.shortestpath.PredecessorsList;
import static org.apache.commons.graph.visit.VisitState.CONTINUE;
import static org.apache.commons.graph.visit.VisitState.ABORT;
import static org.apache.commons.graph.visit.VisitState.SKIP;
final class FlowNetworkHandler<V, E, W>
    private final Map<E, W> residualEdgeCapacities = new HashMap<E, W>();
    private static Value clz = ContextInitializer.getPythonClass("/flow/FlowNetworkHandler.py", "FlowNetworkHandler");
    private Value obj;
    public FlowNetworkHandler(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public W onCompleted() {
// 
// return maxFlow;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("onCompleted").as(W.class);
}
    public void discoverGraph(DirectedGraph<V, E> graph) {
// 
// predecessors = new PredecessorsList<V, E, W>(graph, weightOperations, weightedEdges);
// foundAugmentingPath = false;
// 

obj.invokeMember("discoverGraph", graph);
}
    public VisitState discoverEdge(V head, E edge, V tail) {
// 
// W residualEdgeCapacity = residualEdgeCapacities.get(edge);
// if (weightOperations.compare(residualEdgeCapacity, weightOperations.identity()) <= 0) {
// return SKIP;
// }
// predecessors.addPredecessor(tail, head);
// return CONTINUE;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("discoverEdge", head, edge, tail).as(VisitState.class);
}
    public VisitState finishVertex(V vertex) {
// 
// if (vertex.equals(target)) {
// foundAugmentingPath = true;
// return ABORT;
// }
// return CONTINUE;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("finishVertex", vertex).as(VisitState.class);
}
    public VisitState discoverVertex(V vertex) {
// 
// return finishVertex(vertex);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("discoverVertex", vertex).as(VisitState.class);
}
    void updateResidualNetworkWithCurrentAugmentingPath() {
// 
// WeightedPath<V, E, W> augmentingPath = predecessors.buildPath0(source, target);
// 
// W flowIncrement = null;
// for (E edge : augmentingPath.getEdges()) {
// W edgeCapacity = residualEdgeCapacities.get(edge);
// if (flowIncrement == null
// || weightOperations.compare(edgeCapacity, flowIncrement) < 0) {
// flowIncrement = edgeCapacity;
// }
// }
// 
// maxFlow = weightOperations.append(maxFlow, flowIncrement);
// for (E edge : augmentingPath.getEdges()) {
// W directCapacity = residualEdgeCapacities.get(edge);
// residualEdgeCapacities.put(
// edge,
// weightOperations.append(
// directCapacity, weightOperations.inverse(flowIncrement)));
// 
// VertexPair<V> vertexPair = flowNetwork.getVertices1(edge);
// E inverseEdge = flowNetwork.getEdge(vertexPair.getTail(), vertexPair.getHead());
// W inverseCapacity = residualEdgeCapacities.get(inverseEdge);
// residualEdgeCapacities.put(
// inverseEdge, weightOperations.append(inverseCapacity, flowIncrement));
// }
// 

obj.invokeMember("updateResidualNetworkWithCurrentAugmentingPath");
}
    boolean hasAugmentingPath() {
// 
// return foundAugmentingPath;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("hasAugmentingPath").as(boolean.class);
}
    FlowNetworkHandler(
            DirectedGraph<V, E> flowNetwork,
            V source,
            V target,
            OrderedMonoid<W> weightOperations,
            Mapper<E, W> weightedEdges) {
// 
// this.flowNetwork = flowNetwork;
// this.source = source;
// this.target = target;
// this.weightOperations = weightOperations;
// this.weightedEdges = weightedEdges;
// 
// maxFlow = weightOperations.identity();
// 
// for (E edge : flowNetwork.getEdges()) {
// residualEdgeCapacities.put(edge, weightedEdges.map(edge));
// }
// 
// predecessors = null;
// 

this.obj = clz.invokeMember("__init__", flowNetwork, source, target, weightOperations, weightedEdges);
}
}
