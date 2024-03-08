package org.apache.commons.graph.scc;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.Stack;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.DirectedGraph;
import org.graalvm.polyglot.Value;

final class CheriyanMehlhornGabowAlgorithm<V, E> implements SccAlgorithm<V> {
  private int sscCounter = 0;
  private int preorderCounter = 0;
  private final Stack<V> p = new Stack<V>();
  private final Stack<V> s = new Stack<V>();
  private final Map<V, Integer> sscId = new HashMap<V, Integer>();
  private final Map<V, Integer> preorder = new HashMap<V, Integer>();
  private final Set<V> marked = new HashSet<V>();
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/scc/CheriyanMehlhornGabowAlgorithm.py", "CheriyanMehlhornGabowAlgorithm");
  private Value obj;

  public CheriyanMehlhornGabowAlgorithm(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Set<Set<V>> perform() {
    //
    // for (V vertex : graph.getVertices0()) {
    // if (!marked.contains(vertex)) {
    // dfs(vertex);
    // }
    // }
    //
    // final List<Set<V>> indexedSccComponents = new ArrayList<Set<V>>();
    // for (int i = 0; i < sscCounter; i++) {
    // indexedSccComponents.add(new HashSet<V>());
    // }
    //
    // for (V w : graph.getVertices0()) {
    // Set<V> component = indexedSccComponents.get(sscId.get(w));
    // component.add(w);
    // }
    //
    // final Set<Set<V>> scc = new HashSet<Set<V>>();
    // scc.addAll(indexedSccComponents);
    // return scc;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("perform").as(Set.class);
  }

  public CheriyanMehlhornGabowAlgorithm(DirectedGraph<V, E> graph) {
    //
    // this.graph = graph;
    //

    this.obj = clz.invokeMember("__init__", graph);
  }

  private void dfs(V vertex) {
    //
    // marked.add(vertex);
    // preorder.put(vertex, preorderCounter++);
    // s.push(vertex);
    // p.push(vertex);
    // for (V w : graph.getConnectedVertices(vertex)) {
    // if (!marked.contains(w)) {
    // dfs(w);
    // } else if (sscId.get(w) == null) {
    // while (preorder.get(p.peek()) > preorder.get(w)) {
    // p.pop();
    // }
    // }
    // }
    //
    // if (p.peek().equals(vertex)) {
    // p.pop();
    // V w = null;
    // do {
    // w = s.pop();
    // sscId.put(w, sscCounter);
    // } while (!vertex.equals(w));
    // sscCounter++;
    // }
    //

    obj.invokeMember("dfs", vertex);
  }
}
