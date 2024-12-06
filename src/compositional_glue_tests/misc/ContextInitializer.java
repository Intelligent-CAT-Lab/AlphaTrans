package {project};
{imports}
import java.io.File;
import java.util.HashMap;
import java.util.Map;
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
      sharedEngine = Engine.create();
      context =
          Context.newBuilder("python")
              .allowExperimentalOptions(true)
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

  private static Map<String, Value> classCache = new HashMap<>();

  public static Value getPythonClass(String filePath, String className) {{
    String fullName = filePath + "::" + className;
    if (classCache.containsKey(fullName)) {{
      return classCache.get(fullName);
    }}
    Value cls = getPythonClasses(filePath, className)[0];
    classCache.put(fullName, cls);
    return cls;
  }}

  public static <T> Value getPythonClass(Class<T> cls) {{
    Boolean isTestClass = cls.getProtectionDomain().getCodeSource().getLocation().getPath().contains("/test-classes/");
    String baseDir = isTestClass ? "test" : "main";
    String filePath = baseDir + "/" + cls.getName().split("\\$", 2)[0].replace(".", "/") + ".py";
    String className = cls.getSimpleName();
    return getPythonClass(filePath, className);
  }}
}}
