package org.apache.commons.graph.scc;

import java.util.Map;
import java.util.Set;
import java.util.Stack;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.DirectedGraph;
import org.graalvm.polyglot.Value;

final class TarjanAlgorithm<V, E> implements SccAlgorithm<V> {
  private static Value clz =
      ContextInitializer.getPythonClass("/scc/TarjanAlgorithm.py", "TarjanAlgorithm");
  private Value obj;

  public TarjanAlgorithm(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Set<Set<V>> perform() {
    //
    // final Map<V, TarjanVertexMetaInfo> verticesMetaInfo =
    // new HashMap<V, TarjanVertexMetaInfo>();
    // final Stack<V> s = new Stack<V>();
    // final Set<Set<V>> stronglyConnectedComponents = new LinkedHashSet<Set<V>>();
    // Integer index = 0;
    //
    // for (V vertex : graph.getVertices0()) {
    // TarjanVertexMetaInfo vertexMetaInfo = getMetaInfo(vertex, verticesMetaInfo);
    // final Set<V> stronglyConnectedComponent = new LinkedHashSet<V>();
    //
    // if (vertexMetaInfo.hasUndefinedIndex()) {
    // strongConnect(
    // graph, vertex, verticesMetaInfo, s, stronglyConnectedComponent, index);
    // stronglyConnectedComponents.add(stronglyConnectedComponent);
    // }
    // }
    //
    // return stronglyConnectedComponents;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("perform").as(Set.class);
  }

  public TarjanAlgorithm(DirectedGraph<V, E> graph) {
    //
    // this.graph = graph;
    //

    this.obj = clz.invokeMember("__init__", graph);
  }

  private static <V, E> void strongConnect(
      DirectedGraph<V, E> graph,
      V vertex,
      Map<V, TarjanVertexMetaInfo> verticesMetaInfo,
      Stack<V> s,
      Set<V> stronglyConnectedComponent,
      Integer index) {
    //
    // TarjanVertexMetaInfo vertexMetaInfo = getMetaInfo(vertex, verticesMetaInfo);
    // vertexMetaInfo.setIndex(index);
    // vertexMetaInfo.setLowLink(index);
    // index++;
    // s.push(vertex);
    //
    // for (V adjacent : graph.getOutbound(vertex)) {
    // TarjanVertexMetaInfo adjacentMetaInfo = getMetaInfo(adjacent, verticesMetaInfo);
    // if (adjacentMetaInfo.hasUndefinedIndex()) {
    // strongConnect(
    // graph, adjacent, verticesMetaInfo, s, stronglyConnectedComponent, index);
    // vertexMetaInfo.setLowLink(
    // min(vertexMetaInfo.getLowLink(), adjacentMetaInfo.getLowLink()));
    // } else if (s.contains(adjacent)) {
    // vertexMetaInfo.setLowLink(
    // min(vertexMetaInfo.getLowLink(), adjacentMetaInfo.getIndex()));
    // }
    // }
    //
    // if (vertexMetaInfo.getLowLink() == vertexMetaInfo.getIndex()) {
    // V v;
    // do {
    // v = s.pop();
    // stronglyConnectedComponent.add(v);
    // } while (!vertex.equals(v));
    // }
    //

    clz.invokeMember(
        "strongConnect", graph, vertex, verticesMetaInfo, s, stronglyConnectedComponent, index);
  }

  private static <V> TarjanVertexMetaInfo getMetaInfo(
      V vertex, Map<V, TarjanVertexMetaInfo> verticesMetaInfo) {
    //
    // TarjanVertexMetaInfo vertexMetaInfo = verticesMetaInfo.get(vertex);
    // if (vertexMetaInfo == null) {
    // vertexMetaInfo = new TarjanVertexMetaInfo();
    // verticesMetaInfo.put(vertex, vertexMetaInfo);
    // }
    // return vertexMetaInfo;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getMetaInfo", vertex, verticesMetaInfo).as(TarjanVertexMetaInfo.class);
  }
}
