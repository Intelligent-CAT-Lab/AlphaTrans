package org.apache.commons.fileupload;


public interface UploadContext extends RequestContext {
  long contentLength();
}
