package org.apache.commons.fileupload;

import org.graalvm.polyglot.Value;

public class InvalidFileNameException extends RuntimeException {
  private static final long serialVersionUID = 7922042602454350470L;
  private static Value clz =
      ContextInitializer.getPythonClass("<placeholder>", "InvalidFileNameException");
  private Value obj;

  public InvalidFileNameException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String getName() {
    //
    // return name;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getName").as(String.class);
  }

  public InvalidFileNameException(String pName, String pMessage) {
    //
    // super(pMessage);
    // name = pName;
    //

    this.obj = clz.invokeMember("__init__", pName, pMessage);
  }
}
