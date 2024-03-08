package org.apache.commons.cli;

import org.graalvm.polyglot.Value;

final class Util {
  static final String[] EMPTY_STRING_ARRAY = {};
  private static Value clz = ContextInitializer.getPythonClass("/Util.py", "Util");
  private Value obj;

  public Util(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  static String stripLeadingHyphens(final String str) {
    //
    // if (str == null) {
    // return null;
    // }
    // if (str.startsWith("--")) {
    // return str.substring(2);
    // }
    // if (str.startsWith("-")) {
    // return str.substring(1);
    // }
    //
    // return str;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("stripLeadingHyphens", str).as(String.class);
  }

  static String stripLeadingAndTrailingQuotes(String str) {
    //
    // final int length = str.length();
    // if (length > 1
    // && str.startsWith("\"")
    // && str.endsWith("\"")
    // && str.substring(1, length - 1).indexOf('"') == -1) {
    // str = str.substring(1, length - 1);
    // }
    //
    // return str;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("stripLeadingAndTrailingQuotes", str).as(String.class);
  }
}
