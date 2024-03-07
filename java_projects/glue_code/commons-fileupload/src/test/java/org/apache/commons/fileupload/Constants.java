package org.apache.commons.fileupload;

import org.graalvm.polyglot.Value;

public final class Constants {
  public static final String CONTENT_TYPE = "multipart/form-data; boundary=---1234";
  private static Value clz = ContextInitializer.getPythonClass("Constants.py", "Constants");
  private Value obj;

  public Constants(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  private Constants() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
