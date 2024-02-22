package org.apache.commons.fileupload.disk;

import java.io.File;
import java.util.UUID;
import java.util.concurrent.atomic.AtomicInteger;

import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.FileItemHeaders;
import org.graalvm.polyglot.Value;

public class DiskFileItem {
  public static final String DEFAULT_CHARSET = "ISO-8859-1";
  private String defaultCharset = DEFAULT_CHARSET;
  private long size = -1;
  private static final AtomicInteger COUNTER = new AtomicInteger(0);
  private static final String UID = UUID.randomUUID().toString().replace('-', '_');
  private static Value clz = ContextInitializer.getPythonClass("<placeholder>", "DiskFileItem");
  private Value obj;

  public DiskFileItem(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setDefaultCharset(String charset) {
    //
    // defaultCharset = charset;
    //

    obj.invokeMember("setDefaultCharset", charset);
  }

  public String getDefaultCharset() {
    //
    // return defaultCharset;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDefaultCharset").as(String.class);
  }

  public void setHeaders(FileItemHeaders pHeaders) {
    //
    // headers = pHeaders;
    //

    obj.invokeMember("setHeaders", pHeaders);
  }

  public FileItemHeaders getHeaders() {
    //
    // return headers;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaders").as(FileItemHeaders.class);
  }

  protected File getTempFile() {
    //
    // if (tempFile == null) {
    // File tempDir = repository;
    // if (tempDir == null) {
    // tempDir = new File(System.getProperty("java.io.tmpdir"));
    // }
    //
    // String tempFileName = format("upload_%s_%s.tmp", UID, getUniqueId());
    //
    // tempFile = new File(tempDir, tempFileName);
    // }
    // return tempFile;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTempFile").as(File.class);
  }

  public void setFormField(boolean state) {
    //
    // isFormField = state;
    //

    obj.invokeMember("setFormField", state);
  }

  public boolean isFormField() {
    //
    // return isFormField;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isFormField").as(boolean.class);
  }

  public void setFieldName(String fieldName) {
    //
    // this.fieldName = fieldName;
    //

    obj.invokeMember("setFieldName", fieldName);
  }

  public String getFieldName() {
    //
    // return fieldName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFieldName").as(String.class);
  }

  public String getName() {
    //
    // return Streams.checkFileName(fileName);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getName").as(String.class);
  }

  public String getCharSet() {
    //
    // ParameterParser parser = new ParameterParser();
    // parser.setLowerCaseNames(true);
    // Map<String, String> params = parser.parse1(getContentType(), ';');
    // return params.get("charset");
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCharSet").as(String.class);
  }

  public String getContentType() {
    //
    // return contentType;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getContentType").as(String.class);
  }

  public DiskFileItem(
      String fieldName,
      String contentType,
      boolean isFormField,
      String fileName,
      int sizeThreshold,
      File repository) {
    //
    // this.fieldName = fieldName;
    // this.contentType = contentType;
    // this.isFormField = isFormField;
    // this.fileName = fileName;
    // this.sizeThreshold = sizeThreshold;
    // this.repository = repository;
    //

    this.obj =
        clz.invokeMember(
            "__init__", fieldName, contentType, isFormField, fileName, sizeThreshold, repository);
  }

  private static String getUniqueId() {
    //
    // final int limit = 100000000;
    // int current = COUNTER.getAndIncrement();
    // String id = Integer.toString(current);
    //
    // if (current < limit) {
    // id = ("00000000" + id).substring(id.length());
    // }
    // return id;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getUniqueId").as(String.class);
  }
}
