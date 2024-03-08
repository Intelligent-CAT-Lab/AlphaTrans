package org.apache.commons.codec.language.bm;

import org.apache.commons.codec.CharEncoding;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

class ResourceConstants {
  static final String EXT_CMT_START = "/*";
  static final String EXT_CMT_END = "*/";
  static final String ENCODING = CharEncoding.UTF_8;
  static final String CMT = "//";
  private static Value clz =
      ContextInitializer.getPythonClass("/language/bm/ResourceConstants.py", "ResourceConstants");
  private Value obj;

  public ResourceConstants(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}
