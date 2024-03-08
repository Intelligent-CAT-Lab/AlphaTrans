package org.apache.commons.graph.elo;


public interface KFactorBuilder<P> {
  void withKFactor(int kFactor);

  void withDefaultKFactor();
}
