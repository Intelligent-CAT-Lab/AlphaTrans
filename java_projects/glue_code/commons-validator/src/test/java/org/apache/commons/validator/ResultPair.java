package org.apache.commons.validator;

import org.graalvm.polyglot.Value;

public class ResultPair {
  private static Value clz = ContextInitializer.getPythonClass("/ResultPair.py", "ResultPair");
  private Value obj;

  public ResultPair(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public ResultPair(String item, boolean valid) {
    //
    // this.item = item;
    // this.valid = valid; // Whether the individual part of url is valid.
    //

    this.obj = clz.invokeMember("__init__", item, valid);
  }
}
