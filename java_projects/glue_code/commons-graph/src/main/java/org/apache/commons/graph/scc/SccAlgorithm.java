package org.apache.commons.graph.scc;

import java.util.Set;

interface SccAlgorithm<V> {
  Set<Set<V>> perform();
}
