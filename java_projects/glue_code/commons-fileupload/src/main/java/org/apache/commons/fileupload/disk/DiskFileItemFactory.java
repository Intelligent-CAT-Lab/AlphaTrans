package org.apache.commons.fileupload;

import java.io.File;
import org.graalvm.polyglot.Value;

public class DiskFileItemFactory {
  public static final int DEFAULT_SIZE_THRESHOLD = 10240;
  private String defaultCharset = DiskFileItem.DEFAULT_CHARSET;
  private int sizeThreshold = DEFAULT_SIZE_THRESHOLD;
  private static Value clz =
      ContextInitializer.getPythonClass("<placeholder>", "DiskFileItemFactory");
  private Value obj;

  public DiskFileItemFactory(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setDefaultCharset(String pCharset) {
    //
    // defaultCharset = pCharset;
    //

    obj.invokeMember("setDefaultCharset", pCharset);
  }

  public String getDefaultCharset() {
    //
    // return defaultCharset;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDefaultCharset").as(String.class);
  }

  public void setSizeThreshold(int sizeThreshold) {
    //
    // this.sizeThreshold = sizeThreshold;
    //

    obj.invokeMember("setSizeThreshold", sizeThreshold);
  }

  public int getSizeThreshold() {
    //
    // return sizeThreshold;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSizeThreshold").as(int.class);
  }

  public void setRepository(File repository) {
    //
    // this.repository = repository;
    //

    obj.invokeMember("setRepository", repository);
  }

  public File getRepository() {
    //
    // return repository;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRepository").as(File.class);
  }

  public static DiskFileItemFactory DiskFileItemFactory1() {
    //
    // return new DiskFileItemFactory(DEFAULT_SIZE_THRESHOLD, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("DiskFileItemFactory1").as(DiskFileItemFactory.class);
  }

  public DiskFileItemFactory(int sizeThreshold, File repository) {
    //
    // this.sizeThreshold = sizeThreshold;
    // this.repository = repository;
    //

    this.obj = clz.invokeMember("__init__", sizeThreshold, repository);
  }
}
