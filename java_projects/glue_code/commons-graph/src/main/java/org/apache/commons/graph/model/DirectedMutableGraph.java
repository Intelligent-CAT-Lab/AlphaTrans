package org.apache.commons.graph.model;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import java.util.Map;
import java.util.Set;
import java.util.HashMap;
import java.util.LinkedHashSet;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.VertexPair;
public class DirectedMutableGraph<V, E> extends BaseMutableGraph<V, E>
    private final Map<V, Set<V>> outbound = new HashMap<V, Set<V>>();
    private final Map<V, Set<V>> inbound = new HashMap<V, Set<V>>();
    private static final long serialVersionUID = 630111985439492792L;
    private static Value clz = ContextInitializer.getPythonClass("/model/DirectedMutableGraph.py", "DirectedMutableGraph");
    private Value obj;
    public DirectedMutableGraph(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    protected void decorateRemoveVertex(V v) {
// 
// inbound.remove(v);
// outbound.remove(v);
// 

obj.invokeMember("decorateRemoveVertex", v);
}
    protected void decorateRemoveEdge(E e) {
// 
// final VertexPair<V> vertices = getVertices1(e);
// inbound.get(vertices.getTail()).remove(vertices.getHead());
// outbound.get(vertices.getHead()).remove(vertices.getTail());
// 

obj.invokeMember("decorateRemoveEdge", e);
}
    protected void decorateAddVertex(V v) {
// 
// inbound.put(v, new LinkedHashSet<V>());
// outbound.put(v, new LinkedHashSet<V>());
// 

obj.invokeMember("decorateAddVertex", v);
}
    protected void decorateAddEdge(V head, E e, V tail) {
// 
// inbound.get(tail).add(head);
// outbound.get(head).add(tail);
// 

obj.invokeMember("decorateAddEdge", head, e, tail);
}
    public final int getOutDegree(V v) {
// 
// return outbound.get(v).size();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getOutDegree", v).as(int.class);
}
    public final Iterable<V> getOutbound(V v) {
// 
// return outbound.get(v);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getOutbound", v).as(Iterable.class);
}
    public final int getInDegree(V v) {
// 
// return inbound.get(v).size();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getInDegree", v).as(int.class);
}
    public final Iterable<V> getInbound(V v) {
// 
// return inbound.get(v);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getInbound", v).as(Iterable.class);
}
    public final int getDegree(V v) {
// 
// return getInDegree(v) + getOutDegree(v);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDegree", v).as(int.class);
}
}
