package org.apache.commons.codec;

import java.util.Comparator;
import org.graalvm.polyglot.Value;

public class StringEncoderComparator implements Comparator {
  private static Value clz =
      ContextInitializer.getPythonClass("/StringEncoderComparator.py", "StringEncoderComparator");
  private Value obj;

  public StringEncoderComparator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public int compare(final Object o1, final Object o2) {
    //
    //
    // int compareCode = 0;
    //
    // try {
    // @SuppressWarnings(
    // "unchecked") // May fail with CCE if encode returns something that is not
    // final Comparable<Comparable<?>> s1 =
    // (Comparable<Comparable<?>>) this.stringEncoder.encode(o1);
    // final Comparable<?> s2 = (Comparable<?>) this.stringEncoder.encode(o2);
    // compareCode = s1.compareTo(s2);
    // } catch (final EncoderException ee) {
    // compareCode = 0;
    // }
    // return compareCode;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", o1, o2).as(int.class);
  }

  public StringEncoderComparator(int constructorId, final StringEncoder stringEncoder) {
    //
    // if (constructorId == 0) {
    // this.stringEncoder = stringEncoder;
    // } else {
    // this.stringEncoder = null; // Trying to use this will cause things to break
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, stringEncoder);
  }
}
