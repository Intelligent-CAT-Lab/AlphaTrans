package org.apache.commons.graph;

import org.graalvm.polyglot.Value;

public class BaseLabeledWeightedEdge<W> extends BaseLabeledEdge {
  private static final long serialVersionUID = 5935967858178091436L;
  private static Value clz =
      ContextInitializer.getPythonClass("/BaseLabeledWeightedEdge.py", "BaseLabeledWeightedEdge");
  private Value obj;

  public BaseLabeledWeightedEdge(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return format("%s( %s )", getLabel(), weight);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // return hash(super.hashCode(), 31, weight);
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
    // if (!super.equals(obj)) {
    // return false;
    // }
    //
    // if (getClass() != obj.getClass()) {
    // return false;
    // }
    // @SuppressWarnings("unchecked")
    // BaseLabeledWeightedEdge<W> other = (BaseLabeledWeightedEdge<W>) obj;
    // return eq(weight, other.getWeight());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", obj).as(boolean.class);
  }

  public W getWeight() {
    //
    // return weight;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getWeight").as(W.class);
  }

  public BaseLabeledWeightedEdge(String label, W weight) {
    //
    // super(label);
    // this.weight = checkNotNull(weight, "Argument 'weight' must not be null");
    //

    this.obj = clz.invokeMember("__init__", label, weight);
  }
}
