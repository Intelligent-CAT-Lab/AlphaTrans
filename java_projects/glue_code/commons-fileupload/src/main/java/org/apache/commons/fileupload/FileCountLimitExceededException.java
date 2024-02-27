package org.apache.commons.fileupload;

import org.graalvm.polyglot.Value;

public class FileCountLimitExceededException extends FileUploadException {
  private static final long serialVersionUID = 6904179610227521789L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "FileCountLimitExceededException.py", "FileCountLimitExceededException");
  private Value obj;

  public FileCountLimitExceededException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public long getLimit() {
    //
    // return limit;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLimit").as(long.class);
  }

  public FileCountLimitExceededException(final String message, final long limit) {
    //
    // super(message, null);
    // this.limit = limit;
    //

    this.obj = clz.invokeMember("__init__", message, limit);
  }
}
