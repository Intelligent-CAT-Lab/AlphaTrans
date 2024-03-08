package org.apache.commons.graph.weight.primitive;

import java.math.BigInteger;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

public class BigIntegerWeightBaseOperations implements OrderedMonoid<BigInteger> {
  private static final long serialVersionUID = 4118152508299694652L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/weight/primitive/BigIntegerWeightBaseOperations.py", "BigIntegerWeightBaseOperations");
  private Value obj;

  public BigIntegerWeightBaseOperations(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public BigInteger inverse(BigInteger element) {
    //
    // return element.negate();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("inverse", element).as(BigInteger.class);
  }

  public BigInteger identity() {
    //
    // return ZERO;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("identity").as(BigInteger.class);
  }

  public int compare(BigInteger o1, BigInteger o2) {
    //
    // return o1.compareTo(o2);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", o1, o2).as(int.class);
  }

  public BigInteger append(BigInteger s1, BigInteger s2) {
    //
    // if (s1 == null || s2 == null) {
    // return null;
    // }
    // return s1.add(s2);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("append", s1, s2).as(BigInteger.class);
  }
}
