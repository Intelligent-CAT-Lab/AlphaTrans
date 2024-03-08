package org.apache.commons.graph.visit;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.model.BaseMutableGraph;
import org.apache.commons.graph.model.DirectedMutableGraph;
final class VisitGraphBuilder<V, E, G extends Graph<V, E>>
    private static Value clz = ContextInitializer.getPythonClass("/visit/VisitGraphBuilder.py", "VisitGraphBuilder");
    private Value obj;
    public VisitGraphBuilder(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public Graph<V, E> onCompleted() {
// 
// return visitGraph;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("onCompleted").as(Graph.class);
}
    public void discoverGraph(G graph) {
// 
// if (graph instanceof DirectedGraph) {
// visitGraph = new DirectedMutableGraph<V, E>();
// } else {
// visitGraph = new UndirectedMutableGraph<V, E>();
// }
// 
// for (V vertex : graph.getVertices0()) {
// visitGraph.addVertex(vertex);
// }
// 

obj.invokeMember("discoverGraph", graph);
}
    public VisitState discoverEdge(V head, E edge, V tail) {
// 
// visitGraph.addEdge(head, edge, tail);
// return VisitState.CONTINUE;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("discoverEdge", head, edge, tail).as(VisitState.class);
}
}
