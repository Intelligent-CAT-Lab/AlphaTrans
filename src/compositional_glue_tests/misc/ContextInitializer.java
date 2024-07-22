package {project};
{imports}
import java.io.File;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {{
  private static Engine sharedEngine;
  private static String srcDirectory = "{src_directory}";
  private static String packageDirectory = "{package_directory}";
  private static Context context;

  static {{
    try {{
      HostAccess hostAccess = HostAccess.newBuilder(HostAccess.ALL).build();

      sharedEngine = Engine.create();
      context =
          Context.newBuilder("python")
              .allowHostAccess(hostAccess)
              .allowAllAccess(true)
              .option("python.PythonPath", packageDirectory)
              .engine(sharedEngine)
              .build();
    }} catch (Exception e) {{
      System.out.println("[-] " + e);
    }}
  }}

  public static Value[] getPythonClasses(
      String filePath, String... classNames) {{
    try {{
      File file = new File(srcDirectory, filePath);
      Source source = Source.newBuilder("python", file).build();
      assert source != null;

      context.eval(source);

      Value[] result = new Value[classNames.length];
      for (int i = 0; i < classNames.length; i++) {{
        result[i] = context.getBindings("python").getMember(classNames[i]);
      }}
      return result;
    }} catch (Exception e) {{
      System.out.println("[-] In File " + filePath + ": " + e);
      return null;
    }}
  }}

  public static Value getPythonClass(String filePath, String className) {{
    return getPythonClasses(filePath, className)[0];
  }}
}}
