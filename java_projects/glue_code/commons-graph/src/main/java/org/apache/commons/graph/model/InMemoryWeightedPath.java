package org.apache.commons.graph.model;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.weight.Monoid;
import static java.lang.String.format;
import static org.apache.commons.graph.utils.Objects.eq;
public final class InMemoryWeightedPath<V, WE, W> extends InMemoryPath<V, WE>
    private static final long serialVersionUID = 7937494144459068796L;
    private static Value clz = ContextInitializer.getPythonClass("/model/InMemoryWeightedPath.py", "InMemoryWeightedPath");
    private Value obj;
    public InMemoryWeightedPath(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public String toString() {
// 
// return format(
// "InMemoryPath [weigth=%s, vertices=%s, edges=%s]",
// weight, getVertices0(), getEdges());
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
    public int hashCode() {
// 
// final int prime = 31;
// int result = super.hashCode();
// result = prime * result + ((weight == null) ? 0 : weight.hashCode());
// return result;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("hashCode").as(int.class);
}
    public boolean equals(Object obj) {
// 
// if (this == obj) {
// return true;
// }
// 
// if (!super.equals(obj)) {
// return false;
// }
// 
// if (getClass() != obj.getClass()) {
// return false;
// }
// 
// @SuppressWarnings("unchecked") // test against any WeightedPath typed instance
// InMemoryWeightedPath<Object, Object, W> other =
// (InMemoryWeightedPath<Object, Object, W>) obj;
// return eq(weight, other.getWeight());
// 


// TODO: Check the type mapping below!
return obj.invokeMember("equals", obj).as(boolean.class);
}
    public void addConnectionInTail(V head, WE edge, V tail) {
// 
// super.addConnectionInTail(head, edge, tail);
// increaseWeight(edge);
// 

obj.invokeMember("addConnectionInTail", head, edge, tail);
}
    public void addConnectionInHead(V head, WE edge, V tail) {
// 
// super.addConnectionInHead(head, edge, tail);
// increaseWeight(edge);
// 

obj.invokeMember("addConnectionInHead", head, edge, tail);
}
    public W getWeight() {
// 
// return weight;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getWeight").as(W.class);
}
    public InMemoryWeightedPath(
            V start, V target, Monoid<W> weightOperations, Mapper<WE, W> weightedEdges) {
// 
// super(start, target);
// this.weightOperations = weightOperations;
// this.weightedEdges = weightedEdges;
// 
// this.weight = weightOperations.identity();
// 

this.obj = clz.invokeMember("__init__", start, target, weightOperations, weightedEdges);
}
    private void increaseWeight(WE edge) {
// 
// weight = weightOperations.append(weightedEdges.map(edge), weight);
// 

obj.invokeMember("increaseWeight", edge);
}
}
