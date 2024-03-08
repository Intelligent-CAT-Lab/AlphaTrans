package org.apache.commons.graph.coloring;

import java.util.Set;

public interface ColorsBuilder<V, E> {
  <C> ColoringAlgorithmsSelector<V, E, C> withColors(Set<C> colors);
}
