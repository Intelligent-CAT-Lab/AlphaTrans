package org.apache.commons.graph;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
final class SynchronizedMutableGraph<V, E> extends SynchronizedGraph<V, E>
    private static final long serialVersionUID = -5985121601939852063L;
    private static Value clz = ContextInitializer.getPythonClass("/SynchronizedMutableGraph.py", "SynchronizedMutableGraph");
    private Value obj;
    public SynchronizedMutableGraph(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public void removeVertex(V v) {
// 
// synchronized (lock) {
// mutableGraph.removeVertex(v);
// }
// 

obj.invokeMember("removeVertex", v);
}
    public void removeEdge(E e) {
// 
// synchronized (lock) {
// mutableGraph.removeEdge(e);
// }
// 

obj.invokeMember("removeEdge", e);
}
    public void addVertex(V v) {
// 
// synchronized (lock) {
// mutableGraph.addVertex(v);
// }
// 

obj.invokeMember("addVertex", v);
}
    public void addEdge(V head, E e, V tail) {
// 
// synchronized (lock) {
// mutableGraph.addEdge(head, e, tail);
// }
// 

obj.invokeMember("addEdge", head, e, tail);
}
    public SynchronizedMutableGraph(MutableGraph<V, E> g) {
// 
// super(g);
// this.mutableGraph = g;
// 

this.obj = clz.invokeMember("__init__", g);
}
}
