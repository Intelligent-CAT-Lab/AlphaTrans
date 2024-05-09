package org.apache.commons.fileupload;

import java.io.File;
import org.apache.commons.fileupload.util.FileItemHeadersImpl;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
  private static Engine sharedEngine;
  private static String codeDirectory =
      "../../../../data/verified_projects/commons-fileupload/src/main/org/apache/commons/fileupload/";
  private static String packageDirectory = "../../../../data/verified_projects/commons-fileupload/";
  private static Context context;

  static {
    try {
      HostAccess hostAccess =
          HostAccess.newBuilder(HostAccess.ALL)
              .targetTypeMapping(
                  Value.class, FileItemHeadersImpl.class, null, (v) -> new FileItemHeadersImpl(v))
              // TODO: Add other mappings
              .build();

      sharedEngine = Engine.create();
      context =
          Context.newBuilder("python")
              .allowHostAccess(hostAccess)
              .allowAllAccess(true)
              .option("python.PythonPath", packageDirectory)
              .engine(sharedEngine)
              .build();
    } catch (Exception e) {
      System.out.println("[-] " + e);
    }
  }

  public static Value[] getPythonClasses(String fileName, String... classNames) {
    try {
      File file = new File(codeDirectory, fileName);
      Source source = Source.newBuilder("python", file).build();
      assert source != null;

      context.eval(source);

      Value[] result = new Value[classNames.length];
      for (int i = 0; i < classNames.length; i++) {
        result[i] = context.getBindings("python").getMember(classNames[i]);
      }
      return result;
    } catch (Exception e) {
      System.out.println("[-] " + e);
      return null; // ??
    }
  }

  public static Value getPythonClass(String fileName, String className) {
    return getPythonClasses(fileName, className)[0];
  }
}
