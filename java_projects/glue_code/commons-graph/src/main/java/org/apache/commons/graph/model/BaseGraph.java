package org.apache.commons.graph.model;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.VertexPair;
import org.graalvm.polyglot.Value;

public abstract class BaseGraph<V, E> implements Graph<V, E> {
  private final Map<E, VertexPair<V>> indexedVertices = new HashMap<E, VertexPair<V>>();
  private final Map<VertexPair<V>, E> indexedEdges = new HashMap<VertexPair<V>, E>();
  private final Set<E> allEdges = new HashSet<E>();
  private final Map<V, Set<V>> adjacencyList = new HashMap<V, Set<V>>();
  private static final long serialVersionUID = -8066786787634472712L;
  private static Value clz = ContextInitializer.getPythonClass("/model/BaseGraph.py", "BaseGraph");
  private Value obj;

  public BaseGraph(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return String.valueOf(adjacencyList);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // final int prime = 31;
    // return hash(1, prime, adjacencyList, allEdges, indexedEdges, indexedVertices);
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
    // if (obj == null || getClass() != obj.getClass()) {
    // return false;
    // }
    //
    // @SuppressWarnings("unchecked")
    // BaseGraph<Object, Object> other = (BaseGraph<Object, Object>) obj;
    // return eq(adjacencyList, other.getAdjacencyList());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", obj).as(boolean.class);
  }

  public final VertexPair<V> getVertices1(E e) {
    //
    // return indexedVertices.get(e);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices1", e).as(VertexPair.class);
  }

  public final Iterable<V> getVertices0() {
    //
    // return unmodifiableSet(adjacencyList.keySet());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices0").as(Iterable.class);
  }

  public int getSize() {
    //
    // return allEdges.size();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSize").as(int.class);
  }

  public final int getOrder() {
    //
    // return adjacencyList.size();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOrder").as(int.class);
  }

  protected Map<E, VertexPair<V>> getIndexedVertices() {
    //
    // return indexedVertices;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIndexedVertices").as(Map.class);
  }

  protected Map<VertexPair<V>, E> getIndexedEdges() {
    //
    // return indexedEdges;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIndexedEdges").as(Map.class);
  }

  public final Iterable<E> getEdges() {
    //
    // return unmodifiableCollection(allEdges);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdges").as(Iterable.class);
  }

  public final E getEdge(V source, V target) {
    //
    // checkGraphCondition(
    // containsVertex(source), "Vertex %s does not exist in the Graph", source);
    // checkGraphCondition(
    // containsVertex(target), "Vertex %s does not exist in the Graph", target);
    //
    // return indexedEdges.get(new VertexPair<V>(source, target));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdge", source, target).as(E.class);
  }

  public final Iterable<V> getConnectedVertices(V v) {
    //
    // checkGraphCondition(containsVertex(v), "Vertex %s does not exist in the Graph", v);
    // final Set<V> adj = adjacencyList.get(v);
    // return unmodifiableSet(adj);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getConnectedVertices", v).as(Iterable.class);
  }

  protected Set<E> getAllEdges() {
    //
    // return allEdges;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getAllEdges").as(Set.class);
  }

  protected final Map<V, Set<V>> getAdjacencyList() {
    //
    // return adjacencyList;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getAdjacencyList").as(Map.class);
  }

  public boolean containsVertex(V v) {
    //
    // return adjacencyList.containsKey(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsVertex", v).as(boolean.class);
  }

  public boolean containsEdge(E e) {
    //
    // return indexedVertices.containsKey(e);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsEdge", e).as(boolean.class);
  }

  protected static void checkGraphCondition(
      boolean expression, String errorMessageTemplate, Object... errorMessageArgs) {
    //
    // if (!expression) {
    // throw new GraphException(format(errorMessageTemplate, errorMessageArgs), null, null);
    // }
    //

    clz.invokeMember("checkGraphCondition", expression, errorMessageTemplate, errorMessageArgs);
  }
}
