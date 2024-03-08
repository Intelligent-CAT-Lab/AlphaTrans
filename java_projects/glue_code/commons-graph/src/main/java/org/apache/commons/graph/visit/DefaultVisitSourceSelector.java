package org.apache.commons.graph.visit;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.Graph;
import static org.apache.commons.graph.utils.Assertions.checkNotNull;
import static org.apache.commons.graph.utils.Assertions.checkState;
public final class DefaultVisitSourceSelector<V, E, G extends Graph<V, E>>
    private static Value clz = ContextInitializer.getPythonClass("/visit/DefaultVisitSourceSelector.py", "DefaultVisitSourceSelector");
    private Value obj;
    public DefaultVisitSourceSelector(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public <S extends V> VisitAlgorithmsSelector<V, E, G> from(S source) {
// 
// source = checkNotNull(source, "Impossible to visit input graph %s with null source", graph);
// checkState(graph.containsVertex(source), "Vertex %s does not exist in the Graph", source);
// return new DefaultVisitAlgorithmsSelector<V, E, G>(graph, source);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("from", source).as(VisitAlgorithmsSelector.class);
}
    public DefaultVisitSourceSelector(G graph) {
// 
// this.graph = graph;
// 

this.obj = clz.invokeMember("__init__", graph);
}
}
