package org.apache.commons.fileupload;

import java.io.File;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.graalvm.polyglot.Value;

public class DefaultFileItemFactory extends DiskFileItemFactory {
  private static Value clz =
      ContextInitializer.getPythonClass("DefaultFileItemFactory.py", "DefaultFileItemFactory");
  private Value obj;

  public DefaultFileItemFactory(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public DefaultFileItemFactory(int sizeThreshold, File repository) {
    //
    // super(sizeThreshold, repository);
    //

    this.obj = clz.invokeMember("__init__", sizeThreshold, repository);
  }

  public static DefaultFileItemFactory DefaultFileItemFactory1() {
    //
    // return new DefaultFileItemFactory(0, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("DefaultFileItemFactory1").as(DefaultFileItemFactory.class);
  }
}
