package org.apache.commons.graph.model;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.MutableGraph;
import org.graalvm.polyglot.Value;

public abstract class BaseMutableGraph<V, E> extends BaseGraph<V, E> implements MutableGraph<V, E> {
  private static final long serialVersionUID = 1549113549446254183L;
  private static Value clz =
      ContextInitializer.getPythonClass("/model/BaseMutableGraph.py", "BaseMutableGraph");
  private Value obj;

  public BaseMutableGraph(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public final void removeVertex(V v) {
    //
    // checkGraphCondition(v != null, "Impossible to remove a null Vertex from the Graph");
    // checkGraphCondition(containsVertex(v), "Vertex '%s' not present in the Graph", v);
    //
    // for (V tail : getAdjacencyList().get(v)) {
    // getIndexedEdges().remove(new VertexPair<V>(v, tail));
    // }
    // getAdjacencyList().remove(v);
    //
    // decorateRemoveVertex(v);
    //

    obj.invokeMember("removeVertex", v);
  }

  public final void removeEdge(E e) {
    //
    // checkGraphCondition(e != null, "Impossible to remove a null Edge from the Graph");
    // checkGraphCondition(containsEdge(e), "Edge '%s' not present in the Graph", e);
    // final VertexPair<V> vertexPair = getVertices1(e);
    // decorateRemoveEdge(e);
    // internalRemoveEdge(vertexPair.getHead(), e, vertexPair.getTail());
    // getAllEdges().remove(e);
    //

    obj.invokeMember("removeEdge", e);
  }

  protected void internalRemoveEdge(V head, E e, V tail) {
    //
    // final VertexPair<V> vertexPair = new VertexPair<V>(head, tail);
    // getIndexedVertices().remove(e);
    // getIndexedEdges().remove(vertexPair);
    // getAdjacencyList().get(vertexPair.getHead()).remove(vertexPair.getTail());
    //

    obj.invokeMember("internalRemoveEdge", head, e, tail);
  }

  protected void internalAddEdge(V head, E e, V tail) {
    //
    // getAdjacencyList().get(head).add(tail);
    //
    // final VertexPair<V> vertexPair = new VertexPair<V>(head, tail);
    // getIndexedEdges().put(vertexPair, e);
    //
    // if (!getIndexedVertices().containsKey(e)) {
    // getIndexedVertices().put(e, vertexPair);
    // }
    //

    obj.invokeMember("internalAddEdge", head, e, tail);
  }

  public final void addVertex(V v) {
    //
    // checkGraphCondition(v != null, "Impossible to add a null Vertex to the Graph");
    // checkGraphCondition(!containsVertex(v), "Vertex '%s' already present in the Graph", v);
    //
    // getAdjacencyList().put(v, new LinkedHashSet<V>());
    //
    // decorateAddVertex(v);
    //

    obj.invokeMember("addVertex", v);
  }

  public void addEdge(V head, E e, V tail) {
    //
    // checkGraphCondition(head != null, "Null head Vertex not admitted");
    // checkGraphCondition(e != null, "Impossible to add a null Edge in the Graph");
    // checkGraphCondition(tail != null, "Null tail Vertex not admitted");
    // checkGraphCondition(
    // containsVertex(head), "Head Vertex '%s' not present in the Graph", head);
    // checkGraphCondition(
    // containsVertex(tail), "Head Vertex '%s' not present in the Graph", tail);
    // checkGraphCondition(
    // getEdge(head, tail) == null, "Edge %s is already present in the Graph", e);
    //
    // getAllEdges().add(e);
    //
    // internalAddEdge(head, e, tail);
    //
    // decorateAddEdge(head, e, tail);
    //

    obj.invokeMember("addEdge", head, e, tail);
  }

  protected abstract void decorateRemoveVertex(V v);

  protected abstract void decorateRemoveEdge(E e);

  protected abstract void decorateAddVertex(V v);

  protected abstract void decorateAddEdge(V head, E e, V tail);
}
