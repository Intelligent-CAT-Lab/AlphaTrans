package org.apache.commons.fileupload;

import org.graalvm.polyglot.Value;

public class FileUpload extends FileUploadBase {
  private static Value clz = ContextInitializer.getPythonClass("FileUpload.py", "FileUpload");
  private Value obj;

  public FileUpload(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setFileItemFactory(FileItemFactory factory) {
    //
    // this.fileItemFactory = factory;
    //

    obj.invokeMember("setFileItemFactory", factory);
  }

  public FileItemFactory getFileItemFactory() {
    //
    // return fileItemFactory;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFileItemFactory").as(FileItemFactory.class);
  }

  public FileUpload(int constructorId, FileItemFactory fileItemFactory) {
    super();
    // if (constructorId == 1) {
    // this.fileItemFactory = fileItemFactory;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, fileItemFactory);
  }
}
