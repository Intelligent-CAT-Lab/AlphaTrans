package org.apache.commons.graph.scc;

import java.util.Set;

public interface SccAlgorithmSelector<V, E> {
  Set<Set<V>> applyingTarjan();

  Set<V> applyingKosarajuSharir1(V source);

  Set<Set<V>> applyingKosarajuSharir0();

  Set<Set<V>> applyingCheriyanMehlhornGabow();
}
