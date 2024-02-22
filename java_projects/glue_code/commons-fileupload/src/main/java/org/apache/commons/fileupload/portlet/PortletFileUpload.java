package org.apache.commons.fileupload.portlet;

import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.FileItemFactory;
import org.apache.commons.fileupload.FileUpload;
import org.graalvm.polyglot.Value;

public class PortletFileUpload extends FileUpload {
  private static Value clz =
      ContextInitializer.getPythonClass("<placeholder>", "PortletFileUpload");
  private Value obj;

  public PortletFileUpload(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static PortletFileUpload PortletFileUpload1() {
    //
    // return new PortletFileUpload(null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("PortletFileUpload1").as(PortletFileUpload.class);
  }

  public PortletFileUpload(FileItemFactory fileItemFactory) {
    //
    // super(0, fileItemFactory);
    //

    this.obj = clz.invokeMember("__init__", fileItemFactory);
  }
}
