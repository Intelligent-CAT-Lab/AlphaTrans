package org.apache.commons.fileupload;

import java.io.IOException;
import java.io.InputStream;
import org.graalvm.polyglot.Value;

class ItemSkippedException extends IOException {
  private static final long serialVersionUID = -7280778431581963740L;
  private static Value clz =
      ContextInitializer.getPythonClass("<placeholder>", "ItemSkippedException");
  private Value obj;

  public ItemSkippedException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}

public interface FileItemStream extends FileItemHeadersSupport {
  boolean isFormField();

  String getFieldName();

  String getName();

  String getContentType();

  InputStream openStream() throws IOException;
}
