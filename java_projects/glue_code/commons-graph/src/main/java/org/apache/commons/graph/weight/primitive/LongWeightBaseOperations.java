package org.apache.commons.graph.weight.primitive;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

public class LongWeightBaseOperations implements OrderedMonoid<Long> {
  private static final long serialVersionUID = 3149327896191098756L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/weight/primitive/LongWeightBaseOperations.py", "LongWeightBaseOperations");
  private Value obj;

  public LongWeightBaseOperations(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Long inverse(Long element) {
    //
    // return -element;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("inverse", element).as(Long.class);
  }

  public Long identity() {
    //
    // return 0L;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("identity").as(Long.class);
  }

  public int compare(Long s1, Long s2) {
    //
    // return s1.compareTo(s2);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", s1, s2).as(int.class);
  }

  public Long append(Long s1, Long s2) {
    //
    // if (s1 == null || s2 == null) {
    // return null;
    // }
    // return s1 + s2;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("append", s1, s2).as(Long.class);
  }
}
