package org.apache.commons.graph.coloring;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class ColoredVertices<V, C> {
  private final List<C> usedColor = new ArrayList<C>();
  private final Map<V, C> coloredVertices = new HashMap<V, C>();
  private static Value clz =
      ContextInitializer.getPythonClass("/coloring/ColoredVertices.py", "ColoredVertices");
  private Value obj;

  public ColoredVertices(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public int getRequiredColors() {
    //
    // return usedColor.size();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRequiredColors").as(int.class);
  }

  public C getColor(V v) {
    //
    // v = checkNotNull(v, "Impossible to get the color for a null Vertex");
    //
    // return coloredVertices.get(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getColor", v).as(C.class);
  }

  public boolean containsColoredVertex(V vertex) {
    //
    // return coloredVertices.containsKey(vertex);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsColoredVertex", vertex).as(boolean.class);
  }

  void removeColor(V v) {
    //
    // C color = coloredVertices.remove(v);
    // usedColor.remove(color);
    //

    obj.invokeMember("removeColor", v);
  }

  void addColor(V v, C color) {
    //
    // coloredVertices.put(v, color);
    // int idx = usedColor.indexOf(color);
    // if (idx == -1) {
    // usedColor.add(color);
    // } else {
    // usedColor.set(idx, color);
    // }
    //

    obj.invokeMember("addColor", v, color);
  }

  ColoredVertices() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
