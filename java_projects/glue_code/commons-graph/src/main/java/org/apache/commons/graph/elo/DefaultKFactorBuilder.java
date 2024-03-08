package org.apache.commons.graph.elo;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.DirectedGraph;
import org.graalvm.polyglot.Value;

final class DefaultKFactorBuilder<P> implements KFactorBuilder<P> {
  private static final int DEFAULT_K_FACTOR = 32;
  private static final double DEFAULT_DIVISOR = 400;
  private static final double DEFAULT_POW_BASE = 10;
  private static Value clz =
      ContextInitializer.getPythonClass("/elo/DefaultKFactorBuilder.py", "DefaultKFactorBuilder");
  private Value obj;

  public DefaultKFactorBuilder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void withKFactor(int kFactor) {
    //
    // for (P player : tournamentGraph.getVertices0()) {
    // for (P opponent : tournamentGraph.getOutbound(player)) {
    // GameResult gameResult = tournamentGraph.getEdge(player, opponent);
    // evaluateMatch(player, gameResult, opponent, kFactor);
    // }
    // }
    //

    obj.invokeMember("withKFactor", kFactor);
  }

  public void withDefaultKFactor() {
    //
    // withKFactor(DEFAULT_K_FACTOR);
    //

    obj.invokeMember("withDefaultKFactor");
  }

  public DefaultKFactorBuilder(
      DirectedGraph<P, GameResult> tournamentGraph, PlayersRank<P> playerRanking) {
    //
    // this.tournamentGraph = tournamentGraph;
    // this.playerRanking = playerRanking;
    //

    this.obj = clz.invokeMember("__init__", tournamentGraph, playerRanking);
  }

  private void updateRanking(P player, double kFactor, double sFactor, double eFactor) {
    //
    // double newRanking = playerRanking.getRanking(player) + (kFactor * (sFactor - eFactor));
    // playerRanking.updateRanking(player, newRanking);
    //

    obj.invokeMember("updateRanking", player, kFactor, sFactor, eFactor);
  }

  private boolean evaluateMatch(P playerA, GameResult gameResult, P playerB, int kFactor) {
    //
    // double qA = calculateQFactor(playerA);
    // double qB = calculateQFactor(playerB);
    //
    // double eA = calculateEFactor(qA, qB);
    // double eB = calculateEFactor(qB, qA);
    //
    // double sA;
    // double sB;
    // switch (gameResult) {
    // case WIN:
    // sA = 1;
    // sB = 0;
    // break;
    //
    // case DRAW:
    // final double number = 0.5;
    // sA = number;
    // sB = number;
    // break;
    //
    // default: // should not happen
    // throw new IllegalArgumentException("Input GameResult not accepted");
    // }
    //
    // updateRanking(playerA, kFactor, sA, eA);
    // updateRanking(playerB, kFactor, sB, eB);
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("evaluateMatch", playerA, gameResult, playerB, kFactor)
        .as(boolean.class);
  }

  private double calculateQFactor(P player) {
    //
    // double ranking = playerRanking.getRanking(player);
    // return pow(DEFAULT_POW_BASE, ranking / DEFAULT_DIVISOR);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("calculateQFactor", player).as(double.class);
  }

  private static double calculateEFactor(double qA, double qB) {
    //
    // return qA / (qA + qB);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("calculateEFactor", qA, qB).as(double.class);
  }
}
