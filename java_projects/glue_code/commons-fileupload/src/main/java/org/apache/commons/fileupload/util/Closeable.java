package org.apache.commons.fileupload;

import java.io.IOException;

public interface Closeable {
  boolean isClosed() throws IOException;

  void close() throws IOException;
}
