package org.apache.commons.validator;

import java.io.Serializable;
import org.graalvm.polyglot.Value;

public class Msg implements Cloneable, Serializable {
  protected boolean resource = true;
  protected String name = null;
  protected String key = null;
  protected String bundle = null;
  private static final long serialVersionUID = 5690015734364127124L;
  private static Value clz = ContextInitializer.getPythonClass("/Msg.py", "Msg");
  private Value obj;

  public Msg(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // StringBuilder results = new StringBuilder();
    //
    // results.append("Msg: name=");
    // results.append(name);
    // results.append("  key=");
    // results.append(key);
    // results.append("  resource=");
    // results.append(resource);
    // results.append("  bundle=");
    // results.append(bundle);
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

  public void setKey(String key) {
    //
    // this.key = key;
    //

    obj.invokeMember("setKey", key);
  }

  public String getKey() {
    //
    // return key;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getKey").as(String.class);
  }

  public void setName(String name) {
    //
    // this.name = name;
    //

    obj.invokeMember("setName", name);
  }

  public String getName() {
    //
    // return name;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getName").as(String.class);
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
}
