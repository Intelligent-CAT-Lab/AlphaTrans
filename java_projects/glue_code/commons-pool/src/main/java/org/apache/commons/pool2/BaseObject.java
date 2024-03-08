package org.apache.commons.pool;

import org.graalvm.polyglot.Value;

public abstract class BaseObject {
  private static Value clz = ContextInitializer.getPythonClass("/BaseObject.py", "BaseObject");
  private Value obj;

  public BaseObject(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder builder = new StringBuilder();
    // builder.append(getClass().getSimpleName());
    // builder.append(" [");
    // toStringAppendFields(builder);
    // builder.append("]");
    // return builder.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  protected void toStringAppendFields(final StringBuilder builder) {
    //

    obj.invokeMember("toStringAppendFields", builder);
  }
}
