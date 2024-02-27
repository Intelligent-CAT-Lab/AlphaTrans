package org.apache.commons.fileupload;


public interface ProgressListener {
  void update(long pBytesRead, long pContentLength, int pItems);
}
