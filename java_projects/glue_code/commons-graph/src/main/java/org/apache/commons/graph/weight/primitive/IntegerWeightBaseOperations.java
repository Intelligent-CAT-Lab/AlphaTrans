package org.apache.commons.graph.weight.primitive;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

public class IntegerWeightBaseOperations implements OrderedMonoid<Integer> {
  private static final long serialVersionUID = -8641477350652350485L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/weight/primitive/IntegerWeightBaseOperations.py", "IntegerWeightBaseOperations");
  private Value obj;

  public IntegerWeightBaseOperations(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Integer inverse(Integer element) {
    //
    // return -element;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("inverse", element).as(Integer.class);
  }

  public Integer identity() {
    //
    // return 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("identity").as(Integer.class);
  }

  public int compare(Integer o1, Integer o2) {
    //
    // return o1.compareTo(o2);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", o1, o2).as(int.class);
  }

  public Integer append(Integer s1, Integer s2) {
    //
    // if (s1 == null || s2 == null) {
    // return null;
    // }
    // return s1 + s2;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("append", s1, s2).as(Integer.class);
  }
}
