package org.apache.commons.graph.weight.primitive;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

public class FloatWeightBaseOperations implements OrderedMonoid<Float> {
  private static final long serialVersionUID = 8542498901286671169L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/weight/primitive/FloatWeightBaseOperations.py", "FloatWeightBaseOperations");
  private Value obj;

  public FloatWeightBaseOperations(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Float inverse(Float element) {
    //
    // return -element;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("inverse", element).as(Float.class);
  }

  public Float identity() {
    //
    // return 0.0F;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("identity").as(Float.class);
  }

  public int compare(Float s1, Float s2) {
    //
    // return s1.compareTo(s2);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", s1, s2).as(int.class);
  }

  public Float append(Float s1, Float s2) {
    //
    // if (s1 == null || s2 == null) {
    // return null;
    // }
    // return s1 + s2;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("append", s1, s2).as(Float.class);
  }
}
