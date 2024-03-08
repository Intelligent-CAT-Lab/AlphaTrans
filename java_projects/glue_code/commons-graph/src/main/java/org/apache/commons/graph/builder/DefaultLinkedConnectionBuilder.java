package org.apache.commons.graph.builder;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.MutableGraph;
import static org.apache.commons.graph.utils.Assertions.checkNotNull;
public final class DefaultLinkedConnectionBuilder<V, E, G extends MutableGraph<V, E>>
    private static Value clz = ContextInitializer.getPythonClass("/builder/DefaultLinkedConnectionBuilder.py", "DefaultLinkedConnectionBuilder");
    private Value obj;
    public DefaultLinkedConnectionBuilder(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public G withConnections(GraphConnection<V, E> graphConnection) {
// 
// graphConnection =
// checkNotNull(
// graphConnection, "Input graph cannot be configured with null connections");
// 
// GraphConnector<V, E> grapher = new DefaultGrapher<V, E>(graph);
// graphConnection.connect(grapher);
// 
// return graph;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("withConnections", graphConnection).as(G.class);
}
    public DefaultLinkedConnectionBuilder(G graph) {
// 
// this.graph = graph;
// 

this.obj = clz.invokeMember("__init__", graph);
}
}
