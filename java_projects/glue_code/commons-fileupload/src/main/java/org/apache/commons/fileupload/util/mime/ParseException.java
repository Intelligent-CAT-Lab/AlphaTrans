package org.apache.commons.fileupload.util.mime;

import org.apache.commons.fileupload.ContextInitializer;
import org.graalvm.polyglot.Value;

final class ParseException extends Exception {
  private static final long serialVersionUID = 5355281266579392077L;
  private static Value clz =
      ContextInitializer.getPythonClass("/util/mimParseException.py", "ParseException");
  private Value obj;

  public ParseException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  ParseException(String message) {
    //
    // super(message);
    //

    this.obj = clz.invokeMember("__init__", message);
  }
}
