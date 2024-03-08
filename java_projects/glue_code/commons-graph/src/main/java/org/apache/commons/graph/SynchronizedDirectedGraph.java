package org.apache.commons.graph;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
final class SynchronizedDirectedGraph<V, E> extends SynchronizedGraph<V, E>
    private static final long serialVersionUID = 2275587906693672253L;
    private static Value clz = ContextInitializer.getPythonClass("/SynchronizedDirectedGraph.py", "SynchronizedDirectedGraph");
    private Value obj;
    public SynchronizedDirectedGraph(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public int getOutDegree(V v) {
// 
// synchronized (lock) {
// return directedGraph.getOutDegree(v);
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getOutDegree", v).as(int.class);
}
    public Iterable<V> getOutbound(V v) {
// 
// synchronized (lock) {
// return directedGraph.getOutbound(v);
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getOutbound", v).as(Iterable.class);
}
    public int getInDegree(V v) {
// 
// synchronized (lock) {
// return directedGraph.getInDegree(v);
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getInDegree", v).as(int.class);
}
    public Iterable<V> getInbound(V v) {
// 
// synchronized (lock) {
// return directedGraph.getInbound(v);
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getInbound", v).as(Iterable.class);
}
    public SynchronizedDirectedGraph(DirectedGraph<V, E> g) {
// 
// super(g);
// directedGraph = g;
// 

this.obj = clz.invokeMember("__init__", g);
}
}
