package org.apache.commons.codec;

import java.io.InputStream;
import org.graalvm.polyglot.Value;

public class Resources {
  private static Value clz = ContextInitializer.getPythonClass("/Resources.py", "Resources");
  private Value obj;

  public Resources(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static InputStream getInputStream(final String name) {
    //
    // final InputStream inputStream = Resources.class.getClassLoader().getResourceAsStream(name);
    // if (inputStream == null) {
    // throw new IllegalArgumentException("Unable to resolve required resource: " + name);
    // }
    // return inputStream;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInputStream", name).as(InputStream.class);
  }
}
