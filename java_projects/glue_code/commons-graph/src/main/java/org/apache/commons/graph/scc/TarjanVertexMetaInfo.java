package org.apache.commons.graph.scc;

import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

final class TarjanVertexMetaInfo {
  private int lowLink = UNDEFINED;
  private int index = UNDEFINED;
  private static final int UNDEFINED = -1;
  private static Value clz =
      ContextInitializer.getPythonClass("/scc/TarjanVertexMetaInfo.py", "TarjanVertexMetaInfo");
  private Value obj;

  public TarjanVertexMetaInfo(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setLowLink(int lowLink) {
    //
    // this.lowLink = lowLink;
    //

    obj.invokeMember("setLowLink", lowLink);
  }

  public void setIndex(int index) {
    //
    // this.index = index;
    //

    obj.invokeMember("setIndex", index);
  }

  public boolean hasUndefinedIndex() {
    //
    // return UNDEFINED == index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasUndefinedIndex").as(boolean.class);
  }

  public int getLowLink() {
    //
    // return lowLink;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLowLink").as(int.class);
  }

  public int getIndex() {
    //
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIndex").as(int.class);
  }
}
