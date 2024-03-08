package org.apache.commons.csv;

import java.util.List;
import org.graalvm.polyglot.Value;

final class Utils {
  private static Value clz = ContextInitializer.getPythonClass("/Utils.py", "Utils");
  private Value obj;

  public Utils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static void compare(
      final String message, final String[][] expected, final List<CSVRecord> actual) {
    //
    // final int expectedLength = expected.length;
    // assertEquals(expectedLength, actual.size(), message + "  - outer array size");
    // for (int i = 0; i < expectedLength; i++) {
    // assertArrayEquals(expected[i], actual.get(i).values(), message + " (entry " + i + ")");
    // }
    //

    clz.invokeMember("compare", message, expected, actual);
  }

  private Utils() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
