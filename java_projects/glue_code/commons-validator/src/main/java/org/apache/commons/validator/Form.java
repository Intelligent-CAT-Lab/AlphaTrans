package org.apache.commons.validator;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import org.graalvm.polyglot.Value;

public class Form implements Serializable {
  protected String inherit = null;
  protected List<Field> lFields = new ArrayList<Field>();
  protected String name = null;
  private boolean processed = false;
  private static final long serialVersionUID = 6445211789563796371L;
  private static Value clz = ContextInitializer.getPythonClass("/Form.py", "Form");
  private Value obj;

  public Form(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // StringBuilder results = new StringBuilder();
    //
    // results.append("Form: ");
    // results.append(name);
    // results.append("\n");
    //
    // for (Iterator<Field> i = lFields.iterator(); i.hasNext(); ) {
    // results.append("\tField: \n");
    // results.append(i.next());
    // results.append("\n");
    // }
    //
    // return results.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public boolean isExtending() {
    //
    // return inherit != null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isExtending").as(boolean.class);
  }

  public void setExtends(String inherit) {
    //
    // this.inherit = inherit;
    //

    obj.invokeMember("setExtends", inherit);
  }

  public String getExtends() {
    //
    // return inherit;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getExtends").as(String.class);
  }

  public boolean isProcessed() {
    //
    // return processed;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isProcessed").as(boolean.class);
  }

  public List<Field> getFields() {
    //
    // return Collections.unmodifiableList(lFields);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFields").as(List.class);
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
}
