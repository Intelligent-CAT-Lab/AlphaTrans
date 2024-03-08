package org.apache.commons.validator;

import org.graalvm.polyglot.Value;

public class NameBean {
  protected String lastName = null;
  protected String middleName = null;
  protected String firstName = null;
  private static Value clz = ContextInitializer.getPythonClass("/NameBean.py", "NameBean");
  private Value obj;

  public NameBean(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setLastName(String lastName) {
    //
    // this.lastName = lastName;
    //

    obj.invokeMember("setLastName", lastName);
  }

  public String getLastName() {
    //
    // return lastName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastName").as(String.class);
  }

  public void setMiddleName(String middleName) {
    //
    // this.middleName = middleName;
    //

    obj.invokeMember("setMiddleName", middleName);
  }

  public String getMiddleName() {
    //
    // return middleName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMiddleName").as(String.class);
  }

  public void setFirstName(String firstName) {
    //
    // this.firstName = firstName;
    //

    obj.invokeMember("setFirstName", firstName);
  }

  public String getFirstName() {
    //
    // return firstName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFirstName").as(String.class);
  }
}
