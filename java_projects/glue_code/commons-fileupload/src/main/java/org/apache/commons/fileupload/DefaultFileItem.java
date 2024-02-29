package org.apache.commons.fileupload;

import java.io.File;
import org.apache.commons.fileupload.disk.DiskFileItem;
import org.graalvm.polyglot.Value;

public class DefaultFileItem extends DiskFileItem {
  private static Value clz =
      ContextInitializer.getPythonClass("DefaultFileItem.py", "DefaultFileItem");
  private Value obj;

  public DefaultFileItem(Value obj) {
    super(obj);
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public DefaultFileItem(
      String fieldName,
      String contentType,
      boolean isFormField,
      String fileName,
      int sizeThreshold,
      File repository) {
    super(fieldName, contentType, isFormField, fileName, sizeThreshold, repository);

    this.obj =
        clz.invokeMember(
            "__init__", fieldName, contentType, isFormField, fileName, sizeThreshold, repository);
  }
}
