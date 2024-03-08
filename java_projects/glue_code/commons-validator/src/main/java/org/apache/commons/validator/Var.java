package org.apache.commons.validator;

import java.io.Serializable;
import org.graalvm.polyglot.Value;

public class Var implements Cloneable, Serializable {
  public static final String JSTYPE_REGEXP = "regexp";
  public static final String JSTYPE_STRING = "string";
  public static final String JSTYPE_INT = "int";
  private String bundle = null;
  private boolean resource = false;
  private String jsType = null;
  private String value = null;
  private String name = null;
  private static final long serialVersionUID = -684185211548420224L;
  private static Value clz = ContextInitializer.getPythonClass("/Var.py", "Var");
  private Value obj;

  public Var(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // StringBuilder results = new StringBuilder();
    //
    // results.append("Var: name=");
    // results.append(name);
    // results.append("  value=");
    // results.append(value);
    // results.append("  resource=");
    // results.append(resource);
    // if (resource) {
    // results.append("  bundle=");
    // results.append(bundle);
    // }
    // results.append("  jsType=");
    // results.append(jsType);
    // results.append("\n");
    //
    // return results.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public Object clone() {
    //
    // try {
    // return super.clone();
    //
    // } catch (CloneNotSupportedException e) {
    // throw new RuntimeException(e.toString());
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("clone").as(Object.class);
  }

  public void setJsType(String jsType) {
    //
    // this.jsType = jsType;
    //

    obj.invokeMember("setJsType", jsType);
  }

  public String getJsType() {
    //
    // return this.jsType;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getJsType").as(String.class);
  }

  public void setBundle(String bundle) {
    //
    // this.bundle = bundle;
    //

    obj.invokeMember("setBundle", bundle);
  }

  public String getBundle() {
    //
    // return this.bundle;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getBundle").as(String.class);
  }

  public void setResource(boolean resource) {
    //
    // this.resource = resource;
    //

    obj.invokeMember("setResource", resource);
  }

  public boolean isResource() {
    //
    // return this.resource;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isResource").as(boolean.class);
  }

  public void setValue(String value) {
    //
    // this.value = value;
    //

    obj.invokeMember("setValue", value);
  }

  public String getValue() {
    //
    // return this.value;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValue").as(String.class);
  }

  public void setName(String name) {
    //
    // this.name = name;
    //

    obj.invokeMember("setName", name);
  }

  public String getName() {
    //
    // return this.name;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getName").as(String.class);
  }

  public Var(int constructorId, String name, String value, String jsType) {
    //
    // super();
    // if (constructorId == 1) {
    // this.name = name;
    // this.value = value;
    // this.jsType = jsType;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, name, value, jsType);
  }
}
