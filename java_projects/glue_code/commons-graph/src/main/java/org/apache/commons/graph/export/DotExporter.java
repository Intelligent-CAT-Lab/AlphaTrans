package org.apache.commons.graph.export;

import java.util.Map;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

final class DotExporter<V, E> extends AbstractExporter<V, E, DotExporter<V, E>> {
  private static final String LABEL = "label";
  private static final String WEIGHT = "weight";
  private static final String DICONNECTOR = "->";
  private static final String CONNECTOR = "--";
  private static final String DIGRAPH = "digraph";
  private static final String GRAPH = "graph";
  private static Value clz =
      ContextInitializer.getPythonClass("/export/DotExporter.py", "DotExporter");
  private Value obj;

  public DotExporter(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected void vertex(V vertex, Map<String, Object> properties) throws Exception {
    try {
      //
      // printWriter.format("  %s", vertexIdentifiers.get(vertex));
      //
      // printVertexOrEdgeProperties(properties);
      //

      obj.invokeMember("vertex", vertex, properties);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DotExporter.vertex");
    }
  }

  protected void startSerialization() throws Exception {
    try {
      //
      // printWriter = new PrintWriter(getWriter());
      //

      obj.invokeMember("startSerialization");
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DotExporter.startSerialization");
    }
  }

  protected void startGraph(String name) throws Exception {
    try {
      //
      // String graphDeclaration;
      //
      // if (getGraph() instanceof DirectedGraph) {
      // graphDeclaration = DIGRAPH;
      // connector = DICONNECTOR;
      // } else {
      // graphDeclaration = GRAPH;
      // connector = CONNECTOR;
      // }
      //
      // printWriter.format("%s %s {%n", graphDeclaration, name);
      //

      obj.invokeMember("startGraph", name);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DotExporter.startGraph");
    }
  }

  protected void enlistVerticesProperty(String name, Class<?> type) throws Exception {
    try {
      //

      obj.invokeMember("enlistVerticesProperty", name, type);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DotExporter.enlistVerticesProperty");
    }
  }

  protected void enlistEdgesProperty(String name, Class<?> type) throws Exception {
    try {
      //

      obj.invokeMember("enlistEdgesProperty", name, type);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DotExporter.enlistEdgesProperty");
    }
  }

  protected void endSerialization() throws Exception {
    try {
      //

      obj.invokeMember("endSerialization");
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DotExporter.endSerialization");
    }
  }

  protected void endGraph() throws Exception {
    try {
      //
      // printWriter.write('}');
      //

      obj.invokeMember("endGraph");
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DotExporter.endGraph");
    }
  }

  protected void edge(E edge, V head, V tail, Map<String, Object> properties) throws Exception {
    try {
      //
      // printWriter.format(
      // "  %s %s %s", vertexIdentifiers.get(head), connector, vertexIdentifiers.get(tail));
      //
      // printVertexOrEdgeProperties(properties);
      //

      obj.invokeMember("edge", edge, head, tail, properties);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DotExporter.edge");
    }
  }

  protected void comment(String text) throws Exception {
    try {
      //
      // printWriter.write(text);
      //

      obj.invokeMember("comment", text);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DotExporter.comment");
    }
  }

  public DotExporter<V, E> withVertexLabels(Mapper<V, String> vertexLabels) {
    //
    // super.addVertexProperty(LABEL, vertexLabels);
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("withVertexLabels", vertexLabels).as(DotExporter.class);
  }

  public <N extends Number> DotExporter<V, E> withEdgeWeights(Mapper<E, N> edgeWeights) {
    //
    // super.addEdgeProperty(WEIGHT, edgeWeights);
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("withEdgeWeights", edgeWeights).as(DotExporter.class);
  }

  public DotExporter<V, E> withEdgeLabels(Mapper<E, String> edgeLabels) {
    //
    // super.addEdgeProperty(LABEL, edgeLabels);
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("withEdgeLabels", edgeLabels).as(DotExporter.class);
  }

  private void printVertexOrEdgeProperties(Map<String, Object> properties) {
    //
    // if (!properties.isEmpty()) {
    // int countAddedProperties = 0;
    // printWriter.write(" [");
    //
    // for (Entry<String, Object> property : properties.entrySet()) {
    // String formattedString =
    // countAddedProperties == properties.size() - 1 ? "%s=\"%s\"" : "%s=\"%s\" ";
    // printWriter.format(formattedString, property.getKey(), property.getValue());
    // countAddedProperties++;
    // }
    //
    // printWriter.format("];%n");
    // }
    //

    obj.invokeMember("printVertexOrEdgeProperties", properties);
  }

  private Map<V, Integer> generateVertexIdentifiers(Graph<V, E> graph) {
    //
    // Map<V, Integer> vertexIdentifiers = new HashMap<V, Integer>();
    // int count = 1;
    //
    // for (V vertex : graph.getVertices0()) {
    // vertexIdentifiers.put(vertex, count++);
    // }
    //
    // return vertexIdentifiers;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("generateVertexIdentifiers", graph).as(Map.class);
  }

  DotExporter(Graph<V, E> graph, String name) {
    //
    // super(graph, name);
    // this.vertexIdentifiers = generateVertexIdentifiers(graph);
    //

    this.obj = clz.invokeMember("__init__", graph, name);
  }
}
