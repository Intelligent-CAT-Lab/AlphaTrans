package org.apache.commons.fileupload.util;

import org.apache.commons.fileupload.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class Streams {
  public static final int DEFAULT_BUFFER_SIZE = 8192;
  private static Value clz = ContextInitializer.getPythonClass("<placeholder>", "Streams");
  private Value obj;

  public Streams(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static String checkFileName(String fileName) {
    //
    // if (fileName != null && fileName.indexOf('\u0000') != -1) {
    // final StringBuilder sb = new StringBuilder();
    // for (int i = 0; i < fileName.length(); i++) {
    // char c = fileName.charAt(i);
    // switch (c) {
    // case 0:
    // sb.append("\\0");
    // break;
    // default:
    // sb.append(c);
    // break;
    // }
    // }
    // throw new InvalidFileNameException(fileName, "Invalid file name: " + sb);
    // }
    // return fileName;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("checkFileName", fileName).as(String.class);
  }

  private Streams() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
