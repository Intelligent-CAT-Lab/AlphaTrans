package org.apache.commons.graph.spanning;

import java.util.Comparator;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Mapper;
import org.graalvm.polyglot.Value;

public class WeightedEdgesComparator<W, WE> implements Comparator<WE> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/spanning/WeightedEdgesComparator.py", "WeightedEdgesComparator");
  private Value obj;

  public WeightedEdgesComparator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public int compare(WE o1, WE o2) {
    //
    // return weightComparator.compare(weightedEdges.map(o1), weightedEdges.map(o2));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", o1, o2).as(int.class);
  }

  public WeightedEdgesComparator(Comparator<W> weightComparator, Mapper<WE, W> weightedEdges) {
    //
    // this.weightComparator = weightComparator;
    // this.weightedEdges = weightedEdges;
    //

    this.obj = clz.invokeMember("__init__", weightComparator, weightedEdges);
  }
}
