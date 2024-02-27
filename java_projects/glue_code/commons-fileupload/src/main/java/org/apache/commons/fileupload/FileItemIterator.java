package org.apache.commons.fileupload;

import java.io.IOException;

public interface FileItemIterator {
  FileItemStream next() throws FileUploadException, IOException;

  boolean hasNext() throws FileUploadException, IOException;
}
