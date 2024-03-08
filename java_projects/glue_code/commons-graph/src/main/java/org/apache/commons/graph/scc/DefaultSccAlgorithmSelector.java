package org.apache.commons.graph.scc;

import java.util.Set;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.DirectedGraph;
import org.graalvm.polyglot.Value;

public final class DefaultSccAlgorithmSelector<V, E> implements SccAlgorithmSelector<V, E> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/scc/DefaultSccAlgorithmSelector.py", "DefaultSccAlgorithmSelector");
  private Value obj;

  public DefaultSccAlgorithmSelector(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Set<Set<V>> applyingTarjan() {
    //
    // return applying(new TarjanAlgorithm<V, E>(graph));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("applyingTarjan").as(Set.class);
  }

  public Set<V> applyingKosarajuSharir1(final V source) {
    //
    // return new KosarajuSharirAlgorithm<V, E>(graph).perform1(source);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("applyingKosarajuSharir1", source).as(Set.class);
  }

  public Set<Set<V>> applyingKosarajuSharir0() {
    //
    // return applying(new KosarajuSharirAlgorithm<V, E>(graph));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("applyingKosarajuSharir0").as(Set.class);
  }

  public Set<Set<V>> applyingCheriyanMehlhornGabow() {
    //
    // return applying(new CheriyanMehlhornGabowAlgorithm<V, E>(graph));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("applyingCheriyanMehlhornGabow").as(Set.class);
  }

  public DefaultSccAlgorithmSelector(final DirectedGraph<V, E> graph) {
    //
    // this.graph = graph;
    //

    this.obj = clz.invokeMember("__init__", graph);
  }

  private Set<Set<V>> applying(SccAlgorithm<V> algorithm) {
    //
    // return algorithm.perform();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("applying", algorithm).as(Set.class);
  }
}
