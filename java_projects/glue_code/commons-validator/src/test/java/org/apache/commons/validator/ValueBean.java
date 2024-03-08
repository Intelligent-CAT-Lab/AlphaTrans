package org.apache.commons.validator;

import org.graalvm.polyglot.Value;

public class ValueBean {
  protected String value = null;
  private static Value clz = ContextInitializer.getPythonClass("/ValueBean.py", "ValueBean");
  private Value obj;

  public ValueBean(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setValue(String value) {
    //
    // this.value = value;
    //

    obj.invokeMember("setValue", value);
  }

  public String getValue() {
    //
    // return value;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValue").as(String.class);
  }
}
