package org.apache.commons.fileupload;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.UnsupportedEncodingException;

public interface FileItem extends FileItemHeadersSupport {
  OutputStream getOutputStream() throws IOException;

  void setFormField(boolean state);

  boolean isFormField();

  void setFieldName(String name);

  String getFieldName();

  void delete();

  void write(File file) throws Exception;

  String getString1();

  String getString0(String encoding) throws UnsupportedEncodingException;

  byte[] get();

  long getSize();

  boolean isInMemory();

  String getName();

  String getContentType();

  InputStream getInputStream() throws IOException;
}
