package org.apache.commons.graph.elo;


public interface PlayersRank<P> {
  void updateRanking(P player, Double ranking);

  Double getRanking(P player);
}
