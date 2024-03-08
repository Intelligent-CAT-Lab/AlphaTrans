package org.apache.commons.graph;

import java.util.Map;
import java.util.TreeMap;
import org.graalvm.polyglot.Value;

final class SimplePlayersRank implements PlayersRank<String> {
  private final Map<String, Double> ranks = new TreeMap<String, Double>();
  private static Value clz =
      ContextInitializer.getPythonClass("/SimplePlayersRank.py", "SimplePlayersRank");
  private Value obj;

  public SimplePlayersRank(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return ranks.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public void updateRanking(String player, Double ranking) {
    //
    // ranks.put(player, ranking);
    //

    obj.invokeMember("updateRanking", player, ranking);
  }

  public Double getRanking(String player) {
    //
    // if (!ranks.containsKey(player)) {
    // return 0D;
    // }
    // return ranks.get(player);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRanking", player).as(Double.class);
  }
}
