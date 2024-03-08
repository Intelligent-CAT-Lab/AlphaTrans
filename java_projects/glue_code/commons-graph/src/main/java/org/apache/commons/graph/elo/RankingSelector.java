package org.apache.commons.graph.elo;


public interface RankingSelector<P> {
  KFactorBuilder<P> wherePlayersAreRankedIn(PlayersRank<P> playersRank);
}
