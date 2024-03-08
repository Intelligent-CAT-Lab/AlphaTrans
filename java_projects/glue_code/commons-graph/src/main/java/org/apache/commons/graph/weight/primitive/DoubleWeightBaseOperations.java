package org.apache.commons.graph.weight.primitive;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

public class DoubleWeightBaseOperations implements OrderedMonoid<Double> {
  private static final long serialVersionUID = 4440399710792243877L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/weight/primitive/DoubleWeightBaseOperations.py", "DoubleWeightBaseOperations");
  private Value obj;

  public DoubleWeightBaseOperations(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Double inverse(Double element) {
    //
    // return -element;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("inverse", element).as(Double.class);
  }

  public Double identity() {
    //
    // return 0.0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("identity").as(Double.class);
  }

  public int compare(Double s1, Double s2) {
    //
    // return s1.compareTo(s2);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", s1, s2).as(int.class);
  }

  public Double append(Double s1, Double s2) {
    //
    // if (s1 == null || s2 == null) {
    // return null;
    // }
    // return s1 + s2;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("append", s1, s2).as(Double.class);
  }
}
