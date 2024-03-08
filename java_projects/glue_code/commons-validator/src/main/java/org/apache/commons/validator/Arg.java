package org.apache.commons.validator;

import java.io.Serializable;
import org.graalvm.polyglot.Value;

public class Arg implements Cloneable, Serializable {
  protected boolean resource = true;
  protected int position = -1;
  protected String name = null;
  protected String key = null;
  protected String bundle = null;
  private static final long serialVersionUID = -8922606779669839294L;
  private static Value clz = ContextInitializer.getPythonClass("/Arg.py", "Arg");
  private Value obj;

  public Arg(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // StringBuilder results = new StringBuilder();
    //
    // results.append("Arg: name=");
    // results.append(name);
    // results.append("  key=");
    // results.append(key);
    // results.append("  position=");
    // results.append(position);
    // results.append("  bundle=");
    // results.append(bundle);
    // results.append("  resource=");
    // results.append(resource);
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

  public void setPosition(int position) {
    //
    // this.position = position;
    //

    obj.invokeMember("setPosition", position);
  }

  public void setName(String name) {
    //
    // this.name = name;
    //

    obj.invokeMember("setName", name);
  }

  public void setKey(String key) {
    //
    // this.key = key;
    //

    obj.invokeMember("setKey", key);
  }

  public void setBundle(String bundle) {
    //
    // this.bundle = bundle;
    //

    obj.invokeMember("setBundle", bundle);
  }

  public boolean isResource() {
    //
    // return this.resource;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isResource").as(boolean.class);
  }

  public int getPosition() {
    //
    // return this.position;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPosition").as(int.class);
  }

  public String getName() {
    //
    // return this.name;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getName").as(String.class);
  }

  public String getKey() {
    //
    // return this.key;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getKey").as(String.class);
  }

  public String getBundle() {
    //
    // return this.bundle;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getBundle").as(String.class);
  }
}
