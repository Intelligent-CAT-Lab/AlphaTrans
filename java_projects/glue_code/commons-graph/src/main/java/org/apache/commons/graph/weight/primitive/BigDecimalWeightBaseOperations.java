package org.apache.commons.graph.weight.primitive;

import java.math.BigDecimal;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

public class BigDecimalWeightBaseOperations implements OrderedMonoid<BigDecimal> {
  private static final long serialVersionUID = -317234195461348466L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/weight/primitive/BigDecimalWeightBaseOperations.py", "BigDecimalWeightBaseOperations");
  private Value obj;

  public BigDecimalWeightBaseOperations(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public BigDecimal inverse(BigDecimal element) {
    //
    // return element.negate();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("inverse", element).as(BigDecimal.class);
  }

  public BigDecimal identity() {
    //
    // return ZERO;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("identity").as(BigDecimal.class);
  }

  public int compare(BigDecimal o1, BigDecimal o2) {
    //
    // return o1.compareTo(o2);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", o1, o2).as(int.class);
  }

  public BigDecimal append(BigDecimal s1, BigDecimal s2) {
    //
    // if (s1 == null || s2 == null) {
    // return null;
    // }
    // return s1.add(s2);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("append", s1, s2).as(BigDecimal.class);
  }
}
