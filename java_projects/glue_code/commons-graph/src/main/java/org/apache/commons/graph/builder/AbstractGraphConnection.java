package org.apache.commons.graph.builder;

import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

public abstract class AbstractGraphConnection<V, E> implements GraphConnection<V, E> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/builder/AbstractGraphConnection.py", "AbstractGraphConnection");
  private Value obj;

  public AbstractGraphConnection(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public final void connect1(GraphConnector<V, E> connector) {
    //
    // checkState(this.connector == null, "Re-entry not allowed!");
    // this.connector = connector;
    //
    // try {
    // connect0();
    // } finally {
    // this.connector = null;
    // }
    //

    obj.invokeMember("connect1", connector);
  }

  public final void connect(GraphConnector<V, E> connector) {
    //
    // connect1(connector);
    //

    obj.invokeMember("connect", connector);
  }

  protected final <N extends V> N addVertex(N node) {
    //
    // return connector.addVertex(node);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addVertex", node).as(N.class);
  }

  protected final <A extends E> HeadVertexConnector<V, E> addEdge(A arc) {
    //
    // return connector.addEdge(arc);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addEdge", arc).as(HeadVertexConnector.class);
  }

  public abstract void connect0();
}
