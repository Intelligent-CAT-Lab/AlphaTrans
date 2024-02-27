package org.apache.commons.fileupload;

import java.io.PrintStream;
import java.io.PrintWriter;
import org.graalvm.polyglot.Value;

public class FileUploadException extends Exception {
  private static final long serialVersionUID = 8881893724388807504L;
  private static Value clz =
      ContextInitializer.getPythonClass("FileUploadException.py", "FileUploadException");
  private Value obj;

  public FileUploadException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Throwable getCause() {
    //
    // return cause;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCause").as(Throwable.class);
  }

  public void printStackTrace1(PrintWriter writer) {
    //
    // super.printStackTrace(writer);
    // if (cause != null) {
    // writer.println("Caused by:");
    // cause.printStackTrace(writer);
    // }
    //

    obj.invokeMember("printStackTrace1", writer);
  }

  public void printStackTrace0(PrintStream stream) {
    //
    // super.printStackTrace(stream);
    // if (cause != null) {
    // stream.println("Caused by:");
    // cause.printStackTrace(stream);
    // }
    //

    obj.invokeMember("printStackTrace0", stream);
  }

  public FileUploadException(String msg, Throwable cause) {
    //
    // super(msg);
    // this.cause = cause;
    //

    this.obj = clz.invokeMember("__init__", msg, cause);
  }

  public static FileUploadException FileUploadException1(final String msg) {
    //
    // return new FileUploadException(msg, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("FileUploadException1", msg).as(FileUploadException.class);
  }

  public static FileUploadException FileUploadException0() {
    //
    // return new FileUploadException(null, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("FileUploadException0").as(FileUploadException.class);
  }
}
