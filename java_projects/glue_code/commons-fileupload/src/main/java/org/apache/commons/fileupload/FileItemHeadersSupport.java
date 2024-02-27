package org.apache.commons.fileupload;


public interface FileItemHeadersSupport {
  void setHeaders(FileItemHeaders headers);

  FileItemHeaders getHeaders();
}
