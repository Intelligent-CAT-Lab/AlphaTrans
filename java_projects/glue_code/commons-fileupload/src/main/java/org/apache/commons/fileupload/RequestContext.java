package org.apache.commons.fileupload;

import java.io.IOException;
import java.io.InputStream;

public interface RequestContext {
  InputStream getInputStream() throws IOException;

  int getContentLength();

  String getContentType();

  String getCharacterEncoding();
}
