package org.apache.commons.graph.model;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.weight.Monoid;
public final class MutableSpanningTree<V, WE, W> extends UndirectedMutableGraph<V, WE>
    private static final long serialVersionUID = -4371938772248573879L;
    private static Value clz = ContextInitializer.getPythonClass("/model/MutableSpanningTree.py", "MutableSpanningTree");
    private Value obj;
    public MutableSpanningTree(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    protected void decorateRemoveEdge(WE e) {
// 
// weight = weightOperations.append(weight, weightOperations.inverse(weightedEdges.map(e)));
// 

obj.invokeMember("decorateRemoveEdge", e);
}
    protected void decorateAddEdge(V head, WE e, V tail) {
// 
// super.decorateAddEdge(head, e, tail);
// weight = weightOperations.append(weight, weightedEdges.map(e));
// 

obj.invokeMember("decorateAddEdge", head, e, tail);
}
    public W getWeight() {
// 
// return weight;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getWeight").as(W.class);
}
    public MutableSpanningTree(Monoid<W> weightOperations, Mapper<WE, W> weightedEdges) {
// 
// this.weightOperations = weightOperations;
// this.weightedEdges = weightedEdges;
// 
// this.weight = weightOperations.identity();
// 

this.obj = clz.invokeMember("__init__", weightOperations, weightedEdges);
}
}
