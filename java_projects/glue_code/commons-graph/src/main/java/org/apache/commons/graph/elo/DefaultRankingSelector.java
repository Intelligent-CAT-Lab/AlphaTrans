package org.apache.commons.graph.elo;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.DirectedGraph;
import org.graalvm.polyglot.Value;

public final class DefaultRankingSelector<P> implements RankingSelector<P> {
  private static Value clz =
      ContextInitializer.getPythonClass("/elo/DefaultRankingSelector.py", "DefaultRankingSelector");
  private Value obj;

  public DefaultRankingSelector(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public KFactorBuilder<P> wherePlayersAreRankedIn(PlayersRank<P> playersRank) {
    //
    // playersRank =
    // checkNotNull(
    // playersRank,
    // "ELO ranking can not be applied if players can not be ranked!");
    // return new DefaultKFactorBuilder<P>(tournamentGraph, playersRank);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("wherePlayersAreRankedIn", playersRank).as(KFactorBuilder.class);
  }

  public DefaultRankingSelector(DirectedGraph<P, GameResult> tournamentGraph) {
    //
    // this.tournamentGraph = tournamentGraph;
    //

    this.obj = clz.invokeMember("__init__", tournamentGraph);
  }
}
