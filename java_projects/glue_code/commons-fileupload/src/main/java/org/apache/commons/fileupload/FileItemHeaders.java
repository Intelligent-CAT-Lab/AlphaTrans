package org.apache.commons.fileupload;

import java.util.Iterator;

public interface FileItemHeaders {
  Iterator<String> getHeaderNames();

  Iterator<String> getHeaders(String name);

  String getHeader(String name);
}
