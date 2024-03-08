package org.apache.commons.graph.connectivity;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import java.util.List;
import java.util.Collection;
import java.util.ArrayList;
import java.util.LinkedList;
import org.apache.commons.graph.Graph;
import static org.apache.commons.graph.CommonsGraph.visit;
import static org.apache.commons.graph.utils.Assertions.checkState;
final class DefaultConnectivityAlgorithmsSelector<V, E>
    private static Value clz = ContextInitializer.getPythonClass("/connectivity/DefaultConnectivityAlgorithmsSelector.py", "DefaultConnectivityAlgorithmsSelector");
    private Value obj;
    public DefaultConnectivityAlgorithmsSelector(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public Collection<List<V>> applyingMinimumSpanningTreeAlgorithm() {
// 
// final List<V> untouchedVertices = new ArrayList<V>();
// 
// for (V v : includedVertices) {
// checkState(graph.containsVertex(v), "Vertex %s does not exist in the Graph", v);
// untouchedVertices.add(v);
// }
// 
// final Collection<List<V>> connectedVertices = new LinkedList<List<V>>();
// 
// while (untouchedVertices.size() > 0) {
// V source = untouchedVertices.remove(0);
// 
// connectedVertices.add(
// visit(graph)
// .from(source)
// .applyingDepthFirstSearch1(
// new ConnectedComponentHandler<V, E>(untouchedVertices)));
// }
// return connectedVertices;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("applyingMinimumSpanningTreeAlgorithm").as(Collection.class);
}
    public DefaultConnectivityAlgorithmsSelector(Graph<V, E> graph, Iterable<V> includedVertices) {
// 
// this.graph = graph;
// this.includedVertices = includedVertices;
// 

this.obj = clz.invokeMember("__init__", graph, includedVertices);
}
}
