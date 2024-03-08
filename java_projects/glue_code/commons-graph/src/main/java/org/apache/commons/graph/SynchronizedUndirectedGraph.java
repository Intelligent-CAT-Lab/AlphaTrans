package org.apache.commons.graph;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
final class SynchronizedUndirectedGraph<V, E> extends SynchronizedGraph<V, E>
    private static final long serialVersionUID = 2207884889346410427L;
    private static Value clz = ContextInitializer.getPythonClass("/SynchronizedUndirectedGraph.py", "SynchronizedUndirectedGraph");
    private Value obj;
    public SynchronizedUndirectedGraph(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public SynchronizedUndirectedGraph(Graph<V, E> g) {
// 
// super(g);
// 

this.obj = clz.invokeMember("__init__", g);
}
}
