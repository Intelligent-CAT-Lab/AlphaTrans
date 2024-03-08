package org.apache.commons.graph.model;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.UndirectedGraph;
public class UndirectedMutableGraph<V, E> extends BaseMutableGraph<V, E>
    private static final long serialVersionUID = 3067145277295525946L;
    private static Value clz = ContextInitializer.getPythonClass("/model/UndirectedMutableGraph.py", "UndirectedMutableGraph");
    private Value obj;
    public UndirectedMutableGraph(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    protected void decorateRemoveVertex(V v) {
// 

obj.invokeMember("decorateRemoveVertex", v);
}
    protected void decorateRemoveEdge(E e) {
// 
// internalRemoveEdge(getVertices1(e).getTail(), e, getVertices1(e).getHead());
// 

obj.invokeMember("decorateRemoveEdge", e);
}
    protected void decorateAddVertex(V v) {
// 

obj.invokeMember("decorateAddVertex", v);
}
    protected void decorateAddEdge(V head, E e, V tail) {
// 
// internalAddEdge(tail, e, head);
// 

obj.invokeMember("decorateAddEdge", head, e, tail);
}
    public final int getDegree(V v) {
// 
// return getAdjacencyList().get(v).size();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDegree", v).as(int.class);
}
}
