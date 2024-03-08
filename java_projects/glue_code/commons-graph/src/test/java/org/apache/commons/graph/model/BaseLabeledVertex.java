package org.apache.commons.graph;

import java.io.Serializable;
import org.graalvm.polyglot.Value;

public class BaseLabeledVertex implements Serializable {
  private static final long serialVersionUID = -5167021719818162490L;
  private static Value clz =
      ContextInitializer.getPythonClass("/BaseLabeledVertex.py", "BaseLabeledVertex");
  private Value obj;

  public BaseLabeledVertex(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return format("{ %s }", label);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // return hash(1, 31, label);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hashCode").as(int.class);
  }

  public boolean equals(Object obj) {
    //
    // if (this == obj) {
    // return true;
    // }
    //
    // if (obj == null || getClass() != obj.getClass()) {
    // return false;
    // }
    //
    // BaseLabeledVertex other = (BaseLabeledVertex) obj;
    // return eq(label, other.getLabel());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", obj).as(boolean.class);
  }

  public final String getLabel() {
    //
    // return label;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLabel").as(String.class);
  }

  public BaseLabeledVertex(String label) {
    //
    // this.label = checkNotNull(label, "Argument 'label' must not be null");
    //

    this.obj = clz.invokeMember("__init__", label);
  }
}
