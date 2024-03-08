package org.apache.commons.pool;

import org.graalvm.polyglot.Value;

public class CglibProxySource<T> {
  private static Value clz =
      ContextInitializer.getPythonClass("/CglibProxySource.py", "CglibProxySource");
  private Value obj;

  public CglibProxySource(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder builder = new StringBuilder();
    // builder.append("CglibProxySource [superclass=");
    // builder.append(superclass);
    // builder.append("]");
    // return builder.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public CglibProxySource(final Class<? extends T> superclass) {
    //
    // this.superclass = superclass;
    //

    this.obj = clz.invokeMember("__init__", superclass);
  }
}
