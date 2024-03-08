package org.apache.commons.graph.scc;

import java.util.Collection;
import java.util.List;
import java.util.Set;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.DirectedGraph;
import org.graalvm.polyglot.Value;

final class KosarajuSharirAlgorithm<V, E> implements SccAlgorithm<V> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/scc/KosarajuSharirAlgorithm.py", "KosarajuSharirAlgorithm");
  private Value obj;

  public KosarajuSharirAlgorithm(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Set<V> perform1(final V source) {
    //
    // checkNotNull(
    // source,
    // "Kosaraju Sharir algorithm cannot be calculated without expressing the source"
    // + " vertex");
    // checkState(graph.containsVertex(source), "Vertex %s does not exist in the Graph", source);
    //
    // final Set<V> visitedVertices = new HashSet<V>();
    // final List<V> expandedVertexList = getExpandedVertexList(source, visitedVertices);
    // final DirectedGraph<V, E> reverted = new RevertedGraph<V, E>(graph);
    //
    // final V v = expandedVertexList.remove(expandedVertexList.size() - 1);
    // final Set<V> sccSet = new HashSet<V>();
    // searchRecursive(reverted, v, sccSet, visitedVertices, false);
    // return sccSet;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("perform1", source).as(Set.class);
  }

  public Set<Set<V>> perform0() {
    //
    // final Set<V> visitedVertices = new HashSet<V>();
    // final List<V> expandedVertexList = getExpandedVertexList(null, visitedVertices);
    // final DirectedGraph<V, E> reverted = new RevertedGraph<V, E>(graph);
    //
    // final Set<Set<V>> sccs = new HashSet<Set<V>>();
    //
    // final LinkedHashSet<V> stack = new LinkedHashSet<V>();
    // for (int i = expandedVertexList.size() - 1; i >= 0; i--) {
    // stack.add(expandedVertexList.get(i));
    // }
    //
    // while (stack.size() > 0) {
    // final V v = stack.iterator().next();
    // final Set<V> sccSet = new HashSet<V>();
    // searchRecursive(reverted, v, sccSet, visitedVertices, false);
    //
    // stack.removeAll(sccSet);
    // sccs.add(sccSet);
    // }
    //
    // return sccs;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("perform0").as(Set.class);
  }

  public Set<Set<V>> perform() {
    //
    // return perform0();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("perform").as(Set.class);
  }

  public KosarajuSharirAlgorithm(final DirectedGraph<V, E> graph) {
    //
    // this.graph = graph;
    //

    this.obj = clz.invokeMember("__init__", graph);
  }

  private void searchRecursive(
      final DirectedGraph<V, E> g,
      final V source,
      final Collection<V> coll,
      final Set<V> visited,
      final boolean forward) {
    //
    // final LinkedList<V> stack = new LinkedList<V>();
    // stack.addLast(source);
    //
    // while (!stack.isEmpty()) {
    // final V v = stack.removeLast();
    //
    // if (!(forward ^ visited.contains(v))) {
    // coll.add(v);
    // continue;
    // }
    //
    // stack.addLast(v);
    // if (forward) {
    // visited.add(v);
    // } else {
    // visited.remove(v);
    // }
    //
    // for (V w : g.getOutbound(v)) {
    // if (!(forward ^ !visited.contains(w))) {
    // stack.addLast(w);
    // }
    // }
    // }
    //

    obj.invokeMember("searchRecursive", g, source, coll, visited, forward);
  }

  private List<V> getExpandedVertexList(final V source, final Set<V> visitedVertices) {
    //
    // final int size = (source != null) ? 13 : graph.getOrder();
    // final Set<V> vertices = new HashSet<V>(size);
    //
    // if (source != null) {
    // vertices.add(source);
    // } else {
    // for (V vertex : graph.getVertices0()) {
    // vertices.add(vertex);
    // }
    // }
    //
    // final ArrayList<V> expandedVertexList = new ArrayList<V>();
    //
    // int idx = 0;
    // while (!vertices.isEmpty()) {
    // final V v = vertices.iterator().next();
    // searchRecursive(graph, v, expandedVertexList, visitedVertices, true);
    // vertices.removeAll(expandedVertexList.subList(idx, expandedVertexList.size()));
    // idx = expandedVertexList.size();
    // }
    //
    // return expandedVertexList;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getExpandedVertexList", source, visitedVertices).as(List.class);
  }
}
